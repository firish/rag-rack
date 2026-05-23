"""ContextualChunker + LLMContextualizer tests.

Uses scripted chunkers and contextualizers — no real LLM calls.
"""

from __future__ import annotations

from dataclasses import replace
from unittest.mock import MagicMock, patch

import pytest

from tests.chunkers.conftest import build_document
from verifiable_rag.chunkers import (
    Chunker,
    ContextualChunker,
    LLMContextualizer,
    embedding_text,
)
from verifiable_rag.chunkers.contextual import (
    _split_chunk_block,
    _split_document_block,
)
from verifiable_rag.models.chunk import Chunk
from verifiable_rag.models.document import Document


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


def _make_doc() -> Document:
    return build_document(
        sections_spec=[
            ("Intro", [["First sentence.", "Second sentence."]]),
            ("Methods", [["Third sentence."]]),
        ],
        doc_id="paper",
    )


class _StubChunker:
    """A chunker that returns hand-crafted chunks."""

    def __init__(self, chunks: list[Chunk]) -> None:
        self._chunks = chunks

    def chunk(self, document: Document) -> list[Chunk]:
        return list(self._chunks)


class _StubContextualizer:
    """Returns canned preambles for each chunk, or None to simulate failure."""

    def __init__(self, preambles: list[str | None]) -> None:
        self._preambles = preambles
        self.calls: list[tuple[str, list[str]]] = []

    def generate_batch(
        self, document_text: str, chunk_texts: list[str]
    ) -> list[str | None]:
        self.calls.append((document_text, list(chunk_texts)))
        # Pad / trim to match request
        out = list(self._preambles[: len(chunk_texts)])
        while len(out) < len(chunk_texts):
            out.append(None)
        return out


def _make_chunk(
    chunk_id: str,
    text: str,
    doc: Document,
    sentence_id: str,
    section_id: str | None = None,
    paragraph_id: str | None = None,
) -> Chunk:
    """Build a Chunk for tests. Defaults to the document's first section/para
    so the default-granularity ('section') path works without per-call args.
    """
    sent = doc.sentence_by_id(sentence_id)
    if section_id is None:
        section_id = doc.sections[0].id
    if paragraph_id is None:
        paragraph_id = doc.sections[0].paragraphs[0].id
    return Chunk(
        chunk_id=chunk_id,
        text=text,
        doc_id=doc.doc_id,
        sentence_ids=(sentence_id,),
        span=sent.span,
        metadata={
            "source": "test",
            "section_id": section_id,
            "paragraph_id": paragraph_id,
        },
    )


# --------------------------------------------------------------------------- #
# embedding_text helper
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_embedding_text_falls_back_to_chunk_text() -> None:
    doc = _make_doc()
    c = _make_chunk("paper::c0", "Some chunk text.", doc, "paper::s0")
    assert embedding_text(c) == "Some chunk text."


@pytest.mark.smoke
def test_embedding_text_prepends_preamble_when_present() -> None:
    doc = _make_doc()
    c = Chunk(
        chunk_id="paper::c0",
        text="Some chunk text.",
        doc_id=doc.doc_id,
        sentence_ids=("paper::s0",),
        span=doc.sentence_by_id("paper::s0").span,
        metadata={"contextual_preamble": "This section introduces foo."},
    )
    out = embedding_text(c)
    assert out == "This section introduces foo.\n\nSome chunk text."


# --------------------------------------------------------------------------- #
# ContextualChunker
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_contextual_chunker_satisfies_chunker_protocol() -> None:
    base = _StubChunker([])
    cx = _StubContextualizer([])
    assert isinstance(ContextualChunker(base, cx), Chunker)


