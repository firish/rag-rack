"""Round-trip tests for Document JSON serialization."""
from __future__ import annotations

from pathlib import Path

import pytest

from verifiable_rag.models.document import Document, Paragraph, Section, Sentence
from verifiable_rag.models.span import BBox, PageBBox, Span
from verifiable_rag.parsers._serde import (
    _SERDE_VERSION,
    document_from_dict,
    document_to_dict,
    load_document,
    save_document,
)

DOC_ID = "serde-test-doc"


def _build_rich_document() -> Document:
    """A Document covering all interesting cases: bboxes, multi-page, multi-section."""
    s0 = Sentence(
        id=f"{DOC_ID}::s0",
        text="First sentence on page zero.",
        span=Span(
            doc_id=DOC_ID,
            char_start=0,
            char_end=28,
            bboxes=(PageBBox(page=0, bbox=BBox(x0=10, y0=20, x1=300, y1=40)),),
        ),
    )
    s1 = Sentence(
        id=f"{DOC_ID}::s1",
        text="Second sentence crosses to page one.",
        span=Span(
            doc_id=DOC_ID,
            char_start=29,
            char_end=65,
            bboxes=(
                PageBBox(page=0, bbox=BBox(x0=10, y0=50, x1=300, y1=70)),
                PageBBox(page=1, bbox=BBox(x0=10, y0=10, x1=300, y1=30)),
            ),
        ),
    )
    s2 = Sentence(
        id=f"{DOC_ID}::s2",
        text="Third sentence has no bbox.",
        span=Span(doc_id=DOC_ID, char_start=66, char_end=93),
    )

    para1 = Paragraph(
        id=f"{DOC_ID}::para0",
        sentences=[s0, s1],
        span=Span(doc_id=DOC_ID, char_start=0, char_end=65),
    )
    para2 = Paragraph(
        id=f"{DOC_ID}::para1",
        sentences=[s2],
        span=Span(doc_id=DOC_ID, char_start=66, char_end=93),
    )

    sec1 = Section(
        id=f"{DOC_ID}::sec0",
        title="Introduction",
        paragraphs=[para1],
        span=Span(doc_id=DOC_ID, char_start=0, char_end=65),
    )
    sec2 = Section(
        id=f"{DOC_ID}::sec1",
        title=None,
        paragraphs=[para2],
        span=Span(doc_id=DOC_ID, char_start=66, char_end=93),
    )

    return Document(
        doc_id=DOC_ID,
        source_path=Path("/tmp/example.pdf"),
        sections=[sec1, sec2],
        page_breaks=[0, 60],
        full_text="placeholder full text " * 10,
        metadata={"author": "Anon", "year": 2026},
    )


@pytest.mark.smoke
def test_document_roundtrip_dict() -> None:
    original = _build_rich_document()
    payload = document_to_dict(original)
    restored = document_from_dict(payload)

    assert restored.doc_id == original.doc_id
    assert restored.source_path == original.source_path
    assert restored.page_breaks == original.page_breaks
    assert restored.full_text == original.full_text
    assert restored.metadata == original.metadata
    assert len(restored.sections) == len(original.sections)
    assert restored.sentences == original.sentences  # frozen dataclasses compare by value


@pytest.mark.smoke
def test_document_roundtrip_file(tmp_path: Path) -> None:
    original = _build_rich_document()
    cache_file = tmp_path / "doc.json"

    save_document(original, cache_file)
    assert cache_file.exists()

    restored = load_document(cache_file)
    assert restored.sentences == original.sentences
    assert restored.page_breaks == original.page_breaks


@pytest.mark.smoke
def test_serde_preserves_pagebboxes_across_pages() -> None:
    """Cross-page bboxes (the whole point of the refactor) must round-trip exactly."""
    original = _build_rich_document()
    restored = document_from_dict(document_to_dict(original))

    s1_orig = original.sentence_by_id(f"{DOC_ID}::s1")
    s1_restored = restored.sentence_by_id(f"{DOC_ID}::s1")
    assert len(s1_restored.span.bboxes) == 2
    assert s1_restored.span.bboxes == s1_orig.span.bboxes
    assert s1_restored.span.pages == (0, 1)


@pytest.mark.smoke
def test_serde_version_mismatch_rejected() -> None:
    payload = document_to_dict(_build_rich_document())
    payload["_serde_version"] = _SERDE_VERSION + 999
    with pytest.raises(ValueError, match="version mismatch"):
        document_from_dict(payload)


@pytest.mark.smoke
def test_serde_missing_version_rejected() -> None:
    payload = document_to_dict(_build_rich_document())
    del payload["_serde_version"]
    with pytest.raises(ValueError):
        document_from_dict(payload)


@pytest.mark.smoke
def test_serde_roundtrips_parser_name() -> None:
    doc = _build_rich_document()
    object.__setattr__(doc, "parser_name", "pymupdf")  # frozen-ish via dataclass=normal
    restored = document_from_dict(document_to_dict(doc))
    assert restored.parser_name == "pymupdf"


@pytest.mark.smoke
def test_serde_parser_name_missing_in_old_cache_defaults_to_none() -> None:
    payload = document_to_dict(_build_rich_document())
    # Simulate a cache file written before the parser_name field existed.
    payload.pop("parser_name", None)
    restored = document_from_dict(payload)
    assert restored.parser_name is None


@pytest.mark.smoke
def test_serde_handles_empty_sections_and_no_full_text() -> None:
    doc = Document(
        doc_id="empty-doc",
        source_path=Path("nope.pdf"),
        sections=[],
        page_breaks=[0],
        full_text=None,
    )
    restored = document_from_dict(document_to_dict(doc))
    assert restored.full_text is None
    assert restored.sections == []
    assert restored.page_breaks == [0]
