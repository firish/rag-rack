"""HybridIndex: dense + sparse retrieval with Reciprocal Rank Fusion.

RRF (Reciprocal Rank Fusion) merges ranked lists without needing to normalise
raw scores onto a common scale.  For each candidate chunk the fused score is:

    rrf_score = Σ  1 / (k + rank_i)

where ``rank_i`` is the 1-based rank from retriever *i* and ``k`` (default 60)
is a smoothing constant that dampens the advantage of top-ranked results.

Design notes
------------
* We over-retrieve from each sub-index (``k * over_fetch`` candidates, capped
  at the index size) so that RRF has a rich enough pool to promote chunks that
  appear in both lists.
* Chunks that appear in only one list still score — they just receive a RRF
  contribution from one retriever only.
* Chunks are deduplicated by ``chunk_id``; the ``RetrievedChunk`` returned
  carries the merged RRF score and ``retrieval_method="hybrid"``.
"""
from __future__ import annotations

from typing import Any

from verifiable_rag.models.chunk import Chunk, RetrievedChunk


def _rrf_fuse(
    ranked_lists: list[list[RetrievedChunk]],
    k: int = 60,
) -> list[RetrievedChunk]:
    """Merge *ranked_lists* with RRF; return results sorted by descending score."""
    scores: dict[str, float] = {}
    best_chunk: dict[str, RetrievedChunk] = {}

    for ranked in ranked_lists:
        for rank, rc in enumerate(ranked, start=1):
            cid = rc.chunk.chunk_id
            scores[cid] = scores.get(cid, 0.0) + 1.0 / (k + rank)
            if cid not in best_chunk:
                best_chunk[cid] = rc

    return sorted(
        [
            RetrievedChunk(
                chunk=best_chunk[cid].chunk,
                score=score,
                retrieval_method="hybrid",
            )
            for cid, score in scores.items()
        ],
        key=lambda rc: rc.score,
        reverse=True,
    )


class HybridIndex:
    """Combined dense + sparse index with RRF fusion.

    Parameters
    ----------
    dense:
        A ``DenseIndex`` instance (e.g. ``LanceDBIndex``).
    sparse:
        A ``SparseIndex`` instance (e.g. ``BM25Index``).
    rrf_k:
        RRF smoothing constant (default 60, from the original RRF paper).
    over_fetch:
        Multiplier on *k* when querying sub-indexes.  Larger pools give RRF
        more candidates to promote chunks appearing in both lists.
    """

    def __init__(
        self,
        dense: Any,
        sparse: Any,
        rrf_k: int = 60,
        over_fetch: int = 3,
    ) -> None:
        if rrf_k <= 0:
            raise ValueError(f"rrf_k must be positive, got {rrf_k}")
        if over_fetch < 1:
            raise ValueError(f"over_fetch must be >= 1, got {over_fetch}")
        self._dense = dense
        self._sparse = sparse
        self._rrf_k = rrf_k
        self._over_fetch = over_fetch

    # ------------------------------------------------------------------ #
    # HybridIndex Protocol
    # ------------------------------------------------------------------ #

    def add(self, chunks: list[Chunk], embeddings: list[list[float]]) -> None:
        """Index *chunks* into both sub-indexes."""
        self._dense.add(chunks, embeddings)
        self._sparse.add(chunks)

    def search(
        self,
        query: str,
        query_embedding: list[float],
        k: int,
    ) -> list[RetrievedChunk]:
        """Return up to *k* chunks fused from dense and sparse results via RRF."""
        fetch = k * self._over_fetch
        dense_results = self._dense.search(query_embedding, fetch)
        sparse_results = self._sparse.search(query, fetch)
        fused = _rrf_fuse([dense_results, sparse_results], k=self._rrf_k)
        return fused[:k]

    # ------------------------------------------------------------------ #
    # Extra operations
    # ------------------------------------------------------------------ #

    def clear(self) -> None:
        """Clear both sub-indexes."""
        self._dense.clear()
        self._sparse.clear()

    @property
    def count(self) -> int:
        """Number of documents in the dense sub-index (both are kept in sync)."""
        return int(self._dense.count)
