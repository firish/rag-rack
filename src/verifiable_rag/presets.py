"""Preset pipeline factories — sensible component combos for common use cases.

Each factory returns a fully-wired :class:`Pipeline`. Imports are lazy
inside each function so the ``presets`` module itself doesn't pull in
torch / transformers / cohere unless a preset that uses them is actually
called — keeping ``import verifiable_rag`` fast.

When to use which preset
------------------------

+---------------------+---------------------------------------------+-------------+
| Preset              | Use case                                    | API keys    |
+=====================+=============================================+=============+
| ``local_minimal``   | Hobbyist / academic, no verification        | generator   |
+---------------------+---------------------------------------------+-------------+
| ``local_verified``  | Local everything + HHEM NLI verification    | generator   |
+---------------------+---------------------------------------------+-------------+
| ``hybrid_balanced`` | **Recommended.** Cohere retrieval + Dual NLI| generator + |
| (RECOMMENDED)       | + constrained Haiku generator               | Cohere      |
+---------------------+---------------------------------------------+-------------+
| ``hybrid_strict``   | Same as balanced, refuses on borderline     | generator + |
|                     | faithfulness                                | Cohere      |
+---------------------+---------------------------------------------+-------------+
| ``hybrid_paranoid`` | Sonnet generation, Dual NLI, hard refusal   | generator + |
|                     | unless extremely confident                  | Cohere      |
+---------------------+---------------------------------------------+-------------+
| ``llm_judge_       | LLM-as-judge verifier (Sonnet 4.6 default). | generator + |
| verified``          | Strictest single-model verifier; offline    | Cohere      |
|                     | "ceiling" reference. >100x cost per call.   |             |
+---------------------+---------------------------------------------+-------------+

For full customization, use :func:`build_pipeline` with explicit knobs,
or load a YAML config via ``Pipeline.from_yaml(path)``.

Every preset accepts ``index_dir`` so the user can keep separate indexes
per experiment / per corpus without rebuilding.
"""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from verifiable_rag.models.answer import Strictness
    from verifiable_rag.pipeline import Pipeline


_DEFAULT_INDEX_DIR = Path(".verifiable_rag_cache/indexes/verifiable_rag")
_DEFAULT_HAIKU = "anthropic/claude-haiku-4-5"
_DEFAULT_SONNET = "anthropic/claude-sonnet-4-6"


# --------------------------------------------------------------------------- #
# Named presets
# --------------------------------------------------------------------------- #


def local_minimal(
    *,
    generator_model: str = _DEFAULT_HAIKU,
    index_dir: Path = _DEFAULT_INDEX_DIR,
) -> "Pipeline":
    """All-local pipeline, no verifier. Cheapest path to "it works."

    * Parser: PyMuPDF (fast, text-only — no layout fidelity, no OCR)
    * Chunker: ParentChildChunker (default sizing)
    * Embedder: BGE-small-en-v1.5 (local, 384-dim)
    * Index: HybridIndex (LanceDB + BM25)
    * Reranker: none
    * Generator: Prompted (works with any LiteLLM model)
    * Verifier: none, strictness=``"loose"``

    Generator still hits an LLM API (Haiku 4.5 by default), so you need
    ``ANTHROPIC_API_KEY``. For fully air-gapped, swap *generator_model*
    to a local Ollama / vLLM endpoint via LiteLLM.
    """
    from verifiable_rag.chunkers import ParentChildChunker
    from verifiable_rag.embedders import SentenceTransformerEmbedder
    from verifiable_rag.generators import PromptedCitedGenerator
    from verifiable_rag.indexers import BM25Index, HybridIndex, LanceDBIndex
    from verifiable_rag.parsers import PyMuPDFParser
    from verifiable_rag.pipeline import Pipeline

    return Pipeline(
        parser=PyMuPDFParser(),
        chunker=ParentChildChunker(max_child_tokens=400, min_child_tokens=100),
        embedder=SentenceTransformerEmbedder(model_name="BAAI/bge-small-en-v1.5"),
        indexer=HybridIndex(dense=LanceDBIndex(uri=index_dir), sparse=BM25Index()),
        generator=PromptedCitedGenerator(model=generator_model),
        strictness="loose",
        top_k_retrieve=40,
        top_k_rerank=8,
    )


