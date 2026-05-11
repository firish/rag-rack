"""Smoke tests for the HarryPotterMicroBench dataset definition."""

from __future__ import annotations

import pytest

from verifiable_rag.eval import Benchmark, EvalQuestion
from verifiable_rag.eval.datasets import HarryPotterMicroBench


@pytest.mark.smoke
def test_satisfies_benchmark_protocol() -> None:
    bench = HarryPotterMicroBench()
    assert isinstance(bench, Benchmark)
    assert bench.name == "harry_potter_micro"


@pytest.mark.smoke
def test_yields_questions() -> None:
    bench = HarryPotterMicroBench()
    qs = list(bench.questions())
    assert len(qs) == 15
    assert all(isinstance(q, EvalQuestion) for q in qs)


@pytest.mark.smoke
def test_question_ids_are_unique() -> None:
    bench = HarryPotterMicroBench()
    ids = [q.id for q in bench.questions()]
    assert len(ids) == len(set(ids)), "duplicate question IDs in benchmark"


@pytest.mark.smoke
def test_includes_refusal_cases() -> None:
    """Tier 1 needs refusal questions to score abstention metrics meaningfully."""
    bench = HarryPotterMicroBench()
    refusals = [q for q in bench.questions() if q.should_refuse]
    assert len(refusals) >= 3, "expected at least 3 refusal cases"
    # Refusal questions must have empty gold (enforced by EvalQuestion __post_init__)
    for q in refusals:
        assert not q.gold_sentence_ids


@pytest.mark.smoke
def test_answerable_questions_have_gold_ids() -> None:
    bench = HarryPotterMicroBench()
    for q in bench.questions():
        if not q.should_refuse:
            assert q.gold_sentence_ids, f"question {q.id} has no gold IDs"


@pytest.mark.smoke
def test_all_questions_share_one_pdf() -> None:
    """Single source document — runner should ingest it exactly once."""
    bench = HarryPotterMicroBench()
    paths = {p for q in bench.questions() for p in q.document_paths}
    assert len(paths) == 1
