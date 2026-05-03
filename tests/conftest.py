"""Shared pytest fixtures."""
from __future__ import annotations

from pathlib import Path

import pytest

from verifiable_rag.models.document import Document, Paragraph, Section, Sentence
from verifiable_rag.models.span import Span

DOC_ID = "test-doc-001"


@pytest.fixture
def simple_span() -> Span:
    return Span(doc_id=DOC_ID, char_start=0, char_end=50)


@pytest.fixture
def simple_sentence(simple_span: Span) -> Sentence:
    return Sentence(
        id=f"{DOC_ID}::s0",
        text="The quick brown fox jumps over the lazy dog.",
        span=simple_span,
    )


@pytest.fixture
def simple_document() -> Document:
    sentences = [
        Sentence(
            id=f"{DOC_ID}::s{i}",
            text=f"Sentence {i} with some content about topic {i}.",
            span=Span(doc_id=DOC_ID, char_start=i * 60, char_end=(i + 1) * 60 - 1),
        )
        for i in range(3)
    ]
    para = Paragraph(
        id=f"{DOC_ID}::para0",
        sentences=sentences,
        span=Span(doc_id=DOC_ID, char_start=0, char_end=179),
    )
    section = Section(
        id=f"{DOC_ID}::sec0",
        title="Introduction",
        paragraphs=[para],
        span=Span(doc_id=DOC_ID, char_start=0, char_end=179),
    )
    return Document(
        doc_id=DOC_ID,
        source_path=Path("test.pdf"),
        sections=[section],
        page_breaks=[0],
    )