@pytest.mark.smoke
def test_attaches_preamble_to_metadata_preserves_text_and_span() -> None:
    """Span preservation invariant: text and span must NOT be modified."""
    doc = _make_doc()
    c0 = _make_chunk("paper::c0", "Chunk zero text.", doc, "paper::s0")
    c1 = _make_chunk("paper::c1", "Chunk one text.", doc, "paper::s1")
    base = _StubChunker([c0, c1])
    cx = _StubContextualizer(["Preamble for 0.", "Preamble for 1."])

    # granularity="chunk" so each chunk gets its own preamble (matches the
    # contextualizer's per-chunk script). Section/paragraph grouping tested
    # in separate tests below.
    chunker = ContextualChunker(base, cx, granularity="chunk")
    out = chunker.chunk(doc)

    assert len(out) == 2
    # Text and span unchanged — only metadata grew
    assert out[0].text == c0.text
    assert out[0].span == c0.span
    assert out[0].sentence_ids == c0.sentence_ids
    # Preamble landed in metadata
    assert out[0].metadata["contextual_preamble"] == "Preamble for 0."
    assert out[1].metadata["contextual_preamble"] == "Preamble for 1."
    # Original metadata preserved
    assert out[0].metadata["source"] == "test"


@pytest.mark.smoke
def test_passes_full_document_text_to_contextualizer() -> None:
    """The contextualizer must always receive the FULL document text as the
    *context*; the passage being contextualized varies by granularity but
    document_text is invariant.
    """
    doc = _make_doc()
    c = _make_chunk("paper::c0", "Chunk text.", doc, "paper::s0")
    base = _StubChunker([c])
    cx = _StubContextualizer(["preamble"])

    ContextualChunker(base, cx).chunk(doc)

    assert len(cx.calls) == 1
    document_text_arg, _passages = cx.calls[0]
    assert document_text_arg == doc.full_text


@pytest.mark.smoke
def test_keep_on_failure_default_keeps_chunks_without_preamble() -> None:
    """If contextualizer returns None for a chunk, default behavior keeps
    it with no preamble (so embedding falls back to chunk.text)."""
    doc = _make_doc()
    c0 = _make_chunk("paper::c0", "Chunk zero.", doc, "paper::s0")
    c1 = _make_chunk("paper::c1", "Chunk one.", doc, "paper::s1")
    base = _StubChunker([c0, c1])
    cx = _StubContextualizer(["Preamble OK.", None])  # second chunk fails

    out = ContextualChunker(
        base, cx, granularity="chunk", keep_on_failure=True
    ).chunk(doc)

    assert len(out) == 2
    assert out[0].metadata.get("contextual_preamble") == "Preamble OK."
    assert "contextual_preamble" not in out[1].metadata
    # Embedding text for failed chunk falls back to original
    assert embedding_text(out[1]) == "Chunk one."


@pytest.mark.smoke
def test_keep_on_failure_false_drops_failed_chunks() -> None:
    doc = _make_doc()
    c0 = _make_chunk("paper::c0", "Chunk zero.", doc, "paper::s0")
    c1 = _make_chunk("paper::c1", "Chunk one.", doc, "paper::s1")
    base = _StubChunker([c0, c1])
    cx = _StubContextualizer([None, "Second OK."])

    out = ContextualChunker(
        base, cx, granularity="chunk", keep_on_failure=False
    ).chunk(doc)

    assert len(out) == 1
    assert out[0].chunk_id == "paper::c1"


@pytest.mark.smoke
def test_empty_base_chunks_returns_empty() -> None:
    cx = _StubContextualizer([])
    out = ContextualChunker(_StubChunker([]), cx).chunk(_make_doc())
    assert out == []
    assert cx.calls == []  # no LLM calls if no chunks


