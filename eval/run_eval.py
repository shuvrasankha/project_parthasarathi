"""Run retrieval on eval/queries.yaml and write eval/report.md. Reports numbers as they are; no tuning.

Theme match: both sides are mapped to the controlled vocabulary (data/themes.yaml, so "jealousy" ->
"envy"), then two themes match if equal or one contains the other ("fear" ~ "fear of failure").
"""
from __future__ import annotations

import argparse
import hashlib
import json
import logging
import time
from collections import defaultdict
from datetime import date
from pathlib import Path

import yaml

from rag.config import ROOT, settings
from rag.llm import chat_json
from rag.search import retrieve, rewrite
from rag.themes import canonical
from rag.ingest import read_jsonl

EVAL = ROOT / "eval"


def theme_match(a: str, b: str) -> bool:
    a, b = canonical(a), canonical(b)
    return a == b or a in b or b in a


def overlap(expected: list[str], got: list[str]) -> float | None:
    if not expected or not got:
        return None
    return sum(any(theme_match(e, g) for g in got) for e in expected) / len(expected)


def pct(xs: list[float | None]) -> str:
    xs = [x for x in xs if x is not None]
    return f"{100 * sum(xs) / len(xs):.0f}% (n={len(xs)})" if xs else "n/a (n=0)"


CACHE = EVAL / ".rewrite_cache.json"


def cached_rewrite(message: str, cache: dict, fresh: bool) -> tuple[str, list[str]]:
    """Rewrites keyed by message + prompt + LLM chain, so retrieval experiments see identical queries."""
    prompt = (ROOT / "prompts" / "query_rewrite.md").read_text(encoding="utf-8")
    key = hashlib.sha256(f"{settings.llm_provider}|{settings.groq_models}|{prompt}|{message}".encode()).hexdigest()
    if fresh or key not in cache:
        query, themes = rewrite(message)
        if query == message:  # rewrite failed and fell back to the raw message; don't cache that
            return query, themes
        cache[key] = [query, themes]
        CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
        time.sleep(2.1)  # stay under Groq's ~30 req/min so the primary model answers every query
    return cache[key][0], cache[key][1]


JUDGE_CACHE = EVAL / ".judge_cache.json"


def judge(message: str, query: str, hits: list, cache: dict) -> list[int | None]:
    """LLM relevance grades (0-2) for verses/passages; cached per (message, rewrite, item id)."""
    todo = [h for h in hits if f"{message}|{query}|{h.id}" not in cache]
    if todo:
        items = "\n\n".join(f"{i}. " + " ".join(h.content.split()[:150]) for i, h in enumerate(todo, 1))
        prompt = (ROOT / "prompts" / "eval_judge.md").read_text(encoding="utf-8").format(message=message, query=query, items=items)
        try:
            grades = chat_json("You are a strict, fair relevance judge. Reply with JSON only.", prompt, max_tokens=2000)["grades"]
            for h, g in zip(todo, grades):
                cache[f"{message}|{query}|{h.id}"] = max(0, min(2, int(g)))
            JUDGE_CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
        except Exception as e:  # an unjudged query is reported as missing, not as 0
            logging.warning("judge failed: %s", e)
        time.sleep(2.1)
    return [cache.get(f"{message}|{query}|{h.id}") for h in hits]


def mean(xs: list) -> float | None:
    xs = [x for x in xs if x is not None]
    return sum(xs) / len(xs) if xs else None