def local_verified(
    *,
    generator_model: str = _DEFAULT_HAIKU,
    index_dir: Path = _DEFAULT_INDEX_DIR,
    strictness: "Strictness" = "balanced",
) -> "Pipeline":
    """All-local + HHEM NLI verification (~600M, downloads on first use).

    Same retrieval stack as :func:`local_minimal` plus:
    * Reranker: BGE rerank-v2-m3 (local, ~568M)
    * Verifier: HHEM-2.1-open with default threshold

    Good middle ground: NLI verification with no API costs beyond the
    generator LLM.
    """
    from verifiable_rag.chunkers import ParentChildChunker
    from verifiable_rag.embedders import SentenceTransformerEmbedder
    from verifiable_rag.generators import PromptedCitedGenerator
    from verifiable_rag.indexers import BM25Index, HybridIndex, LanceDBIndex
    from verifiable_rag.parsers import PyMuPDFParser
    from verifiable_rag.pipeline import Pipeline
    from verifiable_rag.rerankers import BGERerankerV2
    from verifiable_rag.verifiers import HHEMVerifier

    return Pipeline(
        parser=PyMuPDFParser(),
        chunker=ParentChildChunker(max_child_tokens=400, min_child_tokens=100),
        embedder=SentenceTransformerEmbedder(model_name="BAAI/bge-small-en-v1.5"),
        indexer=HybridIndex(dense=LanceDBIndex(uri=index_dir), sparse=BM25Index()),
        reranker=BGERerankerV2(),
        generator=PromptedCitedGenerator(model=generator_model),
        verifier=HHEMVerifier(),
        strictness=strictness,
        top_k_retrieve=60,
        top_k_rerank=8,
    )


def hybrid_balanced(
    *,
    generator_model: str = _DEFAULT_HAIKU,
    index_dir: Path = _DEFAULT_INDEX_DIR,
) -> "Pipeline":
    """**Recommended default.** Cohere retrieval + Dual NLI + constrained Haiku.

    * Parser: Docling primary, PyMuPDF fallback (caching wrapper)
    * Chunker: ParentChildChunker
    * Embedder: Cohere embed-english-v3.0 (hosted)
    * Reranker: Cohere rerank-v3 (hosted)
    * Generator: ConstrainedCitedGenerator (schema-forced cites, ReClaim-style)
    * Verifier: DualNLIVerifier(HHEM + MiniCheck), min aggregation
    * Strictness: ``"balanced"``

    Matches the published verifiable-rag baseline that hits 0.875 mc_acc
    on LitQA2 and 0.844 AUROC on RAGTruth. The defaults that "just work."

    Requires ``ANTHROPIC_API_KEY`` and ``COHERE_API_KEY``.
    """
    from verifiable_rag.chunkers import ParentChildChunker
    from verifiable_rag.embedders import CohereEmbedder
    from verifiable_rag.generators import ConstrainedCitedGenerator
    from verifiable_rag.indexers import BM25Index, HybridIndex, LanceDBIndex
    from verifiable_rag.parsers import (
        CachingParser,
        CompositeParser,
        DoclingParser,
        PyMuPDFParser,
    )
    from verifiable_rag.pipeline import Pipeline
    from verifiable_rag.rerankers import CohereReranker
    from verifiable_rag.verifiers import (
        DualNLIVerifier,
        HHEMVerifier,
        MiniCheckVerifier,
    )

    return Pipeline(
        parser=CachingParser(
            CompositeParser(primary=DoclingParser(), fallbacks=[PyMuPDFParser()])
        ),
        chunker=ParentChildChunker(max_child_tokens=400, min_child_tokens=100),
        embedder=CohereEmbedder(),
        indexer=HybridIndex(dense=LanceDBIndex(uri=index_dir), sparse=BM25Index()),
        reranker=CohereReranker(),
        generator=ConstrainedCitedGenerator(model=generator_model),
        verifier=DualNLIVerifier(HHEMVerifier(), MiniCheckVerifier()),
        strictness="balanced",
        top_k_retrieve=100,
        top_k_rerank=10,
    )


def hybrid_strict(
    *,
    generator_model: str = _DEFAULT_HAIKU,
    index_dir: Path = _DEFAULT_INDEX_DIR,
) -> "Pipeline":
    """Same components as :func:`hybrid_balanced`, but strictness=strict.

    Refuses any answer where the Dual NLI faithfulness score is below
    the strict threshold (0.7). Higher refusal rate; only confident
    answers slip through.
    """
    pipeline = hybrid_balanced(generator_model=generator_model, index_dir=index_dir)
    pipeline.strictness = "strict"
    return pipeline