# --------------------------------------------------------------------------- #
# Granularity — section / paragraph / chunk / group_by
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_section_granularity_one_call_per_section() -> None:
    """Default ('section') makes one LLM call per unique section_id; all
    chunks under the same section share the preamble.
    """
    doc = _make_doc()  # has two sections: 'sec_0' (Intro), 'sec_1' (Methods)
    sec_intro = doc.sections[0].id
    sec_methods = doc.sections[1].id
    # Three chunks: two in Intro, one in Methods
    c0 = _make_chunk("paper::c0", "Intro chunk A.", doc, "paper::s0", section_id=sec_intro)
    c1 = _make_chunk("paper::c1", "Intro chunk B.", doc, "paper::s1", section_id=sec_intro)
    c2 = _make_chunk("paper::c2", "Methods chunk.", doc, "paper::s2", section_id=sec_methods)
    base = _StubChunker([c0, c1, c2])
    cx = _StubContextualizer(["Intro preamble.", "Methods preamble."])

    out = ContextualChunker(base, cx, granularity="section").chunk(doc)

    # Only 2 LLM calls — one per section
    assert len(cx.calls) == 1  # generate_batch is one call with 2 passages
    _doc_text, passage_texts = cx.calls[0]
    assert len(passage_texts) == 2  # two sections
    # Section text is the passage, not chunk text
    assert passage_texts[0] == doc.sections[0].text
    assert passage_texts[1] == doc.sections[1].text
    # Both Intro chunks get the SAME preamble
    by_id = {c.chunk_id: c for c in out}
    assert by_id["paper::c0"].metadata["contextual_preamble"] == "Intro preamble."
    assert by_id["paper::c1"].metadata["contextual_preamble"] == "Intro preamble."
    # Methods chunk gets its own
    assert by_id["paper::c2"].metadata["contextual_preamble"] == "Methods preamble."


@pytest.mark.smoke
def test_paragraph_granularity_one_call_per_paragraph() -> None:
    doc = _make_doc()
    p0 = doc.sections[0].paragraphs[0].id
    # Two chunks in same paragraph + one in a different one (synth a 2nd paragraph)
    c0 = _make_chunk("paper::c0", "Para0 chunk A.", doc, "paper::s0", paragraph_id=p0)
    c1 = _make_chunk("paper::c1", "Para0 chunk B.", doc, "paper::s1", paragraph_id=p0)
    # Methods section's first paragraph
    p_methods = doc.sections[1].paragraphs[0].id
    c2 = _make_chunk("paper::c2", "Methods chunk.", doc, "paper::s2", paragraph_id=p_methods)
    base = _StubChunker([c0, c1, c2])
    cx = _StubContextualizer(["Para0 preamble.", "Methods preamble."])

    out = ContextualChunker(base, cx, granularity="paragraph").chunk(doc)

    _doc_text, passages = cx.calls[0]
    assert len(passages) == 2  # 2 unique paragraphs
    by_id = {c.chunk_id: c for c in out}
    assert by_id["paper::c0"].metadata["contextual_preamble"] == "Para0 preamble."
    assert by_id["paper::c1"].metadata["contextual_preamble"] == "Para0 preamble."
    assert by_id["paper::c2"].metadata["contextual_preamble"] == "Methods preamble."


@pytest.mark.smoke
def test_chunk_granularity_each_chunk_gets_own_preamble() -> None:
    doc = _make_doc()
    c0 = _make_chunk("paper::c0", "First chunk.", doc, "paper::s0")
    c1 = _make_chunk("paper::c1", "Second chunk.", doc, "paper::s1")
    base = _StubChunker([c0, c1])
    cx = _StubContextualizer(["P0", "P1"])

    out = ContextualChunker(base, cx, granularity="chunk").chunk(doc)

    _doc_text, passages = cx.calls[0]
    assert passages == ["First chunk.", "Second chunk."]
    assert out[0].metadata["contextual_preamble"] == "P0"
    assert out[1].metadata["contextual_preamble"] == "P1"


@pytest.mark.smoke
def test_section_granularity_missing_metadata_raises_helpful_error() -> None:
    """If chunks lack section_id, raise a clear error pointing to ParentChildChunker."""
    doc = _make_doc()
    # Build a chunk WITHOUT section_id in metadata
    sent = doc.sentence_by_id("paper::s0")
    bad = Chunk(
        chunk_id="paper::c0",
        text="text",
        doc_id=doc.doc_id,
        sentence_ids=("paper::s0",),
        span=sent.span,
        metadata={},  # no section_id!
    )
    base = _StubChunker([bad])
    cx = _StubContextualizer(["preamble"])
    with pytest.raises(ValueError, match="section_id"):
        ContextualChunker(base, cx, granularity="section").chunk(doc)


