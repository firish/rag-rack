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
from verifiable_rag.models.answer import Strictness
from verifiable_rag.parsers import CachingParser, DoclingParser
from verifiable_rag.pipeline import Pipeline
from verifiable_rag.rerankers import BGERerankerV2
from verifiable_rag.verifiers import HHEMVerifier

_BENCHMARKS = {
    "harry_potter_micro": HarryPotterMicroBench,
}


def build_baseline_pipeline(
    model: str,
    min_child_tokens: int = 100,
    use_reranker: bool = True,
    verifier_name: str = "none",
    strictness: Strictness = "loose",
    top_k_retrieve: int = 80,
    top_k_rerank: int = 8,
) -> Pipeline:
    """Wire the eval pipeline.

    *min_child_tokens* is the chunker's lower bound. 100 (~75 words) gives
    BGE-small enough semantic surface for stable embeddings on dialogue-heavy
    text without over-merging. Set to 0 to reproduce the v1 baseline.

    With *use_reranker* (default True), top-K candidates from the hybrid
    retriever go through a cross-encoder reranker before reaching the LLM.
    Defaults: retrieve 80 candidates, rerank to 8 for the LLM.

    With *verifier_name="hhem"*, each generated cited sentence is checked
    by HHEM-2.1-open against the cited source span via NLI. The Pipeline
    *strictness* threshold governs whether low-faithfulness sentences get
    refused (loose=never, balanced=0.5, strict=0.7, paranoid=0.9).
    """
    verifier = HHEMVerifier() if verifier_name == "hhem" else None

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
        reranker=BGERerankerV2() if use_reranker else None,
        verifier=verifier,
        generator=PromptedCitedGenerator(model=model),
        strictness=strictness,
        top_k_retrieve=top_k_retrieve,
        top_k_rerank=top_k_rerank,
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
        default=100,
        help=(
            "ParentChildChunker.min_child_tokens. Set to 0 to reproduce the "
            "v1 baseline (no merging of small paragraphs)."
        ),
    )
    p.add_argument(
        "--no-reranker",
        action="store_true",
        help="Disable the BGE cross-encoder reranker (for ablation).",
    )
    p.add_argument(
        "--top-k-retrieve",
        type=int,
        default=80,
        help="Candidates pulled from the hybrid index before reranking.",
    )
    p.add_argument(
        "--top-k-rerank",
        type=int,
        default=8,
        help="Chunks sent to the LLM after reranking.",
    )
    p.add_argument(
        "--verifier",
        choices=("none", "hhem"),
        default="none",
        help="NLI verifier to use. 'hhem' uses Vectara HHEM-2.1-open.",
    )
    p.add_argument(
        "--strictness",
        choices=("loose", "balanced", "strict", "paranoid"),
        default="loose",
        help=(
            "Refusal threshold mode. loose=never refuse on faithfulness, "
            "balanced=0.5, strict=0.7, paranoid=0.9. The verifier always "
            "runs if enabled; this only controls refusal."
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
    pipeline = build_baseline_pipeline(
        args.model,
        min_child_tokens=args.min_tokens,
        use_reranker=not args.no_reranker,
        verifier_name=args.verifier,
        strictness=args.strictness,
        top_k_retrieve=args.top_k_retrieve,
        top_k_rerank=args.top_k_rerank,
    )
    rerank_label = "bge-rerank-v2-m3" if not args.no_reranker else "no-reranker"
    verifier_label = "hhem-2.1-open" if args.verifier == "hhem" else "no-verifier"
    label = (
        f"{args.model} | bge-small | hybrid(BM25+lance) | "
        f"min_tokens={args.min_tokens} | {rerank_label} | "
        f"retrieve={args.top_k_retrieve}/rerank={args.top_k_rerank} | "
        f"{verifier_label} | {args.strictness}"
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
