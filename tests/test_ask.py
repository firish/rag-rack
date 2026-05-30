"""Top-level ask() helper tests — uses a fake preset so no models load."""

from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock

import pytest

import verifiable_rag
from verifiable_rag._ask import ask
from verifiable_rag.models.answer import (
    Answer,
    FaithfulnessComponents,
)


def _make_dummy_answer() -> Answer:
    return Answer(
        query="Q",
        sentences=[],
        faithfulness_score=0.5,
        faithfulness_components=FaithfulnessComponents(
            retrieval_score=0.5, nli_score=0.5
        ),
        unsupported_claims=[],
        retrieved_chunks=[],
        verification_results=[],
        strictness="balanced",
    )


def _fake_pipeline_factory(answer: Answer | None = None) -> MagicMock:
    """Return a callable that produces a MagicMock Pipeline returning *answer*."""
    answer = answer or _make_dummy_answer()
    pipeline = MagicMock()
    pipeline.ask.return_value = answer
    pipeline.ingest.return_value = None

    def _factory(**_kw: object) -> MagicMock:
        return pipeline

    _factory.pipeline = pipeline  # type: ignore[attr-defined]
    return _factory


# --------------------------------------------------------------------------- #
# Top-level exposure
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_ask_is_exposed_at_top_level() -> None:
    assert callable(verifiable_rag.ask)


# --------------------------------------------------------------------------- #
# ask() — basic flow
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_ask_calls_ingest_then_ask(monkeypatch: pytest.MonkeyPatch) -> None:
    factory = _fake_pipeline_factory()
    monkeypatch.setattr("verifiable_rag.presets.hybrid_balanced", factory)

    answer = ask("What is X?", docs="paper.pdf")

    assert isinstance(answer, Answer)
    factory.pipeline.ingest.assert_called_once_with(Path("paper.pdf"))
    factory.pipeline.ask.assert_called_once_with("What is X?")


@pytest.mark.smoke
def test_ask_accepts_list_of_docs(monkeypatch: pytest.MonkeyPatch) -> None:
    factory = _fake_pipeline_factory()
    monkeypatch.setattr("verifiable_rag.presets.hybrid_balanced", factory)

    ask("Q?", docs=["a.pdf", Path("b.pdf"), "c.pdf"])

    assert factory.pipeline.ingest.call_count == 3
    actual_paths = [
        call.args[0] for call in factory.pipeline.ingest.call_args_list
    ]
    assert actual_paths == [Path("a.pdf"), Path("b.pdf"), Path("c.pdf")]


@pytest.mark.smoke
def test_ask_uses_named_preset(monkeypatch: pytest.MonkeyPatch) -> None:
    """Switching preset routes through the named factory."""
    balanced = _fake_pipeline_factory()
    strict = _fake_pipeline_factory()
    monkeypatch.setattr("verifiable_rag.presets.hybrid_balanced", balanced)
    monkeypatch.setattr("verifiable_rag.presets.hybrid_strict", strict)

    ask("Q?", docs="x.pdf", preset="hybrid_strict")
    strict.pipeline.ingest.assert_called_once()
    balanced.pipeline.ingest.assert_not_called()


@pytest.mark.smoke
def test_ask_rejects_unknown_preset() -> None:
    with pytest.raises(ValueError, match="Unknown preset"):
        ask("Q?", docs="x.pdf", preset="nope_no_such_preset")


@pytest.mark.smoke
def test_ask_passes_preset_kwargs_through(monkeypatch: pytest.MonkeyPatch) -> None:
    captured: dict[str, object] = {}

    def _factory(**kw: object) -> MagicMock:
        captured.update(kw)
        pipeline = MagicMock()
        pipeline.ask.return_value = _make_dummy_answer()
        return pipeline

    monkeypatch.setattr("verifiable_rag.presets.hybrid_balanced", _factory)

    ask("Q?", docs="x.pdf", generator_model="anthropic/claude-sonnet-4-6")
    assert captured.get("generator_model") == "anthropic/claude-sonnet-4-6"


# --------------------------------------------------------------------------- #
# HTML side-effect
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_ask_writes_html_when_output_html_provided(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    factory = _fake_pipeline_factory()
    monkeypatch.setattr("verifiable_rag.presets.hybrid_balanced", factory)

    html_path = tmp_path / "report.html"
    ask("Q?", docs="x.pdf", output_html=html_path)

    assert html_path.exists()
    content = html_path.read_text()
    assert content.startswith("<!DOCTYPE html>")


@pytest.mark.smoke
def test_ask_does_not_write_html_when_not_requested(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    factory = _fake_pipeline_factory()
    monkeypatch.setattr("verifiable_rag.presets.hybrid_balanced", factory)

    ask("Q?", docs="x.pdf")
    # No html file created in tmp_path
    assert not list(tmp_path.glob("*.html"))


@pytest.mark.smoke
def test_ask_html_title_override(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    factory = _fake_pipeline_factory()
    monkeypatch.setattr("verifiable_rag.presets.hybrid_balanced", factory)

    html_path = tmp_path / "report.html"
    ask(
        "Q?",
        docs="x.pdf",
        output_html=html_path,
        output_html_title="My Audit Report",
    )
    assert "My Audit Report" in html_path.read_text()
