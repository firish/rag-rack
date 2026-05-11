# Locked baselines

Versioned snapshots of `python -m verifiable_rag.eval` runs. Each lock is a
reference point future changes are measured against.

## Active baseline

**`v2_phase2_baseline.md`** — Phase 2 baseline with `min_child_tokens=100`.

| field | value |
|---|---|
| Pipeline | Gemma 4 31B (Gemini API) + bge-small + hybrid(BM25 + LanceDB) + RRF k=60 |
| Chunker | `ParentChildChunker(max=400, min=100)` |
| Top-K | retrieve=40, rerank=15 |
| Strictness | loose (no verifier yet) |
| Benchmark | `harry_potter_micro` v1 (15 questions) |
| Errors | 1/15 |

| Metric | Value | Notes |
|---|---|---|
| `citation_precision` | 0.319 | Over-citing; verifier will tighten |
| `citation_recall` | 0.405 | Improvable with reranker |
| `citation_f1` | 0.290 | Up from v1's 0.241 (+0.05) |
| `coverage` | 0.818 | Up from v1's 0.500 (+0.32) ⭐ |
| `localization_accuracy` | 0.214 | Roughly flat |
| `abstention_f1` | 1.000 | Architectural refusal works |

Reproduce:

```bash
python -m verifiable_rag.eval \
    --benchmark harry_potter_micro \
    --model "gemini/gemma-4-31b-it" \
    --delay 4.0 \
    --min-tokens 100
```

## Historical / reference baselines

| File | What it represents | Why kept |
|---|---|---|
| `v1_phase1_baseline.md` | Original Phase 1 baseline on **Groq Llama 3.3 70B**, `min=0`, 15Q | First-ever locked numbers; documents Llama behavior |
| `gemma4_v1_min0.md` | Gemma 4 31B with `min=0`, 15Q | v1 of the chunker A/B (vs v2_phase2) |
| `gemma4_v2_min150.md` | Gemma 4 31B with `min=150`, 15Q | Mid-point of the chunker sweep |
| `gemma4_v3_min100.md` | Gemma 4 31B with `min=100`, 15Q | Same content as `v2_phase2_baseline.md` (kept as the original "v3" name from the sweep) |
| `gemini_v1_min0.md` | Failed gemini/gemini-2.0-flash run | Documents the project-quota-zero issue |
| `v2_min100_expanded29.md` | Partial run on 29-Q expanded set, 14 Gemini 500s | **Incomplete** — re-run when Gemma free tier stabilizes or after we switch to a paid model |

## Conventions

- File name: `vN_<phase>_<descriptor>.md` for canonical locks. Sweep variants
  use the `gemma4_vN_<config>.md` pattern.
- Locked baselines are NEVER edited after creation. Re-run = new file.
- Update **the "Active baseline" section above** when a new pipeline change
  ships and beats the current one on the benchmark.

## Pending re-runs

- **29-question benchmark** — the partial `v2_min100_expanded29.md` is a
  flawed expansion run (14/29 errors due to Gemma free-tier 500s). Schedule
  the re-run after the reranker lands (next planned milestone) so we
  capture both the chunker delta and reranker delta on the same clean run.
