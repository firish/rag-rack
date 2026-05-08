"""BM25Index: sparse keyword retrieval index backed by bm25s.

bm25s builds an in-memory BM25 index in pure Python (NumPy backend) — no JVM,
no Elasticsearch, no server.  Index state is held in memory; call ``save()`` /
``load()`` for disk persistence between sessions.

Tokenisation
------------
We use bm25s's own ``tokenize()`` helper by default (lowercasing, punctuation
stripping, no stop-word removal).  Pass a custom ``tokenize`` callable at
construction for language-specific tokenisation.

Score convention
----------------
BM25 scores are non-negative; higher = more relevant.  Scores are not
comparable across different index sizes — use RRF fusion when combining with
cosine scores from a dense index.

Persistence
-----------
Call ``save(path)`` to write the index and corpus to disk.
Call ``BM25Index.load(path)`` to restore.  In-memory use works fine too.
"""
from __future__ import annotations

import json
from collections.abc import Callable
from pathlib import Path
from typing import Any

from verifiable_rag.models.chunk import Chunk, RetrievedChunk
from verifiable_rag.models.span import BBox, PageBBox, Span


class BM25Index:
    """Sparse BM25 retrieval index backed by bm25s.

    Parameters
    ----------
    tokenize:
        Callable ``(texts: list[str]) -> list[list[str]]`` that converts raw
        texts into token lists.  Defaults to ``bm25s.tokenize``.
    method:
        BM25 variant — ``"bm25"`` (Okapi, default), ``"bm25l"``, ``"bm25+"``.
    """

    def __init__(
        self,
        tokenize: Callable[[list[str]], Any] | None = None,
        method: str = "robertson",
    ) -> None:
        self._tokenize = tokenize
        self._method = method
        self._index: Any = None
        self._corpus: list[dict[str, Any]] = []

    # ------------------------------------------------------------------ #
    # SparseIndex Protocol
    # ------------------------------------------------------------------ #

    def add(self, chunks: list[Chunk]) -> None:
        """Index *chunks*.  Rebuilds the internal BM25 index from scratch."""
        if not chunks:
            return
        self._corpus.extend(self._chunk_to_row(c) for c in chunks)
        self._rebuild()

    def search(self, query: str, k: int) -> list[RetrievedChunk]:
        """Return up to *k* chunks ranked by BM25 score for *query*."""
        if self._index is None or not self._corpus:
            return []

        bm25s = self._import_bm25s()
        tokenizer = self._tokenize or bm25s.tokenize
        query_tokens = tokenizer([query])
        results, scores = self._index.retrieve(
            query_tokens,
            corpus=self._corpus,
            k=min(k, len(self._corpus)),
            show_progress=False,
        )

        retrieved: list[RetrievedChunk] = []
        for doc_row, score in zip(results[0], scores[0], strict=True):
            chunk = self._row_to_chunk(doc_row)
            retrieved.append(
                RetrievedChunk(chunk=chunk, score=float(score), retrieval_method="sparse")
            )
        return retrieved

    # ------------------------------------------------------------------ #
    # Extra operations
    # ------------------------------------------------------------------ #

    def clear(self) -> None:
        """Remove all indexed documents."""
        self._index = None
        self._corpus = []

    def save(self, path: str | Path) -> None:
        """Persist the index and corpus to *path* directory."""
        if self._index is None:
            raise RuntimeError("Nothing to save — index is empty.")
        path = Path(path)
        path.mkdir(parents=True, exist_ok=True)
        self._index.save(str(path / "bm25"))
        (path / "corpus.json").write_text(json.dumps(self._corpus, ensure_ascii=False))

    @classmethod
    def load(cls, path: str | Path) -> BM25Index:
        """Restore a previously saved BM25Index from *path* directory."""
        bm25s = cls._import_bm25s()
        path = Path(path)
        instance = cls()
        instance._index = bm25s.BM25.load(str(path / "bm25"), load_corpus=False)
        instance._corpus = json.loads((path / "corpus.json").read_text())
        return instance

    @property
    def count(self) -> int:
        """Number of documents currently indexed."""
        return len(self._corpus)

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #

    @staticmethod
    def _import_bm25s() -> Any:
        try:
            import bm25s
            return bm25s
        except ImportError as exc:
            raise ImportError(
                "bm25s is required for BM25Index. "
                "Install with: pip install 'verifiable-rag[bm25]'"
            ) from exc

    def _rebuild(self) -> None:
        bm25s = self._import_bm25s()
        texts = [row["text"] for row in self._corpus]
        tokenizer = self._tokenize or bm25s.tokenize
        tokenized = tokenizer(texts)
        index = bm25s.BM25(method=self._method)
        index.index(tokenized)
        self._index = index

    @staticmethod
    def _chunk_to_row(chunk: Chunk) -> dict[str, Any]:
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
        }

    @staticmethod
    def _row_to_chunk(row: dict[str, Any]) -> Chunk:
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
