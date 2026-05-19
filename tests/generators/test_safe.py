"""SAFECitedGenerator tests.

litellm is patched into sys.modules so no network calls are made. Tests
exercise schema construction, atomic-claim parsing (flattened to
CitedSentence), refusal handling, and defensive enum filtering.
"""
from __future__ import annotations

import json
import sys
from typing import Any
from unittest.mock import MagicMock

import pytest

from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.generators import Generator, SAFECitedGenerator
from verifiable_rag.models.answer import CitedSentence
from verifiable_rag.models.chunk import Chunk, RetrievedChunk

from tests.chunkers.conftest import build_document


def _fake_response(text: str) -> Any:
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
    gen = SAFECitedGenerator(model="anthropic/claude-haiku-4-5")
    assert isinstance(gen, Generator)
    assert gen.mode == "safe"


@pytest.mark.smoke
def test_rejects_bad_init_args() -> None:
    with pytest.raises(ValueError, match="temperature"):
        SAFECitedGenerator(temperature=-1)
    with pytest.raises(ValueError, match="max_tokens"):
        SAFECitedGenerator(max_tokens=0)
    with pytest.raises(ValueError, match="num_retries"):
        SAFECitedGenerator(num_retries=-1)
    with pytest.raises(ValueError, match="max_citations_per_claim"):
        SAFECitedGenerator(max_citations_per_claim=0)
    with pytest.raises(ValueError, match="max_claims_per_sentence"):
        SAFECitedGenerator(max_claims_per_sentence=0)


# --------------------------------------------------------------------------- #
# Schema construction
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_schema_enum_populated_from_valid_ids() -> None:
    gen = SAFECitedGenerator()
    schema = gen._build_schema(["bio::s1", "bio::s2", "bio::s3"])
    sentences_item = schema["schema"]["properties"]["sentences"]["items"]
    atomic_item = sentences_item["properties"]["atomic_claims"]["items"]
    enum = atomic_item["properties"]["citations"]["items"]["enum"]
    assert enum == ["bio::s1", "bio::s2", "bio::s3"]


@pytest.mark.smoke
def test_schema_enforces_atomic_claim_bounds() -> None:
    gen = SAFECitedGenerator(max_citations_per_claim=2, max_claims_per_sentence=3)
    schema = gen._build_schema(["a"])
    sent_item = schema["schema"]["properties"]["sentences"]["items"]
    claims_block = sent_item["properties"]["atomic_claims"]
    cites_block = claims_block["items"]["properties"]["citations"]
    assert claims_block["minItems"] == 1
    assert claims_block["maxItems"] == 3
    assert cites_block["minItems"] == 1
    assert cites_block["maxItems"] == 2


@pytest.mark.smoke
def test_schema_requires_all_top_level_fields() -> None:
    schema = SAFECitedGenerator()._build_schema(["a"])
    required = schema["schema"]["required"]
    assert set(required) == {"refused", "selected_option", "sentences"}


# --------------------------------------------------------------------------- #
# Parsing — flatten happy path
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_generate_flattens_atomic_claims_into_cited_sentences(
    fake_litellm: MagicMock,
) -> None:
    """Two atomic claims under one sentence → one CitedSentence with the
    union of their cites."""
    doc, chunks = _make_doc_and_chunks()
    sids = [s.id for sec in doc.sections for p in sec.paragraphs for s in p.sentences]
    payload = {
        "refused": False,
        "selected_option": "Mitochondria",
        "sentences": [
            {
                "text": "Mitochondria produce ATP and are organelles.",
                "atomic_claims": [
                    {"claim": "Mitochondria produce ATP", "citations": [sids[0]]},
                    {"claim": "Mitochondria are organelles", "citations": [sids[1]]},
                ],
            }
        ],
    }
    fake_litellm.completion.return_value = _fake_response(json.dumps(payload))

    out = SAFECitedGenerator().generate(
        "What is mitochondria?", _retrieved(chunks), {doc.doc_id: doc}
    )

    # 2 entries: bolded headline + 1 flattened sentence
    assert len(out) == 2
    assert all(isinstance(c, CitedSentence) for c in out)
    # Headline
    assert out[0].text == "**Mitochondria**"
    assert out[0].supporting_sentence_ids == ()
    # Flattened sentence — union of atomic cites
    assert out[1].text == "Mitochondria produce ATP and are organelles."
    assert set(out[1].supporting_sentence_ids) == {sids[0], sids[1]}
    assert out[1].confidence == 1.0


@pytest.mark.smoke
def test_generate_dedupes_union_cites(fake_litellm: MagicMock) -> None:
    """Two atomic claims that cite the same source → one cite in the union."""
    doc, chunks = _make_doc_and_chunks()
    sids = [s.id for sec in doc.sections for p in sec.paragraphs for s in p.sentences]
    payload = {
        "refused": False,
        "selected_option": "X",
        "sentences": [
            {
                "text": "Compound sentence with two claims.",
                "atomic_claims": [
                    {"claim": "Claim A", "citations": [sids[0]]},
                    {"claim": "Claim B", "citations": [sids[0]]},  # same cite
                ],
            }
        ],
    }
    fake_litellm.completion.return_value = _fake_response(json.dumps(payload))
    out = SAFECitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    # Headline + flattened sentence
    assert len(out) == 2
    assert out[1].supporting_sentence_ids == (sids[0],)


