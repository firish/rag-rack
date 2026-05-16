"""CompositeParser: fallback chain on ValueError / AssertionError."""
from __future__ import annotations

from pathlib import Path

import pytest

from verifiable_rag.models.document import Document, Paragraph, Section, Sentence
from verifiable_rag.models.span import Span
from verifiable_rag.parsers import CompositeParser


def _make_doc(doc_id: str) -> Document:
    sent = Sentence(
        id=f"{doc_id}::s0",
        text="Hello.",
        span=Span(doc_id=doc_id, char_start=0, char_end=6),
    )
    para = Paragraph(
        id=f"{doc_id}::para0",
        sentences=[sent],
        span=Span(doc_id=doc_id, char_start=0, char_end=6),
    )
    sec = Section(
        id=f"{doc_id}::sec0",
        title=None,
        paragraphs=[para],
        span=Span(doc_id=doc_id, char_start=0, char_end=6),
    )
    return Document(
        doc_id=doc_id,
        source_path=Path("/tmp/x.pdf"),
        sections=[sec],
        page_breaks=[0],
        full_text="Hello.",
    )


class _Stub:
    def __init__(self, name: str, exc: Exception | None) -> None:
        self.name = name
        self.exc = exc
        self.calls = 0

    def parse(self, path: Path) -> Document:
        self.calls += 1
        if self.exc is not None:
            raise self.exc
        return _make_doc(self.name)


@pytest.mark.smoke
def test_primary_wins_when_primary_succeeds() -> None:
    primary = _Stub("primary", None)
    fallback = _Stub("fallback", None)
    cp = CompositeParser(primary=primary, fallbacks=[fallback])
    doc = cp.parse(Path("anywhere.pdf"))
    assert doc.doc_id == "primary"
    assert primary.calls == 1
    assert fallback.calls == 0


@pytest.mark.smoke
def test_fallback_used_on_value_error() -> None:
    primary = _Stub("primary", ValueError("page_breaks must be sorted ascending"))
    fallback = _Stub("fallback", None)
    cp = CompositeParser(primary=primary, fallbacks=[fallback])
    doc = cp.parse(Path("x.pdf"))
    assert doc.doc_id == "fallback"
    assert primary.calls == 1
    assert fallback.calls == 1


@pytest.mark.smoke
def test_fallback_used_on_assertion_error() -> None:
    primary = _Stub("primary", AssertionError())
    fallback = _Stub("fallback", None)
    cp = CompositeParser(primary=primary, fallbacks=[fallback])
    doc = cp.parse(Path("x.pdf"))
    assert doc.doc_id == "fallback"


@pytest.mark.smoke
def test_re_raises_last_exception_when_all_fail() -> None:
    primary = _Stub("primary", ValueError("docling-fail"))
    fallback = _Stub("fallback", ValueError("pymupdf-fail"))
    cp = CompositeParser(primary=primary, fallbacks=[fallback])
    with pytest.raises(ValueError, match="pymupdf-fail"):
        cp.parse(Path("x.pdf"))


@pytest.mark.smoke
def test_non_catch_exceptions_propagate_immediately() -> None:
    """FileNotFoundError must not trigger fallback — wrong file is not a parser bug."""
    primary = _Stub("primary", FileNotFoundError("missing"))
    fallback = _Stub("fallback", None)
    cp = CompositeParser(primary=primary, fallbacks=[fallback])
    with pytest.raises(FileNotFoundError):
        cp.parse(Path("missing.pdf"))
    assert fallback.calls == 0


@pytest.mark.smoke
def test_chain_falls_through_multiple_fallbacks() -> None:
    primary = _Stub("primary", ValueError("a"))
    middle = _Stub("middle", AssertionError())
    last = _Stub("last", None)
    cp = CompositeParser(primary=primary, fallbacks=[middle, last])
    doc = cp.parse(Path("x.pdf"))
    assert doc.doc_id == "last"
    assert primary.calls == middle.calls == last.calls == 1


@pytest.mark.smoke
def test_empty_fallbacks_rejected() -> None:
    primary = _Stub("primary", None)
    with pytest.raises(ValueError, match="at least one fallback"):
        CompositeParser(primary=primary, fallbacks=[])


@pytest.mark.smoke
def test_composite_parser_satisfies_protocol() -> None:
    from verifiable_rag.parsers import Parser

    cp = CompositeParser(primary=_Stub("p", None), fallbacks=[_Stub("f", None)])
    assert isinstance(cp, Parser)
