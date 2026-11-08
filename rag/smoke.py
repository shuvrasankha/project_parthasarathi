"""Phase-1 smoke test: embed, upsert twice (second must skip), nearest-neighbour lookup, clean up."""
from __future__ import annotations

import logging
import time

from rag.db import Row, connect, upsert_chunks
from rag.embed import get_embedder


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    t = time.time()
    emb = get_embedder()
    print(f"model loaded in {time.time() - t:.1f}s on {emb.model.device}")  # type: ignore[attr-defined]

    rows = [
        Row("smoke-1", "You have a right to your work, but not to its fruits.", {"lang": "en"}),
        Row("smoke-2", "Amar boss amake shobar shamne opoman korlo.", {"lang": "banglish"}),
        Row("smoke-3", "The recipe needs two cups of flour.", {"lang": "en"}),
    ]
    with connect() as conn:
        t = time.time()
        first = upsert_chunks(conn, "smoke", rows, emb)
        print(f"first upsert: {first} in {time.time() - t:.2f}s")
        second = upsert_chunks(conn, "smoke", rows, emb)
        assert second.written == 0 and second.skipped == 3, second
        print(f"second upsert (should skip all): {second}")

        q = emb.embed(["My manager humiliated me in front of everyone"])[0]
        hits = conn.execute(
            "select id, 1 - (embedding <=> %s::vector) as sim from chunks where collection='smoke' order by embedding <=> %s::vector",
            (q, q),
        ).fetchall()
        for id_, sim in hits:
            print(f"  {id_}: cosine={sim:.3f}")
        assert hits[0][0] == "smoke-2", "cross-lingual match should rank first"

        dim = conn.execute("select vector_dims(embedding) from chunks where id='smoke-1'").fetchone()[0]
        assert dim == 1024, dim
        conn.execute("delete from chunks where collection='smoke'")
        conn.commit()
    print("SMOKE OK")


if __name__ == "__main__":
    main()
