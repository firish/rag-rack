"""CLI entry point: ``python -m verifiable_rag.eval``.

Usage:
    python -m verifiable_rag.eval [--benchmark NAME] [--model MODEL]
                                  [--max-questions N] [--out PATH]

Currently supports the ``harry_potter_micro`` benchmark and any LiteLLM
model string. Writes a markdown report to ``benchmarks/<benchmark>_<ts>.md``
by default and prints aggregate metrics to stdout.

This wires the same baseline pipeline as ``examples/ask_pdf.py`` (no
reranker, no verifier, loose strictness) so the numbers are comparable.
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime
from pathlib import Path

from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.embedders import SentenceTransformerEmbedder
from verifiable_rag.eval import EvalReport
from verifiable_rag.eval.datasets import HarryPotterMicroBench
from verifiable_rag.eval.reporter import write_markdown
from verifiable_rag.eval.runners import run_benchmark
from verifiable_rag.generators import PromptedCitedGenerator
from verifiable_rag.indexers import BM25Index, HybridIndex, LanceDBIndex
from verifiable_rag.parsers import CachingParser, DoclingParser
from verifiable_rag.pipeline import Pipeline

_BENCHMARKS = {
    "harry_potter_micro": HarryPotterMicroBench,
}


def build_baseline_pipeline(model: str, min_child_tokens: int = 150) -> Pipeline:
    """The same baseline used in examples/ask_pdf.py — no reranker / verifier.

    *min_child_tokens* is the chunker's lower bound. 150 (~120 words) gives
    BGE-small enough semantic surface for stable embeddings on dialogue-heavy
    text. Set to 0 to reproduce the v1 baseline.
    """
    return Pipeline(
        parser=CachingParser(DoclingParser()),
        chunker=ParentChildChunker(
            max_child_tokens=400,
            min_child_tokens=min_child_tokens,
        ),
        embedder=SentenceTransformerEmbedder(model_name="BAAI/bge-small-en-v1.5"),
        indexer=HybridIndex(
            dense=LanceDBIndex(uri=Path(".verifiable_rag_cache/indexes/eval_lance")),
            sparse=BM25Index(),
        ),
        generator=PromptedCitedGenerator(model=model),
        strictness="loose",
        top_k_retrieve=40,
        top_k_rerank=15,
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(
        prog="python -m verifiable_rag.eval",
        description="Run a verifiable-rag eval benchmark and write a markdown report.",
    )
    p.add_argument(
        "--benchmark",
        choices=sorted(_BENCHMARKS),
        default="harry_potter_micro",
    )
    p.add_argument(
        "--model",
        default="groq/llama-3.3-70b-versatile",
        help="LiteLLM model string for the generator.",
    )
    p.add_argument(
        "--max-questions",
        type=int,
        default=None,
        help="Limit the number of questions (smoke runs).",
    )
    p.add_argument(
        "--out",
        type=Path,
        default=None,
        help="Markdown report output path. Defaults to benchmarks/<bench>_<ts>.md",
    )
    p.add_argument(
        "--delay",
        type=float,
        default=7.0,
        help=(
            "Seconds to sleep between questions — required to stay under "
            "free-tier rate limits (Groq free tier = 12K TPM). "
            "Set to 0 if you have a paid LLM tier."
        ),
    )
    p.add_argument(
        "--min-tokens",
        type=int,
        default=150,
        help=(
            "ParentChildChunker.min_child_tokens. Set to 0 to reproduce the "
            "v1 baseline (no merging of small paragraphs)."
        ),
    )
    return p.parse_args(argv)


def _print_summary(report: EvalReport) -> None:
    print()
    print(f"== {report.benchmark_name}  ({report.pipeline_label}) ==")
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
            print(f"  {key:<24s} {report.metrics[key]:.3f}")
    if report.metrics.get("n_errors"):
        print(f"  {'errors':<24s} {int(report.metrics['n_errors'])}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    benchmark = _BENCHMARKS[args.benchmark]()
    pipeline = build_baseline_pipeline(args.model, min_child_tokens=args.min_tokens)
    label = (
        f"{args.model} | bge-small | hybrid(BM25+lance) | "
        f"min_tokens={args.min_tokens} | top_k=15 | loose"
    )

    report = run_benchmark(
        pipeline=pipeline,
        benchmark=benchmark,
        pipeline_label=label,
        max_questions=args.max_questions,
        delay_between_questions=args.delay,
    )

    gold_by_id = {q.id: (q.gold_sentence_ids, q.should_refuse) for q in benchmark.questions()}

    out_path = args.out or Path(
        f"benchmarks/{args.benchmark}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    )
    write_markdown(report, gold_by_id, out_path)

    _print_summary(report)
    print(f"\nReport written to: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