@pytest.mark.smoke
def test_group_by_callable_overrides_granularity() -> None:
    """A custom group_by callable supersedes the named granularity."""
    doc = _make_doc()
    # Tag chunks with a custom "topic" key in metadata
    c0 = replace(
        _make_chunk("paper::c0", "About cats.", doc, "paper::s0"),
        metadata={"source": "test", "topic": "cats"},
    )
    c1 = replace(
        _make_chunk("paper::c1", "More cats.", doc, "paper::s1"),
        metadata={"source": "test", "topic": "cats"},
    )
    c2 = replace(
        _make_chunk("paper::c2", "About dogs.", doc, "paper::s2"),
        metadata={"source": "test", "topic": "dogs"},
    )
    base = _StubChunker([c0, c1, c2])
    cx = _StubContextualizer(["Cats preamble.", "Dogs preamble."])

    chunker = ContextualChunker(
        base,
        cx,
        granularity="section",  # would normally group by section_id
        group_by=lambda c: c.metadata.get("topic"),
    )
    out = chunker.chunk(doc)

    by_id = {c.chunk_id: c for c in out}
    assert by_id["paper::c0"].metadata["contextual_preamble"] == "Cats preamble."
    assert by_id["paper::c1"].metadata["contextual_preamble"] == "Cats preamble."
    assert by_id["paper::c2"].metadata["contextual_preamble"] == "Dogs preamble."


@pytest.mark.smoke
def test_group_by_returning_none_skips_chunk() -> None:
    """Chunks where group_by returns None pass through with no preamble."""
    doc = _make_doc()
    c0 = replace(
        _make_chunk("paper::c0", "Has topic.", doc, "paper::s0"),
        metadata={"source": "test", "topic": "x"},
    )
    c1 = _make_chunk("paper::c1", "No topic.", doc, "paper::s1")
    # c1 has no 'topic' key
    base = _StubChunker([c0, c1])
    cx = _StubContextualizer(["X preamble."])
    chunker = ContextualChunker(
        base, cx, group_by=lambda c: c.metadata.get("topic")
    )
    out = chunker.chunk(doc)
    by_id = {c.chunk_id: c for c in out}
    assert by_id["paper::c0"].metadata["contextual_preamble"] == "X preamble."
    assert "contextual_preamble" not in by_id["paper::c1"].metadata


@pytest.mark.smoke
def test_invalid_granularity_raises() -> None:
    base = _StubChunker([])
    cx = _StubContextualizer([])
    with pytest.raises(ValueError, match="granularity"):
        ContextualChunker(base, cx, granularity="page")  # type: ignore[arg-type]


@pytest.mark.smoke
def test_section_granularity_preserves_chunk_order() -> None:
    """When grouping by section, output chunks must still appear in the
    same order as base produced them — downstream consumers rely on this."""
    doc = _make_doc()
    sec_intro = doc.sections[0].id
    sec_methods = doc.sections[1].id
    # Interleave sections to make sure ordering isn't accidentally preserved
    # by the natural group-iteration order alone.
    c0 = _make_chunk("paper::c0", "Intro A.", doc, "paper::s0", section_id=sec_intro)
    c1 = _make_chunk("paper::c1", "Methods A.", doc, "paper::s2", section_id=sec_methods)
    c2 = _make_chunk("paper::c2", "Intro B.", doc, "paper::s1", section_id=sec_intro)
    base = _StubChunker([c0, c1, c2])
    cx = _StubContextualizer(["Intro P.", "Methods P."])

    out = ContextualChunker(base, cx, granularity="section").chunk(doc)
    # Order matches base output
    assert [c.chunk_id for c in out] == ["paper::c0", "paper::c1", "paper::c2"]


# --------------------------------------------------------------------------- #
# LLMContextualizer — message shape + caching breakpoints
# --------------------------------------------------------------------------- #


