"""LLMJudgeVerifier tests — mock litellm so no real API calls happen."""

from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from verifiable_rag.verifiers.llm_judge import LLMJudgeVerifier, _parse_judgment


# --------------------------------------------------------------------------- #
# _parse_judgment — pure function, easy to exercise
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_parse_supported_high_confidence() -> None:
    s = _parse_judgment('{"supported": true, "confidence": 0.95}')
    assert s == pytest.approx(0.95)


@pytest.mark.smoke
def test_parse_unsupported_high_confidence() -> None:
    s = _parse_judgment('{"supported": false, "confidence": 0.95}')
    assert s == pytest.approx(0.05)


@pytest.mark.smoke
def test_parse_supported_low_confidence_floor() -> None:
    """Confidence clamps to [0.5, 1.0] — boolean is the dominant signal."""
    s = _parse_judgment('{"supported": true, "confidence": 0.3}')
    assert s == pytest.approx(0.5)


@pytest.mark.smoke
def test_parse_code_fenced_json() -> None:
    raw = '```json\n{"supported": true, "confidence": 0.9}\n```'
    assert _parse_judgment(raw) == pytest.approx(0.9)


@pytest.mark.smoke
def test_parse_with_surrounding_prose() -> None:
    raw = 'Here is my judgment: {"supported": true, "confidence": 0.8} done.'
    assert _parse_judgment(raw) == pytest.approx(0.8)


@pytest.mark.smoke
def test_parse_malformed_returns_zero() -> None:
    assert _parse_judgment("not json at all") == 0.0
    assert _parse_judgment("") == 0.0
    assert _parse_judgment("{garbage}") == 0.0


@pytest.mark.smoke
def test_parse_missing_confidence_uses_default() -> None:
    """Missing confidence → defaults to 0.5; supported=true → 0.5."""
    assert _parse_judgment('{"supported": true}') == pytest.approx(0.5)
    assert _parse_judgment('{"supported": false}') == pytest.approx(0.5)


@pytest.mark.smoke
def test_parse_non_dict_returns_zero() -> None:
    assert _parse_judgment("[1, 2, 3]") == 0.0


# --------------------------------------------------------------------------- #
# score_pairs — mock litellm.completion
# --------------------------------------------------------------------------- #


def _fake_completion_returning(text: str) -> MagicMock:
    response = MagicMock()
    response.choices = [MagicMock()]
    response.choices[0].message.content = text
    return response


@pytest.mark.smoke
def test_score_pairs_empty_returns_empty() -> None:
    v = LLMJudgeVerifier()
    assert v.score_pairs([]) == []


@pytest.mark.smoke
def test_score_pairs_filters_empty_without_llm_call() -> None:
    v = LLMJudgeVerifier()
    with patch("litellm.completion") as completion:
        scores = v.score_pairs([("", "x"), ("x", ""), ("", "")])
    assert scores == [0.0, 0.0, 0.0]
    completion.assert_not_called()


@pytest.mark.smoke
def test_score_pairs_with_scripted_judgments() -> None:
    """Each LLM call returns a canned JSON judgment; check the mapping."""
    responses = [
        _fake_completion_returning('{"supported": true, "confidence": 0.9}'),
        _fake_completion_returning('{"supported": false, "confidence": 0.9}'),
        _fake_completion_returning('not json'),  # → 0.0
    ]
    v = LLMJudgeVerifier(max_workers=1)  # sequential to keep order deterministic
    with patch("litellm.completion", side_effect=responses):
        scores = v.score_pairs(
            [
                ("Paris is in France.", "Paris is in France."),
                ("Paris is in France.", "Paris is on Mars."),
                ("p", "h"),
            ]
        )
    assert scores[0] == pytest.approx(0.9)
    assert scores[1] == pytest.approx(0.1)
    assert scores[2] == 0.0


@pytest.mark.smoke
def test_score_pairs_recovers_from_per_call_errors() -> None:
    """If one LLM call raises, that pair scores 0 and the batch continues."""
    def _completion(**kwargs: object) -> MagicMock:
        user_text = kwargs["messages"][1]["content"]
        if "boom" in user_text:
            raise RuntimeError("simulated provider error")
        return _fake_completion_returning('{"supported": true, "confidence": 0.85}')

    v = LLMJudgeVerifier(max_workers=1)
    with patch("litellm.completion", side_effect=_completion):
        scores = v.score_pairs([("p1", "h1"), ("boom", "h2"), ("p3", "h3")])
    assert scores[0] == pytest.approx(0.85)
    assert scores[1] == 0.0
    assert scores[2] == pytest.approx(0.85)
