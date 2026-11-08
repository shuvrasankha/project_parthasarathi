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

## Without the LLM rewrite (2026-11-08)

`run_eval.py --no-rewrite`: search with the raw message and no themes, which is what `retrieve()` does when
the rewrite call fails. Same 43 situations, same judge.

| | dev v3 | dev no rewrite | held-out v3 | held-out no rewrite |
|---|---|---|---|---|
| situation hit rate | 64% | 36% | 67% | 59% |
| verse relevance (judge) | 58% | 29% | 45% | 27% |
| passage relevance (judge) | 56% | 44% | 55% | 43% |

The rewrite roughly doubles verse relevance. Without it, non-English messages suffer most (held-out Bengali
verses 6%, Hinglish and Banglish passages 10% and 8%; English passages hold up at 57%; n is 3-5 per language). The fallback works but is a big step down, so the
rewrite should stay; it needs a reliable LLM, not necessarily a fast or large one.
Reports: `report_norewrite_{dev,heldout}.md`.

## v4: sections filled for 4 needs_check entries (2026-11-08)

Sections found by searching the Ganguli text and checked with `quote_in`: Ekachakra (Adi 158-159),
Parashurama (Vana 116), Shakuntala (Adi 74), Vikarna (Sabha 66, shares the scene with
`draupadi-disrobing-sabha`). `vidura-insomnia-burden-of-knowledge` stays needs_check: in Udyoga 33 it is
Dhritarashtra who cannot sleep, not Vidura, so the entry itself is wrong.

Also fixed: `upsert_chunks` skipped rows whose text was unchanged even when their meta changed, so section
and `reviewed` edits never reached the DB. Meta is now updated without re-embedding.

| | dev v3 | dev v4 | held-out v3 | held-out v4 |
|---|---|---|---|---|
| situation hit rate | 64% | 64% | 67% | 67% |
| verse relevance (judge) | 58% | 58% | 45% | 46% |
| passage relevance (judge) | 56% | 58% | 55% | 55% |

Within noise, as expected for 4 entries.

Deleted `vidura-insomnia-burden-of-knowledge` (wrong character); marked `rejected` in plan.json. 42 situations.

## Linked vs direct verses (2026-11-08)

Judged grade of the verses and passages that make the final cut, by origin (cached grades, v4):

| | dev direct | dev linked | held-out direct | held-out linked |
|---|---|---|---|---|
| verses | 58% (n=123) | 56% (n=27) | 45% (n=70) | 50% (n=20) |
| passages | 57% (n=93) | 64% (n=7) | 55% (n=52) | 56% (n=8) |

Linked items are not worse once cosine ordering has picked them, so the planned filter was not built.
Verse quality is low across the board; that is a verse-text problem (`meaning_simple` is empty for all 701).

## v5: coverage gaps from the dev set (2026-11-08)

Judging the top-2 situations on every dev query (best grade of the two): 30 fit well, 16 partly, 4 not at all.
The weak ones cluster on career pressure from parents, grief for a parent, betrayal by a friend and parental
favouritism. Added 3 dev-derived topics (46-48) and re-ran drafting, which also retried topics 34 and 36:

- topics 34 (Pandu's death) and 36 (Kunti's confession): dropped again by the duplicate guard
- `bhishma-vow-for-father`: Adi 100, quote found by searching the text and checked with `quote_in`
- `drupada-insults-drona`: Adi 132-133, verified at drafting
- `dhritarashtra-ignores-bhima-poisoning`: needs_check. Adi 128-129 narrate the poisoning but not
  Dhritarashtra knowing about it, so the premise may be unsupported

| | dev v4 | dev v5 | held-out v4 | held-out v5 |
|---|---|---|---|---|
| situation hit rate | 64% | 64% | 67% | 70% |
| verse relevance (judge) | 58% | 58% | 46% | 46% |
| passage relevance (judge) | 58% | 58% | 55% | 53% |

Dev best-of-2 situation fit: 30/17/3 (was 30/16/4). Within noise; the new entries do surface for the career,
promise-to-a-parent and favouritism queries, but rarely as the best fit. 45 situations.