@pytest.mark.smoke
def test_generate_passes_response_format_to_litellm(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_and_chunks()
    fake_litellm.completion.return_value = _fake_response(
        '{"refused": false, "selected_option": "", "sentences": []}'
    )
    SAFECitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    call_kwargs = fake_litellm.completion.call_args.kwargs
    assert call_kwargs["response_format"]["type"] == "json_schema"
    sentences_item = call_kwargs["response_format"]["json_schema"]["schema"][
        "properties"]["sentences"]["items"]
    # atomic_claims layer present
    assert "atomic_claims" in sentences_item["properties"]


# --------------------------------------------------------------------------- #
# Refusal + edge cases
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_refused_true_returns_empty(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_and_chunks()
    fake_litellm.completion.return_value = _fake_response(
        '{"refused": true, "selected_option": "Insufficient information to answer", "sentences": []}'
    )
    out = SAFECitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    assert out == []


@pytest.mark.smoke
def test_empty_chunks_returns_empty_without_calling_llm(fake_litellm: MagicMock) -> None:
    out = SAFECitedGenerator().generate("q", [], {})
    assert out == []
    fake_litellm.completion.assert_not_called()


@pytest.mark.smoke
def test_malformed_json_treated_as_refusal(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_and_chunks()
    fake_litellm.completion.return_value = _fake_response("not valid json at all")
    out = SAFECitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    assert out == []


@pytest.mark.smoke
def test_invalid_citation_ids_filtered_from_union(fake_litellm: MagicMock) -> None:
    """If a provider's enum enforcement was soft, defensively drop unknown IDs."""
    doc, chunks = _make_doc_and_chunks()
    sids = [s.id for sec in doc.sections for p in sec.paragraphs for s in p.sentences]
    payload = {
        "refused": False,
        "selected_option": "Y",
        "sentences": [
            {
                "text": "Claim with one valid and one invalid cite.",
                "atomic_claims": [
                    {"claim": "A", "citations": [sids[0], "made-up::s999"]},
                ],
            }
        ],
    }
    fake_litellm.completion.return_value = _fake_response(json.dumps(payload))
    out = SAFECitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    assert len(out) == 2  # headline + sentence
    # Invalid cite dropped from union
    assert out[1].supporting_sentence_ids == (sids[0],)


@pytest.mark.smoke
def test_sentence_with_zero_valid_cites_has_zero_confidence(
    fake_litellm: MagicMock,
) -> None:
    doc, chunks = _make_doc_and_chunks()
    payload = {
        "refused": False,
        "selected_option": "Z",
        "sentences": [
            {
                "text": "Unsupported claim.",
                "atomic_claims": [{"claim": "X", "citations": ["made-up::s1"]}],
            }
        ],
    }
    fake_litellm.completion.return_value = _fake_response(json.dumps(payload))
    out = SAFECitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    assert len(out) == 2
    assert out[1].supporting_sentence_ids == ()
    assert out[1].confidence == 0.0


@pytest.mark.smoke
def test_selected_option_prepends_bold_headline(fake_litellm: MagicMock) -> None:
    """SAFE mirrors constrained's selected_option headline trick so the
    existing MC matcher works."""
    doc, chunks = _make_doc_and_chunks()
    sids = [s.id for sec in doc.sections for p in sec.paragraphs for s in p.sentences]
    payload = {
        "refused": False,
        "selected_option": "2.7 fold",
        "sentences": [
            {
                "text": "Active genes increase contacts by 2.7-fold.",
                "atomic_claims": [{"claim": "increase by 2.7-fold", "citations": [sids[0]]}],
            }
        ],
    }
    fake_litellm.completion.return_value = _fake_response(json.dumps(payload))
    out = SAFECitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    assert out[0].text == "**2.7 fold**"
    assert out[0].supporting_sentence_ids == ()


@pytest.mark.smoke
def test_empty_selected_option_does_not_prepend_headline(fake_litellm: MagicMock) -> None:
    doc, chunks = _make_doc_and_chunks()
    sids = [s.id for sec in doc.sections for p in sec.paragraphs for s in p.sentences]
    payload = {
        "refused": False,
        "selected_option": "",
        "sentences": [
            {
                "text": "A claim.",
                "atomic_claims": [{"claim": "A", "citations": [sids[0]]}],
            }
        ],
    }
    fake_litellm.completion.return_value = _fake_response(json.dumps(payload))
    out = SAFECitedGenerator().generate("q", _retrieved(chunks), {doc.doc_id: doc})
    assert len(out) == 1
    assert not out[0].text.startswith("**")
