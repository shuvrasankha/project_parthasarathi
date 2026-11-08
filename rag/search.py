"""Retrieval: `retrieve(user_message, history) -> RetrievalResult`, plus `format_for_prompt()`.

1. The LLM rewrites the message (any language) into an English dilemma description + themes.
2. Per collection: vector top-20 and full-text top-20, merged with RRF (k=60).
3. Top 2 situations; their `related_verses` and Ganguli `sections` are fetched by id.
4. Plus the top 3 directly matched verses (deduplicated) and the top 3 directly matched passages.
5. Verse and passage candidates are ordered by cosine similarity to the query, or by the
   cross-encoder when RERANK_ENABLED=true; situations by RRF (or the reranker over the top 5).

CLI: `python -m rag.search "Amar boss amake shobar shamne opoman korlo" [--prompt]`
"""
from __future__ import annotations

import argparse
import logging
import re
from dataclasses import asdict, dataclass, field

from rag.config import ROOT, settings
from rag.db import connect
from rag.embed import get_embedder
from rag.llm import chat_json
from rag.rrf import rrf
from rag.themes import canonical_list
from rag.themes import names as theme_names

log = logging.getLogger("search")

TOP_K = 20
N_SITUATIONS, N_VERSES, N_PASSAGES = 2, 3, 2


@dataclass
class Hit:
    id: str
    collection: str
    score: float  # RRF score for situations; cosine similarity (or rerank score) for verses/passages
    content: str
    meta: dict
    via: str  # "direct" or "situation:<id>"


@dataclass
class RetrievalResult:
    user_message: str
    rewritten_query: str
    themes: list[str]
    situations: list[Hit] = field(default_factory=list)
    verses: list[Hit] = field(default_factory=list)
    passages: list[Hit] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


# ---------- step 1: rewrite ----------

def rewrite(user_message: str, history: list[str] | None = None) -> tuple[str, list[str]]:
    prompt = ((ROOT / "prompts" / "query_rewrite.md").read_text(encoding="utf-8")
              .replace("{{history}}", "\n".join(f"- {h}" for h in (history or [])[-6:]) or "(none)")
              .replace("{{message}}", user_message)
              .replace("{{themes}}", ", ".join(theme_names())))
    try:
        out = chat_json("You turn messages into search queries. Reply with JSON only.", prompt, max_tokens=4000)
        query = str(out["query"]).strip()
        themes = canonical_list([str(t) for t in out.get("themes", [])])[:5]
        if query:
            return query, themes
    except Exception as e:  # retrieval still works on the raw message; BGE-M3 is multilingual
        log.warning("query rewrite failed (%s); searching with the raw message", e)
    return user_message, []


# ---------- step 2: hybrid search ----------

def hybrid(conn, collection: str, qvec, qtext: str, k: int = TOP_K) -> list[tuple[str, float]]:
    vec_ids = [r[0] for r in conn.execute(
        "select id from chunks where collection = %s order by embedding <=> %s::vector limit %s",
        (collection, qvec, k)).fetchall()]
    # OR the words together; websearch_to_tsquery drops stopwords and stems
    words = " or ".join(re.findall(r"[A-Za-z]+", qtext))
    fts_ids = [r[0] for r in conn.execute(
        """select id from chunks, websearch_to_tsquery('english', %s) q
           where collection = %s and tsv @@ q order by ts_rank_cd(tsv, q) desc limit %s""",
        (words, collection, k)).fetchall()] if words else []
    return rrf([vec_ids, fts_ids])


def fetch(conn, qvec, where: str, params: tuple) -> dict[str, tuple[str, str, dict, float]]:
    """id -> (collection, content, meta, cosine similarity to the query)."""
    rows = conn.execute(
        f"select id, collection, content, meta, 1 - (embedding <=> %s::vector) from chunks where {where}",
        (qvec, *params)).fetchall()
    return {r[0]: (r[1], r[2], {k: v for k, v in r[3].items() if k != "content_hash"}, float(r[4])) for r in rows}


def _order(query: str, hits: list[Hit], n: int) -> list[Hit]:
    if settings.rerank_enabled and hits:
        from rag.rerank import rerank_scores

        for h, s in zip(hits, rerank_scores(query, [h.content for h in hits])):
            h.score = s
    if settings.linked_first:  # situation-linked items first, each group by score
        return sorted(hits, key=lambda h: (h.via == "direct", -h.score))[:n]
    return sorted(hits, key=lambda h: -h.score)[:n]


# ---------- the whole pipeline ----------

