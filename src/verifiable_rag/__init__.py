"""verifiable-rag: document-grounded Q&A with sentence-level citations."""

from verifiable_rag.models import (
    Answer,
    BBox,
    Chunk,
    CitedSentence,
    Document,
    FaithfulnessComponents,
    PageBBox,
    Paragraph,
    RetrievedChunk,
    Section,
    Sentence,
    Span,
    Strictness,
    VerificationResult,
)
from verifiable_rag._ask import ask
from verifiable_rag.pipeline import Pipeline
from verifiable_rag.presets import (
    build_pipeline,
    hybrid_balanced,
    hybrid_paranoid,
    hybrid_strict,
    llm_judge_verified,
    local_minimal,
    local_verified,
)

__version__ = "0.5.2"

__all__ = [
    "__version__",
    "Pipeline",
    "ask",
    # Presets
    "build_pipeline",
    "hybrid_balanced",
    "hybrid_paranoid",
    "hybrid_strict",
    "llm_judge_verified",
    "local_minimal",
    "local_verified",
    # Models
    "Answer",
    "BBox",
    "Chunk",
    "CitedSentence",
    "Document",
    "FaithfulnessComponents",
    "PageBBox",
    "Paragraph",
    "RetrievedChunk",
    "Section",
    "Sentence",
    "Span",
    "Strictness",
    "VerificationResult",
]
