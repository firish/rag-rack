"""LitQA2 adapter + multi-choice scoring tests."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from unittest.mock import MagicMock

import pytest

from verifiable_rag.eval import EvalRecord
from verifiable_rag.eval.metrics import multi_choice_accuracy, multi_choice_selected

# --------------------------------------------------------------------------- #
# Fixtures — fake HuggingFace + index
# --------------------------------------------------------------------------- #


@pytest.fixture
def fake_hf_dataset(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> Path:
    """Write a tiny LitQA2-shaped parquet to disk and patch hf_hub_download.

    Three rows: one normal Q, one with insufficient-info gold, one with a
    different DOI.
    """
    pd = pytest.importorskip("pandas")
    rows = [
        {
            "id": "q1",
            "question": "What antibiotic was the bug evolved against?",
            "ideal": "ciprofloxacin",
            "distractors": ["meropenem", "gentamicin", "ampicillin"],
            "sources": ["https://doi.org/10.1/bug-paper"],
            "is_opensource": True,
            "key-passage": "evolved resistance to ciprofloxacin",
        },
        {
            "id": "q2",
            "question": "Some unanswerable thing?",
            "ideal": "Insufficient information to answer",
            "distractors": ["a", "b", "c"],
            "sources": ["https://doi.org/10.1/another-paper"],
            "is_opensource": True,
            "key-passage": "irrelevant",
        },
        {
            "id": "q3",
            "question": "Yet another q?",
            "ideal": "the answer",
            "distractors": ["wrong1"],
            "sources": ["https://doi.org/10.1/third-paper"],
            "is_opensource": False,
            "key-passage": "the answer is the answer",
        },
    ]
    df = pd.DataFrame(rows)
    parquet_path = tmp_path / "litqa2.parquet"
    df.to_parquet(parquet_path)

    # Patch hf_hub_download in BOTH modules that import it
    def fake_download(*_args, **_kwargs):  # type: ignore[no-untyped-def]
        return str(parquet_path)

    fake_module = MagicMock()
    fake_module.hf_hub_download = fake_download
    monkeypatch.setitem(sys.modules, "huggingface_hub", fake_module)

    # Force reimport of litqa2 module so the patched huggingface_hub is used
    import importlib

    import verifiable_rag.eval.datasets.litqa2 as litqa2_mod

    importlib.reload(litqa2_mod)

    return parquet_path


@pytest.fixture
def index_with_two_pdfs(tmp_path: Path) -> Path:
    """Write a minimal index file matching 2 of 3 fake-dataset rows.

    Includes ``key_passage_sentence_ids`` for q1 (so we can assert it flows
    into the EvalQuestion's gold_sentence_ids) and an empty list for q3.
    """
    pdf1 = tmp_path / "paper1.pdf"
    pdf2 = tmp_path / "paper3.pdf"
    pdf1.write_bytes(b"%PDF-1.4\nfake1")
    pdf2.write_bytes(b"%PDF-1.4\nfake3")

    index = {
        "q1": {
            "doi": "10.1/bug-paper",
            "is_opensource": True,
            "path": str(pdf1),
            "source": "unpaywall",
            "error": None,
            "key_passage_sentence_ids": ["bug::s5", "bug::s6"],
            "align_error": None,
        },
        # q2 missing — PDF wasn't fetched
        "q3": {
            "doi": "10.1/third-paper",
            "is_opensource": False,
            "path": str(pdf2),
            "source": "unpaywall+playwright",
            "error": None,
            "key_passage_sentence_ids": [],
            "align_error": None,
        },
    }
    index_path = tmp_path / "_index.json"
    index_path.write_text(json.dumps(index))
    return index_path


# --------------------------------------------------------------------------- #
# multi_choice_selected — core logic
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_mc_selected_picks_unique_match() -> None:
    selected = multi_choice_selected(
        answer_text="The bug evolved resistance to ciprofloxacin [s5]",
        ideal="ciprofloxacin",
        distractors=["meropenem", "gentamicin"],
    )
    assert selected == "ciprofloxacin"


@pytest.mark.smoke
def test_mc_selected_returns_none_on_no_match() -> None:
    selected = multi_choice_selected(
        answer_text="The system cannot answer this from the sources.",
        ideal="ciprofloxacin",
        distractors=["meropenem"],
    )
    assert selected is None


@pytest.mark.smoke
def test_mc_selected_returns_none_on_multiple_matches() -> None:
    """Ambiguous: answer mentions both ideal and a distractor → None."""
    selected = multi_choice_selected(
        answer_text="It evolved resistance to both ciprofloxacin and meropenem",
        ideal="ciprofloxacin",
        distractors=["meropenem"],
    )
    assert selected is None


@pytest.mark.smoke
def test_mc_selected_case_insensitive() -> None:
    selected = multi_choice_selected(
        answer_text="The answer is CIPROFLOXACIN.",
        ideal="ciprofloxacin",
        distractors=["meropenem"],
    )
    assert selected == "ciprofloxacin"


@pytest.mark.smoke
def test_mc_selected_handles_empty_answer() -> None:
    assert multi_choice_selected("", "x", ["y"]) is None


# --------------------------------------------------------------------------- #
# multi_choice_accuracy — aggregation
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_mc_accuracy_counts_correctly() -> None:
    records = [
        EvalRecord(
            question_id="q1",
            was_refused=False,
            cited_sentence_ids=frozenset(),
            answer_text="The answer is X",
            faithfulness_score=0.9,
        ),
        EvalRecord(
            question_id="q2",
            was_refused=False,
            cited_sentence_ids=frozenset(),
            answer_text="The answer is Y",
            faithfulness_score=0.7,
        ),
        EvalRecord(
            question_id="q3",
            was_refused=False,
            cited_sentence_ids=frozenset(),
            answer_text="No clear answer here",
            faithfulness_score=0.1,
        ),
    ]
    gold = {
        "q1": ("X", ["Y", "Z"]),  # correct
        "q2": ("Z", ["Y", "W"]),  # picked Y → wrong
        "q3": ("X", ["Y"]),  # nothing matched → unanswered
    }
    metrics = multi_choice_accuracy(records, gold)
    assert metrics["mc_correct"] == 1
    assert metrics["mc_wrong"] == 1
    assert metrics["mc_unanswered"] == 1
    assert metrics["mc_accuracy_over_answered"] == pytest.approx(0.5)
    assert metrics["mc_accuracy_over_all"] == pytest.approx(1 / 3)


@pytest.mark.smoke
def test_mc_accuracy_skips_errored_records() -> None:
    records = [
        EvalRecord(
            question_id="q1",
            was_refused=False,
            cited_sentence_ids=frozenset(),
            answer_text="The answer is X",
            faithfulness_score=0.9,
        ),
        EvalRecord(
            question_id="q2",
            was_refused=False,
            cited_sentence_ids=frozenset(),
            answer_text="",
            faithfulness_score=0.0,
            error="boom",
        ),
    ]
    gold = {"q1": ("X", ["Y"]), "q2": ("X", ["Y"])}
    metrics = multi_choice_accuracy(records, gold)
    assert metrics["mc_correct"] == 1
    assert metrics["n_errors"] == 1


# --------------------------------------------------------------------------- #
# LitQA2Bench — adapter behavior
# --------------------------------------------------------------------------- #


@pytest.mark.smoke
def test_bench_satisfies_protocol(fake_hf_dataset: Path, index_with_two_pdfs: Path) -> None:
    from verifiable_rag.eval import Benchmark
    from verifiable_rag.eval.datasets.litqa2 import LitQA2Bench

    bench = LitQA2Bench(index_path=index_with_two_pdfs)
    assert isinstance(bench, Benchmark)
    assert bench.name == "litqa2"


@pytest.mark.smoke
def test_bench_skips_questions_missing_pdf(
    fake_hf_dataset: Path, index_with_two_pdfs: Path
) -> None:
    from verifiable_rag.eval.datasets.litqa2 import LitQA2Bench

    bench = LitQA2Bench(index_path=index_with_two_pdfs)
    qs = list(bench.questions())

    # q2 was missing → skipped. q1 + q3 present.
    ids = [q.id for q in qs]
    assert "q1" in ids
    assert "q3" in ids
    assert "q2" not in ids
    assert len(qs) == 2


@pytest.mark.smoke
def test_bench_includes_missing_with_allow_missing_flag(
    fake_hf_dataset: Path, index_with_two_pdfs: Path
) -> None:
    from verifiable_rag.eval.datasets.litqa2 import LitQA2Bench

    bench = LitQA2Bench(index_path=index_with_two_pdfs, allow_missing=True)
    qs = list(bench.questions())
    assert len(qs) == 3
    # q2 yields a question with empty document_paths
    by_id = {q.id: q for q in qs}
    assert by_id["q2"].document_paths == ()


@pytest.mark.smoke
def test_bench_detects_should_refuse_for_insufficient_info(
    fake_hf_dataset: Path, index_with_two_pdfs: Path
) -> None:
    from verifiable_rag.eval.datasets.litqa2 import LitQA2Bench

    bench = LitQA2Bench(index_path=index_with_two_pdfs, allow_missing=True)
    by_id = {q.id: q for q in bench.questions()}
    assert by_id["q1"].should_refuse is False
    # q2's ideal starts with "Insufficient" → should_refuse True
    assert by_id["q2"].should_refuse is True


@pytest.mark.smoke
def test_bench_surfaces_key_passage_sentence_ids_as_gold(
    fake_hf_dataset: Path, index_with_two_pdfs: Path
) -> None:
    """Index entries with key_passage_sentence_ids should drive gold_sentence_ids."""
    from verifiable_rag.eval.datasets.litqa2 import LitQA2Bench

    bench = LitQA2Bench(index_path=index_with_two_pdfs)
    by_id = {q.id: q for q in bench.questions()}

    # q1 has key_passage_sentence_ids = ["bug::s5", "bug::s6"] in the fixture
    assert by_id["q1"].gold_sentence_ids == frozenset({"bug::s5", "bug::s6"})
    # q3 has empty key_passage_sentence_ids → gold_sentence_ids is empty
    assert by_id["q3"].gold_sentence_ids == frozenset()


@pytest.mark.smoke
def test_bench_refusal_question_keeps_empty_gold(
    fake_hf_dataset: Path, index_with_two_pdfs: Path
) -> None:
    """Even if an index entry has gold IDs, refusal questions stay empty.

    Refusal questions (ideal == 'Insufficient information...') get
    should_refuse=True. EvalQuestion.__post_init__ requires gold to be
    empty when should_refuse is True, so the adapter must enforce that.
    """
    from verifiable_rag.eval.datasets.litqa2 import LitQA2Bench

    bench = LitQA2Bench(index_path=index_with_two_pdfs, allow_missing=True)
    by_id = {q.id: q for q in bench.questions()}
    # q2's ideal starts with "Insufficient" → should_refuse, gold must be empty
    assert by_id["q2"].should_refuse is True
    assert by_id["q2"].gold_sentence_ids == frozenset()


@pytest.mark.smoke
def test_bench_max_questions_caps(fake_hf_dataset: Path, index_with_two_pdfs: Path) -> None:
    from verifiable_rag.eval.datasets.litqa2 import LitQA2Bench

    bench = LitQA2Bench(index_path=index_with_two_pdfs, max_questions=1)
    qs = list(bench.questions())
    assert len(qs) == 1


@pytest.mark.smoke
def test_bench_question_embeds_mc_options(fake_hf_dataset: Path, index_with_two_pdfs: Path) -> None:
    """q.question must include all options so the LLM can select from them."""
    from verifiable_rag.eval.datasets.litqa2 import LitQA2Bench

    bench = LitQA2Bench(index_path=index_with_two_pdfs)
    by_id = {q.id: q for q in bench.questions()}
    q1 = by_id["q1"]
    # Original question text still present
    assert "antibiotic" in q1.question
    # All MC options embedded
    assert "ciprofloxacin" in q1.question  # ideal
    assert "meropenem" in q1.question  # distractor
    assert "Insufficient information to answer" in q1.question
    # Formatted as a choice block
    assert "Select the best answer" in q1.question


@pytest.mark.smoke
def test_bench_raises_when_index_missing(tmp_path: Path) -> None:
    from verifiable_rag.eval.datasets.litqa2 import LitQA2Bench

    with pytest.raises(FileNotFoundError, match="LitQA2 PDF index"):
        LitQA2Bench(index_path=tmp_path / "nope.json")
