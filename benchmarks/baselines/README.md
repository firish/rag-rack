# Locked baselines

Versioned snapshots of `python -m verifiable_rag.eval` runs. Each lock is a
reference point future changes are measured against.

## Active baseline

**`v6_phase2_baseline.md`** — Phase 2 baseline with `min_child_tokens=100`,
BGE rerank v2-m3, and the **tightened generator prompt** (verbatim-leaning
citation style, single-source-per-claim).

| field | value |
|---|---|
| Model | Gemma 4 31B (via Gemini API) |
| Embedder | BAAI/bge-small-en-v1.5 |
| Indexer | HybridIndex(LanceDB cosine + bm25s, RRF k=60) |
| Reranker | BAAI/bge-reranker-v2-m3 (cross-encoder) |
| Chunker | `ParentChildChunker(max=400, min=100)` |
| Top-K | retrieve=80, rerank=8 |
| Generator prompt | v6 (tight, prefers verbatim, single-citation-per-claim) |
| Strictness | loose (no verifier — see Phase 4 findings below) |
| Benchmark | `harry_potter_micro` v2 (29 questions, 12 categories) |
| Errors | 0/29 |

| Metric | Value | Δ vs v3 | Δ% |
|---|---|---|---|
| `citation_precision` | 0.569 | +0.158 | +38% |
| `citation_recall` | 0.497 | 0 | 0 |
| `citation_f1` | 0.439 | +0.076 | +21% |
| `coverage` | 0.800 | +0.031 | +4% |
| `localization_accuracy` | 0.241 | +0.069 | +40% |
| `abstention_precision` | 1.000 | 0 | 0 |
| `abstention_recall` | 0.800 | +0.200 | +33% |
| `abstention_f1` | 0.889 | +0.139 | +19% |

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

## Why no verifier in the active baseline

A full 5-run sweep against this benchmark (see "Phase 4 experiments" below)
showed that **HHEM verifier on top of the tightened prompt does not improve
F1 and hurts abstention F1**. The new prompt is already steering the LLM
toward tight, source-faithful citations — adding NLI on top mostly
over-refuses borderline-supported claims that the prompt has pre-filtered.

The verifier is **shipped opt-in** (`--verifier hhem` CLI flag, with
configurable `--verifier-threshold`). Future use cases that warrant it:
- Generators without the tight prompt (e.g. other LLMs that don't follow it)
- Stricter strictness modes (paranoid)
- Proper threshold calibration via RAGTruth (future milestone)

## Phase 4 experiments (verifier shipped, opt-in)

See `v4_phase4_hhem.md`, `v5_phase4_hhem_surgical.md`,
`v5_phase4_hhem_surgical_rerun.md` for HHEM behavior with the OLD prompt.
See `v6_prompt_hhem_010.md` through `v6_prompt_hhem_030.md` for HHEM
behavior with the NEW prompt across thresholds.

### v6 + HHEM threshold sweep (with tightened prompt)

| Threshold | Cit P | Cit R | Cit F1 | Coverage | Abst F1 |
|---|---|---|---|---|---|
| no verifier | 0.569 | 0.497 | **0.439** | 0.800 | **0.889** |
| 0.10 | 0.611 | 0.489 | 0.427 | 0.760 | 0.727 |
| 0.15 | 0.633 | 0.489 | 0.441 | 0.760 | 0.727 |
| 0.20 | 0.617 | 0.406 | 0.348 | 0.667 | 0.615 |
| 0.30 | 0.633 | 0.389 | 0.335 | 0.640 | 0.571 |

Threshold 0.15 ties F1 (0.441 vs 0.439) but loses abstention F1 (0.727 vs
0.889). Higher thresholds hurt across the board. The no-verifier path wins
on the harmonic balance of metrics.

### Old finding (with OLD prompt, kept for audit)

At placeholder thresholds (0.3-0.5) with the old looser prompt, HHEM
over-refused correct paraphrased answers. Example: "Hagrid's first name is
Rubeus" cited from "Rubeus Hagrid, Keeper of Keys" → HHEM 0.23, refused.
This was the *symptom*; the *cause* was the LLM paraphrasing more than HHEM
expects. The new prompt mostly resolves this by encouraging verbatim
citation style.

## Historical / reference baselines

| File | What it represents | Why kept |
|---|---|---|
| `v1_phase1_baseline.md` | Phase 1 on **Groq Llama 3.3 70B**, `min=0`, 15Q | First-ever locked numbers |
| `v2_phase2_baseline.md` | Phase 2 (min=100, no reranker), 15Q on Gemma | Superseded by v3 |
| `v2_phase2_29q_noreranker.md` | A/B counterpart for v3 reranker | Attribution row |
| `v3_phase2_baseline.md` | Phase 2 (min=100 + reranker, 29Q) | Previous active baseline |
| `v3_phase2_reranked.md` | Source of v3 baseline | Pre-promotion copy |
| `gemma4_v{1,2,3}_min{0,150,100}.md` | Chunker sweep on 15Q | Documents min_child_tokens A/B |
| `gemini_v1_min0.md` | Failed gemini/gemini-2.0-flash run | Project-quota-zero diagnostic |
| `v2_min100_expanded29.md` | First failed 29Q (14 Gemma 500s) | Gemma stability reference |
| `v4_phase4_hhem.md` | HHEM hard-refusal experiment, OLD prompt | Documents the hard-refusal failure |
| `v5_phase4_hhem_surgical*.md` | HHEM surgical experiments, OLD prompt | Documents Phase 4 calibration finding |
| `v6_prompt_no_verifier.md` | **Source of the active v6 baseline** | Pre-promotion copy |
| `v6_prompt_hhem_*.md` | HHEM threshold sweep (0.10/0.15/0.20/0.30) with NEW prompt | Documents verifier-vs-no-verifier with tight prompt |

## Conventions

- File name: `vN_<phase>_<descriptor>.md` for canonical locks. Sweep variants
  use the `<base>_<config>.md` pattern.
- Locked baselines are NEVER edited after creation. Re-run = new file.
- Update **the "Active baseline" section above** when a new pipeline change
  ships and beats the current one on the benchmark.

## Planned next experiments

1. **LitQA2 loader** — first external benchmark. Validates that HP signal
   generalizes; lets us compare numbers vs PaperQA2.
2. **HaluBench loader** — hallucination detection benchmark.
3. **RAGTruth loader + threshold calibration** — proper calibration of the
   verifier on a real dataset; may re-engage the verifier for production
   use cases.
4. **Contextual Retrieval** — Anthropic chunk-preamble technique. Phase 5
   retrieval upgrade.
5. **Production readiness** — package polish, docs, config files, examples.
