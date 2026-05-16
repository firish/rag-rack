"""Audit refused questions from the v8b run.

Picks N refused question_ids from the latest v8 report, replays them through
the same Cohere pipeline, captures the raw LLM response (which is normally
discarded), and categorises each refusal into:

  A. explicit_refusal      LLM said "I cannot answer" / matched one of the
                           generator's refusal patterns.
  B. no_brackets           LLM produced prose but didn't bracket any sentence
                           IDs → parsed to 0 CitedSentences → empty answer.
  C. bad_citations         LLM bracketed IDs but they weren't in valid_ids.
  D. insufficient_choice   LLM picked LitQA2's "Insufficient information"
                           multi-choice option (a specific anti-pattern).
  E. other                 raw text exists but doesn't fit above.

Usage:
    python scripts/audit_refusals.py \
        --report benchmarks/baselines/v8_litqa2_haiku_cohere.md \
        --n 20 \
        --out /tmp/refusal_audit.jsonl
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, "src")

from verifiable_rag.eval.datasets import LitQA2Bench, load_litqa2_meta
from verifiable_rag.eval.__main__ import build_baseline_pipeline
from verifiable_rag.generators.prompted import _REFUSAL_PATTERNS


def _refused_ids_from_report(report_path: Path) -> list[str]:
    """Parse the report markdown for question_ids marked refused (Refused=✓)."""
    text = report_path.read_text()
    # Row format: | `<id>` | ✓ | ✗ | ... |
    refused: list[str] = []
    row_re = re.compile(r"\|\s*`([^`]+)`\s*\|\s*✓\s*\|\s*✗\s*\|")
    for m in row_re.finditer(text):
        refused.append(m.group(1))
    return refused


def categorise(raw: str, parsed_count: int, valid_ids_count: int) -> str:
    lowered = raw.lower()
    if any(p in lowered for p in _REFUSAL_PATTERNS):
        return "A_explicit_refusal"
    if "insufficient information" in lowered:
        return "D_insufficient_choice"
    if parsed_count == 0:
        # Did the LLM put any [bracket] markers in the output at all?
        if re.search(r"\[[^\]]+\]", raw):
            return "C_bad_citations"
        return "B_no_brackets"
    return "E_other"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--report", type=Path, default=Path("benchmarks/baselines/v8_litqa2_haiku_cohere.md"))
    p.add_argument("--n", type=int, default=20)
    p.add_argument("--out", type=Path, default=Path("/tmp/refusal_audit.jsonl"))
    p.add_argument("--delay", type=float, default=5.0,
                   help="Seconds between asks (rate-limit hygiene).")
    args = p.parse_args()

    os.environ.setdefault("ANTHROPIC_API_KEY", os.environ.get("CLAUDE_API_KEY", ""))

    refused_ids = _refused_ids_from_report(args.report)
    print(f"[audit] {len(refused_ids)} refused questions in {args.report.name}", flush=True)

    target_ids = refused_ids[: args.n]
    print(f"[audit] sampling first {len(target_ids)}", flush=True)

    # Build the same Cohere pipeline as v8b (reuses the populated index).
    pipeline = build_baseline_pipeline(
        model="anthropic/claude-haiku-4-5",
        min_child_tokens=100,
        embedder_name="cohere",
        reranker_name="cohere",
        top_k_retrieve=100,
        top_k_rerank=10,
        index_dir=Path(".verifiable_rag_cache/indexes/eval_lance_cohere_full"),
    )

    # Monkeypatch the generator's _call_llm to capture raw output.
    gen = pipeline.generator  # type: ignore[attr-defined]
    captured: dict[str, str] = {"raw": ""}
    original_call = gen._call_llm  # type: ignore[attr-defined]

    def capturing_call(prompt: str) -> str:
        out = original_call(prompt)
        captured["raw"] = out
        return out

    gen._call_llm = capturing_call  # type: ignore[attr-defined]

    # We also need each question's text + documents to ask().
    bench = LitQA2Bench()
    q_by_id = {q.id: q for q in bench.questions()}
    meta = load_litqa2_meta()

    # Re-ingest documents — but pipeline cache makes this near-instant.
    needed_paths: set[Path] = set()
    for qid in target_ids:
        for path in q_by_id[qid].document_paths:
            needed_paths.add(path)
    print(f"[audit] ingesting {len(needed_paths)} unique source PDFs (cache hits)", flush=True)
    for p_in in needed_paths:
        try:
            pipeline.ingest(p_in)
        except Exception as exc:  # noqa: BLE001
            print(f"  ingest fail: {p_in}: {type(exc).__name__}", flush=True)

    rows: list[dict] = []
    with args.out.open("w") as fout:
        for i, qid in enumerate(target_ids, start=1):
            q = q_by_id[qid]
            print(f"[audit {i}/{len(target_ids)}] {qid[:8]}: {q.question[:80]}", flush=True)
            captured["raw"] = ""
            try:
                answer = pipeline.ask(q.question)
            except Exception as exc:  # noqa: BLE001
                rows.append({"id": qid, "error": f"{type(exc).__name__}: {exc}"})
                fout.write(json.dumps(rows[-1]) + "\n")
                fout.flush()
                time.sleep(args.delay)
                continue

            raw = captured["raw"]
            parsed_count = len(answer.sentences)
            bucket = categorise(raw, parsed_count, valid_ids_count=10)
            mc = meta.get(qid, {})
            row = {
                "id": qid,
                "question": q.question,
                "ideal_choice": mc.get("ideal", ""),
                "distractors": mc.get("distractors", []),
                "raw_llm_text": raw,
                "parsed_cited_count": parsed_count,
                "was_refused": answer.was_refused,
                "bucket": bucket,
                "retrieved_count": len(answer.retrieved_chunks),
            }
            rows.append(row)
            fout.write(json.dumps(row) + "\n")
            fout.flush()
            time.sleep(args.delay)

    # Summary
    print()
    print("=== bucket counts ===")
    counts: dict[str, int] = {}
    for r in rows:
        b = r.get("bucket", "ERROR")
        counts[b] = counts.get(b, 0) + 1
    for b, n in sorted(counts.items()):
        print(f"  {b:<25s} {n:>3d}")

    print(f"\nFull audit written to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
