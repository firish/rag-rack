"""CohereReranker: hosted reranker via Cohere's rerank API.

Network-bound (not CPU-bound like BGERerankerV2), so parallel asks scale
well — each rerank call hits Cohere's GPUs and returns in 100-500ms.

Authentication
--------------
``COHERE_API_KEY`` env var, or pass ``api_key=`` explicitly.

Limits
------
Cohere rerank accepts up to 100 documents per call. If you pass more, this
class raises rather than silently truncating.
"""
from __future__ import annotations

import os
from typing import Any

from verifiable_rag.models.chunk import RetrievedChunk

_COHERE_RERANK_LIMIT = 100


class CohereReranker:
    """Cohere-hosted cross-encoder reranker.

    Parameters
    ----------
    model:
        Cohere rerank model id. Defaults to ``"rerank-english-v3.0"``.
        Multilingual: ``"rerank-multilingual-v3.0"``. Newer: ``"rerank-v3.5"``.
    api_key:
        Cohere API key. Falls back to ``COHERE_API_KEY`` env var.
    """

    def __init__(
        self,
        model: str = "rerank-english-v3.0",
        api_key: str | None = None,
    ) -> None:
        self._model = model
        self._api_key = api_key or os.environ.get("COHERE_API_KEY")
        self._client: Any = None

    def rerank(
        self,
        query: str,
        chunks: list[RetrievedChunk],
        top_k: int = 5,
    ) -> list[RetrievedChunk]:
        if not chunks or top_k <= 0:
            return []
        if len(chunks) > _COHERE_RERANK_LIMIT:
            raise ValueError(
                f"CohereReranker accepts at most {_COHERE_RERANK_LIMIT} chunks "
                f"per call (got {len(chunks)}). Reduce top_k_retrieve."
            )

        client = self._load()
        documents = [rc.chunk.text for rc in chunks]
        response = client.rerank(
            model=self._model,
            query=query,
            documents=documents,
            top_n=min(top_k, len(chunks)),
        )

        # response.results is a list of objects with .index and .relevance_score
        return [
            RetrievedChunk(
                chunk=chunks[r.index].chunk,
                score=float(r.relevance_score),
                retrieval_method="reranked",
            )
            for r in response.results
        ]

    def _load(self) -> Any:
        if self._client is None:
            try:
                import cohere
            except ImportError as exc:
                raise ImportError(
                    "cohere is required for CohereReranker. "
                    "Install with: pip install 'verifiable-rag[cohere]'"
                ) from exc
            if not self._api_key:
                raise RuntimeError(
                    "CohereReranker requires COHERE_API_KEY in env or "
                    "api_key kwarg."
                )
            self._client = cohere.ClientV2(api_key=self._api_key)
        return self._client

    def __repr__(self) -> str:
        return f"CohereReranker(model={self._model!r})"
