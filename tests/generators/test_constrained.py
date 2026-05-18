"""ConstrainedCitedGenerator tests.

litellm is patched into sys.modules so no network calls are made. The fake
returns canned JSON-string responses; we then check that the generator
parses them correctly and that we passed the right schema to LiteLLM.
"""
from __future__ import annotations

import json
import sys
from typing import Any
from unittest.mock import MagicMock

import pytest

from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.generators import ConstrainedCitedGenerator, Generator
from verifiable_rag.models.answer import CitedSentence
from verifiable_rag.models.chunk import Chunk, RetrievedChunk

from tests.chunkers.conftest import build_document


# --------------------------------------------------------------------------- #
# Fixtures
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
    fake = MagicMock()
    fake.completion = MagicMock()
    monkeypatch.setitem(sys.modules, "litellm", fake)
    return fake


def _make_doc_and_chunks() -> tuple[Any, list[Chunk]]:
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
# Protocol + construction
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_satisfies_generator_protocol() -> None:
    gen = ConstrainedCitedGenerator(model="anthropic/claude-haiku-4-5")
    assert isinstance(gen, Generator)
    assert gen.mode == "constrained"


@pytest.mark.smoke
def test_rejects_bad_init_args() -> None:
    with pytest.raises(ValueError, match="temperature"):
        ConstrainedCitedGenerator(temperature=-1)
    with pytest.raises(ValueError, match="max_tokens"):
        ConstrainedCitedGenerator(max_tokens=0)
    with pytest.raises(ValueError, match="num_retries"):
        ConstrainedCitedGenerator(num_retries=-1)
    with pytest.raises(ValueError, match="max_citations_per_sentence"):
        ConstrainedCitedGenerator(max_citations_per_sentence=0)


# --------------------------------------------------------------------------- #
# Schema construction
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_schema_enum_populated_from_valid_ids() -> None:
    gen = ConstrainedCitedGenerator()
    schema = gen._build_schema(["bio::s1", "bio::s2", "bio::s3"])
    item = schema["schema"]["properties"]["sentences"]["items"]
    enum = item["properties"]["citations"]["items"]["enum"]
    assert enum == ["bio::s1", "bio::s2", "bio::s3"]


@pytest.mark.smoke
def test_schema_enforces_minmax_citations() -> None:
    gen = ConstrainedCitedGenerator(max_citations_per_sentence=2)
    schema = gen._build_schema(["a"])
    citations_schema = schema["schema"]["properties"]["sentences"]["items"]["properties"]["citations"]
    assert citations_schema["minItems"] == 1
    assert citations_schema["maxItems"] == 2


@pytest.mark.smoke
def test_schema_requires_refused_field() -> None:
    schema = ConstrainedCitedGenerator()._build_schema(["a"])
    required = schema["schema"]["required"]
    assert "refused" in required
    assert "selected_option" in required
    assert "sentences" in required


# --------------------------------------------------------------------------- #
# Parsing — happy path
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_generate_returns_cited_sentences(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_and_chunks()
    sentence_ids = [s.id for sec in doc.sections for p in sec.paragraphs for s in p.sentences]
    payload = {
        "refused": False,
        "selected_option": "Mitochondria",
        "sentences": [
            {"text": "Mitochondria produce ATP.", "citations": [sentence_ids[0]]},
            {"text": "They are organelles.", "citations": [sentence_ids[1]]},
        ],
    }
    fake_litellm.completion.return_value = _fake_response(json.dumps(payload))

    gen = ConstrainedCitedGenerator()
    out = gen.generate("What is mitochondria?", _retrieved(chunks), {doc.doc_id: doc})

    # 3 entries: bolded headline (selected_option) + 2 cited explanation sentences
    assert len(out) == 3
    assert all(isinstance(c, CitedSentence) for c in out)
    # Headline: bolded selected_option, no citations
    assert out[0].text == "**Mitochondria**"
    assert out[0].supporting_sentence_ids == ()
    assert out[0].confidence == 0.0
    # First real sentence carries citations
    assert out[1].text == "Mitochondria produce ATP."
    assert out[1].supporting_sentence_ids == (sentence_ids[0],)
    assert out[1].confidence == 1.0


@pytest.mark.smoke
def test_generate_passes_response_format_to_litellm(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_and_chunks()
    fake_litellm.completion.return_value = _fake_response(
        '{"refused": false, "sentences": []}'
    )

    ConstrainedCitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})

    call_kwargs = fake_litellm.completion.call_args.kwargs
    assert call_kwargs["response_format"]["type"] == "json_schema"
    # Schema must contain the valid sentence IDs as enum values
    enum = call_kwargs["response_format"]["json_schema"]["schema"][
        "properties"]["sentences"]["items"]["properties"]["citations"]["items"]["enum"]
    assert any(eid.startswith(doc.doc_id) for eid in enum)