def retrieve(user_message: str, history: list[str] | None = None,
             rewritten: tuple[str, list[str]] | None = None) -> RetrievalResult:
    """`rewritten` skips the LLM call (the eval passes cached rewrites so experiments are comparable)."""
    query, themes = rewritten or rewrite(user_message, history)
    qtext = f"{query} {' '.join(themes)}".strip()
    qvec = get_embedder().embed([qtext])[0]
    fts = " ".join(themes) if settings.fts_text == "themes" and themes else qtext
    res = RetrievalResult(user_message=user_message, rewritten_query=query, themes=themes)

    with connect() as conn:
        # situations
        sit_rank = hybrid(conn, "situations", qvec, fts)[: (5 if settings.rerank_enabled else N_SITUATIONS)]
        rows = fetch(conn, qvec, "id = any(%s)", ([i for i, _ in sit_rank],))
        sits = [Hit(i, rows[i][0], s, rows[i][1], rows[i][2], "direct") for i, s in sit_rank if i in rows]
        res.situations = _order(qtext, sits, N_SITUATIONS) if settings.rerank_enabled else sits[:N_SITUATIONS]

        # verses: linked from situations + top direct matches
        verse_via: dict[str, str] = {}
        for s in res.situations:
            for v in s.meta.get("related_verses", []):
                verse_via.setdefault(v, f"situation:{s.id}")
        direct = [i for i, _ in hybrid(conn, "gita_verses", qvec, fts) if i not in verse_via][:N_VERSES]
        verse_via.update({i: "direct" for i in direct})
        rows = fetch(conn, qvec, "id = any(%s)", (list(verse_via),))
        res.verses = _order(qtext, [_hit(i, rows[i], verse_via[i]) for i in verse_via if i in rows], N_VERSES)

        # passages: best chunk of each situation's sections + top direct matches
        cands: dict[str, Hit] = {}
        for s in res.situations:
            if s.meta.get("sections"):
                rows = fetch(conn, qvec, "collection = 'mb_passages' and meta->>'parva' = %s and (meta->>'section')::int = any(%s)",
                             (s.meta["parva"].lower(), s.meta["sections"]))
                if rows:
                    best = max(rows, key=lambda i: rows[i][3])
                    cands.setdefault(best, _hit(best, rows[best], f"situation:{s.id}"))
        direct = [i for i, _ in hybrid(conn, "mb_passages", qvec, fts) if i not in cands][:3]
        rows = fetch(conn, qvec, "id = any(%s)", (direct,))
        cands.update({i: _hit(i, rows[i], "direct") for i in direct if i in rows})
        res.passages = _order(qtext, list(cands.values()), N_PASSAGES)
    return res


def _hit(id_: str, row: tuple[str, str, dict, float], via: str) -> Hit:
    collection, content, meta, sim = row
    return Hit(id=id_, collection=collection, score=sim, content=content, meta=meta, via=via)


# ---------- prompt blocks ----------

def blocks(res: RetrievalResult) -> dict[str, str]:
    """Text for the {{retrieved_verses}} and {{retrieved_episodes}} placeholders."""
    verses = []
    for v in res.verses:
        m = v.meta
        verses.append(f"[Bhagavad Gita {m['chapter']}.{m['verse']}]\n{m['sanskrit']}\n{m['transliteration']}\n"
                      f"Translation ({m['translator']}): {m['translation']}"
                      + (f"\nIn simple words: {m['meaning_simple']}" if m.get("meaning_simple") else ""))
    episodes = []
    for s in res.situations:
        m = s.meta
        where = f"{m['parva']} Parva, sections {', '.join(map(str, m['sections']))}" if m["sections"] else f"{m['parva']} Parva"
        episodes.append(f"[Episode: {m['title']}] ({where})\nDilemma: {m['dilemma'].strip()}"
                        + ("\n(Section references not yet verified.)" if m.get("needs_check") else ""))
    for p in res.passages:
        m = p.meta
        episodes.append(f"[Mahabharata, {m['parva'].capitalize()} Parva, Section {m['section']} (K. M. Ganguli translation)]\n{p.content}")
    return {"retrieved_verses": "\n\n".join(verses) or "(none)", "retrieved_episodes": "\n\n".join(episodes) or "(none)"}


def format_for_prompt(res: RetrievalResult, template: str | None = None) -> str:
    """Fill a system prompt's {{retrieved_verses}} / {{retrieved_episodes}}; without a template, both blocks."""
    b = blocks(res)
    if template is None:
        return f"## Retrieved verses\n{b['retrieved_verses']}\n\n## Retrieved episodes\n{b['retrieved_episodes']}"
    return template.replace("{{retrieved_verses}}", b["retrieved_verses"]).replace("{{retrieved_episodes}}", b["retrieved_episodes"])


# ---------- CLI ----------

def _summary(res: RetrievalResult) -> str:
    out = [f"message:   {res.user_message}", f"rewritten: {res.rewritten_query}", f"themes:    {', '.join(res.themes) or '-'}", ""]
    for label, hits in (("situations", res.situations), ("verses", res.verses), ("passages", res.passages)):
        out.append(f"{label}:")
        for h in hits:
            title = h.meta.get("title") or h.content.replace("\n", " ")[:90]
            out.append(f"  {h.score:7.4f}  {h.id:<34} [{h.via}]  {title}")
    return "\n".join(out)


def main() -> None:
    logging.basicConfig(level=logging.WARNING, format="%(levelname)s %(name)s: %(message)s")
    p = argparse.ArgumentParser(description="Search the Krishna Guide index.")
    p.add_argument("message")
    p.add_argument("--history", action="append", default=[], help="earlier user message (repeatable)")
    p.add_argument("--prompt", action="store_true", help="also print the rendered prompt blocks")
    a = p.parse_args()
    res = retrieve(a.message, a.history)
    print(_summary(res))
    if a.prompt:
        print("\n" + format_for_prompt(res))


if __name__ == "__main__":
    main()
