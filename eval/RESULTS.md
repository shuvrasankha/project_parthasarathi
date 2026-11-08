# Improvement log (2026-11-07/08)

Judged on `heldout.yaml` (30 messages written before any change); `queries.yaml` is the dev set.
Rewrites are cached per prompt version, so retrieval experiments compare identical queries.
LLM: Groq `openai/gpt-oss-120b` (fallback `qwen/qwen3.8-27b`). Theme matching uses `data/themes.yaml`.
"judge" = LLM relevance grade 0-2 (as %) for retrieved verses/passages; same model family as the
rewriter and some grades fell back to Qwen on rate limits, so treat it as a rough signal.

Situation hit rate = expected situation in top 2. Labels name only the 30 original situations, so
new situations that answer a query well still count as misses.

| version | change | dev hit | held-out hit | held-out verses (judge) | held-out passages (judge) |
|---|---|---|---|---|---|
| v0 | baseline | 55% | 74% | – | – |
| v1 | drop duplicate Arjuna entry, fix 3 needs_check entries, canonical themes, everyday phrasings | 68% | 70% | – | – |
| v2 | rewrite chooses themes from the vocabulary | 73% | 74% | – | – |
| **v3 (current)** | +14 new situations (43 total) | 64% | 67% | 45% | 55% |
| v3 + LINKED_FIRST | situation-linked verses/passages ranked first | 64% | 67% | 31% | 48% |
| v3 + FTS_TEXT=themes | full-text search on themes only | 55% | 48% | 41% | 59% |
| v3 + RERANK_ENABLED | bge-reranker-v2-m3, 5-6x slower | 64% | 63% | 47% | 53% |

Kept: v1, v2, v3 data. Rejected (switches left off): LINKED_FIRST, FTS_TEXT=themes, rerank.
Also rejected: a 15-entry Groq-drafted batch (repeated existing episodes, 10/15 failed verification).

What the v3 misses show (reports: `report_v3_*.md`):
- new entries sometimes win with a fair substitute (Uttara freezing before battle for exam fear,
  Vikarna's protest for public humiliation) and sometimes a poor one (Draupadi's marital jealousy
  for sibling envy)
- `nala-damayanti-teaches-patience` (24 sections, generic phrasing) appears in 9 misses: a catch-all
- linked `related_verses` from drafts are weaker than direct verse matches

## Did the 14 new situations degrade retrieval? (label-free check, held-out)
The hit rate can't credit new entries, so the top-2 situations were LLM-judged (0-2) with all 43
entries vs. only the original 29 (one-off script, same cached rewrites):

| situations | relevance | grade 2 / 1 / 0 |
|---|---|---|
| original 29 | 66% | 25 / 29 / 6 |
| all 43 | 68% | 26 / 29 / 5 |

No overall degradation (difference is within noise). The top 2 changed for 14 of 30 queries: better
for 4 (h10, h14, h20, h25), worse for 2 (h02, h06: Draupadi's marital jealousy and Vikarna displacing
envy/humiliation matches), roughly even for the rest.
