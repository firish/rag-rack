"""MiniCheckVerifier tests — mock transformers so no real model is loaded."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from unittest.mock import MagicMock, patch

import pytest

from verifiable_rag.verifiers.minicheck import MiniCheckVerifier


@dataclass
class _FakeGenerateOutput:
    scores: tuple  # tuple of (batch, vocab) tensors


def _make_fake_tokenizer(yes_id: int = 5, no_id: int = 7) -> MagicMock:
    tok = MagicMock(name="tokenizer")

    def _call(*args: Any, **kwargs: Any) -> Any:
        texts = args[0] if args else kwargs.get("text") or kwargs.get("texts")
        if isinstance(texts, str):
            if texts == "1":
                return MagicMock(input_ids=[yes_id])
            if texts == "0":
                return MagicMock(input_ids=[no_id])
            texts = [texts]
        # Batch call from score_pairs — return a Mapping[str, Tensor]-like
        import torch

        ids = torch.zeros((len(texts), 8), dtype=torch.long)
        attn = torch.ones_like(ids)
        out = {"input_ids": ids, "attention_mask": attn}

        class _BatchEncoding(dict):
            def to(self, _device: str) -> Any:
                return self

            def items(self):  # for k, v in inputs.items() compatibility
                return super().items()

        return _BatchEncoding(out)

    tok.side_effect = _call
    tok.return_value = MagicMock()
    return tok


def _make_fake_model(scores_per_call: list[list[tuple[float, float]]]) -> MagicMock:
    """Build a model whose generate() returns canned (no_logit, yes_logit) pairs.

    Each call consumes one entry from ``scores_per_call``; that entry is a
    list of (no_logit, yes_logit) tuples, one per batch row.
    """
    import torch

    model = MagicMock(name="model")
    model.eval.return_value = model
    call_idx = {"i": 0}

    def _generate(**kwargs: Any) -> _FakeGenerateOutput:
        batch = scores_per_call[call_idx["i"]]
        call_idx["i"] += 1
        vocab_size = 10
        logits = torch.full((len(batch), vocab_size), -1e9)
        for row, (no_l, yes_l) in enumerate(batch):
            logits[row, 7] = no_l  # matches _make_fake_tokenizer's no_id
            logits[row, 5] = yes_l  # matches yes_id
        return _FakeGenerateOutput(scores=(logits,))

    model.generate.side_effect = _generate
    return model


@pytest.mark.smoke
def test_score_pairs_empty_returns_empty() -> None:
    v = MiniCheckVerifier()
    assert v.score_pairs([]) == []


@pytest.mark.smoke
def test_score_pairs_filters_empty_strings_without_loading_model() -> None:
    """All-empty input should never trigger a model load."""
    v = MiniCheckVerifier()
    with patch("transformers.AutoTokenizer.from_pretrained") as ptok, patch(
        "transformers.AutoModelForSeq2SeqLM.from_pretrained"
    ) as pmodel:
        scores = v.score_pairs([("", "x"), ("x", ""), ("", "")])
    assert scores == [0.0, 0.0, 0.0]
    ptok.assert_not_called()
    pmodel.assert_not_called()


@pytest.mark.smoke
def test_score_pairs_returns_softmax_over_yes_no() -> None:
    """Logits (no=0, yes=10) → softmax ≈ 1.0; (no=10, yes=0) → ≈ 0.0."""
    fake_tok = _make_fake_tokenizer(yes_id=5, no_id=7)
    fake_model = _make_fake_model(
        scores_per_call=[
            [
                (0.0, 10.0),  # very supported
                (10.0, 0.0),  # very unsupported
                (5.0, 5.0),  # 50/50
            ]
        ]
    )

    v = MiniCheckVerifier()
    with patch("transformers.AutoTokenizer.from_pretrained", return_value=fake_tok), patch(
        "transformers.AutoModelForSeq2SeqLM.from_pretrained", return_value=fake_model
    ):
        scores = v.score_pairs(
            [
                ("Paris is in France.", "Paris is in France."),
                ("Paris is in France.", "Paris is on Mars."),
                ("ambiguous text", "ambiguous claim"),
            ]
        )

    assert scores[0] == pytest.approx(1.0, abs=1e-3)
    assert scores[1] == pytest.approx(0.0, abs=1e-3)
    assert scores[2] == pytest.approx(0.5, abs=1e-3)


@pytest.mark.smoke
def test_score_pairs_skips_empty_within_mixed_batch() -> None:
    fake_tok = _make_fake_tokenizer()
    # Only 2 valid pairs reach the model.
    fake_model = _make_fake_model([[(0.0, 10.0), (10.0, 0.0)]])
    v = MiniCheckVerifier()
    with patch("transformers.AutoTokenizer.from_pretrained", return_value=fake_tok), patch(
        "transformers.AutoModelForSeq2SeqLM.from_pretrained", return_value=fake_model
    ):
        scores = v.score_pairs(
            [
                ("good premise", "good hypothesis"),
                ("", "skipped"),
                ("other premise", "other hypothesis"),
            ]
        )
    assert scores[0] == pytest.approx(1.0, abs=1e-3)
    assert scores[1] == 0.0
    assert scores[2] == pytest.approx(0.0, abs=1e-3)


@pytest.mark.smoke
def test_raises_on_empty_tokenizer_encoding_for_yes_no() -> None:
    """If '1' / '0' encode to empty lists, surface a clear error.

    Multi-token encodings are accepted — Flan-T5 legitimately splits
    "0" into [SP_marker, "0"] and the model emits the first token, so
    we read position-0 logits for whatever the first encoded id is.
    """

    def _empty_tok(*args: Any, **kwargs: Any) -> Any:
        text = args[0] if args else kwargs.get("text")
        if text in ("1", "0"):
            return MagicMock(input_ids=[])  # empty
        return MagicMock()

    bad_tok = MagicMock()
    bad_tok.side_effect = _empty_tok

    v = MiniCheckVerifier()
    with patch("transformers.AutoTokenizer.from_pretrained", return_value=bad_tok), patch(
        "transformers.AutoModelForSeq2SeqLM.from_pretrained", return_value=MagicMock()
    ), pytest.raises(RuntimeError, match="Empty tokenizer encoding"):
        v.score_pairs([("p", "h")])
