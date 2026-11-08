"""Situations: Mahabharata episodes framed as modern dilemmas (data/situations/situations.yaml).

`python -m rag.situations` drafts entries with the LLM. Nothing the model says about the text is
trusted: a section is kept only if the model quotes it verbatim and the section names a character
or search term; otherwise the entry gets `sections: []` and `needs_check: true`. Verses can only
come from a candidate list taken from `gita_verses`. Every entry is written with `reviewed: false`.
Re-running drafts only ids not yet in the YAML, so hand edits are never overwritten.
"""
from __future__ import annotations

import argparse
import json
import logging
import re
from collections import defaultdict
from pathlib import Path

import yaml

from rag.config import ROOT, settings
from rag.ingest import read_jsonl
from rag.llm import chat_json
from rag.sources.ganguli import PARVAS
from rag.themes import canonical_list

log = logging.getLogger("situations")

SIT_DIR = settings.data_dir / "situations"
YAML_PATH = SIT_DIR / "situations.yaml"
PLAN_PATH = SIT_DIR / "plan.json"
PROMPTS = ROOT / "prompts"

TOPICS = [
    "duty to your role vs. love for your family (being asked to fight or oppose relatives)",
    "loyalty to a friend who helped you vs. telling the truth or doing what is right",
    "uncontrolled anger and its consequences",
    "grief after losing a child or someone you love",
    "envy of a rival's success",
    "public humiliation in front of others",
    "injustice when people in power stay silent",
    "a vow or promise that became a trap",
    "fear of failure and freezing before a big task",
    "choosing your own path or career vs. what others expect of you",
    "ego and pride that will not let you back down",
    "forgiving someone who wronged you deeply",
    "the urge for revenge",
    "being rejected or abandoned by family; questions of identity",
    "addiction or reckless risk-taking (gambling everything away)",
    "being excluded or looked down on because of birth or background",
    "a teacher or boss who demands an unfair sacrifice",
    "telling a lie for what seems a good cause",
    "trying to make peace before a conflict escalates",
    "a parent blind to their own child's faults",
    "jealousy and rivalry between siblings or cousins",
    "staying loyal to a friend or leader you know is doing wrong",
    "standing by a partner against fate or authority",
    "answering hard questions under pressure; keeping your head in a crisis",
    "patience and dignity through exile, setbacks or a long hard period",
    "guilt and emptiness after winning",
    "letting go and renouncing at the end of life",
    "a desperate act of violence born of humiliation and grief",
    "keeping your word even when it costs you dearly",
    "self-worth and dignity when people mock your weakness or circumstances",
    # added after the first eval: common problems with no matching episode yet
    "heartbreak: being rejected or left by someone you love",
    "loneliness and isolation, feeling that nobody understands you",
    "regret after acting in anger and hurting someone",
    "caring for a sick or dying loved one",
    "parents pushing you into a path that is not yours",
    "confessing a hidden mistake or secret to the people close to you",
    "jealousy and insecurity inside a marriage or relationship",
    "being falsely accused or doubted by people close to you",
    "someone you deeply respect stands on the wrong side",
    "losing your status and having to start over in humble work",
    "burnout from carrying everyone else's burdens",
    "estrangement from a sibling and the chance to reconcile",
    "being ignored or sidelined by your own children in old age",
    "temptation: being offered something you want that you know is wrong",
    "finding the courage to speak up when everyone else stays quiet",
]


# ---------- text helpers (pure, tested) ----------

