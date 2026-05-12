"""HHEMVerifier tests.

The transformers module is patched into sys.modules so no model is
downloaded. The fake ``AutoModelForSequenceClassification.from_pretrained``
returns a mock whose ``predict`` returns a controllable score array — letting
us assert ordering, threshold application, and edge cases deterministically.
"""

from __future__ import annotations

import sys
from typing import Any
from unittest.mock import MagicMock

import pytest

from tests.chunkers.conftest import build_document
from verifiable_rag.models.answer import CitedSentence
from verifiable_rag.models.document import Document
from verifiable_rag.verifiers import HHEMVerifier, Verifier

# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #


@pytest.fixture
def fake_transformers(monkeypatch: pytest.MonkeyPatch) -> MagicMock:
    """Inject a fake transformers module that returns canned NLI scores."""
    mock_model = MagicMock()

    # Default: every pair scores 0.8 (above default threshold)
    def fake_predict(pairs: list[tuple[str, str]]) -> list[float]:
        return [0.8] * len(pairs)

    mock_model.predict.side_effect = fake_predict

    fake_module = MagicMock()
    fake_module.AutoModelForSequenceClassification.from_pretrained.return_value = mock_model
    monkeypatch.setitem(sys.modules, "transformers", fake_module)
    return mock_model


def _make_doc() -> Document:
    return build_document(
        sections_spec=[
            ("Intro", [["Hagrid is a wizard.", "He keeps the keys at Hogwarts."]]),
            ("Methods", [["Harry has a lightning-bolt scar."]]),
        ],
        doc_id="bio",
    )


# --------------------------------------------------------------------------- #
# Protocol conformance + construction
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_satisfies_verifier_protocol() -> None:
    assert isinstance(HHEMVerifier(), Verifier)


@pytest.mark.smoke
def test_construction_does_not_load_model(monkeypatch: pytest.MonkeyPatch) -> None:
    loaded: list[bool] = []

    def fake_from_pretrained(*_a: object, **_kw: object) -> MagicMock:
        loaded.append(True)
        return MagicMock()

    fake_module = MagicMock()
    fake_module.AutoModelForSequenceClassification.from_pretrained.side_effect = (
        fake_from_pretrained
    )
    monkeypatch.setitem(sys.modules, "transformers", fake_module)

    HHEMVerifier()  # must not call from_pretrained
    assert not loaded


@pytest.mark.smoke
def test_invalid_threshold_raises() -> None:
    with pytest.raises(ValueError, match="threshold"):
        HHEMVerifier(threshold=1.5)
    with pytest.raises(ValueError, match="threshold"):
        HHEMVerifier(threshold=-0.1)


# --------------------------------------------------------------------------- #
# verify() — edge cases
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_verify_empty_sentences_returns_empty(fake_transformers: MagicMock) -> None:
    v = HHEMVerifier()
    assert v.verify([], {}) == []
    fake_transformers.predict.assert_not_called()


@pytest.mark.smoke
def test_verify_no_cited_ids_yields_zero_score(fake_transformers: MagicMock) -> None:
    """A CitedSentence with no citations gets nli_score=0, is_supported=False."""
    doc = _make_doc()
    cs = CitedSentence(
        text="Some unsupported claim.",
        supporting_sentence_ids=(),  # empty!
        confidence=0.0,
    )
    v = HHEMVerifier()
    results = v.verify([cs], {doc.doc_id: doc})

    assert len(results) == 1
    assert results[0].nli_score == 0.0
    assert results[0].is_supported is False
    assert results[0].claim_text == "Some unsupported claim."
    # And we didn't burn a model call on an empty pair
    fake_transformers.predict.assert_not_called()


@pytest.mark.smoke
def test_verify_unknown_cited_id_yields_zero_score(fake_transformers: MagicMock) -> None:
    """If every cited id is missing from the documents dict, score=0."""
    doc = _make_doc()
    cs = CitedSentence(
        text="Made-up claim.",
        supporting_sentence_ids=("bio::sNOPE",),
        confidence=1.0,
    )
    v = HHEMVerifier()
    results = v.verify([cs], {doc.doc_id: doc})

    assert results[0].nli_score == 0.0
    assert results[0].is_supported is False
    fake_transformers.predict.assert_not_called()


