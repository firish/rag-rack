"""DoclingParser tests.

The pure helpers (_compute_page_breaks, _assign_char_offsets, _build_sections)
are tested without docling installed, using fabricated _RawBlock instances.
The end-to-end docling integration test is gated on the optional dep being
available AND a sample PDF being present at tests/parsers/fixtures/sample.pdf.
"""
from __future__ import annotations

from pathlib import Path

import pytest

from tests.parsers.conftest import SimpleSplitter, assert_span_invariants
from verifiable_rag.parsers.docling_parser import (
    _assign_char_offsets,
    _BBoxData,
    _build_sections,
    _compute_page_breaks,
    _make_doc_id,
    _RawBlock,
)

# --------------------------------------------------------------------------- #
# _make_doc_id — content-derived, stable, filename-sanitised
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_make_doc_id_stable_across_calls(tmp_path: Path) -> None:
    f = tmp_path / "paper.pdf"
    f.write_bytes(b"identical content")
    assert _make_doc_id(f) == _make_doc_id(f)


@pytest.mark.smoke
def test_make_doc_id_changes_with_content(tmp_path: Path) -> None:
    f = tmp_path / "paper.pdf"
    f.write_bytes(b"content a")
    id_a = _make_doc_id(f)
    f.write_bytes(b"content b")
    id_b = _make_doc_id(f)
    assert id_a != id_b


@pytest.mark.smoke
def test_make_doc_id_sanitises_special_chars_in_stem(tmp_path: Path) -> None:
    f = tmp_path / "weird name (v2)!.pdf"
    f.write_bytes(b"x")
    doc_id = _make_doc_id(f)
    # Underscores replace non-alphanumerics — keeps doc_id usable in sentence IDs
    assert "(" not in doc_id and " " not in doc_id and "!" not in doc_id


# --------------------------------------------------------------------------- #
# _compute_page_breaks — edge cases that bite cross-page handling later
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_compute_page_breaks_basic() -> None:
    # docling pages 1, 2, 3 → our 0-indexed [0, 1, 2]
    breaks = _compute_page_breaks({1: 0, 2: 500, 3: 1200})
    assert breaks == [0, 500, 1200]


@pytest.mark.smoke
def test_compute_page_breaks_synthesises_missing_first_page() -> None:
    """If docling never reports page 1 (rare — e.g. blank cover), force start at 0."""
    breaks = _compute_page_breaks({2: 100, 3: 500})
    assert breaks[0] == 0
    assert breaks[1] == 100
    assert breaks[2] == 500


@pytest.mark.smoke
def test_compute_page_breaks_fills_empty_pages() -> None:
    """A page with no extracted text inherits the previous page's offset."""
    breaks = _compute_page_breaks({1: 0, 3: 700})  # page 2 has no content
    assert breaks == [0, 0, 700]


@pytest.mark.smoke
def test_compute_page_breaks_single_page() -> None:
    breaks = _compute_page_breaks({1: 0})
    assert breaks == [0]


@pytest.mark.smoke
def test_compute_page_breaks_empty_returns_single_zero() -> None:
    """Empty input still yields a valid [0] so Document validation passes."""
    assert _compute_page_breaks({}) == [0]


# --------------------------------------------------------------------------- #
# _assign_char_offsets — full_text construction + per-block offsets
# --------------------------------------------------------------------------- #

def _block(text: str, page_no: int, label: str = "paragraph") -> _RawBlock:
    return _RawBlock(
        text=text,
        bbox_list=(_BBoxData(page_no=page_no, l=0.0, t=0.0, r=100.0, b=20.0),),
        label=label,
    )


@pytest.mark.smoke
def test_assign_char_offsets_basic() -> None:
    blocks = [
        _block("Alpha.", page_no=1),
        _block("Beta.", page_no=1),
    ]
    full_text, page_breaks, starts, ends = _assign_char_offsets(blocks)

    # full_text contains both blocks separated by "\n\n"
    assert full_text == "Alpha.\n\nBeta.\n\n"
    # First block: offsets 0..6 (excludes separator)
    assert starts[0] == 0 and ends[0] == 6
    assert full_text[starts[0]:ends[0]] == "Alpha."
    # Second block: starts after "Alpha." + "\n\n" = offset 8
    assert starts[1] == 8 and ends[1] == 13
    assert full_text[starts[1]:ends[1]] == "Beta."
    # Single page — page_breaks is just [0]
    assert page_breaks == [0]


@pytest.mark.smoke
def test_assign_char_offsets_records_page_breaks() -> None:
    blocks = [
        _block("Page one para one.", page_no=1),
        _block("Page one para two.", page_no=1),
        _block("Page two starts here.", page_no=2),
        _block("Page three content.", page_no=3),
    ]
    full_text, page_breaks, starts, _ = _assign_char_offsets(blocks)

    # Page 0 starts at 0
    assert page_breaks[0] == 0
    # Page 1 (docling 2) starts where the third block begins
    assert page_breaks[1] == starts[2]
    # Page 2 (docling 3) starts where the fourth block begins
    assert page_breaks[2] == starts[3]
    # And full_text round-trips for each block
    for i, blk in enumerate(blocks):
        assert full_text[starts[i]:starts[i] + len(blk.text)] == blk.text


