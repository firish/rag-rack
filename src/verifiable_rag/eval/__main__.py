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
import os
import sys
from datetime import datetime
from pathlib import Path

# LiteLLM expects ANTHROPIC_API_KEY; many local .env files use CLAUDE_API_KEY.
# Fall back transparently so `python -m verifiable_rag.eval` works with either.
if "ANTHROPIC_API_KEY" not in os.environ and "CLAUDE_API_KEY" in os.environ:
    os.environ["ANTHROPIC_API_KEY"] = os.environ["CLAUDE_API_KEY"]

from verifiable_rag.chunkers import ParentChildChunker
from verifiable_rag.embedders import CohereEmbedder, SentenceTransformerEmbedder
from verifiable_rag.eval import EvalReport
from verifiable_rag.eval.datasets import (
    ALCEBench,
    HarryPotterMicroBench,
    LitQA2Bench,
    load_litqa2_meta,
)
from verifiable_rag.eval.metrics import multi_choice_accuracy
from verifiable_rag.eval.reporter import write_markdown
from verifiable_rag.eval.runners import run_alce_benchmark, run_benchmark
from verifiable_rag.generators import (
    ConstrainedCitedGenerator,
    PromptedCitedGenerator,
    SAFECitedGenerator,
)
from verifiable_rag.indexers import BM25Index, HybridIndex, LanceDBIndex
from verifiable_rag.models.answer import Strictness
from verifiable_rag.parsers import (
    CachingParser,
    CompositeParser,
    DoclingParser,
    PyMuPDFParser,
)
from verifiable_rag.pipeline import Pipeline
from verifiable_rag.rerankers import BGERerankerV2, CohereReranker
from verifiable_rag.verifiers import HHEMVerifier

_BENCHMARKS = {
    "harry_potter_micro": HarryPotterMicroBench,
    "litqa2": LitQA2Bench,
    # ALCE sub-benchmarks — bench constructed with the sub-benchmark key as
    # an argument so all variants share the same adapter class.
    # ASQA (factoid Q&A with answer ambiguity, GTR/DPR retrieval, Wikipedia)
    "alce_asqa_oracle": lambda: ALCEBench(subbench="alce_asqa_oracle"),
    "alce_asqa_gtr": lambda: ALCEBench(subbench="alce_asqa_gtr"),
    "alce_asqa_dpr": lambda: ALCEBench(subbench="alce_asqa_dpr"),
    # QAMPARI (multi-hop factoid, entity-set answers, GTR/DPR retrieval, Wikipedia)
    "alce_qampari_gtr": lambda: ALCEBench(subbench="alce_qampari_gtr"),
    "alce_qampari_dpr": lambda: ALCEBench(subbench="alce_qampari_dpr"),
    # ELI5 (long-form Q&A, BM25 retrieval, Sphere/CommonCrawl corpus)
    "alce_eli5_bm25": lambda: ALCEBench(subbench="alce_eli5_bm25"),
}


