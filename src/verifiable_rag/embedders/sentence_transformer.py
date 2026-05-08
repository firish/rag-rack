"""SentenceTransformerEmbedder: wraps sentence-transformers for dense retrieval.

Covers both dev and production BGE models:
  - BAAI/bge-small-en-v1.5  (384-dim, fast, good for dev/CI)
  - BAAI/bge-m3              (1024-dim, multilingual, 8K context, production)

BGE models use asymmetric encoding: queries get an instruction prefix that
improves retrieval recall; documents/passages do not.  The defaults table
below bakes in the right instruction per known model; override with
``query_instruction`` if you add another model.

The sentence-transformers model is loaded lazily on first encode call — so
constructing this class is always cheap.
"""
from __future__ import annotations

from typing import Any

# Known BGE query instructions (passages never use an instruction).
_QUERY_INSTRUCTIONS: dict[str, str] = {
    "BAAI/bge-small-en-v1.5": "Represent this sentence for searching relevant passages: ",
    "BAAI/bge-large-en-v1.5": "Represent this sentence for searching relevant passages: ",
    "BAAI/bge-m3": "",  # M3 is symmetric; no instruction needed
}


class SentenceTransformerEmbedder:
    """Dense embedder backed by sentence-transformers.

    Parameters
    ----------
    model_name:
        HuggingFace model ID.  Defaults to BGE-small-en-v1.5 (384-dim, fast).
    query_instruction:
        Prefix prepended to query strings before encoding.  ``None`` (default)
        uses the built-in table for known BGE models; set to ``""`` to disable
        for any other model.
    normalize:
        L2-normalise output vectors.  Keep ``True`` for cosine similarity
        (which is how LanceDB and most ANN indexes are configured).
    batch_size:
        Number of texts per encode call.  Tune down on low-VRAM GPUs.
    device:
        ``"cpu"``, ``"cuda"``, ``"mps"``, or ``None`` for auto-detect.
    """

    def __init__(
        self,
        model_name: str = "BAAI/bge-small-en-v1.5",
        query_instruction: str | None = None,
        normalize: bool = True,
        batch_size: int = 64,
        device: str | None = None,
    ) -> None:
        self._model_name = model_name
        self._query_instruction: str = (
            query_instruction
            if query_instruction is not None
            else _QUERY_INSTRUCTIONS.get(model_name, "")
        )
        self._normalize = normalize
        self._batch_size = batch_size
        self._device = device
        self._model: Any = None  # sentence_transformers.SentenceTransformer — lazy

    # ------------------------------------------------------------------ #
    # Embedder Protocol
    # ------------------------------------------------------------------ #

    @property
    def dimension(self) -> int:
        return int(self._load().get_sentence_embedding_dimension())

    def embed(self, texts: list[str]) -> list[list[float]]:
        """Embed a batch of document/passage strings."""
        if not texts:
            return []
        return self._encode(texts)

    def embed_query(self, query: str) -> list[float]:
        """Embed a single query string, prepending the instruction prefix."""
        prefixed = self._query_instruction + query if self._query_instruction else query
        return self._encode([prefixed])[0]

    # ------------------------------------------------------------------ #
    # Internals
    # ------------------------------------------------------------------ #

    def _load(self) -> Any:
        if self._model is None:
            try:
                from sentence_transformers import SentenceTransformer
            except ImportError as exc:
                raise ImportError(
                    "sentence-transformers is required for SentenceTransformerEmbedder. "
                    "Install with: pip install 'verifiable-rag[embedders]'"
                ) from exc
            self._model = SentenceTransformer(self._model_name, device=self._device)
        return self._model

    def _encode(self, texts: list[str]) -> list[list[float]]:
        model = self._load()
        vectors = model.encode(
            texts,
            batch_size=self._batch_size,
            normalize_embeddings=self._normalize,
            show_progress_bar=False,
        )
        # sentence-transformers returns np.ndarray; convert to plain Python floats
        return [v.tolist() for v in vectors]

    def __repr__(self) -> str:
        return (
            f"SentenceTransformerEmbedder(model={self._model_name!r}, "
            f"dim={self.dimension if self._model else '?'}, "
            f"normalize={self._normalize})"
        )
