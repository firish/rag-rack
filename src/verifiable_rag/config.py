"""YAML pipeline config loader — build any :class:`Pipeline` from a config file.

Schema
------

The config is a single YAML document with up to eight top-level keys, one
per pipeline component. Each component is ``{type: <name>, config: {...}}``:

.. code-block:: yaml

    parser:
      type: docling
      fallback: pymupdf       # optional: chain a fallback parser
      cache: true             # optional: wrap with CachingParser

    chunker:
      type: parent_child
      config:
        max_child_tokens: 400
        min_child_tokens: 100
      contextual:             # optional ContextualChunker wrapper
        enabled: false
        granularity: section  # section | paragraph | chunk
        model: claude-haiku-4-5-20251001

    embedder:
      type: cohere            # cohere | bge | voyage
      config: {}

    indexer:
      dense:
        type: lancedb
        uri: .verifiable_rag_cache/indexes/my_index
      sparse:
        type: bm25

    reranker:
      type: cohere            # cohere | bge | none
      config: {}

    generator:
      type: constrained       # prompted | constrained | safe
      config:
        model: anthropic/claude-haiku-4-5

    verifier:
      type: dual_nli          # none | hhem | minicheck | dual_nli | llm_judge
      config:
        threshold: 0.0562
        aggregation: min

    pipeline:                 # top-level Pipeline knobs
      strictness: balanced
      top_k_retrieve: 100
      top_k_rerank: 10

Then::

    from verifiable_rag import Pipeline
    pipeline = Pipeline.from_yaml("pipeline.yaml")

Discovery
---------

To see what types are available for each component, call
:func:`registered_types`::

    >>> from verifiable_rag.config import registered_types
    >>> registered_types()
    {'parser': ['docling', 'pymupdf'], 'embedder': ['bge', 'cohere', ...], ...}

Each entry in the registry maps to a factory function that takes the
``config:`` dict and returns the component. New components plug in via
:func:`register`.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from verifiable_rag.pipeline import Pipeline


# --------------------------------------------------------------------------- #
# Component registry
# --------------------------------------------------------------------------- #


_REGISTRY: dict[str, dict[str, Callable[..., Any]]] = {
    "parser": {},
    "chunker": {},
    "embedder": {},
    "dense_indexer": {},
    "sparse_indexer": {},
    "reranker": {},
    "generator": {},
    "verifier": {},
    "scorer": {},  # NLIScorer factories — used by dual_nli verifier
}


def register(component: str, name: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator: register a factory under ``REGISTRY[component][name]``."""
    if component not in _REGISTRY:
        raise ValueError(
            f"Unknown component {component!r}; choose from {sorted(_REGISTRY)}"
        )

    def _wrap(fn: Callable[..., Any]) -> Callable[..., Any]:
        _REGISTRY[component][name] = fn
        return fn

    return _wrap


def registered_types() -> dict[str, list[str]]:
    """Public view of the registry — ``{component: [type1, type2, ...]}``.

    Useful for discoverability::

        for component, types in registered_types().items():
            print(f"{component}: {types}")
    """
    return {k: sorted(v) for k, v in _REGISTRY.items()}


# --------------------------------------------------------------------------- #
# Built-in factories — wire each public component
# --------------------------------------------------------------------------- #


@register("parser", "docling")
def _docling_parser(**_kw: Any) -> Any:
    from verifiable_rag.parsers import DoclingParser

    return DoclingParser()


@register("parser", "pymupdf")
def _pymupdf_parser(**_kw: Any) -> Any:
    from verifiable_rag.parsers import PyMuPDFParser

    return PyMuPDFParser()


@register("chunker", "parent_child")
def _parent_child_chunker(
    max_child_tokens: int = 400, min_child_tokens: int = 100, **_kw: Any
) -> Any:
    from verifiable_rag.chunkers import ParentChildChunker

    return ParentChildChunker(
        max_child_tokens=max_child_tokens, min_child_tokens=min_child_tokens
    )


@register("embedder", "bge")
def _bge_embedder(
    model_name: str = "BAAI/bge-small-en-v1.5", **_kw: Any
) -> Any:
    from verifiable_rag.embedders import SentenceTransformerEmbedder

    return SentenceTransformerEmbedder(model_name=model_name)


@register("embedder", "cohere")
def _cohere_embedder(**_kw: Any) -> Any:
    from verifiable_rag.embedders import CohereEmbedder

    return CohereEmbedder()


