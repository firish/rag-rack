"""PromptedCitedGenerator tests.

litellm is patched into sys.modules so no network calls are made.  The fake
returns a canned assistant message; we then check that the generator parses
citations correctly and that we passed the LLM the right prompt.
"""
from __future__ import annotations

import sys
from typing import Any
from unittest.mock import MagicMock

import pytest

from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.generators import Generator, PromptedCitedGenerator
from verifiable_rag.models.answer import CitedSentence
from verifiable_rag.models.chunk import Chunk, RetrievedChunk
from verifiable_rag.models.document import Document
from verifiable_rag.models.span import Span

from tests.chunkers.conftest import build_document


# --------------------------------------------------------------------------- #
# Fixtures — fake LiteLLM
# --------------------------------------------------------------------------- #


def _fake_response(text: str) -> Any:
    """Build a minimal OpenAI-shaped response object."""
    msg = MagicMock()
    msg.content = text
    choice = MagicMock()
    choice.message = msg
    resp = MagicMock()
    resp.choices = [choice]
    return resp


@pytest.fixture
def fake_litellm(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    """Inject a fake litellm module into sys.modules."""
    fake = MagicMock()
    fake.completion = MagicMock()
    monkeypatch.setitem(sys.modules, "litellm", fake)
    return fake


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


def _make_doc_with_chunks() -> tuple[Document, list[Chunk]]:
    """A 2-section document and its parent-child chunks."""
    doc = build_document(
        sections_spec=[
            ("Intro", [["Mitochondria produce ATP.", "They are organelles."]]),
            ("Methods", [["We measured oxygen consumption."]]),
        ],
        doc_id="bio",
    )
    chunks = ParentChildChunker().chunk(doc)
    return doc, chunks


def _retrieved(chunks: list[Chunk]) -> list[RetrievedChunk]:
    return [
        RetrievedChunk(chunk=c, score=1.0 - i * 0.1, retrieval_method="hybrid")
        for i, c in enumerate(chunks)
    ]


# --------------------------------------------------------------------------- #
# Protocol conformance + construction
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_satisfies_generator_protocol() -> None:
    gen = PromptedCitedGenerator()
    assert isinstance(gen, Generator)
    assert gen.mode == "prompted"


@pytest.mark.smoke
def test_invalid_temperature_raises() -> None:
    with pytest.raises(ValueError, match="temperature"):
        PromptedCitedGenerator(temperature=-1)
    with pytest.raises(ValueError, match="temperature"):
        PromptedCitedGenerator(temperature=3)


@pytest.mark.smoke
def test_invalid_max_tokens_raises() -> None:
    with pytest.raises(ValueError, match="max_tokens"):
        PromptedCitedGenerator(max_tokens=0)


# --------------------------------------------------------------------------- #
# Edge cases — no chunks, no documents
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_generate_with_no_chunks_returns_empty(fake_litellm: MagicMock) -> None:
    gen = PromptedCitedGenerator()
    out = gen.generate("anything?", chunks=[], documents={})
    assert out == []
    fake_litellm.completion.assert_not_called()


@pytest.mark.smoke
def test_generate_falls_back_to_chunk_text_when_doc_missing(
    fake_litellm: MagicMock,
) -> None:
    """No Document supplied — generator still includes the chunk text."""
    _, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response(
        f"ATP is energy currency. [{chunks[0].chunk_id}]"
    )

    gen = PromptedCitedGenerator()
    out = gen.generate("what is ATP?", chunks=_retrieved(chunks), documents={})

    # Prompt must have included chunk text since we had no Document
    user_msg = fake_litellm.completion.call_args.kwargs["messages"][1]["content"]
    assert chunks[0].chunk_id in user_msg
    assert chunks[0].text in user_msg

    assert len(out) == 1
    assert out[0].supporting_sentence_ids == (chunks[0].chunk_id,)


# --------------------------------------------------------------------------- #
# Source formatting — sentence_ids and texts must reach the prompt
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_prompt_contains_sentence_ids_and_text(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response("Stub. [bio::s0]")

    gen = PromptedCitedGenerator()
    gen.generate("question?", chunks=_retrieved(chunks), documents={doc.doc_id: doc})

    user_msg = fake_litellm.completion.call_args.kwargs["messages"][1]["content"]
    for sentence in doc.sentences:
        assert sentence.id in user_msg
        assert sentence.text in user_msg


@pytest.mark.smoke
def test_prompt_dedupes_sentences_seen_in_multiple_chunks(
    fake_litellm: MagicMock,
) -> None:
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response("Stub. [bio::s0]")

    gen = PromptedCitedGenerator()
    # Pass the SAME chunk twice — sentence lines should still appear once
    duplicated = _retrieved(chunks) + _retrieved(chunks[:1])
    gen.generate("question?", chunks=duplicated, documents={doc.doc_id: doc})

    user_msg = fake_litellm.completion.call_args.kwargs["messages"][1]["content"]
    # The first sentence id should appear exactly once as a source line marker
    # (it may also appear later if the model uses it, but we control the model).
    assert user_msg.count(f"[{doc.sentences[0].id}]") == 1


@pytest.mark.smoke
def test_prompt_skips_unknown_sentence_ids(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_with_chunks()
    # Forge a chunk that references a sentence id not in the document.
    # Mix it with a real chunk so we still have at least one valid source line.
    bad_chunk = Chunk(
        chunk_id="bio::chBAD",
        text="Phantom text.",
        doc_id="bio",
        sentence_ids=("bio::sNOT_REAL",),
        span=Span(doc_id="bio", char_start=0, char_end=12),
        metadata={"section_id": "bio::sec0", "paragraph_id": "bio::p0"},
    )
    fake_litellm.completion.return_value = _fake_response("Stub. [bio::s0]")
    gen = PromptedCitedGenerator()
    gen.generate(
        "q?",
        chunks=_retrieved([bad_chunk] + chunks),
        documents={doc.doc_id: doc},
    )
    user_msg = fake_litellm.completion.call_args.kwargs["messages"][1]["content"]
    assert "bio::sNOT_REAL" not in user_msg
    # But the real sentence IDs should be present
    assert "bio::s0" in user_msg


# --------------------------------------------------------------------------- #
# LLM call wiring — model, temperature, max_tokens
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_litellm_called_with_configured_model(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response("ATP is energy. [bio::s0]")

    gen = PromptedCitedGenerator(
        model="openai/gpt-4o-mini",
        temperature=0.3,
        max_tokens=256,
    )
    gen.generate("q?", chunks=_retrieved(chunks), documents={doc.doc_id: doc})

    kwargs = fake_litellm.completion.call_args.kwargs
    assert kwargs["model"] == "openai/gpt-4o-mini"
    assert kwargs["temperature"] == 0.3
    assert kwargs["max_tokens"] == 256
    assert kwargs["messages"][0]["role"] == "system"
    assert kwargs["messages"][1]["role"] == "user"


@pytest.mark.smoke
def test_api_base_passed_through_when_set(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response("X. [bio::s0]")

    gen = PromptedCitedGenerator(api_base="http://localhost:8000/v1")
    gen.generate("q?", chunks=_retrieved(chunks), documents={doc.doc_id: doc})

    kwargs = fake_litellm.completion.call_args.kwargs
    assert kwargs["api_base"] == "http://localhost:8000/v1"


@pytest.mark.smoke
def test_api_base_omitted_when_none(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response("X. [bio::s0]")

    gen = PromptedCitedGenerator()
    gen.generate("q?", chunks=_retrieved(chunks), documents={doc.doc_id: doc})

    kwargs = fake_litellm.completion.call_args.kwargs
    assert "api_base" not in kwargs


# --------------------------------------------------------------------------- #
# Output parsing
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_parses_single_cited_sentence(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response(
        "Mitochondria produce ATP. [bio::s0]"
    )
    gen = PromptedCitedGenerator()
    out = gen.generate("q?", chunks=_retrieved(chunks), documents={doc.doc_id: doc})

    assert len(out) == 1
    assert out[0].text == "Mitochondria produce ATP."
    assert out[0].supporting_sentence_ids == ("bio::s0",)
    assert out[0].confidence == 1.0


@pytest.mark.smoke
def test_parses_multiple_citations_in_one_sentence(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response(
        "Combined claim. [bio::s0, bio::s1]"
    )
    gen = PromptedCitedGenerator()
    out = gen.generate("q?", chunks=_retrieved(chunks), documents={doc.doc_id: doc})

    assert len(out) == 1
    assert set(out[0].supporting_sentence_ids) == {"bio::s0", "bio::s1"}


@pytest.mark.smoke
def test_parses_multiple_sentences(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response(
        "Mitochondria make ATP. [bio::s0] They are organelles. [bio::s1]"
    )
    gen = PromptedCitedGenerator()
    out = gen.generate("q?", chunks=_retrieved(chunks), documents={doc.doc_id: doc})

    assert len(out) == 2
    assert out[0].supporting_sentence_ids == ("bio::s0",)
    assert out[1].supporting_sentence_ids == ("bio::s1",)


@pytest.mark.smoke
def test_drops_invented_citation_ids(fake_litellm: MagicMock) -> None:
    """Hallucinated IDs that we never gave the LLM must be stripped."""
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response(
        "Bogus claim. [bio::s99, fake::s0, bio::s0]"
    )
    gen = PromptedCitedGenerator()
    out = gen.generate("q?", chunks=_retrieved(chunks), documents={doc.doc_id: doc})

    assert len(out) == 1
    assert out[0].supporting_sentence_ids == ("bio::s0",)


@pytest.mark.smoke
def test_uncited_sentence_gets_zero_confidence(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response(
        "An unsupported claim with no bracket."
    )
    gen = PromptedCitedGenerator()
    out = gen.generate("q?", chunks=_retrieved(chunks), documents={doc.doc_id: doc})

    assert len(out) == 1
    assert out[0].supporting_sentence_ids == ()
    assert out[0].confidence == 0.0


@pytest.mark.smoke
def test_only_invented_ids_results_in_zero_confidence(fake_litellm: MagicMock) -> None:
    """A bracket of only invented IDs leaves no kept_ids → confidence 0."""
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response(
        "Made-up claim. [fake::s0, fake::s1]"
    )
    gen = PromptedCitedGenerator()
    out = gen.generate("q?", chunks=_retrieved(chunks), documents={doc.doc_id: doc})
    assert len(out) == 1
    assert out[0].supporting_sentence_ids == ()
    assert out[0].confidence == 0.0


# --------------------------------------------------------------------------- #
# Refusal handling
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_refusal_returns_empty_list(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response(
        "I cannot answer this from the provided sources."
    )
    gen = PromptedCitedGenerator()
    out = gen.generate("unanswerable?", chunks=_retrieved(chunks), documents={doc.doc_id: doc})
    assert out == []


@pytest.mark.smoke
def test_refusal_pattern_match_is_case_insensitive(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response(
        "I CANNOT ANSWER this question."
    )
    gen = PromptedCitedGenerator()
    assert gen.generate("q?", chunks=_retrieved(chunks), documents={doc.doc_id: doc}) == []


# --------------------------------------------------------------------------- #
# Output type sanity
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_returns_cited_sentence_instances(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_with_chunks()
    fake_litellm.completion.return_value = _fake_response("X. [bio::s0]")
    gen = PromptedCitedGenerator()
    out = gen.generate("q?", chunks=_retrieved(chunks), documents={doc.doc_id: doc})
    assert all(isinstance(c, CitedSentence) for c in out)