# --------------------------------------------------------------------------- #
# verify() — scoring + threshold
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_verify_returns_one_result_per_sentence(fake_transformers: MagicMock) -> None:
    doc = _make_doc()
    cs1 = CitedSentence(text="Hagrid is a wizard.", supporting_sentence_ids=("bio::s0",), confidence=1.0)
    cs2 = CitedSentence(text="Harry has a scar.", supporting_sentence_ids=("bio::s2",), confidence=1.0)

    v = HHEMVerifier()
    results = v.verify([cs1, cs2], {doc.doc_id: doc})

    assert len(results) == 2
    assert results[0].cited_sentence_index == 0
    assert results[1].cited_sentence_index == 1


@pytest.mark.smoke
def test_verify_threshold_above_yields_supported(fake_transformers: MagicMock) -> None:
    """Score above threshold → is_supported=True."""
    fake_transformers.predict.side_effect = lambda pairs: [0.85]
    doc = _make_doc()
    cs = CitedSentence(text="Claim.", supporting_sentence_ids=("bio::s0",), confidence=1.0)

    v = HHEMVerifier(threshold=0.5)
    results = v.verify([cs], {doc.doc_id: doc})

    assert results[0].nli_score == pytest.approx(0.85)
    assert results[0].is_supported is True


@pytest.mark.smoke
def test_verify_threshold_below_yields_unsupported(fake_transformers: MagicMock) -> None:
    fake_transformers.predict.side_effect = lambda pairs: [0.30]
    doc = _make_doc()
    cs = CitedSentence(text="Claim.", supporting_sentence_ids=("bio::s0",), confidence=1.0)

    v = HHEMVerifier(threshold=0.5)
    results = v.verify([cs], {doc.doc_id: doc})

    assert results[0].nli_score == pytest.approx(0.30)
    assert results[0].is_supported is False


@pytest.mark.smoke
def test_verify_custom_threshold(fake_transformers: MagicMock) -> None:
    fake_transformers.predict.side_effect = lambda pairs: [0.65]
    doc = _make_doc()
    cs = CitedSentence(text="Claim.", supporting_sentence_ids=("bio::s0",), confidence=1.0)

    # Score 0.65, threshold 0.7 → unsupported
    v_strict = HHEMVerifier(threshold=0.7)
    results = v_strict.verify([cs], {doc.doc_id: doc})
    assert results[0].is_supported is False

    # Same score, threshold 0.5 → supported
    fake_transformers.predict.side_effect = lambda pairs: [0.65]
    v_balanced = HHEMVerifier(threshold=0.5)
    results = v_balanced.verify([cs], {doc.doc_id: doc})
    assert results[0].is_supported is True


# --------------------------------------------------------------------------- #
# verify() — premise construction
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_verify_premise_uses_only_cited_sentence_texts(fake_transformers: MagicMock) -> None:
    """Premise is built from cited sentence texts — NOT the surrounding chunk."""
    doc = _make_doc()
    cs = CitedSentence(
        text="Hagrid keeps keys.",
        supporting_sentence_ids=("bio::s1",),  # "He keeps the keys at Hogwarts."
        confidence=1.0,
    )
    v = HHEMVerifier()
    v.verify([cs], {doc.doc_id: doc})

    args, _kw = fake_transformers.predict.call_args
    pairs = args[0]
    assert len(pairs) == 1
    premise, hypothesis = pairs[0]
    # Only s1's text should be in the premise — not s0 ("Hagrid is a wizard")
    assert "keeps the keys" in premise
    assert "wizard" not in premise
    assert hypothesis == "Hagrid keeps keys."