@register("embedder", "voyage")
def _voyage_embedder(**_kw: Any) -> Any:
    from verifiable_rag.embedders import VoyageEmbedder

    return VoyageEmbedder()


@register("dense_indexer", "lancedb")
def _lancedb_index(uri: str | Path | None = None, **_kw: Any) -> Any:
    from verifiable_rag.indexers import LanceDBIndex

    return LanceDBIndex(uri=Path(uri)) if uri else LanceDBIndex()


@register("sparse_indexer", "bm25")
def _bm25_index(**_kw: Any) -> Any:
    from verifiable_rag.indexers import BM25Index

    return BM25Index()


@register("reranker", "bge")
def _bge_reranker(**_kw: Any) -> Any:
    from verifiable_rag.rerankers import BGERerankerV2

    return BGERerankerV2()


@register("reranker", "cohere")
def _cohere_reranker(**_kw: Any) -> Any:
    from verifiable_rag.rerankers import CohereReranker

    return CohereReranker()


@register("generator", "prompted")
def _prompted_generator(model: str = "anthropic/claude-haiku-4-5", **_kw: Any) -> Any:
    from verifiable_rag.generators import PromptedCitedGenerator

    return PromptedCitedGenerator(model=model)


@register("generator", "constrained")
def _constrained_generator(
    model: str = "anthropic/claude-haiku-4-5", **_kw: Any
) -> Any:
    from verifiable_rag.generators import ConstrainedCitedGenerator

    return ConstrainedCitedGenerator(model=model)


@register("generator", "safe")
def _safe_generator(model: str = "anthropic/claude-haiku-4-5", **_kw: Any) -> Any:
    from verifiable_rag.generators import SAFECitedGenerator

    return SAFECitedGenerator(model=model)


@register("scorer", "hhem")
def _hhem_scorer(**kw: Any) -> Any:
    from verifiable_rag.verifiers import HHEMVerifier

    return HHEMVerifier(**kw)


@register("scorer", "minicheck")
def _minicheck_scorer(**kw: Any) -> Any:
    from verifiable_rag.verifiers import MiniCheckVerifier

    return MiniCheckVerifier(**kw)


@register("scorer", "llm_judge")
def _llm_judge_scorer(**kw: Any) -> Any:
    from verifiable_rag.verifiers import LLMJudgeVerifier

    return LLMJudgeVerifier(**kw)


@register("verifier", "hhem")
def _hhem_verifier(**kw: Any) -> Any:
    from verifiable_rag.verifiers import HHEMVerifier

    return HHEMVerifier(**kw)


@register("verifier", "dual_nli")
def _dual_nli_verifier(
    scorer_a: str = "hhem",
    scorer_b: str = "minicheck",
    aggregation: str = "min",
    threshold: float = 0.0562,
    scorer_a_config: dict[str, Any] | None = None,
    scorer_b_config: dict[str, Any] | None = None,
    **_kw: Any,
) -> Any:
    """DualNLIVerifier with two named scorers from the scorer registry."""
    from verifiable_rag.verifiers import DualNLIVerifier

    a = _instantiate("scorer", scorer_a, scorer_a_config or {})
    b = _instantiate("scorer", scorer_b, scorer_b_config or {})
    return DualNLIVerifier(a, b, aggregation=aggregation, threshold=threshold)


# --------------------------------------------------------------------------- #
# YAML loading
# --------------------------------------------------------------------------- #


def _instantiate(component: str, type_name: str, config: dict[str, Any]) -> Any:
    """Look up ``REGISTRY[component][type_name]`` and call it with ``**config``."""
    if component not in _REGISTRY:
        raise ValueError(
            f"Unknown component {component!r}; choose from {sorted(_REGISTRY)}"
        )
    factories = _REGISTRY[component]
    if type_name not in factories:
        raise ValueError(
            f"Unknown {component} type {type_name!r}; "
            f"choose from {sorted(factories)}"
        )
    return factories[type_name](**config)