def _fake_completion(text: str = "Generated preamble.") -> MagicMock:
    response = MagicMock()
    response.choices = [MagicMock()]
    response.choices[0].message.content = text
    return response


@pytest.mark.smoke
def test_user_template_validation() -> None:
    with pytest.raises(ValueError, match="document_text"):
        LLMContextualizer(user_template="missing both placeholders")
    with pytest.raises(ValueError, match="chunk_text"):
        LLMContextualizer(user_template="only {document_text} but no chunk")


@pytest.mark.smoke
def test_generate_batch_empty_returns_empty() -> None:
    c = LLMContextualizer()
    assert c.generate_batch("doc", []) == []


@pytest.mark.smoke
def test_generate_batch_returns_one_preamble_per_chunk() -> None:
    c = LLMContextualizer(max_workers=1)  # sequential for determinism
    with patch("litellm.completion", return_value=_fake_completion("PREAMBLE")):
        out = c.generate_batch("doc text", ["chunk A", "chunk B", "chunk C"])
    assert out == ["PREAMBLE", "PREAMBLE", "PREAMBLE"]


@pytest.mark.smoke
def test_messages_use_cache_breakpoints_on_system_and_document() -> None:
    """The cache_control breakpoints must be set so Anthropic caches the
    expensive (system + document) prefix across the batch."""
    c = LLMContextualizer(max_workers=1)
    captured: list[dict] = []

    def _capture(**kwargs) -> MagicMock:  # type: ignore[no-untyped-def]
        captured.append(kwargs)
        return _fake_completion()

    with patch("litellm.completion", side_effect=_capture):
        c.generate_batch("doc text", ["chunk A"])

    assert len(captured) == 1
    msgs = captured[0]["messages"]
    # System has one cached block
    assert msgs[0]["role"] == "system"
    assert msgs[0]["content"][0]["cache_control"] == {"type": "ephemeral"}
    # User has document (cached) + chunk (uncached)
    assert msgs[1]["role"] == "user"
    user_blocks = msgs[1]["content"]
    assert len(user_blocks) == 2
    assert user_blocks[0]["cache_control"] == {"type": "ephemeral"}
    assert "cache_control" not in user_blocks[1]
    # The cached user block contains the document tags
    assert "<document>" in user_blocks[0]["text"]
    assert "</document>" in user_blocks[0]["text"]
    # The uncached user block contains the chunk
    assert "<passage>" in user_blocks[1]["text"]


@pytest.mark.smoke
def test_per_call_failure_returns_none_not_raise() -> None:
    """One bad LLM call should produce a None preamble, not crash the batch."""
    c = LLMContextualizer(max_workers=1)

    def _completion(**kwargs) -> MagicMock:  # type: ignore[no-untyped-def]
        # Read the chunk text from the user message blocks
        text = " ".join(b.get("text", "") for b in kwargs["messages"][1]["content"])
        if "boom" in text:
            raise RuntimeError("simulated provider failure")
        return _fake_completion("ok preamble")

    with patch("litellm.completion", side_effect=_completion):
        out = c.generate_batch("doc", ["good", "boom", "good"])

    assert out == ["ok preamble", None, "ok preamble"]


# --------------------------------------------------------------------------- #
# Internal cache-block split helpers
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_split_document_block_returns_prefix_through_close_tag() -> None:
    msg = "<document>\nfoo bar\n</document>\n\n<passage>\nbaz\n</passage>"
    assert _split_document_block(msg) == "<document>\nfoo bar\n</document>"


@pytest.mark.smoke
def test_split_chunk_block_returns_suffix_after_close_tag() -> None:
    msg = "<document>\nfoo bar\n</document>\n\n<passage>\nbaz\n</passage>"
    assert _split_chunk_block(msg) == "<passage>\nbaz\n</passage>"


@pytest.mark.smoke
def test_split_falls_back_when_marker_missing() -> None:
    """Custom user_template without </document> marker → cache the whole."""
    msg = "custom template body no markers"
    assert _split_document_block(msg) == msg
    assert _split_chunk_block(msg) == ""