@pytest.mark.smoke
def test_assign_char_offsets_cross_page_block() -> None:
    """A block whose provenance spans pages 1-2 contributes a bbox per page."""
    cross = _RawBlock(
        text="Long sentence flowing across the page break.",
        bbox_list=(
            _BBoxData(page_no=1, l=0, t=700, r=400, b=720),
            _BBoxData(page_no=2, l=0, t=10, r=400, b=30),
        ),
        label="paragraph",
    )
    blocks = [cross, _block("Page two follow-up.", page_no=2)]
    _, page_breaks, starts, _ = _assign_char_offsets(blocks)

    # Cross-page block should still seed page 2's start at the same offset as the block
    assert page_breaks[0] == 0
    assert page_breaks[1] == starts[0]


# --------------------------------------------------------------------------- #
# _build_sections — paragraph/header grouping, sentence ID assignment
# --------------------------------------------------------------------------- #

@pytest.mark.smoke
def test_build_sections_single_section_no_header() -> None:
    doc_id = "test"
    blocks = [_block("Alpha. Beta.", page_no=1), _block("Gamma.", page_no=1)]
    full_text, _, starts, ends = _assign_char_offsets(blocks)

    sections = _build_sections(blocks, starts, ends, doc_id, SimpleSplitter())

    assert len(sections) == 1
    assert sections[0].title is None
    assert len(sections[0].paragraphs) == 2
    # Sentence IDs are globally numbered within the document
    sent_ids = [s.id for s in sections[0].sentences]
    assert sent_ids == [f"{doc_id}::s0", f"{doc_id}::s1", f"{doc_id}::s2"]
    # Spans round-trip against full_text
    for sent in sections[0].sentences:
        assert full_text[sent.span.char_start:sent.span.char_end] == sent.text


@pytest.mark.smoke
def test_build_sections_with_headers() -> None:
    doc_id = "test"
    blocks = [
        _block("Introduction", page_no=1, label="section_header"),
        _block("First para. Second sentence.", page_no=1),
        _block("Methods", page_no=1, label="section_header"),
        _block("Methods body.", page_no=1),
    ]
    _, _, starts, ends = _assign_char_offsets(blocks)
    sections = _build_sections(blocks, starts, ends, doc_id, SimpleSplitter())

    assert len(sections) == 2
    assert sections[0].title == "Introduction"
    assert sections[1].title == "Methods"
    assert len(sections[0].paragraphs) == 1
    assert len(sections[1].paragraphs) == 1


@pytest.mark.smoke
def test_build_sections_header_followed_by_no_content_is_dropped() -> None:
    doc_id = "test"
    blocks = [
        _block("Body content.", page_no=1),
        _block("Trailing header", page_no=1, label="section_header"),
        # No paragraph after the trailing header
    ]
    _, _, starts, ends = _assign_char_offsets(blocks)
    sections = _build_sections(blocks, starts, ends, doc_id, SimpleSplitter())

    # Only one real section — the trailing empty header doesn't generate one
    assert len(sections) == 1


# --------------------------------------------------------------------------- #
# Full document construction via DoclingParser._build_document — uses a fake
# DoclingDocument-shaped object so we don't need docling installed.
# --------------------------------------------------------------------------- #

class _FakeProv:
    """Quacks like docling's ProvenanceItem; bbox attribute mimics BoundingBox."""

    def __init__(
        self, page_no: int, left: float, top: float, right: float, bottom: float
    ) -> None:
        self.page_no = page_no
        self.bbox = type(
            "BB", (), {"l": left, "t": top, "r": right, "b": bottom}
        )()


class _FakeTextItem:
    """Quacks like docling's TextItem."""

    def __init__(self, text: str, prov: list[_FakeProv]) -> None:
        self.text = text
        self.prov = prov


class _FakeSectionHeaderItem(_FakeTextItem):
    """Quacks like docling's SectionHeaderItem."""


class _FakeDoclingDoc:
    def __init__(self, items: list[_FakeTextItem]) -> None:
        self._items = items

    def iterate_items(self):
        for item in self._items:
            yield item, 0


@pytest.fixture
def patched_extract(monkeypatch):
    """Bypass docling for full _build_document tests."""
    from verifiable_rag.parsers import docling_parser as dp

    def fake_extract(dl_doc):
        blocks = []
        for item, _level in dl_doc.iterate_items():
            label = (
                "section_header"
                if isinstance(item, _FakeSectionHeaderItem)
                else "paragraph"
            )
            text = item.text
            if not text or not text.strip():
                continue
            bbox_list = []
            for p in item.prov:
                bbox_list.append(
                    _BBoxData(
                        page_no=int(p.page_no),
                        l=float(p.bbox.l),
                        t=float(p.bbox.t),
                        r=float(p.bbox.r),
                        b=float(p.bbox.b),
                    )
                )
            bbox_list.sort(key=lambda x: x.page_no)
            blocks.append(_RawBlock(text=text, bbox_list=tuple(bbox_list), label=label))
        return blocks

    monkeypatch.setattr(dp, "_extract_raw_blocks", fake_extract)


