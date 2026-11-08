-- Safe to re-run: every statement is IF NOT EXISTS.
create extension if not exists vector;

create table if not exists chunks (
  id text primary key,
  collection text not null,       -- gita_verses | mb_passages | situations
  content text not null,          -- the text that was embedded
  meta jsonb not null,            -- all other fields, incl. content_hash
  embedding vector(1024),
  tsv tsvector generated always as (to_tsvector('english', content)) stored
);

create index if not exists chunks_embedding_hnsw on chunks using hnsw (embedding vector_cosine_ops);
create index if not exists chunks_tsv_gin on chunks using gin (tsv);
create index if not exists chunks_collection_idx on chunks (collection);
