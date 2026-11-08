# Krishna Guide: retrieval layer

Ingestion, indexing and search over the Bhagavad Gita and the Mahabharata for the Krishna Guide
chat app. No UI: the app calls `rag.search.retrieve()`.

Everything runs locally on an M1 Mac. The LLM (query rewrite and situation drafting) is the only
hosted part.

## Setup

Requirements: [uv](https://docs.astral.sh/uv/) and Docker (OrbStack on macOS).

```bash
uv sync
cp .env.example .env      # then fill in ANTHROPIC_API_KEY or NVIDIA_API_KEY
make db-up                # Postgres 16 + pgvector, applies migrations/
make ingest-all           # first run ~1.5 h on an M1 (BGE-M3 embedding of ~10.6k chunks)
make search q="Amar boss amake shobar shamne opoman korlo"
```

The first run downloads BAAI/bge-m3 (~2.3 GB) from Hugging Face.

### Configuration (`.env`, read by `rag/config.py`)

| variable | default | meaning |
|---|---|---|
| `DATABASE_URL` | `postgresql://krishna:krishna@localhost:5432/krishna` | Postgres |
| `EMBED_PROVIDER` / `EMBED_MODEL` | `bge-m3` / `BAAI/bge-m3` | embedding backend (`rag/embed.py`; add hosted providers there) |
| `EMBED_DEVICE` / `EMBED_BATCH_SIZE` | `mps` / `8` | falls back to CPU without MPS |
| `LLM_PROVIDER` | `anthropic` | `anthropic`, `groq`, `openrouter`, `nvidia`, or a fallback chain like `groq,openrouter` (`rag/llm.py`) |
| `ANTHROPIC_API_KEY` / `REWRITE_MODEL` | – / `claude-haiku-5-5` | used when `LLM_PROVIDER=anthropic` |
| `NVIDIA_API_KEY` / `NVIDIA_MODEL` / `NVIDIA_BASE_URL` | – / `nvidia/nemotron-3-ultra-550b-a55b` / NIM endpoint | used when `LLM_PROVIDER=nvidia` |
| `GROQ_API_KEY` / `GROQ_MODELS` | – / `openai/gpt-oss-120b,qwen/qwen3.8-27b` | used when `LLM_PROVIDER` includes `groq` |
| `OPENROUTER_API_KEY` / `OPENROUTER_MODELS` | – / three `:free` models | free models only; anything else is refused |
| `RERANK_ENABLED` / `RERANK_MODEL` | `false` / `BAAI/bge-reranker-v2-m3` | optional cross-encoder rerank (no gain in eval, 5-6x slower) |
| `LINKED_FIRST` | `false` | rank situation-linked verses/passages first (worse in eval) |
| `FTS_TEXT` | `all` | full-text query words: `all` or `themes` (worse in eval) |
| `DATA_DIR` | `data` | raw downloads and cleaned JSONL |

Changing the embedding model means re-embedding everything: the content hash only tracks the text.

## Commands

| command | what it does |
|---|---|
| `make db-up` / `make db-down` | start (and migrate) / stop Postgres |
| `make ingest-gita` | download Sanskrit + Besant, align 701 verses, validate, upsert `gita_verses` |
| `make ingest-mb` | download Ganguli, parse 18 parvas into sections, chunk, validate, upsert `mb_passages` |
| `make draft-situations` | LLM-draft `data/situations/situations.yaml` (only ids not already there) |
| `make ingest-situations` | validate the YAML and upsert `situations`; rows removed from the YAML are deleted |
| `make ingest-all` | the three ingests in order |
| `make search q="..."` | run `retrieve()` and print hits plus the rendered prompt blocks |
| `make eval` | run the 50 dev queries in `eval/queries.yaml`, write `eval/report.md` (`args="--judge"` adds LLM relevance grades) |
| `make eval-heldout` | same on the 30 held-out queries, `eval/report_heldout.md`; judge changes on this set |
| `make test` | parser, chunking, situation-check and RRF tests |
| `make smoke` | embedding + DB round-trip check |

All ingests are idempotent: rows are upserted by id, and a row is re-embedded only when its
content hash (stored in `meta.content_hash`) changes. Each step logs rows read, written and skipped,
and prints a validation report; it writes nothing if validation fails.

## Collections

All in one `chunks` table (`migrations/001_init.sql`), with `collection` set to:

- **`gita_verses`** (701). Id `2.47`. Sanskrit from the gita/gita repo, IAST generated locally,
  English from Annie Besant (1922). Embedded text: `translation` + `meaning_simple`. You write
  `meaning_simple` and `themes` in `data/clean/gita_verses.jsonl`; re-ingesting keeps them.
- **`mb_passages`** (9,891). Id `udyoga-144-1` (parva-section-chunk). Sections over ~600 tokens are
  split on paragraphs (sentences as a fallback) into ~500-token chunks with ~80 tokens of overlap,
  never mid-sentence. Bhishma 25–42 (the Gita inside the Mahabharata) carry `contains_gita: true`.
- **`situations`** (43 drafts). Episodes framed as modern dilemmas, in
  `data/situations/situations.yaml`. Embedded text: `title` + `dilemma` + `themes` + `everyday`
  (5 modern first-person phrasings of the dilemma, LLM-written, no story content). Themes come from
  the controlled vocabulary in `data/themes.yaml`.

### How situations are drafted (`rag/situations.py`)

1. The LLM picks one real episode for each of 30 dilemma topics (`data/situations/plan.json`;
   delete it to re-plan).
2. Candidate sections are found by searching the local Ganguli text for the episode's names.
3. The LLM reads excerpts and says which sections narrate the episode, quoting each one. A section
   is kept only if the quote is found verbatim in it. If none survive: `sections: []`,
   `needs_check: true` and a `check_reason`.
4. `related_verses` can only be chosen from 8 verses found by embedding search, shown with their text.
5. A draft whose verified sections overlap an existing entry (same parva) is dropped as a duplicate.
6. Every entry is written with `reviewed: false` and an `evidence` list of the verbatim quotes.
7. `everyday` phrasings are added for entries that lack them.

Add a topic to `TOPICS` in `rag/situations.py` and re-run to draft just that topic. Nemotron
(`LLM_PROVIDER=nvidia,openrouter`) drafted far better than Groq's gpt-oss in testing.

Review each entry by hand, set `reviewed: true`, then `make ingest-situations`.

## Retrieval (`rag/search.py`)

```python
from rag.search import retrieve, format_for_prompt
res = retrieve("Amar boss amake shobar shamne opoman korlo", history=["earlier message"])
system_prompt = format_for_prompt(res, template)   # fills {{retrieved_verses}} / {{retrieved_episodes}}
```

1. **Rewrite**: the LLM turns the message (any language) plus the last 6 history messages into a
   1–2 sentence English description and up to 5 themes (`prompts/query_rewrite.md`). If the call
   fails, search continues with the raw message; BGE-M3 is multilingual.
2. **Hybrid search** per collection: vector top-20 + full-text top-20 (`websearch_to_tsquery`,
   words OR-ed), merged with RRF, k=60 (`rag/rrf.py`).
3. **Situations first**: top 2 situations; their `related_verses` and the best-matching chunk of
   their `sections` become candidates.
4. Plus the top 3 direct verse matches and top 3 direct passage matches (deduplicated).
5. Verses (≤3) and passages (≤2) are ordered by cosine similarity to the query, or by the
   reranker when enabled. Linked items are guaranteed to be candidates, not to win.

`RetrievalResult` has `rewritten_query`, `themes`, `situations`, `verses`, `passages`; each hit has
`id`, `score`, `content`, `meta` and `via` (`direct` or `situation:<id>`).

## Evaluation

- `eval/queries.yaml`: 50 dev messages (25 English; 25 Hinglish, Hindi, Banglish, Bengali).
- `eval/heldout.yaml`: 30 messages written before any tuning; judge changes on these only.
- Reports: situation hit rate (expected in top 2), theme overlap (via `data/themes.yaml`), and with
  `--judge` an LLM relevance grade for verses and passages. Rewrites and grades are cached in
  `eval/.rewrite_cache.json` / `.judge_cache.json` (gitignored); `--fresh` re-asks.
- `eval/RESULTS.md`: the improvement log with every experiment, kept or rejected.

## Data sources

All public domain; details, URLs, retrieval dates and what was excluded are in
[data/SOURCES.md](data/SOURCES.md).

- Sanskrit Gita text: gita/gita `verse.json` (`text` field only; its transliteration, translations
  and commentaries are not used)
- English Gita: Annie Besant, 4th ed. 1922, via the Wikisource MediaWiki API
- Mahabharata: K. M. Ganguli, 1883–1896, Project Gutenberg ebooks 15474–15477

Raw downloads go to `data/raw/` (gitignored); cleaned JSONL goes to `data/clean/`.

## Layout

```
rag/            config, embed, db, chunking, llm, rrf, rerank, search, situations, ingest
rag/sources/    fetch (polite cached downloads), gita, ganguli
prompts/        query_rewrite.md, draft_situations_plan.md, draft_situation.md
migrations/     001_init.sql
data/           SOURCES.md, clean/, situations/, raw/ (gitignored)
eval/           queries.yaml, run_eval.py, report.md
tests/
```
