from __future__ import annotations

import bisect
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from verifiable_rag.models.span import Span


@dataclass(frozen=True)
class Sentence:
    """Atomic citable unit.  Every sentence has a globally unique id and a Span.

    Sentences may cross page boundaries — Span uses document-level char offsets.
    The page(s) a sentence touches are looked up via Document.pages_for_span().
    """

    id: str  # format: "{doc_id}::s{global_idx}"  (page is no longer in the id)
    text: str
    span: Span

    def __post_init__(self) -> None:
        if not self.text.strip():
            raise ValueError(f"Sentence {self.id!r} has empty text")
        if self.span.doc_id not in self.id:
            raise ValueError(
                f"Sentence id {self.id!r} does not embed its doc_id {self.span.doc_id!r}"
            )


@dataclass
class Paragraph:
    id: str
    sentences: list[Sentence]
    span: Span

    def __post_init__(self) -> None:
        if not self.sentences:
            raise ValueError(f"Paragraph {self.id!r} has no sentences")

    @property
    def text(self) -> str:
        return " ".join(s.text for s in self.sentences)


@dataclass
class Section:
    id: str
    title: str | None
    paragraphs: list[Paragraph]
    span: Span

    @property
    def sentences(self) -> list[Sentence]:
        return [sent for para in self.paragraphs for sent in para.sentences]

    @property
    def text(self) -> str:
        return "\n\n".join(para.text for para in self.paragraphs)


@dataclass
class Document:
    """A parsed source document.

    Spans throughout the pipeline use char offsets into Document.full_text
    (when supplied) so they can cross page boundaries.  page_breaks maps
    those offsets back to page numbers via Document.page_for_offset().

    page_breaks[i] is the char offset where page i begins.  It must start at 0.
    """

    doc_id: str
    source_path: Path
    sections: list[Section]
    page_breaks: list[int] = field(default_factory=list)
    full_text: str | None = None
    metadata: dict[str, Any] = field(default_factory=dict)
    # Set by the parser that produced this Document (e.g. "docling",
    # "pymupdf"). Lets downstream code slice metrics by parser path
    # without resorting to post-hoc heuristics on section structure.
    # Optional for backwards compat with caches written before this field
    # existed — None means "unknown".
    parser_name: str | None = None

    def __post_init__(self) -> None:
        if self.page_breaks:
            if self.page_breaks[0] != 0:
                raise ValueError(
                    f"page_breaks must start at 0, got {self.page_breaks[0]}"
                )
            if self.page_breaks != sorted(self.page_breaks):
                raise ValueError("page_breaks must be sorted ascending")

    @property
    def sentences(self) -> list[Sentence]:
        return [sent for sec in self.sections for sent in sec.sentences]

    @property
    def paragraphs(self) -> list[Paragraph]:
        return [para for sec in self.sections for para in sec.paragraphs]

    @property
    def num_pages(self) -> int:
        return len(self.page_breaks)

    def page_for_offset(self, offset: int) -> int:
        """Return the page index (0-indexed) containing *offset*."""
        if not self.page_breaks:
            raise ValueError(
                f"Document {self.doc_id!r} has no page_breaks; cannot map offset to page"
            )
        if offset < 0:
            raise ValueError(f"offset must be >= 0, got {offset}")
        # bisect_right finds insertion point AFTER any equal entries; subtract 1
        return max(0, bisect.bisect_right(self.page_breaks, offset) - 1)

    def pages_for_span(self, span: Span) -> tuple[int, int]:
        """Return (first_page, last_page) inclusive — the page range a span touches."""
        if span.doc_id != self.doc_id:
            raise ValueError(
                f"Span doc_id {span.doc_id!r} does not match document {self.doc_id!r}"
            )
        first = self.page_for_offset(span.char_start)
        # char_end is exclusive; subtract 1 so a span ending exactly on a page break
        # does not get attributed to the next page
        last_offset = max(span.char_start, span.char_end - 1)
        last = self.page_for_offset(last_offset)
        return first, last

    def sentence_by_id(self, sentence_id: str) -> Sentence:
        for s in self.sentences:
            if s.id == sentence_id:
                return s
        raise KeyError(f"Sentence {sentence_id!r} not found in document {self.doc_id!r}")

    def __repr__(self) -> str:
        return (
            f"Document(doc_id={self.doc_id!r}, sections={len(self.sections)}, "
            f"sentences={len(self.sentences)}, pages={self.num_pages})"
        )
