"""PyMuPDFParser tests.

Most logic is exercised through pure helpers using fabricated _RawBlock data.
The end-to-end PDF integration test is gated on ``pymupdf`` being installed
and tests/parsers/fixtures/sample.pdf being present.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import pytest

from tests.parsers.conftest import SimpleSplitter, assert_span_invariants
from verifiable_rag.parsers.pymupdf_parser import (
    PyMuPDFParser,
    _assign_char_offsets,
    _RawBlock,
)

# --------------------------------------------------------------------------- #
# _assign_char_offsets — page_breaks invariants must match DoclingParser
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_offsets_single_page() -> None:
    blocks = [
        _RawBlock(text="First.", page=0, bbox=(0, 0, 100, 20)),
        _RawBlock(text="Second.", page=0, bbox=(0, 30, 100, 50)),
    ]
    full_text, page_breaks, starts, ends = _assign_char_offsets(blocks)
    assert page_breaks == [0]
    assert starts == [0, 8]  # "First.\n\n" = 8 chars
    assert ends == [6, 15]
    assert full_text.startswith("First.\n\nSecond.")


@pytest.mark.smoke
def test_offsets_multi_page() -> None:
    blocks = [
        _RawBlock(text="P0a.", page=0, bbox=(0, 0, 10, 10)),
        _RawBlock(text="P1a.", page=1, bbox=(0, 0, 10, 10)),
        _RawBlock(text="P2a.", page=2, bbox=(0, 0, 10, 10)),
    ]
    _full, page_breaks, _starts, _ends = _assign_char_offsets(blocks)
    assert len(page_breaks) == 3
    assert page_breaks[0] == 0
    assert page_breaks == sorted(page_breaks)


@pytest.mark.smoke
def test_offsets_empty() -> None:
    full, breaks, starts, ends = _assign_char_offsets([])
    assert full == ""
    assert breaks == [0]
    assert starts == [] and ends == []


@pytest.mark.smoke
def test_offsets_page_breaks_match_first_block_offset_per_page() -> None:
    blocks = [
        _RawBlock(text="HelloA.", page=0, bbox=(0, 0, 10, 10)),
        _RawBlock(text="HelloB.", page=0, bbox=(0, 0, 10, 10)),
        _RawBlock(text="HelloC.", page=1, bbox=(0, 0, 10, 10)),
    ]
    full, breaks, _starts, _ends = _assign_char_offsets(blocks)
    # Page 1 begins at the position where "HelloC." starts in full_text
    assert breaks[1] == full.index("HelloC.")


# --------------------------------------------------------------------------- #
# _build_document — fake pdf_doc with a captured get_text("dict") output
# --------------------------------------------------------------------------- #


class _FakePage:
    def __init__(self, dict_payload: dict) -> None:
        self._payload = dict_payload

    def get_text(self, mode: str) -> dict:
        assert mode == "dict"
        return self._payload


class _FakePdfDoc:
    def __init__(self, pages: list[_FakePage]) -> None:
        self._pages = pages
        self.page_count = len(pages)

    def load_page(self, i: int) -> _FakePage:
        return self._pages[i]

    def close(self) -> None:
        pass


def _block(text: str, bbox: tuple[float, float, float, float]) -> dict:
    return {
        "type": 0,
        "bbox": bbox,
        "lines": [{"spans": [{"text": text}]}],
    }


@pytest.mark.smoke
def test_build_document_invariants_hold(tmp_path: Path) -> None:
    src = tmp_path / "x.pdf"
    src.write_bytes(b"pdf-ish")
    page0 = _FakePage(
        {
            "blocks": [
                _block("Hello world. Goodbye.", (0, 0, 200, 30)),
                _block("Another paragraph here.", (0, 40, 200, 70)),
            ]
        }
    )
    page1 = _FakePage(
        {"blocks": [_block("Page two starts here.", (0, 0, 200, 30))]}
    )
    pdf_doc: Any = _FakePdfDoc([page0, page1])

    parser = PyMuPDFParser(sentence_splitter=SimpleSplitter())
    doc = parser._build_document(pdf_doc, src)

    assert_span_invariants(doc)
    assert doc.num_pages == 2
    assert len(doc.sections) == 1  # flat hierarchy by design
    assert doc.sections[0].title is None
    assert len(doc.sentences) >= 3
    # bbox attached to every sentence (single-page blocks)
    for s in doc.sentences:
        assert len(s.span.bboxes) == 1


@pytest.mark.smoke
def test_build_document_skips_image_blocks(tmp_path: Path) -> None:
    src = tmp_path / "x.pdf"
    src.write_bytes(b"x")
    page = _FakePage(
        {
            "blocks": [
                {"type": 1, "bbox": (0, 0, 100, 100), "lines": []},  # image
                _block("Real text here.", (0, 0, 100, 20)),
            ]
        }
    )
    parser = PyMuPDFParser(sentence_splitter=SimpleSplitter())
    doc = parser._build_document(_FakePdfDoc([page]), src)
    assert doc.sentences and "Real" in doc.sentences[0].text


@pytest.mark.smoke
def test_build_document_raises_on_empty(tmp_path: Path) -> None:
    src = tmp_path / "x.pdf"
    src.write_bytes(b"x")
    page = _FakePage({"blocks": []})
    parser = PyMuPDFParser(sentence_splitter=SimpleSplitter())
    with pytest.raises(ValueError, match="no content"):
        parser._build_document(_FakePdfDoc([page]), src)


# --------------------------------------------------------------------------- #
# End-to-end integration: real pymupdf on a real PDF
# --------------------------------------------------------------------------- #

pymupdf = pytest.importorskip("pymupdf", reason="pymupdf not installed")
_SAMPLE = Path(__file__).parent / "fixtures" / "sample.pdf"


@pytest.mark.smoke
@pytest.mark.skipif(not _SAMPLE.exists(), reason="sample.pdf fixture missing")
def test_end_to_end_parses_sample_pdf() -> None:
    parser = PyMuPDFParser(sentence_splitter=SimpleSplitter())
    doc = parser.parse(_SAMPLE)
    assert_span_invariants(doc)
    assert doc.full_text and doc.sentences
    assert doc.num_pages >= 1


@pytest.mark.smoke
def test_parser_satisfies_protocol() -> None:
    from verifiable_rag.parsers import Parser

    assert isinstance(PyMuPDFParser(sentence_splitter=SimpleSplitter()), Parser)