def main() -> None:
    logging.basicConfig(level=logging.WARNING)
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--queries", default="queries.yaml", help="file in eval/ (queries.yaml = dev, heldout.yaml)")
    ap.add_argument("--out", default=None, help="report file in eval/ (default report.md / report_heldout.md)")
    ap.add_argument("--fresh", action="store_true", help="ignore cached rewrites")
    ap.add_argument("--no-rewrite", action="store_true", help="search with the raw message, no LLM rewrite")
    ap.add_argument("--judge", action="store_true", help="LLM-grade verse/passage relevance (0-2)")
    args = ap.parse_args()
    out_name = args.out or ("report.md" if args.queries == "queries.yaml" else f"report_{Path(args.queries).stem}.md")
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    jcache = json.loads(JUDGE_CACHE.read_text(encoding="utf-8")) if JUDGE_CACHE.exists() else {}
    queries = yaml.safe_load((EVAL / args.queries).read_text(encoding="utf-8"))
    verses_with_themes = sum(bool(v.get("themes")) for v in read_jsonl(settings.data_dir / "clean" / "gita_verses.jsonl"))
    rows, by_lang = [], defaultdict(list)
    t0 = time.time()
    for q in queries:
        rw = (q["message"], []) if args.no_rewrite else cached_rewrite(q["message"], cache, args.fresh)
        r = retrieve(q["message"], rewritten=rw)
        sit_ids = [h.id for h in r.situations]
        sit_themes = [t for h in r.situations for t in h.meta.get("themes", [])]
        verse_themes = [t for h in r.verses for t in h.meta.get("themes", [])]
        exp = q.get("expected_situation")
        row = {
            "q": q, "r": r, "hit": (exp in sit_ids) if exp else None,
            "rewrite_ov": overlap(q["expected_themes"], r.themes),
            "sit_ov": overlap(q["expected_themes"], sit_themes),
            "verse_ov": overlap(q["expected_themes"], verse_themes),
        }
        if args.judge:
            g = judge(q["message"], r.rewritten_query, r.verses + r.passages, jcache)
            row["verse_rel"], row["passage_rel"] = mean(g[:len(r.verses)]), mean(g[len(r.verses):])
            row["grades"] = g
        rows.append(row)
        by_lang[q["lang"]].append(row)
        print(f"{q['id']} {'HIT ' if row['hit'] else 'miss' if exp else '    '} {q['message'][:60]}")
    elapsed = time.time() - t0

    out = [
        "# Retrieval eval report", "",
        f"- date: {date.today()}  set: {args.queries}  queries: {len(rows)}  runtime: {elapsed:.0f}s",
        f"- LLM chain: {settings.llm_provider} (groq: {settings.groq_models}; openrouter: {settings.openrouter_models};"
        f" nvidia: {settings.nvidia_model}; anthropic: {settings.rewrite_model}), rerank: {settings.rerank_enabled},"
        f" linked_first: {settings.linked_first}, fts_text: {settings.fts_text}, rewrite: {not args.no_rewrite}",
        "- theme match = mapped to data/themes.yaml, then equal or substring", "",
        "## Summary", "",
        "| metric | all | " + " | ".join(by_lang) + " |",
        "|---|---|" + "---|" * len(by_lang),
    ]
    metrics = [
        ("situation hit rate (expected in top 2)", "hit"),
        ("theme overlap: rewrite themes", "rewrite_ov"),
        ("theme overlap: retrieved situations' themes", "sit_ov"),
        ("theme overlap: retrieved verses' themes", "verse_ov"),
    ]
    if args.judge:
        metrics += [("verse relevance, LLM judge (0-2 as %)", "verse_rel_pct"), ("passage relevance, LLM judge (0-2 as %)", "passage_rel_pct")]
        for x in rows:
            x["verse_rel_pct"] = None if x.get("verse_rel") is None else x["verse_rel"] / 2
            x["passage_rel_pct"] = None if x.get("passage_rel") is None else x["passage_rel"] / 2
    for label, key in metrics:
        out.append(f"| {label} | {pct([x[key] for x in rows])} | " + " | ".join(pct([x[key] for x in v]) for v in by_lang.values()) + " |")
    out += ["", f"Verse theme overlap needs `themes` on verses; {verses_with_themes} of 701 verses have them so far.", "",
            "## Situation misses", ""]
    out += [f"- {x['q']['id']} ({x['q']['lang']}): expected `{x['q']['expected_situation']}`, got "
            + ", ".join(f"`{h.id}`" for h in x["r"].situations) for x in rows if x["hit"] is False] or ["- none"]
    out += ["", "## Per query", ""]
    for x in rows:
        q, r = x["q"], x["r"]
        exp = q.get("expected_situation")
        out += [
            f"### {q['id']} ({q['lang']}) {'— HIT' if x['hit'] else '— MISS' if exp else ''}", "",
            f"> {q['message']}", "",
            f"- rewritten: {r.rewritten_query}",
            f"- themes: {', '.join(r.themes) or '-'}  (expected: {', '.join(q['expected_themes'])})",
            f"- expected situation: {exp or '-'}",
            "- situations: " + ("; ".join(f"`{h.id}` {h.score:.4f}" for h in r.situations) or "-"),
            "- verses: " + ("; ".join(f"`{h.id}` {h.score:.3f} [{h.via}] {h.meta['translation'][:70]}…" for h in r.verses) or "-"),
            "- passages: " + ("; ".join(f"`{h.id}` {h.score:.3f} [{h.via}]" for h in r.passages) or "-"),
            *([f"- judge grades (verses then passages): {x['grades']}"] if args.judge else []),
            "",
        ]
    path = EVAL / out_name
    path.write_text("\n".join(out), encoding="utf-8")
    print(f"\nwrote {path}")
    print("\n".join(out[out.index("## Summary"):out.index("## Per query")]))


if __name__ == "__main__":
    main()
