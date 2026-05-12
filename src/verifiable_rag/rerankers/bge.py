"""BGERerankerV2: cross-encoder reranker backed by ``BAAI/bge-reranker-v2-m3``.

A bi-encoder (used in dense retrieval) embeds query and passage independently,
then computes cosine similarity over those isolated summaries.  A cross-encoder
takes the (query, passage) PAIR jointly through a transformer with full
attention — much more accurate at relevance scoring, but ~50ms per pair on
CPU vs. nanoseconds for a dot-product.

Two-stage retrieval pattern
---------------------------
1. Hybrid retrieval (dense + sparse + RRF) gets ~80 candidates fast.
2. Cross-encoder reranks those candidates and returns the top ~8 to the LLM.

This keeps cost bounded: we pay for at most ``top_k_retrieve`` cross-encoder
inferences per query (not per chunk in the corpus).

Score convention
----------------
The cross-encoder emits a single score per pair; higher = more relevant.
The original ``RetrievedChunk.score`` (RRF) is replaced by the cross-encoder
score, and ``retrieval_method`` is updated to ``"reranked"`` so downstream
code can tell which stage produced the ranking.
"""

from __future__ import annotations

from typing import Any

from verifiable_rag.models.chunk import RetrievedChunk


class BGERerankerV2:
    """Cross-encoder reranker using BGE rerank v2-m3 via sentence-transformers.

    Parameters
    ----------
    model_name:
        HuggingFace model id. Default ``"BAAI/bge-reranker-v2-m3"``
        (multilingual, ~568M params). Pass ``"BAAI/bge-reranker-v2-base"``
        for a smaller/faster variant.
    batch_size:
        Pairs per forward pass. Larger = faster on GPU, OOM risk on CPU.
    device:
        ``"cpu"``, ``"cuda"``, ``"mps"``, or ``None`` to autodetect.
    max_length:
        Truncation cap (tokens) for each (query, chunk) pair fed to the model.
        Reranker-v2-m3 supports up to 8192; 512 is enough for ~400-token
        chunks plus a query.
    """

    def __init__(
        self,
        model_name: str = "BAAI/bge-reranker-v2-m3",
        batch_size: int = 16,
        device: str | None = None,
        max_length: int = 512,
    ) -> None:
        if batch_size < 1:
            raise ValueError(f"batch_size must be >= 1, got {batch_size}")
        if max_length < 1:
            raise ValueError(f"max_length must be >= 1, got {max_length}")

        self._model_name = model_name
        self._batch_size = batch_size
        self._device = device
        self._max_length = max_length
        self._model: Any = None  # lazy-loaded

    # ------------------------------------------------------------------ #
    # Reranker Protocol
    # ------------------------------------------------------------------ #

    def rerank(
        self,
        query: str,
        chunks: list[RetrievedChunk],
        top_k: int = 5,
    ) -> list[RetrievedChunk]:
        """Re-score *chunks* against *query* and return the top *top_k*."""
        if not chunks or top_k <= 0:
            return []
        if top_k >= len(chunks):
            top_k = len(chunks)

        model = self._load()
        pairs = [(query, rc.chunk.text) for rc in chunks]
        scores = model.predict(
            pairs,
            batch_size=self._batch_size,
            show_progress_bar=False,
        )

        # Sort by score DESC, take top_k
        ranked_indices = sorted(
            range(len(chunks)),
            key=lambda i: float(scores[i]),
            reverse=True,
        )[:top_k]

        return [
            RetrievedChunk(
                chunk=chunks[i].chunk,
                score=float(scores[i]),
                retrieval_method="reranked",
            )
            for i in ranked_indices
        ]

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #

    def _load(self) -> Any:
        if self._model is not None:
            return self._model
        try:
            from sentence_transformers import CrossEncoder
        except ImportError as exc:
            raise ImportError(
                "sentence-transformers is required for BGERerankerV2. "
                "Install with: pip install 'verifiable-rag[bge]'"
            ) from exc

        kwargs: dict[str, Any] = {"max_length": self._max_length}
        if self._device is not None:
            kwargs["device"] = self._device

        self._model = CrossEncoder(self._model_name, **kwargs)
        return self._model