# --------------------------------------------------------------------------- #
# Multi-citation
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_multi_citation_preserved(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_and_chunks()
    sids = [s.id for sec in doc.sections for p in sec.paragraphs for s in p.sentences]
    payload = {
        "refused": False,
        "sentences": [
            {"text": "Mitochondria are organelles producing ATP.",
             "citations": [sids[0], sids[1]]},
        ],
    }
    fake_litellm.completion.return_value = _fake_response(json.dumps(payload))

    out = ConstrainedCitedGenerator().generate(
        "?", _retrieved(chunks), {doc.doc_id: doc}
    )
    assert len(out) == 1
    assert out[0].supporting_sentence_ids == (sids[0], sids[1])


# --------------------------------------------------------------------------- #
# Refusal + edge cases
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_refused_true_returns_empty(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_and_chunks()
    fake_litellm.completion.return_value = _fake_response(
        '{"refused": true, "sentences": []}'
    )
    out = ConstrainedCitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    assert out == []


@pytest.mark.smoke
def test_empty_chunks_returns_empty_without_calling_llm(fake_litellm: MagicMock) -> None:
    out = ConstrainedCitedGenerator().generate("q", [], {})
    assert out == []
    fake_litellm.completion.assert_not_called()


@pytest.mark.smoke
def test_malformed_json_treated_as_refusal(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_and_chunks()
    fake_litellm.completion.return_value = _fake_response("not valid json at all")
    out = ConstrainedCitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    assert out == []


@pytest.mark.smoke
def test_invalid_citation_ids_filtered_defensively(fake_litellm: MagicMock) -> None:
    """If a provider's enum enforcement was somehow soft and an invalid ID
    snuck through, the parser must drop it rather than emit a bad citation."""
    doc, chunks = _make_doc_and_chunks()
    sids = [s.id for sec in doc.sections for p in sec.paragraphs for s in p.sentences]
    payload = {
        "refused": False,
        "sentences": [
            {"text": "Claim with one valid and one invalid cite.",
             "citations": [sids[0], "made-up::s999"]},
        ],
    }
    fake_litellm.completion.return_value = _fake_response(json.dumps(payload))
    out = ConstrainedCitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    assert len(out) == 1
    assert out[0].supporting_sentence_ids == (sids[0],)  # invalid filtered


@pytest.mark.smoke
def test_selected_option_prepends_bold_headline_for_matcher(fake_litellm: MagicMock) -> None:
    """The bold ``**selected_option**`` sentence is what makes downstream MC
    matchers work on constrained output. Without it, the matcher has to
    parse free prose and fails on the model's reasoning that mentions
    multiple options."""
    doc, chunks = _make_doc_and_chunks()
    sids = [s.id for sec in doc.sections for p in sec.paragraphs for s in p.sentences]
    payload = {
        "refused": False,
        "selected_option": "2.7 fold",
        "sentences": [
            {"text": "Active genes increase contacts by 2.7-fold.",
             "citations": [sids[0]]},
        ],
    }
    fake_litellm.completion.return_value = _fake_response(json.dumps(payload))
    out = ConstrainedCitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    # Headline comes first, exactly as the model picked it, wrapped in bold
    assert out[0].text == "**2.7 fold**"
    # Real sentence preserved with its citation
    assert len(out) == 2
    assert out[1].supporting_sentence_ids == (sids[0],)


@pytest.mark.smoke
def test_empty_selected_option_does_not_prepend_headline(fake_litellm: MagicMock) -> None:
    """If the model leaves selected_option blank, don't pollute the output."""
    doc, chunks = _make_doc_and_chunks()
    sids = [s.id for sec in doc.sections for p in sec.paragraphs for s in p.sentences]
    payload = {
        "refused": False,
        "selected_option": "",  # blank — open-ended question fallback
        "sentences": [
            {"text": "A claim.", "citations": [sids[0]]},
        ],
    }
    fake_litellm.completion.return_value = _fake_response(json.dumps(payload))
    out = ConstrainedCitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    assert len(out) == 1
    assert not out[0].text.startswith("**")


@pytest.mark.smoke
def test_sentence_with_only_invalid_cites_has_zero_confidence(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_and_chunks()
    payload = {
        "refused": False,
        "sentences": [
            {"text": "Unsupported claim.", "citations": ["made-up::s1"]},
        ],
    }
    fake_litellm.completion.return_value = _fake_response(json.dumps(payload))
    out = ConstrainedCitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    assert len(out) == 1
    assert out[0].supporting_sentence_ids == ()
    assert out[0].confidence == 0.0