@pytest.mark.smoke
def test_full_build_document_invariants(tmp_path: Path, patched_extract) -> None:
    """End-to-end build with a fake docling doc — every span invariant holds."""
    from verifiable_rag.parsers.docling_parser import DoclingParser

    src = tmp_path / "synthetic.pdf"
    src.write_bytes(b"placeholder bytes for hashing")

    fake_doc = _FakeDoclingDoc([
        _FakeSectionHeaderItem("Introduction", [_FakeProv(1, 0, 0, 100, 20)]),
        _FakeTextItem(
            "First sentence on page one. Second sentence still on page one.",
            [_FakeProv(1, 0, 30, 400, 60)],
        ),
        _FakeSectionHeaderItem("Methods", [_FakeProv(2, 0, 0, 100, 20)]),
        _FakeTextItem(
            "Methods body sentence. Another methods sentence.",
            [_FakeProv(2, 0, 30, 400, 60)],
        ),
    ])

    parser = DoclingParser(sentence_splitter=SimpleSplitter())
    doc = parser._build_document(fake_doc, src)

    assert_span_invariants(doc)
    assert doc.num_pages == 2
    assert len(doc.sections) == 2
    assert doc.sections[0].title == "Introduction"
    assert doc.sections[1].title == "Methods"
    # Sentence on page 2 should map to page 1 (0-indexed)
    page2_sentence = doc.sections[1].sentences[0]
    first, last = doc.pages_for_span(page2_sentence.span)
    assert first == 1 and last == 1


@pytest.mark.smoke
def test_full_build_document_handles_cross_page_paragraph(
    tmp_path: Path, patched_extract
) -> None:
    """A paragraph whose provenance spans pages still produces correct spans."""
    from verifiable_rag.parsers.docling_parser import DoclingParser

    src = tmp_path / "cross.pdf"
    src.write_bytes(b"x")

    fake_doc = _FakeDoclingDoc([
        _FakeTextItem(
            "Page one head. Sentence flowing past the page break.",
            [
                _FakeProv(1, 0, 700, 400, 720),
                _FakeProv(2, 0, 10, 400, 30),
            ],
        ),
        _FakeTextItem(
            "Page two clean follow-up.",
            [_FakeProv(2, 0, 50, 400, 70)],
        ),
    ])

    parser = DoclingParser(sentence_splitter=SimpleSplitter())
    doc = parser._build_document(fake_doc, src)

    assert_span_invariants(doc)
    assert doc.num_pages == 2
    # The cross-page paragraph carries 2 PageBBoxes
    cross_para = doc.paragraphs[0]
    assert len(cross_para.span.bboxes) == 2
    assert cross_para.span.pages == (0, 1)
    # Sentences within a multi-page block intentionally have no bboxes
    for sent in cross_para.sentences:
        assert sent.span.bboxes == ()
        # ...but their char offsets still resolve to a real page range
        first, last = doc.pages_for_span(sent.span)
        assert 0 <= first <= last < doc.num_pages


@pytest.mark.smoke
def test_full_build_document_empty_blocks_raises(
    tmp_path: Path, patched_extract
) -> None:
    from verifiable_rag.parsers.docling_parser import DoclingParser

    src = tmp_path / "empty.pdf"
    src.write_bytes(b"x")

    fake_doc = _FakeDoclingDoc([])
    parser = DoclingParser(sentence_splitter=SimpleSplitter())

    with pytest.raises(ValueError, match="no content"):
        parser._build_document(fake_doc, src)


@pytest.mark.smoke
def test_parse_missing_file_raises(tmp_path: Path) -> None:
    from verifiable_rag.parsers.docling_parser import DoclingParser

    parser = DoclingParser(sentence_splitter=SimpleSplitter())
    with pytest.raises(FileNotFoundError):
        parser.parse(tmp_path / "nope.pdf")


# --------------------------------------------------------------------------- #
# Real docling integration — runs only if docling+wtpsplit are installed AND a
# sample PDF is present.  This is the test you run after dropping a real PDF
# into tests/parsers/fixtures/ to verify the whole stack end-to-end.
# --------------------------------------------------------------------------- #

_TEST_PDF = Path(__file__).parent / "fixtures" / "sample.pdf"


@pytest.mark.slow
def test_docling_integration_with_real_pdf() -> None:
    pytest.importorskip("docling")
    pytest.importorskip("wtpsplit")
    if not _TEST_PDF.exists():
        pytest.skip(
            f"No sample PDF at {_TEST_PDF}.  "
            "Drop a small (10-25 page) PDF there to run this test."
        )

    from verifiable_rag.parsers import CachingParser, DoclingParser

    parser = CachingParser(DoclingParser())
    doc = parser.parse(_TEST_PDF)

    # The whole point of this test
    assert_span_invariants(doc)
    assert doc.num_pages > 0
    assert len(doc.sentences) > 0
    assert doc.full_text is not None and len(doc.full_text) > 0
