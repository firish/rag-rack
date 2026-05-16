"""Reporter tests — focused on the parser-slice section we just added.

The legacy markdown layout (headline metrics, per-question table, per-question
answers) is already exercised by the smoke runs; here we lock down the new
behaviour so a future refactor doesn't silently drop the parser slice.
"""
from __future__ import annotations

from datetime import datetime

import pytest

from verifiable_rag.eval import EvalRecord, EvalReport
from verifiable_rag.eval.reporter import to_markdown


def _make_report_with_parsers(
    parsers_by_qid: dict[str, list[str]],
) -> tuple[EvalReport, dict[str, tuple[frozenset[str], bool]]]:
    """A 3-question report with citation gold so metrics are non-trivial."""
    records = [
        EvalRecord(
            question_id=qid,
            was_refused=False,
            cited_sentence_ids=frozenset({"x"}),
            answer_text="A.",
            faithfulness_score=0.9,
        )
        for qid in parsers_by_qid
    ]
    report = EvalReport(
        benchmark_name="t",
        pipeline_label="test",
        records=records,
        parsers_by_question_id=parsers_by_qid,
    )
    gold_by_id: dict[str, tuple[frozenset[str], bool]] = {
        qid: (frozenset({"x"}), False) for qid in parsers_by_qid
    }
    return report, gold_by_id


@pytest.mark.smoke
def test_parser_slice_section_appears_when_two_parsers_used() -> None:
    report, gold = _make_report_with_parsers(
        {"q1": ["docling"], "q2": ["pymupdf"], "q3": ["docling"]}
    )
    md = to_markdown(report, gold, timestamp=datetime(2026, 1, 1))
    assert "## Parser slice" in md
    # Both buckets surfaced
    assert "docling" in md and "pymupdf" in md


@pytest.mark.smoke
def test_parser_slice_omitted_when_only_one_parser_used() -> None:
    report, gold = _make_report_with_parsers(
        {"q1": ["docling"], "q2": ["docling"]}
    )
    md = to_markdown(report, gold, timestamp=datetime(2026, 1, 1))
    assert "## Parser slice" not in md


@pytest.mark.smoke
def test_parser_slice_omitted_when_no_provenance_recorded() -> None:
    """Old reports without parsers_by_question_id should render unchanged."""
    record = EvalRecord(
        question_id="q1",
        was_refused=False,
        cited_sentence_ids=frozenset({"x"}),
        answer_text="A.",
        faithfulness_score=0.9,
    )
    report = EvalReport(
        benchmark_name="t",
        pipeline_label="test",
        records=[record],
        # parsers_by_question_id intentionally left empty
    )
    gold = {"q1": (frozenset({"x"}), False)}
    md = to_markdown(report, gold, timestamp=datetime(2026, 1, 1))
    assert "## Parser slice" not in md


@pytest.mark.smoke
def test_mixed_parser_question_appears_in_both_buckets() -> None:
    """A question whose PDFs span two parsers contributes to both slices."""
    report, gold = _make_report_with_parsers(
        {"q1": ["docling", "pymupdf"], "q2": ["docling"]}
    )
    md = to_markdown(report, gold, timestamp=datetime(2026, 1, 1))
    # The slice table should report n=2 for docling and n=1 for pymupdf.
    # Parse the row directly to lock that down.
    line = next(ln for ln in md.splitlines() if ln.startswith("| `n` |"))
    cells = [c.strip() for c in line.strip("|").split("|") if c.strip()]
    # cells = ["`n`", "<docling>", "<pymupdf>"]  (buckets sorted alphabetically)
    assert cells[1] == "2.000"  # docling: q1 + q2
    assert cells[2] == "1.000"  # pymupdf: just q1
