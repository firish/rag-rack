"""LanceDBIndex: file-backed dense vector index.

Stores chunks as a columnar LanceDB table: one row per chunk, one float32
vector column, plus all fields needed to reconstruct Chunk and RetrievedChunk
at query time.  No server required — the database lives in a local directory.

Indexing strategy
-----------------
Flat (brute-force) scan is used by default.  For development and collections
up to ~50K vectors this is fine (<100 ms per query on CPU).  Call
``build_index()`` after bulk-loading to build an HNSW ANN index for larger
collections.

Score convention
----------------
LanceDB returns a ``_distance`` column.  For the cosine metric with
L2-normalised vectors, distance = 1 − similarity, so we report
score = 1 − distance (range [0, 1], higher = more similar).
For ``"l2"`` metric, score = −distance (negative, lower L2 = more similar).

Persistence
-----------
LanceDB auto-persists every write — no explicit flush or save needed.  The
database is ready to reopen after a crash or restart by constructing a new
instance pointing at the same URI.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from verifiable_rag.models.chunk import Chunk, RetrievedChunk
from verifiable_rag.models.span import BBox, PageBBox, Span


class LanceDBIndex:
    """Dense ANN index backed by LanceDB.

    Parameters
    ----------
    uri:
        Directory for the LanceDB database.  Created on first write.
    table_name:
        Name of the table inside the database.  Use different names to keep
        multiple collections in the same URI.
    metric:
        Distance metric: ``"cosine"`` (default, requires normalised vectors)
        or ``"l2"``.
    """

    DEFAULT_URI: Path = Path(".verifiable_rag_cache/indexes/lance")

    def __init__(
        self,
        uri: str | Path = DEFAULT_URI,
        table_name: str = "chunks",
        metric: str = "cosine",
    ) -> None:
        self._uri = Path(uri)
        self._table_name = table_name
        self._metric = metric
        self._db: Any = None
        self._table: Any = None

    # ------------------------------------------------------------------ #
    # DenseIndex Protocol
    # ------------------------------------------------------------------ #

    def add(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        """Persist *chunks* with their *embeddings*.  Appends if table exists."""
        if len(chunks) != len(embeddings):
            raise ValueError(
                f"chunks and embeddings length mismatch: "
                f"{len(chunks)} vs {len(embeddings)}"
            )
        if not chunks:
            return

        records = [self._chunk_to_row(c, e) for c, e in zip(chunks, embeddings, strict=True)]
        db = self._connect()

        if self._table_exists(db):
            tbl = db.open_table(self._table_name)
            tbl.add(records)
        else:
            tbl = db.create_table(self._table_name, records)
        self._table = tbl

    def search(
        self, query_embedding: list[float], k: int
    ) -> list[RetrievedChunk]:
        """Return up to *k* chunks nearest to *query_embedding*."""
        tbl = self._open_table()
        if tbl is None:
            return []

        rows: list[dict[str, Any]] = tbl.search(query_embedding).limit(k).to_list()
        results: list[RetrievedChunk] = []
        for row in rows:
            chunk = self._row_to_chunk(row)
            distance = float(row["_distance"])
            # LanceDB v0.30 cosine: _distance = 2*(1 - cos_similarity) ∈ [0,4]
            # Convert back to cosine similarity ∈ [-1, 1].
            # L2: report negative distance so higher score = smaller distance.
            score = (1.0 - distance / 2.0) if self._metric == "cosine" else -distance
            results.append(
                RetrievedChunk(chunk=chunk, score=score, retrieval_method="dense")
            )
        return results

    # ------------------------------------------------------------------ #
    # Extra operations (not in Protocol — LanceDB-specific)
    # ------------------------------------------------------------------ #

    def build_index(self) -> None:
        """Build an HNSW ANN index.  Call after bulk-loading for fast queries."""
        tbl = self._open_table()
        if tbl is None:
            raise RuntimeError(
                "Cannot build index: table is empty or does not exist yet."
            )
        tbl.create_index(metric=self._metric)

    def clear(self) -> None:
        """Drop the table and all indexed vectors."""
        db = self._connect()
        if self._table_exists(db):
            db.drop_table(self._table_name)
        self._table = None

    @property
    def count(self) -> int:
        """Number of vectors currently stored."""
        tbl = self._open_table()
        return 0 if tbl is None else int(tbl.count_rows())

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #

    def _connect(self) -> Any:
        if self._db is None:
            try:
                import lancedb
            except ImportError as exc:
                raise ImportError(
                    "lancedb is required for LanceDBIndex. "
                    "Install with: pip install 'verifiable-rag[lancedb]'"
                ) from exc
            self._uri.mkdir(parents=True, exist_ok=True)
            self._db = lancedb.connect(str(self._uri))
        return self._db

    def _table_exists(self, db: Any) -> bool:
        """Return True if the table already exists in the database."""
        # list_tables() is the current API (lancedb ≥0.9 / v0.30+).
        # table_names() still works but is deprecated; prefer the new form.
        try:
            result = db.list_tables()
            names: list[str] = result.tables if hasattr(result, "tables") else list(result)
        except AttributeError:
            names = list(db.table_names())  # fallback for very old versions
        return self._table_name in names

    def _open_table(self) -> Any:
        """Return the live table handle, or None if it doesn't exist yet."""
        if self._table is not None:
            return self._table
        db = self._connect()
        if self._table_exists(db):
            self._table = db.open_table(self._table_name)
            return self._table
        return None

    @staticmethod
    def _chunk_to_row(chunk: Chunk, embedding: list[float]) -> dict[str, Any]:
        return {
            "chunk_id": chunk.chunk_id,
            "doc_id": chunk.doc_id,
            "text": chunk.text,
            "sentence_ids_json": json.dumps(list(chunk.sentence_ids)),
            "metadata_json": json.dumps(chunk.metadata),
            "span_doc_id": chunk.span.doc_id,
            "span_char_start": chunk.span.char_start,
            "span_char_end": chunk.span.char_end,
            "span_bboxes_json": json.dumps(
                [
                    {
                        "page": pb.page,
                        "bbox": {
                            "x0": pb.bbox.x0,
                            "y0": pb.bbox.y0,
                            "x1": pb.bbox.x1,
                            "y1": pb.bbox.y1,
                        },
                    }
                    for pb in chunk.span.bboxes
                ]
            ),
            "vector": embedding,
        }

    @staticmethod
    def _row_to_chunk(row: Any) -> Chunk:
        """Reconstruct a Chunk from a pandas row returned by LanceDB."""
        sentence_ids: tuple[str, ...] = tuple(json.loads(row["sentence_ids_json"]))
        metadata: dict[str, Any] = json.loads(row["metadata_json"])
        bboxes = tuple(
            PageBBox(
                page=b["page"],
                bbox=BBox(
                    x0=b["bbox"]["x0"],
                    y0=b["bbox"]["y0"],
                    x1=b["bbox"]["x1"],
                    y1=b["bbox"]["y1"],
                ),
            )
            for b in json.loads(row["span_bboxes_json"])
        )
        span = Span(
            doc_id=row["span_doc_id"],
            char_start=int(row["span_char_start"]),
            char_end=int(row["span_char_end"]),
            bboxes=bboxes,
        )
        return Chunk(
            chunk_id=row["chunk_id"],
            text=row["text"],
            doc_id=row["doc_id"],
            sentence_ids=sentence_ids,
            span=span,
            metadata=metadata,
        )