def normalize(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def quote_in(quote: str, text: str, min_words: int = 6) -> bool:
    """True if `quote` appears verbatim in `text`, ignoring case and punctuation."""
    q = normalize(quote)
    return len(q.split()) >= min_words and f" {q} " in f" {normalize(text)} "


def candidate_sections(sections: dict[tuple[str, int], str], parva: str, terms: list[str],
                       guessed: list[int], k: int = 8) -> list[int]:
    """Top-k sections of `parva` by number of distinct terms present, then occurrences; plus guesses."""
    terms = [t.lower() for t in terms if t.strip()]
    scored = []
    for (p, s), text in sections.items():
        if p != parva:
            continue
        low = text.lower()
        if hits := sum(t in low for t in terms):
            scored.append((hits, sum(low.count(t) for t in terms), -s, s))
    top = [s for *_, s in sorted(scored, reverse=True)[:k]]
    return top + [s for s in guessed if (parva, s) in sections and s not in top]


def excerpt(text: str, terms: list[str], words: int = 300) -> str:
    """The `words`-long window of `text` containing the most term occurrences."""
    toks = text.split()
    if len(toks) <= words:
        return text
    low = [t.lower() for t in toks]
    terms = [t.lower() for t in terms]
    best = max(range(0, len(toks) - words + 1, 50), key=lambda i: sum(any(t in w for t in terms) for w in low[i:i + words]))
    return " ".join(toks[best:best + words])


# ---------- data ----------

def load_sections() -> dict[tuple[str, int], str]:
    """(parva, section) -> section text, rebuilt from chunks (overlap left in; fine for lookup)."""
    parts: dict[tuple[str, int], list[tuple[int, str]]] = defaultdict(list)
    for c in read_jsonl(settings.data_dir / "clean" / "mb_passages.jsonl"):
        parts[(c["parva"], c["section"])].append((c["chunk_index"], c["text"]))
    return {k: "\n\n".join(t for _, t in sorted(v)) for k, v in parts.items()}


def load_verses() -> dict[str, str]:
    return {v["id"]: v["translation"] for v in read_jsonl(settings.data_dir / "clean" / "gita_verses.jsonl")}


def load_yaml(path: Path = YAML_PATH) -> list[dict]:
    if not path.exists():
        return []
    return yaml.safe_load(path.read_text(encoding="utf-8")) or []


def save_yaml(entries: list[dict], path: Path = YAML_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(entries, sort_keys=False, allow_unicode=True, width=100), encoding="utf-8")


def validate(entries: list[dict], verse_ids: set[str], section_keys: set[tuple[str, int]]) -> list[str]:
    """Problems that block ingestion. Empty list means OK."""
    errs, seen = [], set()
    for e in entries:
        eid = e.get("id", "?")
        for f in ("id", "title", "parva", "dilemma", "themes", "sections", "related_verses", "reviewed"):
            if f not in e:
                errs.append(f"{eid}: missing {f}")
        if eid in seen:
            errs.append(f"{eid}: duplicate id")
        seen.add(eid)
        parva = str(e.get("parva", "")).lower()
        if parva not in PARVAS:
            errs.append(f"{eid}: unknown parva {e.get('parva')!r}")
        if not isinstance(e.get("reviewed"), bool):
            errs.append(f"{eid}: reviewed must be true/false")
        errs += [f"{eid}: unknown verse {v}" for v in e.get("related_verses", []) if v not in verse_ids]
        errs += [f"{eid}: no section {parva}-{s}" for s in e.get("sections", []) if (parva, s) not in section_keys]
        if not e.get("sections") and not e.get("needs_check"):
            errs.append(f"{eid}: empty sections needs needs_check: true")
    return errs


def embed_text(e: dict) -> str:
    text = f"{e['title']}\n{e['dilemma'].strip()}\nThemes: {', '.join(e['themes'])}"
    if e.get("everyday"):
        text += "\nSounds like: " + " / ".join(e["everyday"])
    return text


# ---------- drafting ----------

def plan(n: int | None = None) -> list[dict]:
    """Episodes for TOPICS[:n]. Topics already in plan.json are kept; only new topics are planned."""
    out: list[dict] = json.loads(PLAN_PATH.read_text(encoding="utf-8")) if PLAN_PATH.exists() else []
    done_topics = {it.get("topic_number") for it in out}
    topics = [(i, t) for i, t in enumerate(TOPICS[:n], 1) if i not in done_topics]
    if not topics:
        log.info("reusing %s (all topics planned)", PLAN_PATH)
        return out
    template = (PROMPTS / "draft_situations_plan.md").read_text(encoding="utf-8")
    seen: set[str] = {it["id"] for it in out}
    for b in range(0, len(topics), 6):  # small batches: long replies get truncated
        batch = topics[b:b + 6]
        prompt = template.format(parvas=", ".join(PARVAS), n=len(batch),
                                 taken="\n".join(f"- {it['title']}" for it in out) or "(none yet)",
                                 topics="\n".join(f"{i}. {t}" for i, t in batch))
        for it in chat_json("You are a careful scholar of the Mahabharata.", prompt, max_tokens=16000):
            if it.get("id") in seen or str(it.get("parva", "")).lower() not in PARVAS:
                log.warning("dropping plan item %s (duplicate id or bad parva %r)", it.get("id"), it.get("parva"))
                continue
            seen.add(it["id"])
            out.append(it)
        log.info("plan: %d episodes so far", len(out))
    SIT_DIR.mkdir(parents=True, exist_ok=True)
    PLAN_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    log.info("plan: %d episodes -> %s", len(out), PLAN_PATH)
    return out


def similar_verses(conn, embedder, text: str, k: int = 8) -> list[str]:
    vec = embedder.embed([text])[0]
    rows = conn.execute("select id from chunks where collection = 'gita_verses' order by embedding <=> %s::vector limit %s",
                        (vec, k)).fetchall()
    return [r[0] for r in rows]


def draft_one(item: dict, sections, verses, conn, embedder) -> dict:
    parva = item["parva"].lower()
    terms = list(dict.fromkeys(item.get("characters", []) + item.get("search_terms", [])))
    guessed = [s for s in item.get("sections", []) if isinstance(s, int)]
    cands = candidate_sections(sections, parva, terms, guessed)
    verse_ids = similar_verses(conn, embedder, f"{item['title']}. {item['focus']}")
    prompt = (PROMPTS / "draft_situation.md").read_text(encoding="utf-8").format(
        title=item["title"], parva=parva.capitalize(), characters=", ".join(item.get("characters", [])),
        focus=item["focus"],
        excerpts="\n\n".join(f"[Section {s}]\n{excerpt(sections[(parva, s)], terms)}" for s in cands) or "(none found)",
        verses="\n".join(f"[{v}] {verses[v]}" for v in verse_ids),
    )
    reply = chat_json("You are a careful scholar of the Mahabharata. You never invent text.", prompt, max_tokens=10000)

    evidence, rejected = [], []
    for c in reply.get("sections", []):
        s, q = c.get("section"), c.get("quote", "")
        text = sections.get((parva, s), "")
        ok = s in cands and quote_in(q, text) and any(t.lower() in text.lower() for t in terms)
        (evidence if ok else rejected).append({"section": s, "quote": q})
    entry = {
        "id": item["id"], "title": item["title"], "parva": parva.capitalize(),
        "sections": sorted({e["section"] for e in evidence}),
        "characters": item.get("characters", []),
        "dilemma": reply.get("dilemma", "").strip(),
        "themes": canonical_list(reply.get("themes", []))[:6],
        "related_verses": [v for v in reply.get("related_verses", []) if v in verse_ids][:3],
        "reviewed": False,
    }
    if not entry["sections"]:
        entry["needs_check"] = True
        entry["check_reason"] = ("model's quotes not found in the text: " + ", ".join(str(r["section"]) for r in rejected)
                                 if rejected else f"no candidate section narrates the episode (looked at {cands})")
    entry["evidence"] = evidence  # verbatim Ganguli quotes backing each section, for your review
    return entry


def duplicate_of(new: dict, entries: list[dict]) -> str | None:
    """Id of an existing entry in the same parva sharing a verified section with `new`, if any."""
    for e in entries:
        if e["parva"] == new["parva"] and set(e["sections"]) & set(new["sections"]):
            return e["id"]
    return None


def add_everyday(entries: list[dict]) -> None:
    """Fill `everyday`: modern first-person phrasings of the dilemma (no story content), for matching."""
    template = (PROMPTS / "situation_everyday.md").read_text(encoding="utf-8")
    for e in entries:
        if e.get("everyday"):
            continue
        try:
            lines = chat_json("You write realistic short chat messages. Reply with JSON only.",
                              template.format(title=e["title"], dilemma=e["dilemma"].strip()), max_tokens=2000)
            e["everyday"] = [str(x).strip() for x in lines if str(x).strip()][:5]
        except Exception as err:  # keep going; the entry is still usable without it
            log.error("%s: everyday phrasings failed: %s", e["id"], err)
            continue
        save_yaml(entries)
        log.info("everyday phrasings: %s", e["id"])


def draft(n: int | None = None) -> int:
    from rag.db import connect
    from rag.embed import get_embedder

    sections, verses = load_sections(), load_verses()
    entries = load_yaml()
    done = {e["id"] for e in entries}
    todo = [it for it in plan(n) if it["id"] not in done]
    log.info("%d already in %s, drafting %d", len(done), YAML_PATH, len(todo))
    embedder = get_embedder()
    with connect() as conn:
        for i, item in enumerate(todo, 1):
            try:
                new = draft_one(item, sections, verses, conn, embedder)
                if dup := duplicate_of(new, entries):
                    log.warning("%s: dropped, its sections overlap existing entry %s", new["id"], dup)
                    continue
                entries.append(new)
            except Exception as e:  # one bad reply should not lose the others
                log.error("%s: drafting failed: %s", item.get("id"), e)
                continue
            save_yaml(entries)  # after every entry, so an interrupted run keeps its work
            log.info("[%d/%d] %s -> sections=%s", i, len(todo), item["id"], entries[-1]["sections"])

    add_everyday(entries)
    print(report(entries, set(verses), set(sections)))
    return 0


def report(entries: list[dict], verse_ids: set[str], section_keys: set[tuple[str, int]]) -> str:
    check = [e for e in entries if e.get("needs_check")]
    errs = validate(entries, verse_ids, section_keys)
    out = [
        "Situations draft report",
        f"  entries: {len(entries)}   reviewed: {sum(e.get('reviewed') is True for e in entries)}",
        f"  parvas used: {len({e['parva'] for e in entries})}",
        f"  with verified sections: {len(entries) - len(check)}",
        f"  needs_check: {len(check)}",
    ]
    out += [f"    - {e['id']}: {e.get('check_reason', '')}" for e in check]
    out += [f"  entries without related_verses: {[e['id'] for e in entries if not e['related_verses']] or 'none'}",
            f"  validation errors: {errs or 'none'}"]
    return "\n".join(out)


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
    for noisy in ("httpx", "httpcore", "huggingface_hub", "sentence_transformers"):
        logging.getLogger(noisy).setLevel(logging.WARNING)
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("-n", type=int, default=None, help="plan only the first n topics (default: all)")
    raise SystemExit(draft(p.parse_args().n))


if __name__ == "__main__":
    main()
