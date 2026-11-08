.PHONY: db-up db-down db-migrate smoke test ingest-gita ingest-mb draft-situations ingest-situations ingest-all search eval eval-heldout

PSQL = docker compose exec -T db psql -U krishna -d krishna -v ON_ERROR_STOP=1

db-up:            ## start Postgres (waits until healthy) and apply migrations
	docker compose up -d --wait db
	$(MAKE) db-migrate

db-down:
	docker compose down

db-migrate:       ## apply migrations/*.sql in order (each is idempotent)
	@for f in migrations/*.sql; do echo "applying $$f"; $(PSQL) -q -f /$$f || exit 1; done

ingest-gita:      ## download, validate, write data/clean/gita_verses.jsonl, upsert
	uv run python -m rag.ingest gita

ingest-mb:        ## Ganguli Mahabharata: download, validate, chunk, upsert (~1 h first run on M1)
	uv run python -m rag.ingest mb

draft-situations: ## LLM-draft data/situations/situations.yaml (only ids not already there); quotes checked against Ganguli
	uv run python -m rag.situations

ingest-situations: ## validate situations.yaml and upsert it
	uv run python -m rag.ingest situations

ingest-all: ingest-gita ingest-mb ingest-situations

search:           ## make search q="Amar boss amake shobar shamne opoman korlo"
	uv run python -m rag.search "$(q)" --prompt

eval:             ## run eval/queries.yaml through retrieve(), write eval/report.md
	uv run python -m eval.run_eval $(args)
eval-heldout:     ## same on eval/heldout.yaml -> eval/report_heldout.md
	uv run python -m eval.run_eval --queries heldout.yaml $(args)

smoke:            ## embed one sentence and round-trip it through the DB
	uv run python -m rag.smoke

test:
	uv run pytest -q
