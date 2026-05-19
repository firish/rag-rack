"""Post-hoc LLM-as-judge scorer for ALCE eval reports.

Computes ALCE-style citation_recall and citation_precision (LOO) over an
eval report produced by ``python -m verifiable_rag.eval --benchmark alce_*``.

For each cited (sentence_text, cited_passage_text) pair, asks a judge LLM
via structured output: "does this passage entail this claim?". Then:

  citation_recall    — fraction of claims where at least one cited passage
                       entails. Per-claim metric.
  citation_precision — leave-one-out per-cite: a cite is NECESSARY iff it
                       entails the claim AND no other cite for that same
                       claim does. Fraction of cites that are necessary.

ALCE's original paper uses T5-XXL TRUE as judge. We default to Haiku 4.5
for speed/cost; pass ``--judge sonnet`` for the more rigorous cross-check.

Caching: judgments are SHA-256 keyed by (claim || source) and persisted as
JSONL. Re-runs are free on identical pairs; runs across different ALCE
sub-benchmarks share the cache automatically.

Example
-------
    # Haiku-judge ASQA top-100 prompted report
    python scripts/llm_judge_alce.py \\
        --subbench alce_asqa_gtr \\
        --judge haiku \\
        --report benchmarks/baselines/alce_asqa_gtr100_haiku_prompted_v1.md

    # Sonnet-judge same report (cross-validation)
    python scripts/llm_judge_alce.py \\
        --subbench alce_asqa_gtr \\
        --judge sonnet \\
        --report benchmarks/baselines/alce_asqa_gtr100_haiku_prompted_v1.md
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from collections.abc import Iterator
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from pathlib import Path

# Bridge LiteLLM's expected env var name from this project's .env convention
if "ANTHROPIC_API_KEY" not in os.environ and "CLAUDE_API_KEY" in os.environ:
    os.environ["ANTHROPIC_API_KEY"] = os.environ["CLAUDE_API_KEY"]

# Lets the script run from the repo root without ``pip install -e .``
sys.path.insert(0, "src")

# --------------------------------------------------------------------- #
# Configuration tables
# --------------------------------------------------------------------- #

# ALCE source-data filename + id-field-name per sub-benchmark.
# Mirrors verifiable_rag.eval.datasets.alce._SUBBENCHES; kept inline here
# so the script has no project dependency beyond filesystem paths.
_SUBBENCH_CONFIG: dict[str, tuple[str, str | None]] = {
    "alce_asqa_oracle": ("asqa_eval_gtr_top100_reranked_oracle.json", "sample_id"),
    "alce_asqa_gtr": ("asqa_eval_gtr_top100.json", "sample_id"),
    "alce_asqa_dpr": ("asqa_eval_dpr_top100.json", "sample_id"),
    "alce_qampari_gtr": ("qampari_eval_gtr_top100.json", "id"),
    "alce_qampari_dpr": ("qampari_eval_dpr_top100.json", "id"),
    "alce_eli5_bm25": ("eli5_eval_bm25_top100.json", None),  # synthesise row_NNNN
}

# Judge model + tier-aware worker count + cache file per judge backend.
_JUDGE_CONFIG: dict[str, tuple[str, int, str]] = {
    "haiku": ("anthropic/claude-haiku-4-5", 8, "/tmp/alce_judge_cache.jsonl"),
    "sonnet": ("anthropic/claude-sonnet-4-6", 4, "/tmp/alce_judge_sonnet_cache.jsonl"),
}

# --------------------------------------------------------------------- #
# Constants — judge prompt + schema
# --------------------------------------------------------------------- #

JUDGE_SYSTEM = (
    "You are a careful textual entailment judge. Given a SOURCE passage and "
    "a CLAIM, decide whether the claim is fully entailed by the source — "
    "i.e., every fact in the claim is directly supported. Paraphrase, "
    "numeric approximation, and reasonable inference are acceptable. "
    "New facts not in the source are not. Output a boolean entailed flag "
    "and a [0,1] confidence."
)

JUDGE_SCHEMA = {
    "name": "entailment_verdict",
    "strict": True,
    "schema": {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "entailed": {"type": "boolean"},
            "confidence": {"type": "number"},
        },
        "required": ["entailed", "confidence"],
    },
}


# --------------------------------------------------------------------- #
# Cache layer — content-keyed across all benchmarks/judges
# --------------------------------------------------------------------- #


def _cache_key(claim: str, source: str) -> str:
    return hashlib.sha256(f"{claim}|||{source}".encode()).hexdigest()


def _load_cache(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    out: dict[str, dict] = {}
    for line in path.read_text().splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        out[rec["key"]] = rec["judgment"]
    return out


def _append_cache(path: Path, key: str, judgment: dict) -> None:
    with path.open("a") as f:
        f.write(json.dumps({"key": key, "judgment": judgment}) + "\n")


# --------------------------------------------------------------------- #
# ALCE source-data → {qid: passages}
# --------------------------------------------------------------------- #


def _passages_by_qid(source_path: Path, id_field: str | None) -> dict[str, list[dict]]:
    """``id_field=None`` triggers row-index synthesis (ELI5)."""
    data = json.loads(source_path.read_text())
    if id_field is None:
        return {f"row_{i:04d}": ex["docs"] for i, ex in enumerate(data)}
    return {str(ex[id_field]): ex["docs"] for ex in data}


# --------------------------------------------------------------------- #
# Eval-report parsing — prefer v2 per-sentence inline cites
# --------------------------------------------------------------------- #


@dataclass
class ClaimRecord:
    qid: str
    claim_text: str
    cited_passage_indices: list[int]


_BODY_SECTION_RE = re.compile(r"### `([^`]+)`\n(.*?)(?=\n### `|\Z)", re.DOTALL)
_INLINE_CITE_RE = re.compile(
    r"^>\s*(.+?)\s*\[((?:alce::[^\]]+))\]\s*$", re.MULTILINE
)
_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")
_TABLE_ERROR_RE = re.compile(r"\|\s*`([^`]+)`.*⚠️")


def _cite_ids_to_passage_idxs(cite_ids: list[str]) -> list[int]:
    out: list[int] = []
    for cid in cite_ids:
        m = re.search(r"::p(\d+)$", cid)
        if m:
            out.append(int(m.group(1)))
    return out


def parse_report(report_path: Path) -> Iterator[ClaimRecord]:
    """Yield one ClaimRecord per (sentence, cite-group) pair.

    Prefers the v2 inline format produced by the upgraded reporter:

        > Sentence text. [alce::qid::p0, alce::qid::p3]

    Falls back to the legacy union format for old reports:

        > Full answer text.
        Cited: alce::qid::p0, alce::qid::p1, ...

    Legacy parsing attributes the union to every sentence, which silently
    deflates LOO precision. Always prefer v2.
    """
    text = report_path.read_text()
    error_qids = {m.group(1) for m in _TABLE_ERROR_RE.finditer(text)}

    for m in _BODY_SECTION_RE.finditer(text):
        qid = m.group(1)
        if qid in error_qids:
            continue
        body = m.group(2)
        answer_body = body.split("\nCited:")[0]
        if "_Refused._" in answer_body:
            continue

        # v2 inline format — per-sentence cites
        inline_matches = list(_INLINE_CITE_RE.finditer(answer_body))
        if inline_matches:
            for im in inline_matches:
                sentence_text = im.group(1).strip().strip("*").strip()
                if len(sentence_text) < 8:
                    continue
                cite_ids = [c.strip() for c in im.group(2).split(",") if c.strip()]
                passage_idxs = _cite_ids_to_passage_idxs(cite_ids)
                if not passage_idxs:
                    continue
                yield ClaimRecord(qid=qid, claim_text=sentence_text,
                                  cited_passage_indices=passage_idxs)
            continue

        # Legacy fallback — union of cites attributed to every sentence.
        cited_match = re.search(r"\nCited: (.+?)(?:\n|$)", body)
        if not cited_match:
            continue
        cite_ids = [s.strip() for s in cited_match.group(1).split(",") if s.strip()]
        passage_idxs = _cite_ids_to_passage_idxs(cite_ids)
        if not passage_idxs:
            continue
        answer_text = "\n".join(
            (l[2:] if l.startswith("> ") else l) for l in answer_body.splitlines()
        ).strip()
        for piece in _SENTENCE_SPLIT_RE.split(answer_text):
            sentence = piece.strip().strip("*").strip()
            if len(sentence) < 8:
                continue
            yield ClaimRecord(qid=qid, claim_text=sentence,
                              cited_passage_indices=passage_idxs)


# --------------------------------------------------------------------- #
# Judge — one LLM call per (claim, passage) pair, content-cached
# --------------------------------------------------------------------- #


def _judge_one(claim: str, source: str, *, model: str, cache: dict[str, dict],
               cache_path: Path, num_retries: int = 3) -> dict:
    key = _cache_key(claim, source)
    if key in cache:
        return cache[key]
    import litellm
    response = litellm.completion(
        model=model,
        messages=[
            {"role": "system", "content": JUDGE_SYSTEM},
            {"role": "user", "content": f"SOURCE: {source}\n\nCLAIM: {claim}"},
        ],
        temperature=0.0,
        max_tokens=128,
        response_format={"type": "json_schema", "json_schema": JUDGE_SCHEMA},
        num_retries=num_retries,
    )
    raw = str(response.choices[0].message.content or "").strip()
    try:
        judgment = json.loads(raw)
    except json.JSONDecodeError:
        judgment = {"entailed": False, "confidence": 0.0}
    cache[key] = judgment
    _append_cache(cache_path, key, judgment)
    return judgment


# --------------------------------------------------------------------- #
# Score one report → ALCE-style metrics
# --------------------------------------------------------------------- #


@dataclass
class _Tally:
    n_claims: int = 0
    n_cites_total: int = 0
    n_cites_necessary: int = 0
    n_recall_hits: int = 0


def score_report(report_path: Path, passages_by_qid: dict[str, list[dict]],
                 *, model: str, cache: dict[str, dict], cache_path: Path,
                 max_workers: int) -> dict[str, float]:
    """Returns {n_claims, n_cites_total, citation_recall, citation_precision}."""
    print(f"\n[judge] scoring {report_path.name}...", flush=True)
    claims = list(parse_report(report_path))
    print(f"  {len(claims)} (claim, cite_group) records")

    # Collect unique (claim, passage_text) pairs to judge
    unique_pairs: dict[tuple[str, str], None] = {}
    claim_to_pairs: list[tuple[ClaimRecord, list[tuple[str, str]]]] = []
    for c in claims:
        passages = passages_by_qid.get(c.qid)
        if not passages:
            continue
        pairs: list[tuple[str, str]] = []
        for idx in c.cited_passage_indices:
            if idx >= len(passages):
                continue
            passage_text = (passages[idx].get("text") or "").strip()
            if not passage_text:
                continue
            pair = (c.claim_text, passage_text)
            unique_pairs.setdefault(pair, None)
            pairs.append(pair)
        claim_to_pairs.append((c, pairs))

    print(f"  {len(unique_pairs)} unique (claim, passage) pairs to judge")

    # Parallel judging — order doesn't matter, all results land in cache
    done = 0
    cached_hits = 0

    def _do(pair: tuple[str, str]) -> None:
        nonlocal done, cached_hits
        claim_t, source_t = pair
        was_cached = _cache_key(claim_t, source_t) in cache
        _judge_one(claim_t, source_t, model=model, cache=cache,
                   cache_path=cache_path)
        done += 1
        if was_cached:
            cached_hits += 1
        if done % 100 == 0:
            print(f"    [{done}/{len(unique_pairs)}] cache_hits={cached_hits}",
                  flush=True)

    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        list(pool.map(_do, unique_pairs.keys()))
    print(f"    ...done ({done} pairs, {cached_hits} from cache)")

    # Aggregate metrics from cached judgments
    tally = _Tally()
    for crec, pairs in claim_to_pairs:
        if not pairs:
            continue
        entailed_flags = [
            cache[_cache_key(p[0], p[1])].get("entailed", False) for p in pairs
        ]
        tally.n_claims += 1
        if any(entailed_flags):
            tally.n_recall_hits += 1
        # LOO per-cite: necessary iff this cite entails AND no other cite does
        for i in range(len(pairs)):
            tally.n_cites_total += 1
            others_entail = any(entailed_flags[j] for j in range(len(pairs)) if j != i)
            if entailed_flags[i] and not others_entail:
                tally.n_cites_necessary += 1

    recall = tally.n_recall_hits / tally.n_claims if tally.n_claims else 0.0
    precision = (
        tally.n_cites_necessary / tally.n_cites_total
        if tally.n_cites_total else 0.0
    )
    return {
        "n_claims": float(tally.n_claims),
        "n_cites_total": float(tally.n_cites_total),
        "n_cites_necessary": float(tally.n_cites_necessary),
        "citation_recall": recall,
        "citation_precision": precision,
    }


# --------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------- #


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="llm_judge_alce",
        description="Post-hoc LLM-judge scorer for ALCE eval reports.",
    )
    parser.add_argument(
        "--subbench",
        required=True,
        choices=sorted(_SUBBENCH_CONFIG),
        help="ALCE sub-benchmark — determines source-data file + ID field.",
    )
    parser.add_argument(
        "--report",
        required=True,
        type=Path,
        help="Path to the eval report markdown to judge.",
    )
    parser.add_argument(
        "--judge",
        choices=sorted(_JUDGE_CONFIG),
        default="haiku",
        help="Judge LLM backend (default: haiku).",
    )
    parser.add_argument(
        "--alce-data-root",
        type=Path,
        default=Path(".verifiable_rag_cache/alce/ALCE-data"),
        help="Directory containing the extracted ALCE-data/ tree.",
    )
    parser.add_argument(
        "--max-workers",
        type=int,
        default=None,
        help="Override per-judge default workers (Haiku=8, Sonnet=4).",
    )
    args = parser.parse_args(argv)

    source_filename, id_field = _SUBBENCH_CONFIG[args.subbench]
    source_path = args.alce_data_root / source_filename
    if not source_path.exists():
        print(f"ALCE source data not found: {source_path}", file=sys.stderr)
        print("Run `python scripts/fetch_alce.py` first.", file=sys.stderr)
        return 1

    judge_model, default_workers, cache_path_str = _JUDGE_CONFIG[args.judge]
    cache_path = Path(cache_path_str)
    max_workers = args.max_workers if args.max_workers is not None else default_workers

    print(f"[judge] subbench={args.subbench}  judge={args.judge}  workers={max_workers}")
    print(f"[judge] source={source_path}")
    print(f"[judge] cache={cache_path}")
    cache = _load_cache(cache_path)
    print(f"[judge] cache pre-load: {len(cache)} entries")
    passages_by_qid = _passages_by_qid(source_path, id_field)
    print(f"[judge] loaded {len(passages_by_qid)} ALCE questions' passages")

    metrics = score_report(
        args.report, passages_by_qid,
        model=judge_model, cache=cache, cache_path=cache_path,
        max_workers=max_workers,
    )

    print()
    print("=" * 88)
    print(f"  citation_recall    = {metrics['citation_recall']:.3f}")
    print(f"  citation_precision = {metrics['citation_precision']:.3f}")
    print(f"  n_claims           = {metrics['n_claims']:.0f}")
    print(f"  n_cites_total      = {metrics['n_cites_total']:.0f}")
    print(f"  n_cites_necessary  = {metrics['n_cites_necessary']:.0f}")
    print("=" * 88)
    return 0


if __name__ == "__main__":
    sys.exit(main())
