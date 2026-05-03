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
from verifiable_rag.pipeline import Pipeline

__version__ = "0.1.0"

__all__ = [
    "__version__",
    "Pipeline",
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
