"""ParentExpander: compute LLM context for a retrieved chunk.

The chunker stores small child chunks for retrieval precision.  For
generation, the LLM needs richer context — typically the surrounding section
or a window of nearby paragraphs.  This module is the bridge.

Strategies
----------
- ``"section_or_window"`` (default) — full section if it fits in
  ``max_parent_tokens``, otherwise a symmetric window of ``window_paragraphs``
  on each side of the child's paragraph.
- ``"section"`` — always the full section, ignoring the cap (use when you
  trust your sections to be small).
- ``"window"`` — always the symmetric window (predictable size; ignores
  section structure).

This separation matters because section sizes vary wildly across documents:
a focused academic paper has tight 3-paragraph sections; a textbook chapter
might be 50 paragraphs.  ``section_or_window`` adapts; the others let users
override when they know the data.

Note: ``ParentExpander`` only works with chunks produced by
``ParentChildChunker`` — it relies on the ``section_id`` and ``paragraph_id``
metadata keys that chunker writes.
"""

from __future__ import annotations

from collections.abc import Callable
from typing import Literal

from verifiable_rag.models.chunk import Chunk
from verifiable_rag.models.document import Document, Paragraph, Section


def _default_token_count(text: str) -> int:
    return max(1, len(text) // 4)


Strategy = Literal["section_or_window", "section", "window"]


class ParentExpander:
    """Returns the parent context text for a retrieved Chunk."""

    def __init__(
        self,
        strategy: Strategy = "section_or_window",
        max_parent_tokens: int = 2000,
        window_paragraphs: int = 3,
        token_count: Callable[[str], int] = _default_token_count,
    ) -> None:
        if max_parent_tokens <= 0:
            raise ValueError(f"max_parent_tokens must be > 0, got {max_parent_tokens}")
        if window_paragraphs < 0:
            raise ValueError(f"window_paragraphs must be >= 0, got {window_paragraphs}")
        self._strategy = strategy
        self._max = max_parent_tokens
        self._window = window_paragraphs
        self._tok = token_count

    def expand(self, chunk: Chunk, document: Document) -> str:
        """Return the parent context string for *chunk*."""
        if document.doc_id != chunk.doc_id:
            raise ValueError(
                f"Chunk doc_id {chunk.doc_id!r} != document doc_id {document.doc_id!r}"
            )

        section = self._lookup_section(chunk, document)

        if self._strategy == "section":
            return section.text
        if self._strategy == "window":
            return self._window_text(chunk, section)

        # section_or_window
        if self._tok(section.text) <= self._max:
            return section.text
        return self._window_text(chunk, section)

    # --------------------------------------------------------------------- #
    # Internals
    # --------------------------------------------------------------------- #

    @staticmethod
    def _lookup_section(chunk: Chunk, document: Document) -> Section:
        section_id = chunk.metadata.get("section_id")
        if section_id is None:
            raise ValueError(
                f"Chunk {chunk.chunk_id!r} has no 'section_id' metadata; "
                "ParentExpander requires chunks from ParentChildChunker."
            )
        for sec in document.sections:
            if sec.id == section_id:
                return sec
        raise KeyError(f"Section {section_id!r} not found in document {document.doc_id!r}")

    def _window_text(self, chunk: Chunk, section: Section) -> str:
        paragraph_id = chunk.metadata.get("paragraph_id")
        if paragraph_id is None:
            raise ValueError(f"Chunk {chunk.chunk_id!r} has no 'paragraph_id' metadata.")
        para_idx = self._paragraph_index(section, paragraph_id)
        lo = max(0, para_idx - self._window)
        hi = min(len(section.paragraphs), para_idx + self._window + 1)
        return self._join(section.paragraphs[lo:hi])

    @staticmethod
    def _paragraph_index(section: Section, paragraph_id: str) -> int:
        for i, p in enumerate(section.paragraphs):
            if p.id == paragraph_id:
                return i
        raise KeyError(f"Paragraph {paragraph_id!r} not found in section {section.id!r}")

    @staticmethod
    def _join(paragraphs: list[Paragraph]) -> str:
        return "\n\n".join(p.text for p in paragraphs)
