# Locked baselines

Versioned snapshots of `python -m verifiable_rag.eval` runs. Each lock is a
reference point future changes are measured against.

## Active baseline

**`v3_phase2_baseline.md`** — Phase 2 baseline with `min_child_tokens=100`
and BGE rerank v2-m3 cross-encoder reranker.

| field | value |
|---|---|
| Model | Gemma 4 31B (via Gemini API) |
| Embedder | BAAI/bge-small-en-v1.5 |
| Indexer | HybridIndex(LanceDB cosine + bm25s, RRF k=60) |
| Reranker | BAAI/bge-reranker-v2-m3 (cross-encoder) |
| Chunker | `ParentChildChunker(max=400, min=100)` |
| Top-K | retrieve=80, rerank=8 |
| Strictness | loose (no verifier yet) |
| Benchmark | `harry_potter_micro` v2 (29 questions, 12 categories) |
| Errors | 0/29 |

| Metric | Value | Δ vs v2 (no-reranker, 29Q) |
|---|---|---|
| `citation_precision` | 0.411 | +0.04 (+12%) |
| `citation_recall` | 0.497 | +0.01 |
| `citation_f1` | 0.363 | +0.05 (+17%) |
| `coverage` | 0.769 | +0.08 (+11%) |
| `localization_accuracy` | 0.172 | 0 |
| `abstention_precision` | 1.000 | +0.25 (+33%) |
| `abstention_recall` | 0.600 | 0 (verifier territory) |
| `abstention_f1` | 0.750 | +0.08 (+12%) |

Reproduce:

```bash
python -m verifiable_rag.eval \
    --benchmark harry_potter_micro \
    --model "gemini/gemma-4-31b-it" \
    --delay 4.0 \
    --min-tokens 100 \
    --top-k-retrieve 80 \
    --top-k-rerank 8
```

## Historical / reference baselines

| File | What it represents | Why kept |
|---|---|---|
| `v1_phase1_baseline.md` | Phase 1 baseline on **Groq Llama 3.3 70B**, `min=0`, 15Q | First-ever locked numbers; documents Llama behavior |
| `v2_phase2_baseline.md` | Phase 2 baseline (min=100, no reranker), 15Q on Gemma 4 31B | Previous active baseline; superseded by v3 |
| `v2_phase2_29q_noreranker.md` | **A/B counterpart** — same setup as v3 but no reranker, 29Q | Direct comparison row used to attribute the reranker delta |
| `gemma4_v1_min0.md` | Gemma 4 31B with `min=0`, 15Q | v1 of the chunker A/B sweep |
| `gemma4_v2_min150.md` | Gemma 4 31B with `min=150`, 15Q | Mid-point of the chunker sweep |
| `gemma4_v3_min100.md` | Gemma 4 31B with `min=100`, 15Q | v3 of the chunker sweep — same content as old `v2_phase2_baseline.md` |
| `v3_phase2_reranked.md` | Source of the active v3 baseline (pre-promotion copy) | Kept so the original sweep file is preserved |
| `gemini_v1_min0.md` | Failed gemini/gemini-2.0-flash run | Documents the project-quota-zero issue |
| `v2_min100_expanded29.md` | First (failed) attempt at 29-Q with no reranker — 14 Gemma 500s | Documented in case Gemma free-tier behavior is investigated later |

## Conventions

- File name: `vN_<phase>_<descriptor>.md` for canonical locks. Sweep variants
  use the `gemma4_vN_<config>.md` pattern.
- Locked baselines are NEVER edited after creation. Re-run = new file.
- Update **the "Active baseline" section above** when a new pipeline change
  ships and beats the current one on the benchmark.

## What the v3 deltas tell us about what's next

* The reranker addressed retrieval-side issues — coverage, precision, and
  abstention precision all jumped.
* Citation **recall barely moved (+0.01)** — the gold sentences are in the
  pool, just better ordered. Recall improvement needs **better retrieval
  (Contextual Retrieval)** or **better citation strategy (constrained
  decoding)**.
* Abstention **recall stayed at 0.6** — both partial-info refusal questions
  (`hp_refuse_dumbledore_plan`, `hp_refuse_petunia_lily_feelings`) failed
  in both runs. The system answers when it should refuse. This is exactly
  what the **NLI verifier (Phase 4)** is designed to fix.

Next planned milestone: **NLI verifier** (HHEM-2.1-open or MiniCheck +
atomic claim decomposition + calibrated faithfulness aggregation).
