"""RAGTruthBench adapter tests.

Uses a tiny synthetic parquet so the test stays offline and fast.
"""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from verifiable_rag.eval.datasets.ragtruth import (
    HallucinationSpan,
    RAGTruthBench,
    RAGTruthExample,
    _parse_spans,
)

pd = pytest.importorskip("pandas")


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #


def _make_row(
    *,
    row_id: int,
    task_type: str,
    model: str,
    spans: list[dict],
) -> dict:
    """Build one row mirroring wandb/RAGTruth-processed's schema.

    ``hallucination_labels`` is encoded as a *list of single-character*
    strings — that's the on-disk shape that bit us originally.
    """
    encoded = list(json.dumps(spans))
    return {
        "id": row_id,
        "query": f"task prompt {row_id}",
        "context": f"source passage {row_id}",
        "output": f"model response number {row_id} text here",
        "task_type": task_type,
        "quality": "good",
        "model": model,
        "temperature": 0.7,
        "hallucination_labels": encoded,
        "hallucination_labels_processed": {
            "evident_conflict": 1 if any(s["label_type"] == "Evident Conflict" for s in spans) else 0,
            "baseless_info": 0,
        },
        "input_str": f"input str {row_id}",
    }


@pytest.fixture
def synthetic_parquet(tmp_path: Path) -> Path:
    """Write a 4-row RAGTruth-shaped parquet under cache_root/data/."""
    rows = [
        _make_row(row_id=1, task_type="QA", model="gpt-4-0613", spans=[]),
        _make_row(
            row_id=2,
            task_type="Summary",
            model="llama-2-13b-chat",
            spans=[
                {
                    "start": 0,
                    "end": 5,
                    "text": "model",
                    "meta": "x",
                    "label_type": "Evident Conflict",
                    "implicit_true": False,
                    "due_to_null": False,
                }
            ],
        ),
        _make_row(row_id=3, task_type="Data2txt", model="mistral-7B-instruct", spans=[]),
        _make_row(row_id=4, task_type="QA", model="gpt-4-0613", spans=[]),
    ]
    df = pd.DataFrame(rows)
    cache_root = tmp_path / "ragtruth"
    (cache_root / "data").mkdir(parents=True)
    df.to_parquet(cache_root / "data" / "test-00000-of-00001.parquet")
    return cache_root


# --------------------------------------------------------------------------- #
# Tests
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_loads_all_rows(synthetic_parquet: Path) -> None:
    bench = RAGTruthBench(cache_root=synthetic_parquet)
    exs = list(bench.examples())
    assert len(exs) == 4
    assert all(isinstance(e, RAGTruthExample) for e in exs)


@pytest.mark.smoke
def test_parses_span_label_correctly(synthetic_parquet: Path) -> None:
    """The character-chunked JSON encoding is the trap we hit IRL."""
    bench = RAGTruthBench(cache_root=synthetic_parquet)
    by_id = {e.id: e for e in bench.examples()}

    clean = by_id["1"]
    assert clean.hallucination_spans == ()
    assert clean.is_hallucinated is False

    halluc = by_id["2"]
    assert len(halluc.hallucination_spans) == 1
    span = halluc.hallucination_spans[0]
    assert isinstance(span, HallucinationSpan)
    assert span.start == 0
    assert span.end == 5
    assert span.text == "model"
    assert span.label_type == "Evident Conflict"
    assert halluc.is_hallucinated is True


@pytest.mark.smoke
def test_task_filter(synthetic_parquet: Path) -> None:
    bench = RAGTruthBench(
        cache_root=synthetic_parquet,
        task_filter=frozenset({"QA"}),
    )
    assert len(bench) == 2
    assert {e.task_type for e in bench.examples()} == {"QA"}


@pytest.mark.smoke
def test_model_filter(synthetic_parquet: Path) -> None:
    bench = RAGTruthBench(
        cache_root=synthetic_parquet,
        model_filter=frozenset({"gpt-4-0613"}),
    )
    assert len(bench) == 2
    assert {e.model for e in bench.examples()} == {"gpt-4-0613"}


@pytest.mark.smoke
def test_max_examples_caps_count(synthetic_parquet: Path) -> None:
    bench = RAGTruthBench(cache_root=synthetic_parquet, max_examples=2)
    assert len(bench) == 2


@pytest.mark.smoke
def test_rejects_unknown_split() -> None:
    with pytest.raises(ValueError, match="split must be"):
        RAGTruthBench(split="dev")  # type: ignore[arg-type]


@pytest.mark.smoke
def test_rejects_unknown_task_filter(synthetic_parquet: Path) -> None:
    with pytest.raises(ValueError, match="unknown task_type"):
        RAGTruthBench(
            cache_root=synthetic_parquet,
            task_filter=frozenset({"Translation"}),
        )


@pytest.mark.smoke
def test_missing_cache_raises_with_fetch_hint(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="fetch_faithfulness_benches"):
        RAGTruthBench(cache_root=tmp_path / "does-not-exist")


@pytest.mark.smoke
def test_parse_spans_handles_empty_and_malformed() -> None:
    assert _parse_spans(None) == ()
    assert _parse_spans("") == ()
    assert _parse_spans("[]") == ()
    assert _parse_spans(list("[]")) == ()
    assert _parse_spans("not json at all") == ()