def hybrid_paranoid(
    *,
    generator_model: str = _DEFAULT_SONNET,
    index_dir: Path = _DEFAULT_INDEX_DIR,
) -> "Pipeline":
    """Maximum-strictness preset: Sonnet generation + Dual NLI + paranoid threshold.

    Components identical to :func:`hybrid_balanced` except:
    * Generator: Sonnet 4.6 (stronger structured-output behavior)
    * Strictness: ``"paranoid"`` (refuse below faithfulness 0.9)

    Use for high-trust use cases (legal, medical, scientific verification).
    Cost per query is ~5x balanced because of the Sonnet swap.
    """
    pipeline = hybrid_balanced(generator_model=generator_model, index_dir=index_dir)
    pipeline.strictness = "paranoid"
    return pipeline


def llm_judge_verified(
    *,
    generator_model: str = _DEFAULT_HAIKU,
    judge_model: str = _DEFAULT_SONNET,
    judge_threshold: float = 0.5,
    judge_max_workers: int = 4,
    index_dir: Path = _DEFAULT_INDEX_DIR,
    strictness: "Strictness" = "balanced",
) -> "Pipeline":
    """LLM-as-judge verifier preset. The strictest single-model option.

    Same retrieval + generator stack as :func:`hybrid_balanced`, but the
    verifier is a Sonnet 4.6 LLM-judge instead of the Dual NLI ensemble.
    Sonnet evaluates each generated sentence against its cited spans
    and returns ``{"supported": bool, "confidence": float}``.

    When to use this
    ----------------
    * **Adversarial / audit-grade workflows** where every claim must be
      verbatim-sourceable.
    * **Offline eval** as a "ceiling" reference vs the Dual NLI baseline.
    * **Sensitive domains** (legal, medical, scientific) where the cost
      of a missed flag exceeds the API spend.

    Cost: >100x per-call cost vs :func:`hybrid_balanced` (LLM API per
    sentence vs. local NLI). For most production use cases, Dual NLI
    is the right default and this preset is the offline reference.

    Requires ``ANTHROPIC_API_KEY`` (both generator and judge) +
    ``COHERE_API_KEY`` (retrieval).
    """
    from verifiable_rag.chunkers import ParentChildChunker
    from verifiable_rag.embedders import CohereEmbedder
    from verifiable_rag.generators import ConstrainedCitedGenerator
    from verifiable_rag.indexers import BM25Index, HybridIndex, LanceDBIndex
    from verifiable_rag.parsers import (
        CachingParser,
        CompositeParser,
        DoclingParser,
        PyMuPDFParser,
    )
    from verifiable_rag.pipeline import Pipeline
    from verifiable_rag.rerankers import CohereReranker
    from verifiable_rag.verifiers import LLMJudgeVerifier, NLIVerifier

    judge = LLMJudgeVerifier(
        model=judge_model,
        max_workers=judge_max_workers,
        num_retries=5,
    )
    return Pipeline(
        parser=CachingParser(
            CompositeParser(primary=DoclingParser(), fallbacks=[PyMuPDFParser()])
        ),
        chunker=ParentChildChunker(max_child_tokens=400, min_child_tokens=100),
        embedder=CohereEmbedder(),
        indexer=HybridIndex(dense=LanceDBIndex(uri=index_dir), sparse=BM25Index()),
        reranker=CohereReranker(),
        generator=ConstrainedCitedGenerator(model=generator_model),
        verifier=NLIVerifier(judge, threshold=judge_threshold),
        strictness=strictness,
        top_k_retrieve=100,
        top_k_rerank=10,
    )


# --------------------------------------------------------------------------- #
# Parametric factory — when none of the presets match
# --------------------------------------------------------------------------- #


_RetrievalTier = Literal["local", "hybrid"]
_VerifierName = Literal["none", "hhem", "minicheck", "dual_nli"]
_GeneratorName = Literal["prompted", "constrained"]


