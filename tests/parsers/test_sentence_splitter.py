"""SentenceSplitter tests — focus on the offset-tracking invariant.

The wtpsplit model is mocked so tests run without downloading 50+ MB of weights.
A separate slow test exercises the real model when available.
"""
from __future__ import annotations

from typing import Any

import pytest

from verifiable_rag.parsers._sentence_splitter import SentenceSplitter


def _patch_model(splitter: SentenceSplitter, fake: Any) -> None:
    """Replace the lazy-loaded model with *fake*."""
    splitter._sat = fake


class _FakeModel:
    def __init__(self, sentences: list[str]) -> None:
        self._sentences = sentences

    def split(self, text: str, lang_code: str = "en") -> list[str]:
        return self._sentences


@pytest.mark.smoke
def test_split_with_offsets_basic() -> None:
    splitter = SentenceSplitter()
    _patch_model(splitter, _FakeModel(["First sentence.", "Second sentence."]))

    text = "First sentence. Second sentence."
    spans = splitter.split_with_offsets(text)

    assert len(spans) == 2
    # Offset round-trip — the foundational invariant
    for s in spans:
        assert text[s.start:s.end] == s.text
    assert spans[0].text == "First sentence."
    assert spans[1].text == "Second sentence."


@pytest.mark.smoke
def test_split_with_offsets_handles_leading_whitespace() -> None:
    splitter = SentenceSplitter()
    _patch_model(
        splitter,
        _FakeModel(["First sentence.", " Second sentence.", "  Third sentence."]),
    )

    text = "First sentence. Second sentence.  Third sentence."
    spans = splitter.split_with_offsets(text)
    assert len(spans) == 3
    for s in spans:
        assert text[s.start:s.end] == s.text


@pytest.mark.smoke
def test_split_with_offsets_skips_text_not_in_input() -> None:
    """If wtpsplit ever emits text not in the input, we drop it rather than guess."""
    splitter = SentenceSplitter()
    _patch_model(
        splitter,
        _FakeModel(["Real first.", "INVENTED.", "Real last."]),
    )
    text = "Real first. Real last."
    spans = splitter.split_with_offsets(text)
    assert len(spans) == 2
    assert spans[0].text == "Real first."
    assert spans[1].text == "Real last."


@pytest.mark.smoke
def test_split_with_offsets_handles_empty_text() -> None:
    splitter = SentenceSplitter()
    # No model load needed for empty text — short-circuited
    assert splitter.split_with_offsets("") == []
    assert splitter.split_with_offsets("   ") == []


@pytest.mark.smoke
def test_split_with_offsets_advances_cursor_past_repeated_phrase() -> None:
    """Ensure repeated sentences don't all match the first occurrence."""
    splitter = SentenceSplitter()
    _patch_model(splitter, _FakeModel(["Hello.", "Hello.", "World."]))
    text = "Hello. Hello. World."
    spans = splitter.split_with_offsets(text)
    assert len(spans) == 3
    assert [s.start for s in spans] == [0, 7, 14]
    for s in spans:
        assert text[s.start:s.end] == s.text


@pytest.mark.smoke
def test_split_with_offsets_emits_actual_substring_not_model_text() -> None:
    """Even if the model returns a slightly different string (whitespace), we
    emit what's actually in the input — guarantees the offset invariant."""
    splitter = SentenceSplitter()
    # Note: model output has trailing space; input has it stripped between sents
    _patch_model(splitter, _FakeModel(["Alpha.   ", "Beta."]))
    text = "Alpha.   Beta."
    spans = splitter.split_with_offsets(text)
    assert len(spans) == 2
    assert spans[0].text == "Alpha."
    assert spans[1].text == "Beta."
    for s in spans:
        assert text[s.start:s.end] == s.text


@pytest.mark.slow
def test_real_wtpsplit_model_smoke() -> None:
    """Exercise the actual SaT model on a paragraph.  Skipped if wtpsplit absent."""
    pytest.importorskip("wtpsplit")
    splitter = SentenceSplitter(model="sat-3l")
    text = (
        "The transformer architecture introduced multi-head attention. "
        "It became the foundation for modern LLMs. "
        "Subsequent research scaled it dramatically."
    )
    spans = splitter.split_with_offsets(text)
    assert len(spans) >= 2
    for s in spans:
        assert text[s.start:s.end] == s.text
