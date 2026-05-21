"""Run a verifier against RAGTruth and write a baseline report.

Default: full test split (2700 rows), min-aggregation, HHEM-2.1-open.
Outputs three files under ``benchmarks/baselines/``:

  <slug>.md     — human-readable summary (kept in git)
  <slug>.json   — aggregate + per-task + per-model metrics (kept in git)
  <slug>.jsonl  — raw per-example records (gitignore later — see project_backlog_eval_infra)

Examples
--------
  # full HHEM baseline (~20-30 min on CPU, 2700 examples)
  python scripts/run_ragtruth.py --verifier hhem --slug ragtruth_hhem_v1

  # quick smoke with 50 examples
  python scripts/run_ragtruth.py --verifier hhem --max-examples 50 --slug ragtruth_hhem_smoke
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import asdict
from pathlib import Path

from verifiable_rag.eval.datasets import RAGTruthBench
from verifiable_rag.eval.ragtruth_runner import RAGTruthReport, run_ragtruth
from verifiable_rag.verifiers import (
    HHEMVerifier,
    LLMJudgeVerifier,
    MiniCheckVerifier,
    ModalHHEMScorer,
    ModalMiniCheckScorer,
    NLIScorer,
)

_OUTPUT_DIR = Path("benchmarks/baselines")
_VERIFIERS = ("hhem", "minicheck", "llm_judge", "modal_hhem", "modal_minicheck")


def _resolve_device(arg: str) -> str | None:
    """``auto`` → mps if Apple Silicon, cuda if NVIDIA, else cpu."""
    if arg != "auto":
        return None if arg == "default" else arg
    try:
        import torch

        if torch.backends.mps.is_available():
            return "mps"
        if torch.cuda.is_available():
            return "cuda"
    except ImportError:
        pass
    return "cpu"


def _build_verifier(
    name: str, device: str | None, judge_model: str, judge_max_workers: int
) -> tuple[NLIScorer, str]:
    if name == "hhem":
        return HHEMVerifier(device=device), "hhem-2.1-open"
    if name == "minicheck":
        return MiniCheckVerifier(device=device), "minicheck-flan-t5-large"
    if name == "llm_judge":
        return (
            LLMJudgeVerifier(model=judge_model, max_workers=judge_max_workers),
            f"llm-judge::{judge_model}",
        )
    if name == "modal_hhem":
        return ModalHHEMScorer(), "hhem-2.1-open (modal-T4)"
    if name == "modal_minicheck":
        return ModalMiniCheckScorer(), "minicheck-flan-t5-large (modal-T4)"
    raise ValueError(f"unknown --verifier {name!r}; choose from {_VERIFIERS}")


def _format_summary_md(report: RAGTruthReport, args: argparse.Namespace, wall_secs: float) -> str:
    m = report.metrics
    lines: list[str] = [
        f"# RAGTruth baseline — {report.scorer_label}",
        "",
        f"- **scorer:** {report.scorer_label}",
        f"- **split:** {args.split}",
        f"- **aggregation:** {report.aggregation}",
        f"- **task filter:** {args.task or 'all'}",
        f"- **model filter:** {args.model or 'all'}",
        f"- **examples scored:** {int(m.get('n_scored', 0))} (of {int(m.get('n', 0))}; {int(m.get('n_errors', 0))} errors)",
        f"- **base rate (hallucinated):** {m.get('base_rate', 0):.3f}",
        f"- **wall time:** {wall_secs:.1f}s",
        "",
        "## Aggregate metrics",
        "",
        "| metric | value |",
        "|---|---|",
    ]
    for key in ("auroc", "auprc", "f1_best", "precision_best", "recall_best", "threshold_best"):
        if key in m:
            lines.append(f"| {key} | {m[key]:.4f} |")
    lines += ["", "## Per task", "", "| task | n | base_rate | auroc | f1_best |", "|---|---|---|---|---|"]
    for task, sub in report.by_task.items():
        lines.append(
            f"| {task} | {int(sub.get('n_scored', 0))} | "
            f"{sub.get('base_rate', 0):.3f} | "
            f"{sub.get('auroc', float('nan')):.4f} | "
            f"{sub.get('f1_best', float('nan')):.4f} |"
        )
    lines += ["", "## Per model", "", "| model | n | base_rate | auroc | f1_best |", "|---|---|---|---|---|"]
    for model, sub in report.by_model.items():
        lines.append(
            f"| {model} | {int(sub.get('n_scored', 0))} | "
            f"{sub.get('base_rate', 0):.3f} | "
            f"{sub.get('auroc', float('nan')):.4f} | "
            f"{sub.get('f1_best', float('nan')):.4f} |"
        )
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--verifier", choices=_VERIFIERS, default="hhem")
    p.add_argument("--split", choices=("train", "test"), default="test")
    p.add_argument("--task", default=None, help="comma-sep subset of {QA,Data2txt,Summary}")
    p.add_argument("--model", default=None, help="comma-sep upstream LLM filter")
    p.add_argument("--max-examples", type=int, default=None)
    p.add_argument(
        "--stratify",
        action="store_true",
        help="split --max-examples evenly across QA/Data2txt/Summary",
    )
    p.add_argument("--seed", type=int, default=None, help="deterministic shuffle when sampling")
    p.add_argument("--aggregation", choices=("min", "mean"), default="min")
    p.add_argument("--batch-size", type=int, default=32)
    p.add_argument("--slug", default="ragtruth_hhem_v1", help="output filename prefix")
    p.add_argument("--output-dir", type=Path, default=_OUTPUT_DIR)
    p.add_argument(
        "--device",
        default="auto",
        help="auto|cpu|mps|cuda|default. auto picks mps>cuda>cpu; default uses verifier's own default",
    )
    p.add_argument(
        "--judge-model",
        default="claude-haiku-4-5-20251001",
        help="LiteLLM model id when --verifier llm_judge",
    )
    p.add_argument(
        "--judge-max-workers",
        type=int,
        default=4,
        help="concurrent LLM judge calls. Tier-1 Anthropic: 4 (50 RPM ceiling). Higher tiers can go up to 16+",
    )
    args = p.parse_args(argv)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    md_path = args.output_dir / f"{args.slug}.md"
    json_path = args.output_dir / f"{args.slug}.json"
    jsonl_path = args.output_dir / f"{args.slug}.jsonl"

    task_filter = frozenset(args.task.split(",")) if args.task else None
    model_filter = frozenset(args.model.split(",")) if args.model else None

    device = _resolve_device(args.device)
    print(f"[ragtruth] building {args.verifier} verifier (device={device})...", flush=True)
    scorer, label = _build_verifier(
        args.verifier, device, args.judge_model, args.judge_max_workers
    )

    print(f"[ragtruth] loading split={args.split}, task={args.task}, model={args.model}", flush=True)
    bench = RAGTruthBench(
        split=args.split,
        task_filter=task_filter,
        model_filter=model_filter,
        max_examples=args.max_examples,
        stratify_by_task=args.stratify,
        random_seed=args.seed,
    )
    print(f"[ragtruth] {len(bench)} examples to score", flush=True)

    t0 = time.time()
    report = run_ragtruth(
        scorer,
        bench,
        scorer_label=label,
        aggregation=args.aggregation,
        batch_size=args.batch_size,
    )
    wall = time.time() - t0

    summary_md = _format_summary_md(report, args, wall)
    md_path.write_text(summary_md)
    json_path.write_text(
        json.dumps(
            {
                "scorer_label": report.scorer_label,
                "aggregation": report.aggregation,
                "wall_secs": wall,
                "metrics": report.metrics,
                "by_task": report.by_task,
                "by_model": report.by_model,
            },
            indent=2,
        )
    )
    with jsonl_path.open("w") as fh:
        for rec in report.records:
            fh.write(json.dumps(asdict(rec)) + "\n")

    print(summary_md, flush=True)
    print(f"[ragtruth] wrote {md_path}, {json_path}, {jsonl_path}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