def build_pipeline(
    *,
    retrieval: _RetrievalTier = "hybrid",
    verifier: _VerifierName = "dual_nli",
    generator: _GeneratorName = "constrained",
    strictness: "Strictness" = "balanced",
    generator_model: str = _DEFAULT_HAIKU,
    index_dir: Path = _DEFAULT_INDEX_DIR,
    top_k_retrieve: int = 100,
    top_k_rerank: int = 10,
) -> "Pipeline":
    """Parametric pipeline factory — pick your axes, get a wired Pipeline.

    Use this when you want to mix and match outside the named presets.
    For example::

        pipeline = build_pipeline(
            retrieval="local",
            verifier="dual_nli",
            generator="constrained",
            strictness="strict",
        )

    More custom needs (e.g. ContextualChunker, swap in your own
    Embedder) → instantiate :class:`Pipeline` directly, or load from
    YAML via :meth:`Pipeline.from_yaml`.
    """
    # Build component-by-component, importing only what's needed.
    from verifiable_rag.chunkers import ParentChildChunker
    from verifiable_rag.indexers import BM25Index, HybridIndex, LanceDBIndex
    from verifiable_rag.parsers import (
        CachingParser,
        CompositeParser,
        DoclingParser,
        PyMuPDFParser,
    )
    from verifiable_rag.pipeline import Pipeline

    if retrieval == "local":
        from verifiable_rag.embedders import SentenceTransformerEmbedder
        from verifiable_rag.rerankers import BGERerankerV2

        embedder_obj = SentenceTransformerEmbedder(model_name="BAAI/bge-small-en-v1.5")
        reranker_obj = BGERerankerV2()
        parser_obj = PyMuPDFParser()
    elif retrieval == "hybrid":
        from verifiable_rag.embedders import CohereEmbedder
        from verifiable_rag.rerankers import CohereReranker

        embedder_obj = CohereEmbedder()
        reranker_obj = CohereReranker()
        parser_obj = CachingParser(
            CompositeParser(primary=DoclingParser(), fallbacks=[PyMuPDFParser()])
        )
    else:
        raise ValueError(
            f"Unknown retrieval={retrieval!r}; choose 'local' or 'hybrid'"
        )

    if generator == "prompted":
        from verifiable_rag.generators import PromptedCitedGenerator

        generator_obj = PromptedCitedGenerator(model=generator_model)
    elif generator == "constrained":
        from verifiable_rag.generators import ConstrainedCitedGenerator

        generator_obj = ConstrainedCitedGenerator(model=generator_model)
    else:
        raise ValueError(
            f"Unknown generator={generator!r}; choose 'prompted' or 'constrained'"
        )

    verifier_obj = None
    if verifier == "none":
        pass
    elif verifier == "hhem":
        from verifiable_rag.verifiers import HHEMVerifier

        verifier_obj = HHEMVerifier()
    elif verifier == "minicheck":
        from verifiable_rag.verifiers import MiniCheckVerifier

        # MiniCheckVerifier only implements NLIScorer for now; for full
        # Verifier-Protocol use, wrap with DualNLIVerifier alongside HHEM.
        # When used as the only verifier, fall back to dual-NLI defaults.
        from verifiable_rag.verifiers import DualNLIVerifier, HHEMVerifier

        verifier_obj = DualNLIVerifier(HHEMVerifier(), MiniCheckVerifier())
    elif verifier == "dual_nli":
        from verifiable_rag.verifiers import (
            DualNLIVerifier,
            HHEMVerifier,
            MiniCheckVerifier,
        )

        verifier_obj = DualNLIVerifier(HHEMVerifier(), MiniCheckVerifier())
    else:
        raise ValueError(
            f"Unknown verifier={verifier!r}; choose 'none', 'hhem', 'minicheck', or 'dual_nli'"
        )

    return Pipeline(
        parser=parser_obj,
        chunker=ParentChildChunker(max_child_tokens=400, min_child_tokens=100),
        embedder=embedder_obj,
        indexer=HybridIndex(dense=LanceDBIndex(uri=index_dir), sparse=BM25Index()),
        reranker=reranker_obj,
        generator=generator_obj,
        verifier=verifier_obj,
        strictness=strictness,
        top_k_retrieve=top_k_retrieve,
        top_k_rerank=top_k_rerank,
    )


__all__ = [
    "build_pipeline",
    "hybrid_balanced",
    "hybrid_paranoid",
    "hybrid_strict",
    "llm_judge_verified",
    "local_minimal",
    "local_verified",
]
