from __future__ import annotations

from pathlib import Path
from typing import Protocol, runtime_checkable

from verifiable_rag.models.document import Document


@runtime_checkable
class Parser(Protocol):
    """Convert a document file into a span-preserving Document model.

    Implementations must preserve character offsets through the full parsing
    pipeline so every Sentence can be traced back to its source location.
    """

    def parse(self, path: Path) -> Document:
        """Parse the file at *path* and return a Document.

        Raises:
            FileNotFoundError: if *path* does not exist.
            ValueError: if the file format is unsupported or contains no text.
        """
        ...


# Concrete implementations and helpers — imported lazily-friendly: the imports
# below succeed without docling/wtpsplit installed (those deps are only loaded
# when the parser actually runs).
from verifiable_rag.parsers._cache import (  # noqa: E402
    DEFAULT_CACHE_DIR,
    CachingParser,
    DocumentCache,
    file_content_hash,
)
from verifiable_rag.parsers._sentence_splitter import (  # noqa: E402
    SentenceSpan,
    SentenceSplitter,
)
from verifiable_rag.parsers.composite import CompositeParser  # noqa: E402
from verifiable_rag.parsers.docling_parser import DoclingParser  # noqa: E402
from verifiable_rag.parsers.pymupdf_parser import PyMuPDFParser  # noqa: E402

__all__ = [
    "Parser",
    "DoclingParser",
    "PyMuPDFParser",
    "CompositeParser",
    "CachingParser",
    "DocumentCache",
    "DEFAULT_CACHE_DIR",
    "SentenceSplitter",
    "SentenceSpan",
    "file_content_hash",
]