def build_baseline_pipeline(
    model: str,
    min_child_tokens: int = 100,
    embedder_name: str = "bge",
    reranker_name: str = "bge",
    verifier_name: str = "none",
    verifier_threshold: float = 0.3,
    strictness: Strictness = "loose",
    top_k_retrieve: int = 80,
    top_k_rerank: int = 8,
    index_dir: Path = Path(".verifiable_rag_cache/indexes/eval_lance"),
    generator_name: str = "prompted",
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
    verifier = HHEMVerifier(threshold=verifier_threshold) if verifier_name == "hhem" else None

    from verifiable_rag.embedders import Embedder
    from verifiable_rag.rerankers import Reranker

    embedder: Embedder
    if embedder_name == "bge":
        embedder = SentenceTransformerEmbedder(model_name="BAAI/bge-small-en-v1.5")
    elif embedder_name == "cohere":
        embedder = CohereEmbedder()
    else:
        raise ValueError(f"Unknown embedder {embedder_name!r}; choose 'bge' or 'cohere'.")

    reranker: Reranker | None
    if reranker_name == "none":
        reranker = None
    elif reranker_name == "bge":
        reranker = BGERerankerV2()
    elif reranker_name == "cohere":
        reranker = CohereReranker()
    else:
        raise ValueError(
            f"Unknown reranker {reranker_name!r}; choose 'none', 'bge', or 'cohere'."
        )

    from verifiable_rag.generators import Generator

    generator: Generator
    if generator_name == "prompted":
        generator = PromptedCitedGenerator(model=model)
    elif generator_name == "constrained":
        generator = ConstrainedCitedGenerator(model=model)
    elif generator_name == "safe":
        generator = SAFECitedGenerator(model=model)
    else:
        raise ValueError(
            f"Unknown generator {generator_name!r}; choose 'prompted', 'constrained', or 'safe'."
        )

    return Pipeline(
        parser=CachingParser(
            CompositeParser(
                primary=DoclingParser(),
                fallbacks=[PyMuPDFParser()],
            )
        ),
        chunker=ParentChildChunker(
            max_child_tokens=400,
            min_child_tokens=min_child_tokens,
        ),
        embedder=embedder,
        indexer=HybridIndex(
            dense=LanceDBIndex(uri=index_dir),
            sparse=BM25Index(),
        ),
        reranker=reranker,
        verifier=verifier,
        generator=generator,
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
        "--embedder",
        choices=("bge", "cohere"),
        default="bge",
        help=(
            "Dense embedder. bge=BGE-small (local, free, 384-dim). "
            "cohere=embed-english-v3.0 (hosted, $0.10/1M tokens, 1024-dim, "
            "better quality). Switching invalidates any existing index."
        ),
    )
    p.add_argument(
        "--reranker",
        choices=("none", "bge", "cohere"),
        default="bge",
        help=(
            "Reranker stage. bge=local CPU (slow but free). cohere=hosted "
            "(fast, ~$0.002/query). none=skip reranking (quality drops)."
        ),
    )
    p.add_argument(
        "--no-reranker",
        action="store_true",
        help="Back-compat: equivalent to --reranker none.",
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
    p.add_argument(
        "--index-dir",
        type=Path,
        default=Path(".verifiable_rag_cache/indexes/eval_lance"),
        help=(
            "LanceDB index directory. Use a different path when running two "
            "evals concurrently (each needs its own index)."
        ),
    )
    p.add_argument(
        "--max-workers",
        type=int,
        default=1,
        help=(
            "Parallelism for question asks. 1 = sequential (default). "
            "Use >1 only on paid LLM tiers — free tiers (Groq, Gemini) "
            "rate-limit hard. Haiku/Sonnet/4o-mini are fine at 10-20."
        ),
    )
    p.add_argument(
        "--ingest-workers",
        type=int,
        default=1,
        help=(
            "Parallelism for ingest (parse+chunk+embed). 1 = sequential "
            "(default). 4-8 is a good range on a multi-core box for "
            "BGE-small + cached parses."
        ),
    )
    p.add_argument(
        "--verifier-threshold",
        type=float,
        default=0.3,
        help=(
            "Cutoff for the per-sentence is_supported flag (used by surgical "
            "correction in non-loose strictness). HHEM-2.1-open default is "
            "0.3 — empirically loose enough to allow paraphrased citations."
        ),
    )
    p.add_argument(
        "--generator",
        choices=("prompted", "constrained", "safe"),
        default="prompted",
        help=(
            "Cited-generator backend. 'prompted' (default) instructs the LLM "
            "via prompt to cite by sentence ID. 'constrained' uses LiteLLM "
            "response_format JSON schema with a citation enum drawn from the "
            "retrieved chunks — eliminates invented IDs and format drift "
            "(ReClaim, ACL 2024). 'safe' extends constrained with per-sentence "
            "atomic-claim decomposition (SAFE, May 2025) — claims cite at the "
            "fact level, not the sentence level. Requires a structured-output "
            "model: Anthropic Sonnet/Haiku 4.x+, OpenAI GPT-4o family."
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
        # Multi-choice (LitQA2) metrics — only present for that benchmark
        "mc_correct",
        "mc_wrong",
        "mc_unanswered",
        "mc_accuracy_over_answered",
        "mc_accuracy_over_all",
    ):
        if key in report.metrics:
            print(f"  {key:<28s} {report.metrics[key]:.3f}")
    if report.metrics.get("n_errors"):
        print(f"  {'errors':<28s} {int(report.metrics['n_errors'])}")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)

    # Back-compat: --no-reranker overrides --reranker if explicitly passed.
    effective_reranker = "none" if args.no_reranker else args.reranker

    benchmark = _BENCHMARKS[args.benchmark]()
    pipeline = build_baseline_pipeline(
        args.model,
        min_child_tokens=args.min_tokens,
        embedder_name=args.embedder,
        reranker_name=effective_reranker,
        verifier_name=args.verifier,
        verifier_threshold=args.verifier_threshold,
        strictness=args.strictness,
        top_k_retrieve=args.top_k_retrieve,
        top_k_rerank=args.top_k_rerank,
        generator_name=args.generator,
        index_dir=args.index_dir,
    )
    rerank_label = {
        "none": "no-reranker",
        "bge": "bge-rerank-v2-m3",
        "cohere": "cohere-rerank-v3",
    }[effective_reranker]
    embedder_label = {
        "bge": "bge-small",
        "cohere": "cohere-embed-v3",
    }[args.embedder]
    verifier_label = (
        f"hhem-2.1-open@{args.verifier_threshold}" if args.verifier == "hhem" else "no-verifier"
    )
    label = (
        f"{args.model} | {embedder_label} | hybrid(BM25+lance) | "
        f"min_tokens={args.min_tokens} | {rerank_label} | "
        f"retrieve={args.top_k_retrieve}/rerank={args.top_k_rerank} | "
        f"{verifier_label} | {args.strictness} | gen={args.generator}"
    )

    if args.benchmark.startswith("alce_"):
        # ALCE ships per-question pre-retrieved passages, so it uses a
        # separate runner that bypasses the shared-corpus ingestion model.
        report = run_alce_benchmark(
            pipeline=pipeline,
            benchmark=benchmark,
            pipeline_label=label,
            max_questions=args.max_questions,
            delay_between_questions=args.delay,
            max_workers=args.max_workers,
        )
    else:
        report = run_benchmark(
            pipeline=pipeline,
            benchmark=benchmark,
            pipeline_label=label,
            max_questions=args.max_questions,
            delay_between_questions=args.delay,
            max_workers=args.max_workers,
            ingest_workers=args.ingest_workers,
        )

    gold_by_id = {q.id: (q.gold_sentence_ids, q.should_refuse) for q in benchmark.questions()}

    # LitQA2 has multi-choice gold — score that separately and merge into the
    # report's metrics dict so the markdown table includes it.
    if args.benchmark == "litqa2":
        meta = load_litqa2_meta()
        mc_gold = {qid: (m["ideal"], m["distractors"]) for qid, m in meta.items()}
        mc_metrics = multi_choice_accuracy(report.records, mc_gold)
        # Prefix MC metric keys for clarity in the report
        for k, v in mc_metrics.items():
            if k not in ("n_questions", "n_errors"):
                report.metrics[k] = v

    out_path = args.out or Path(
        f"benchmarks/{args.benchmark}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    )
    write_markdown(report, gold_by_id, out_path)

    _print_summary(report)
    print(f"\nReport written to: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
