"""DocumentCache and CachingParser tests — verify hit/miss + content-hash keying."""
from __future__ import annotations

from pathlib import Path

import pytest

from verifiable_rag.models.document import Document, Paragraph, Section, Sentence
from verifiable_rag.models.span import Span
from verifiable_rag.parsers._cache import (
    CachingParser,
    DocumentCache,
    file_content_hash,
)


def _make_doc(doc_id: str = "doc-x") -> Document:
    sent = Sentence(
        id=f"{doc_id}::s0",
        text="The cached sentence.",
        span=Span(doc_id=doc_id, char_start=0, char_end=20),
    )
    para = Paragraph(
        id=f"{doc_id}::para0",
        sentences=[sent],
        span=Span(doc_id=doc_id, char_start=0, char_end=20),
    )
    sec = Section(
        id=f"{doc_id}::sec0",
        title=None,
        paragraphs=[para],
        span=Span(doc_id=doc_id, char_start=0, char_end=20),
    )
    return Document(
        doc_id=doc_id,
        source_path=Path(f"/tmp/{doc_id}.pdf"),
        sections=[sec],
        page_breaks=[0],
        full_text="The cached sentence.",
    )


class _CountingParser:
    """Stub Parser that returns a fixed Document and counts how often it's called."""

    def __init__(self, doc: Document) -> None:
        self._doc = doc
        self.calls = 0

    def parse(self, path: Path) -> Document:
        self.calls += 1
        return self._doc


@pytest.mark.smoke
def test_file_content_hash_stable(tmp_path: Path) -> None:
    f = tmp_path / "data.bin"
    f.write_bytes(b"hello world")
    h1 = file_content_hash(f)
    h2 = file_content_hash(f)
    assert h1 == h2
    assert len(h1) == 64  # sha256 hex


@pytest.mark.smoke
def test_file_content_hash_changes_on_content_change(tmp_path: Path) -> None:
    f = tmp_path / "data.bin"
    f.write_bytes(b"version a")
    h1 = file_content_hash(f)
    f.write_bytes(b"version b")
    h2 = file_content_hash(f)
    assert h1 != h2


@pytest.mark.smoke
def test_file_content_hash_independent_of_filename(tmp_path: Path) -> None:
    a = tmp_path / "a.bin"
    b = tmp_path / "b.bin"
    a.write_bytes(b"identical content")
    b.write_bytes(b"identical content")
    assert file_content_hash(a) == file_content_hash(b)


@pytest.mark.smoke
def test_cache_miss_then_hit(tmp_path: Path) -> None:
    src = tmp_path / "doc.pdf"
    src.write_bytes(b"fake pdf bytes for testing")

    cache = DocumentCache(tmp_path / "cache")
    assert cache.get(src) is None  # miss

    doc = _make_doc()
    cache.put(src, doc)
    restored = cache.get(src)  # hit
    assert restored is not None
    assert restored.doc_id == doc.doc_id
    assert restored.sentences == doc.sentences


@pytest.mark.smoke
def test_cache_invalidated_on_content_change(tmp_path: Path) -> None:
    src = tmp_path / "doc.pdf"
    src.write_bytes(b"original content")
    cache = DocumentCache(tmp_path / "cache")

    cache.put(src, _make_doc("v1"))
    assert cache.get(src) is not None

    # Mutate the file — hash changes, cache key changes, get returns None
    src.write_bytes(b"changed content")
    assert cache.get(src) is None


@pytest.mark.smoke
def test_cache_handles_corrupt_json(tmp_path: Path) -> None:
    src = tmp_path / "doc.pdf"
    src.write_bytes(b"some content")
    cache = DocumentCache(tmp_path / "cache")
    # Manually write garbage at the cache location
    cache._cache_path(src).parent.mkdir(parents=True, exist_ok=True)
    cache._cache_path(src).write_text("{this is not valid json")

    # get() should silently return None and delete the corrupt file
    assert cache.get(src) is None
    assert not cache._cache_path(src).exists()


@pytest.mark.smoke
def test_caching_parser_only_calls_underlying_once(tmp_path: Path) -> None:
    src = tmp_path / "doc.pdf"
    src.write_bytes(b"pdf-ish bytes")

    underlying = _CountingParser(_make_doc())
    parser = CachingParser(underlying, cache_dir=tmp_path / "cache")

    parser.parse(src)
    parser.parse(src)
    parser.parse(src)
    assert underlying.calls == 1


