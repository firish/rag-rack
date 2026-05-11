"""Render an EvalReport as a markdown document.

Two sections:
  1. Summary — pipeline label, benchmark name, aggregate metrics.
  2. Per-question table — id, refused?, citations vs gold, faithfulness.

Markdown is checked into ``benchmarks/`` so we have a versioned trail of
baseline numbers as we tune the pipeline.
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from verifiable_rag.eval import EvalReport


def to_markdown(
    report: EvalReport,
    gold_by_id: dict[str, tuple[frozenset[str], bool]],
    *,
    timestamp: datetime | None = None,
) -> str:
    """Render *report* as a markdown string."""
    ts = (timestamp or datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    lines: list[str] = []
    lines.append(f"# Eval Report: {report.benchmark_name}")
    lines.append("")
    lines.append(f"- **Pipeline:** `{report.pipeline_label}`")
    lines.append(f"- **Run at:** {ts}")
    lines.append(f"- **Questions:** {int(report.metrics.get('n_questions', 0))}")
    if report.metrics.get("n_errors", 0):
        lines.append(f"- **Errors:** {int(report.metrics['n_errors'])}")
    lines.append("")

    lines.append("## Aggregate metrics")
    lines.append("")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    for key in (
        "citation_precision",
        "citation_recall",
        "citation_f1",
        "coverage",
        "localization_accuracy",
        "abstention_precision",
        "abstention_recall",
        "abstention_f1",
    ):
        if key in report.metrics:
            lines.append(f"| `{key}` | {report.metrics[key]:.3f} |")
    lines.append("")

    lines.append("## Per-question results")
    lines.append("")
    lines.append("| ID | Refused | Should refuse | Cited ∩ Gold | Cited | Gold | Faith |")
    lines.append("|---|---|---|---|---|---|---|")
    for record in report.records:
        gold_ids, should_refuse = gold_by_id.get(record.question_id, (frozenset(), False))
        intersect = len(record.cited_sentence_ids & gold_ids)
        cited = len(record.cited_sentence_ids)
        gold = len(gold_ids)
        err = f" ⚠️ {record.error}" if record.error else ""
        lines.append(
            f"| `{record.question_id}` | "
            f"{'✓' if record.was_refused else '✗'} | "
            f"{'✓' if should_refuse else '✗'} | "
            f"{intersect} | {cited} | {gold} | "
            f"{record.faithfulness_score:.2f}{err} |"
        )
    lines.append("")

    lines.append("## Per-question answers")
    lines.append("")
    for record in report.records:
        lines.append(f"### `{record.question_id}`")
        if record.error:
            lines.append(f"**Error:** {record.error}")
            lines.append("")
            continue
        if record.was_refused:
            lines.append("_Refused._")
        else:
            lines.append(f"> {record.answer_text or '_(empty)_'}")
        if record.cited_sentence_ids:
            lines.append("")
            lines.append(f"Cited: {', '.join(sorted(record.cited_sentence_ids))}")
        lines.append("")

    return "\n".join(lines)


def write_markdown(
    report: EvalReport,
    gold_by_id: dict[str, tuple[frozenset[str], bool]],
    output_path: Path,
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(to_markdown(report, gold_by_id), encoding="utf-8")
