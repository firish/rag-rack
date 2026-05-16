"""CohereEmbedder: dense embeddings via Cohere's hosted API.

Cohere embed-v3 family is comparable to Voyage-3 on retrieval benchmarks
and uses an asymmetric input_type prefix (``"search_document"`` for chunks,
``"search_query"`` for queries) — same pattern as Voyage.

Models and dimensions
---------------------
  embed-english-v3.0         1024-dim
  embed-multilingual-v3.0    1024-dim
  embed-english-light-v3.0    384-dim   (cheaper, slightly lower quality)
  embed-multilingual-light-v3.0  384-dim

Authentication
--------------
Pass ``api_key`` directly, or set the ``COHERE_API_KEY`` env var.

Batching
--------
Cohere accepts up to 96 texts per request. ``embed()`` chunks larger lists.
"""
from __future__ import annotations

import os
from typing import Any

_COHERE_DIMENSIONS: dict[str, int] = {
    "embed-english-v3.0": 1024,
    "embed-multilingual-v3.0": 1024,
    "embed-english-light-v3.0": 384,
    "embed-multilingual-light-v3.0": 384,
}
_COHERE_BATCH_LIMIT = 96


class CohereEmbedder:
    """Production-grade embedder backed by Cohere's API.

    Parameters
    ----------
    model:
        Cohere embed model ID. Defaults to ``"embed-english-v3.0"``.
    api_key:
        Cohere API key. Falls back to ``COHERE_API_KEY`` env var.
    batch_size:
        Max texts per API call. Capped at 96 (Cohere's limit).
    """

    def __init__(
        self,
        model: str = "embed-english-v3.0",
        api_key: str | None = None,
        batch_size: int = 96,
    ) -> None:
        if model not in _COHERE_DIMENSIONS:
            raise ValueError(
                f"Unknown Cohere embed model {model!r}. "
                f"Known: {sorted(_COHERE_DIMENSIONS)}"
            )
        if batch_size < 1 or batch_size > _COHERE_BATCH_LIMIT:
            raise ValueError(
                f"batch_size must be 1-{_COHERE_BATCH_LIMIT}, got {batch_size}"
            )
        self._model = model
        self._api_key = api_key or os.environ.get("COHERE_API_KEY")
        self._batch_size = batch_size
        self._client: Any = None

    @property
    def dimension(self) -> int:
        return _COHERE_DIMENSIONS[self._model]

    def embed(self, texts: list[str]) -> list[list[float]]:
        if not texts:
            return []
        return self._call(texts, input_type="search_document")

    def embed_query(self, query: str) -> list[float]:
        return self._call([query], input_type="search_query")[0]

    def _load(self) -> Any:
        if self._client is None:
            try:
                import cohere
            except ImportError as exc:
                raise ImportError(
                    "cohere is required for CohereEmbedder. "
                    "Install with: pip install 'verifiable-rag[cohere]'"
                ) from exc
            if not self._api_key:
                raise RuntimeError(
                    "CohereEmbedder requires COHERE_API_KEY in env or "
                    "api_key kwarg."
                )
            self._client = cohere.ClientV2(api_key=self._api_key)
        return self._client

    def _call(self, texts: list[str], *, input_type: str) -> list[list[float]]:
        client = self._load()
        results: list[list[float]] = []
        for i in range(0, len(texts), self._batch_size):
            batch = texts[i : i + self._batch_size]
            response = client.embed(
                texts=batch,
                model=self._model,
                input_type=input_type,
                embedding_types=["float"],
            )
            # Cohere v2 API: response.embeddings.float is a list of vectors.
            batch_embs = response.embeddings.float_
            results.extend([list(v) for v in batch_embs])
        return results

    def __repr__(self) -> str:
        return f"CohereEmbedder(model={self._model!r}, dim={self.dimension})"