def load_pipeline_from_yaml(path: str | Path) -> "Pipeline":
    """Build a :class:`Pipeline` from a YAML config file.

    See the module docstring for the schema. Raises ``ValueError`` with
    a clear message on unknown component types or missing required keys.
    """
    try:
        import yaml
    except ImportError as exc:
        raise ImportError(
            "PyYAML is required for YAML config loading. "
            "Install with: pip install 'verifiable-rag[yaml]'"
        ) from exc

    from verifiable_rag.chunkers import ContextualChunker, LLMContextualizer
    from verifiable_rag.indexers import HybridIndex
    from verifiable_rag.parsers._cache import CachingParser
    from verifiable_rag.parsers.composite import CompositeParser
    from verifiable_rag.pipeline import Pipeline

    path = Path(path)
    with path.open() as fh:
        cfg = yaml.safe_load(fh) or {}

    # Required components
    parser_obj = _build_parser(cfg.get("parser", {}))
    chunker_obj = _build_chunker(cfg.get("chunker", {}))
    embedder_obj = _instantiate(
        "embedder",
        cfg["embedder"]["type"] if "embedder" in cfg else "bge",
        cfg.get("embedder", {}).get("config", {}),
    )
    indexer_obj = _build_indexer(cfg.get("indexer", {}))
    generator_obj = _instantiate(
        "generator",
        cfg["generator"]["type"] if "generator" in cfg else "prompted",
        cfg.get("generator", {}).get("config", {}),
    )

    # Optional components
    reranker_obj = None
    if "reranker" in cfg and cfg["reranker"].get("type") not in (None, "none"):
        reranker_obj = _instantiate(
            "reranker",
            cfg["reranker"]["type"],
            cfg["reranker"].get("config", {}),
        )

    verifier_obj = None
    if "verifier" in cfg and cfg["verifier"].get("type") not in (None, "none"):
        verifier_obj = _instantiate(
            "verifier",
            cfg["verifier"]["type"],
            cfg["verifier"].get("config", {}),
        )

    pipeline_kw = cfg.get("pipeline", {}) or {}
    return Pipeline(
        parser=parser_obj,
        chunker=chunker_obj,
        embedder=embedder_obj,
        indexer=indexer_obj,
        reranker=reranker_obj,
        generator=generator_obj,
        verifier=verifier_obj,
        strictness=pipeline_kw.get("strictness", "balanced"),
        top_k_retrieve=pipeline_kw.get("top_k_retrieve", 20),
        top_k_rerank=pipeline_kw.get("top_k_rerank", 8),
    )


def _build_parser(spec: dict[str, Any]) -> Any:
    """Parser section supports composite (`fallback:`) and caching wrappers."""
    from verifiable_rag.parsers._cache import CachingParser
    from verifiable_rag.parsers.composite import CompositeParser

    if not spec:
        return _instantiate("parser", "pymupdf", {})
    primary = _instantiate("parser", spec.get("type", "pymupdf"), spec.get("config", {}))
    if "fallback" in spec:
        fallbacks = spec["fallback"]
        if isinstance(fallbacks, str):
            fallbacks = [fallbacks]
        fb_objs = [_instantiate("parser", fb, {}) for fb in fallbacks]
        primary = CompositeParser(primary=primary, fallbacks=fb_objs)
    if spec.get("cache"):
        primary = CachingParser(primary)
    return primary


def _build_chunker(spec: dict[str, Any]) -> Any:
    """Chunker section supports the optional ContextualChunker wrapper."""
    from verifiable_rag.chunkers import ContextualChunker, LLMContextualizer

    base = _instantiate(
        "chunker", spec.get("type", "parent_child"), spec.get("config", {})
    )
    ctx_spec = spec.get("contextual", {})
    if not ctx_spec.get("enabled"):
        return base
    contextualizer = LLMContextualizer(
        model=ctx_spec.get("model", "claude-haiku-4-5-20251001"),
        max_workers=ctx_spec.get("max_workers", 3),
        num_retries=ctx_spec.get("num_retries", 5),
    )
    return ContextualChunker(
        base=base,
        contextualizer=contextualizer,
        granularity=ctx_spec.get("granularity", "section"),
    )


def _build_indexer(spec: dict[str, Any]) -> Any:
    from verifiable_rag.indexers import HybridIndex

    dense_spec = spec.get("dense", {})
    sparse_spec = spec.get("sparse", {})
    dense = _instantiate(
        "dense_indexer", dense_spec.get("type", "lancedb"), dense_spec
    )
    sparse = _instantiate(
        "sparse_indexer", sparse_spec.get("type", "bm25"), sparse_spec
    )
    return HybridIndex(dense=dense, sparse=sparse)


__all__ = [
    "load_pipeline_from_yaml",
    "register",
    "registered_types",
]