@pytest.mark.smoke
def test_caching_parser_reparses_when_content_changes(tmp_path: Path) -> None:
    src = tmp_path / "doc.pdf"
    src.write_bytes(b"first version")

    underlying = _CountingParser(_make_doc())
    parser = CachingParser(underlying, cache_dir=tmp_path / "cache")

    parser.parse(src)
    src.write_bytes(b"second version")
    parser.parse(src)
    assert underlying.calls == 2


@pytest.mark.smoke
def test_caching_parser_raises_on_missing_file(tmp_path: Path) -> None:
    parser = CachingParser(_CountingParser(_make_doc()), cache_dir=tmp_path / "cache")
    with pytest.raises(FileNotFoundError):
        parser.parse(tmp_path / "does-not-exist.pdf")


@pytest.mark.smoke
def test_caching_parser_satisfies_parser_protocol() -> None:
    from verifiable_rag.parsers import Parser

    parser = CachingParser(_CountingParser(_make_doc()))
    assert isinstance(parser, Parser)


# --------------------------------------------------------------------------- #
# Negative cache — failure markers prevent re-parsing broken PDFs
# --------------------------------------------------------------------------- #


class _AlwaysFailsParser:
    def __init__(self, exc: Exception) -> None:
        self._exc = exc
        self.calls = 0

    def parse(self, path: Path) -> Document:
        self.calls += 1
        raise self._exc


@pytest.mark.smoke
def test_failure_cache_get_returns_none_when_absent(tmp_path: Path) -> None:
    src = tmp_path / "doc.pdf"
    src.write_bytes(b"content")
    cache = DocumentCache(tmp_path / "cache")
    assert cache.get_failure(src) is None


@pytest.mark.smoke
def test_failure_cache_roundtrip(tmp_path: Path) -> None:
    src = tmp_path / "doc.pdf"
    src.write_bytes(b"content")
    cache = DocumentCache(tmp_path / "cache")
    cache.put_failure(src, "ValueError: page_breaks must be sorted ascending")
    assert cache.get_failure(src) == "ValueError: page_breaks must be sorted ascending"


@pytest.mark.smoke
def test_success_clears_prior_failure_marker(tmp_path: Path) -> None:
    src = tmp_path / "doc.pdf"
    src.write_bytes(b"content")
    cache = DocumentCache(tmp_path / "cache")
    cache.put_failure(src, "old failure")
    cache.put(src, _make_doc())
    assert cache.get_failure(src) is None


@pytest.mark.smoke
def test_caching_parser_records_and_short_circuits_failure(tmp_path: Path) -> None:
    """The expensive parser is called once; future calls hit the negative cache."""
    src = tmp_path / "broken.pdf"
    src.write_bytes(b"broken pdf bytes")

    underlying = _AlwaysFailsParser(ValueError("page_breaks must be sorted ascending"))
    parser = CachingParser(underlying, cache_dir=tmp_path / "cache")

    with pytest.raises(ValueError, match="page_breaks"):
        parser.parse(src)
    with pytest.raises(ValueError, match="Cached parse failure"):
        parser.parse(src)
    with pytest.raises(ValueError, match="Cached parse failure"):
        parser.parse(src)
    # Underlying parser was only ever called once — that is the whole point.
    assert underlying.calls == 1


@pytest.mark.smoke
def test_caching_parser_caches_assertion_failures(tmp_path: Path) -> None:
    src = tmp_path / "bad.pdf"
    src.write_bytes(b"bytes")
    underlying = _AlwaysFailsParser(AssertionError("internal"))
    parser = CachingParser(underlying, cache_dir=tmp_path / "cache")

    with pytest.raises(AssertionError):
        parser.parse(src)
    with pytest.raises(ValueError, match="Cached parse failure"):
        parser.parse(src)
    assert underlying.calls == 1


@pytest.mark.smoke
def test_invalidate_clears_failure_marker_too(tmp_path: Path) -> None:
    src = tmp_path / "doc.pdf"
    src.write_bytes(b"bytes")
    cache = DocumentCache(tmp_path / "cache")
    cache.put_failure(src, "boom")
    cache.invalidate(src)
    assert cache.get_failure(src) is None