@pytest.mark.smoke
def test_verify_premise_concatenates_multi_id_citations(fake_transformers: MagicMock) -> None:
    """Multi-citation: premise = ALL cited sentence texts concatenated."""
    doc = _make_doc()
    cs = CitedSentence(
        text="Hagrid is a wizard who keeps the keys at Hogwarts.",
        supporting_sentence_ids=("bio::s0", "bio::s1"),
        confidence=1.0,
    )
    v = HHEMVerifier()
    v.verify([cs], {doc.doc_id: doc})

    args, _kw = fake_transformers.predict.call_args
    premise, _ = args[0][0]
    assert "wizard" in premise
    assert "keeps the keys" in premise


@pytest.mark.smoke
def test_verify_premise_skips_unknown_ids_keeps_known(fake_transformers: MagicMock) -> None:
    """Mixed valid/invalid IDs: skip invalid, build premise from valid."""
    doc = _make_doc()
    cs = CitedSentence(
        text="Hagrid is a wizard.",
        supporting_sentence_ids=("bio::s0", "bio::sNOPE"),  # one valid, one missing
        confidence=1.0,
    )
    v = HHEMVerifier()
    v.verify([cs], {doc.doc_id: doc})

    args, _kw = fake_transformers.predict.call_args
    premise, _ = args[0][0]
    assert "wizard" in premise


# --------------------------------------------------------------------------- #
# verify() — batching
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_verify_batches_all_pairs_in_one_predict_call(fake_transformers: MagicMock) -> None:
    """One predict() call covering all pairs — not one per sentence."""
    doc = _make_doc()
    cs_list = [
        CitedSentence(text="A.", supporting_sentence_ids=("bio::s0",), confidence=1.0),
        CitedSentence(text="B.", supporting_sentence_ids=("bio::s1",), confidence=1.0),
        CitedSentence(text="C.", supporting_sentence_ids=("bio::s2",), confidence=1.0),
    ]
    v = HHEMVerifier()
    v.verify(cs_list, {doc.doc_id: doc})

    # One call, three pairs
    assert fake_transformers.predict.call_count == 1
    pairs = fake_transformers.predict.call_args.args[0]
    assert len(pairs) == 3


@pytest.mark.smoke
def test_verify_empty_premise_sentences_skip_predict(fake_transformers: MagicMock) -> None:
    """If 1 of 3 sentences has no citations, only 2 pairs go to predict."""
    fake_transformers.predict.side_effect = lambda pairs: [0.9] * len(pairs)
    doc = _make_doc()
    cs_list = [
        CitedSentence(text="A.", supporting_sentence_ids=("bio::s0",), confidence=1.0),
        CitedSentence(text="No-cite.", supporting_sentence_ids=(), confidence=0.0),
        CitedSentence(text="C.", supporting_sentence_ids=("bio::s2",), confidence=1.0),
    ]
    v = HHEMVerifier()
    results = v.verify(cs_list, {doc.doc_id: doc})

    # Predict called once, with only the 2 scorable pairs
    pairs = fake_transformers.predict.call_args.args[0]
    assert len(pairs) == 2

    # Order preserved in results
    assert results[0].nli_score == pytest.approx(0.9)
    assert results[1].nli_score == 0.0  # the empty-citation one
    assert results[2].nli_score == pytest.approx(0.9)


# --------------------------------------------------------------------------- #
# Slow integration test — real HHEM model
# --------------------------------------------------------------------------- #


@pytest.mark.slow
def test_real_hhem_distinguishes_entailment_from_contradiction() -> None:
    pytest.importorskip("transformers")
    doc = _make_doc()

    cs_supported = CitedSentence(
        text="Hagrid is a wizard.",
        supporting_sentence_ids=("bio::s0",),  # "Hagrid is a wizard."
        confidence=1.0,
    )
    cs_contradicted = CitedSentence(
        text="Hagrid is a vampire.",
        supporting_sentence_ids=("bio::s0",),  # premise says wizard, claim says vampire
        confidence=1.0,
    )

    v = HHEMVerifier()
    results = v.verify([cs_supported, cs_contradicted], {doc.doc_id: doc})

    # The supported claim should score noticeably higher than the
    # contradicted one — exact thresholds depend on the model, so we just
    # check the relative ordering.
    assert results[0].nli_score > results[1].nli_score
