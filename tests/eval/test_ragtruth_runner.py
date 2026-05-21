"""RAGTruth runner tests — use a stub NLIScorer + stub splitter so we
don't pay for HHEM or wtpsplit in CI.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path

import pytest

from verifiable_rag.eval.datasets.ragtruth import RAGTruthBench
from verifiable_rag.eval.ragtruth_runner import (
    compute_metrics,
    RAGTruthRecord,
    run_ragtruth,
)

pd = pytest.importorskip("pandas")


# --------------------------------------------------------------------------- #
# Stubs
# --------------------------------------------------------------------------- #


@dataclass(frozen=True)
class _FakeSpan:
    text: str
    start: int
    end: int


class _SentenceSplitter:
    """Split on '. ' — good enough for tests."""

    def split_with_offsets(self, text: str) -> list[_FakeSpan]:
        spans: list[_FakeSpan] = []
        cursor = 0
        for chunk in text.split(". "):
            if not chunk.strip():
                continue
            start = text.find(chunk, cursor)
            end = start + len(chunk)
            spans.append(_FakeSpan(text=chunk, start=start, end=end))
            cursor = end
        return spans


class _ScriptedScorer:
    """Returns a score from a lookup keyed by hypothesis text.

    Unknown hypotheses default to ``default_score``. ``calls`` records
    every batch so tests can assert batching behavior.
    """

    def __init__(self, scores_by_hypothesis: dict[str, float], default_score: float = 0.5):
        self.scores = scores_by_hypothesis
        self.default = default_score
        self.calls: list[list[tuple[str, str]]] = []

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        self.calls.append(list(pairs))
        return [self.scores.get(h, self.default) for _, h in pairs]


# --------------------------------------------------------------------------- #
# Fixture: a tiny synthetic RAGTruthBench (mirrors test_ragtruth.py shape)
# --------------------------------------------------------------------------- #


def _make_row(*, row_id: int, task_type: str, model: str, output: str, spans: list[dict]) -> dict:
    encoded = list(json.dumps(spans))
    return {
        "id": row_id,
        "query": "q",
        "context": "Paris is the capital of France.",
        "output": output,
        "task_type": task_type,
        "quality": "good",
        "model": model,
        "temperature": 0.7,
        "hallucination_labels": encoded,
        "hallucination_labels_processed": {"evident_conflict": 0, "baseless_info": 0},
        "input_str": "x",
    }


@pytest.fixture
def synthetic_bench(tmp_path: Path) -> RAGTruthBench:
    rows = [
        # Clean response: 2 sentences, both supported (score 0.9)
        _make_row(
            row_id=1,
            task_type="QA",
            model="gpt-4-0613",
            output="Paris is in France. It is the capital.",
            spans=[],
        ),
        # Hallucinated response: 2 sentences, one supported one not (min agg → low)
        _make_row(
            row_id=2,
            task_type="QA",
            model="gpt-4-0613",
            output="Paris is in France. The moon is made of cheese.",
            spans=[
                {
                    "start": 20,
                    "end": 50,
                    "text": "The moon is made of cheese.",
                    "meta": "x",
                    "label_type": "Evident Conflict",
                    "implicit_true": False,
                    "due_to_null": False,
                }
            ],
        ),
        # Clean response, Summary task
        _make_row(
            row_id=3,
            task_type="Summary",
            model="llama-2-13b-chat",
            output="Paris is the French capital.",
            spans=[],
        ),
        # Hallucinated, Summary task
        _make_row(
            row_id=4,
            task_type="Summary",
            model="llama-2-13b-chat",
            output="Berlin is the French capital.",
            spans=[
                {
                    "start": 0,
                    "end": 29,
                    "text": "Berlin is the French capital.",
                    "meta": "x",
                    "label_type": "Evident Conflict",
                    "implicit_true": False,
                    "due_to_null": False,
                }
            ],
        ),
    ]
    df = pd.DataFrame(rows)
    cache_root = tmp_path / "ragtruth"
    (cache_root / "data").mkdir(parents=True)
    df.to_parquet(cache_root / "data" / "test-00000-of-00001.parquet")
    return RAGTruthBench(cache_root=cache_root)


# --------------------------------------------------------------------------- #
# Tests
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_runs_and_produces_one_record_per_example(synthetic_bench: RAGTruthBench) -> None:
    scorer = _ScriptedScorer({}, default_score=0.5)
    report = run_ragtruth(
        scorer,
        synthetic_bench,
        sentence_splitter=_SentenceSplitter(),
        progress=False,
    )
    assert len(report.records) == 4
    assert {r.example_id for r in report.records} == {"1", "2", "3", "4"}


@pytest.mark.smoke
def test_min_aggregation_picks_worst_sentence(synthetic_bench: RAGTruthBench) -> None:
    """The 'moon is made of cheese' sentence should drag the response score down."""
    # The splitter drops the trailing period on non-final sentences and
    # keeps it on the final one. Keys reflect that.
    scorer = _ScriptedScorer(
        {
            "Paris is in France": 0.9,
            "It is the capital.": 0.85,
            "The moon is made of cheese.": 0.05,
            "Paris is the French capital.": 0.9,
            "Berlin is the French capital.": 0.1,
        },
        default_score=0.5,
    )
    report = run_ragtruth(
        scorer,
        synthetic_bench,
        aggregation="min",
        sentence_splitter=_SentenceSplitter(),
        progress=False,
    )
    by_id = {r.example_id: r for r in report.records}
    assert by_id["1"].response_score == pytest.approx(0.85)  # min(0.9, 0.85)
    assert by_id["2"].response_score == pytest.approx(0.05)  # the moon sentence
    assert by_id["3"].response_score == pytest.approx(0.9)
    assert by_id["4"].response_score == pytest.approx(0.1)


@pytest.mark.smoke
def test_mean_aggregation_smooths_scores(synthetic_bench: RAGTruthBench) -> None:
    scorer = _ScriptedScorer(
        {
            "Paris is in France": 0.9,
            "It is the capital.": 0.7,
            "The moon is made of cheese.": 0.1,
            "Paris is the French capital.": 0.9,
            "Berlin is the French capital.": 0.1,
        },
        default_score=0.5,
    )
    report = run_ragtruth(
        scorer,
        synthetic_bench,
        aggregation="mean",
        sentence_splitter=_SentenceSplitter(),
        progress=False,
    )
    by_id = {r.example_id: r for r in report.records}
    assert by_id["1"].response_score == pytest.approx(0.8)  # (0.9 + 0.7) / 2
    assert by_id["2"].response_score == pytest.approx(0.5)  # (0.9 + 0.1) / 2


@pytest.mark.smoke
def test_metrics_reflect_perfect_separation(synthetic_bench: RAGTruthBench) -> None:
    """If the scorer perfectly separates clean from hallucinated, AUROC=1."""
    scorer = _ScriptedScorer(
        {
            "Paris is in France": 0.95,
            "It is the capital.": 0.95,
            "The moon is made of cheese.": 0.05,
            "Paris is the French capital.": 0.95,
            "Berlin is the French capital.": 0.05,
        },
    )
    report = run_ragtruth(
        scorer,
        synthetic_bench,
        sentence_splitter=_SentenceSplitter(),
        progress=False,
    )
    assert report.metrics["n"] == 4
    assert report.metrics["n_hallucinated"] == 2
    assert report.metrics["auroc"] == pytest.approx(1.0)
    assert report.metrics["f1_best"] == pytest.approx(1.0)


@pytest.mark.smoke
def test_per_task_and_per_model_breakdown(synthetic_bench: RAGTruthBench) -> None:
    scorer = _ScriptedScorer({}, default_score=0.5)
    report = run_ragtruth(
        scorer,
        synthetic_bench,
        sentence_splitter=_SentenceSplitter(),
        progress=False,
    )
    assert set(report.by_task) == {"QA", "Summary"}
    assert set(report.by_model) == {"gpt-4-0613", "llama-2-13b-chat"}
    # Each subset has 2 examples
    assert report.by_task["QA"]["n"] == 2
    assert report.by_model["gpt-4-0613"]["n"] == 2


@pytest.mark.smoke
def test_batching_respected(synthetic_bench: RAGTruthBench) -> None:
    """With batch_size=2 and ~7 total sentences, we should see multiple calls."""
    scorer = _ScriptedScorer({}, default_score=0.5)
    run_ragtruth(
        scorer,
        synthetic_bench,
        sentence_splitter=_SentenceSplitter(),
        progress=False,
        batch_size=2,
    )
    # 4 examples × ~2 sentences = ~8 pairs; with batch=2 → 4 calls minimum.
    assert len(scorer.calls) >= 3
    # No single batch should exceed batch_size.
    assert all(len(call) <= 2 for call in scorer.calls)


@pytest.mark.smoke
def test_rejects_unknown_aggregation(synthetic_bench: RAGTruthBench) -> None:
    scorer = _ScriptedScorer({})
    with pytest.raises(ValueError, match="aggregation must be"):
        run_ragtruth(
            scorer,
            synthetic_bench,
            aggregation="median",
            sentence_splitter=_SentenceSplitter(),
            progress=False,
        )


@pytest.mark.smoke
def test_compute_metrics_empty_records() -> None:
    out = compute_metrics([])
    assert out["n"] == 0
    assert out["n_scored"] == 0


@pytest.mark.smoke
def test_compute_metrics_all_one_class() -> None:
    """AUROC undefined when only one class present — should silently skip."""
    records = [
        RAGTruthRecord(
            example_id=str(i),
            task_type="QA",
            model="gpt-4",
            is_hallucinated=False,
            response_score=0.9,
            n_sentences=1,
        )
        for i in range(3)
    ]
    out = compute_metrics(records)
    assert out["n_scored"] == 3
    assert "auroc" not in out
    assert "f1_best" not in out
