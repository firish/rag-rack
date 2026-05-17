# LitQA2 Benchmark — Published Result

- **Model:** `anthropic/claude-haiku-4-5`
- **Date:** 2026-05-17
- **Source report:** `v9_litqa2_haiku_cohere.md`
- **Pipeline:** Cohere embed-english-v3 + BM25 hybrid retrieval → Cohere rerank-v3 → anthropic/claude-haiku-4-5
- **Settings:** `top_k_retrieve=100`, `top_k_rerank=10`, `min_child_tokens=100`, `loose` strictness, no NLI verifier
- **Question set:** 186 questions (LitQA2 ships 199; 13 were excluded because the source PDF could not be fetched)

## Headline result

|                            | Raw   | Cleaned* |
|----------------------------|-------|----------|
| **mc_accuracy_over_all**   | **0.866** | **0.870** |
| mc_accuracy_over_answered  | 0.976 | 0.982 |
| mc_correct                 | 161   | 161 |
| mc_wrong                   | 4     | 3 |
| mc_unanswered              | 21 | 21 |
| **n (denominator)**        | 186   | 185    |

\* *Cleaned excludes 1 questions with documented LitQA2 dataset-annotation errors (see Methodology).*

## Citation metrics

|                       | Raw   | Cleaned* |
|-----------------------|-------|----------|
| citation_precision    | 0.680 | 0.712 |
| citation_recall       | 0.514    | 0.492 |
| citation_f1           | 0.451        | 0.475 |
| coverage              | 0.757           | 0.794 |
| localization_accuracy | 0.258 | 0.209 |

\* *Cleaned excludes 27 questions where alignment between LitQA2's key-passage and our parsed sentences failed at index time (so no gold span exists to measure citations against). Excluding these gives a fair read on citation quality on the subset where ground truth is well-defined.*

## Methodology

### Multi-choice scoring

We embed all answer options (the ideal answer + distractors + "Insufficient information to answer") in the question prompt, sorted alphabetically. The model is asked to select one option and cite the supporting source sentence(s).

We extract the model's selection using a three-tier matcher:

1. **Bold extraction** — look for `**X**` markdown bolds; map to options with normalization (strip "Answer:" / "Best answer is:" preambles, NFKD Unicode normalization for superscripts and the Unicode minus sign, conservative fuzzy match at threshold 90).
2. **Multi-bold tie-break** — if the model walks through reasoning with multiple bolds, the LAST distinct match wins (empirically the model's chosen answer).
3. **Relaxed substring fallback** — if no bold resolves, case-insensitive substring search with non-alphanumeric boundaries (so options ending in `%`, `-`, or pure digits match correctly).

Refusal-style ideals (LitQA2 uses `'null'` for ~3 questions and `'Insufficient information to answer'` for others) are scored as **correct** when the model correctly refuses or picks the "Insufficient information" option, and **wrong** when the model commits to a real distractor.

### Citation scoring

Gold sentence IDs come from rapidfuzz alignment between LitQA2's `key-passage` field and our parsed sentences (run once at index time by `scripts/fetch_litqa2.py`). For each question, citation precision/recall is computed over the set of predicted-vs-gold sentence IDs.

Questions where the alignment fuzzy match failed (no `key_passage_sentence_ids` produced) have **no ground truth for citation metrics**. They are excluded from the cleaned citation numbers above. We do not penalize the model for citing in these cases because there's no way to know if its citation was correct.

### Excluded questions (cleaned mc_accuracy)

The following questions were excluded from the cleaned `mc_accuracy_over_all` denominator after manual audit confirmed the LitQA2 gold annotation is inconsistent with the source paper:

| question_id | reason |
|-------------|--------|
| `dbb51a1c-f9a2-4960-a93c-118957659790` | ideal='-3' contradicts source text which specifies positions 3 or -8 |

### Excluded questions (cleaned citation metrics)

27 additional questions have no gold sentence IDs because the LitQA2 key-passage failed to fuzzy-align to any of our parsed sentences. These are excluded from cleaned citation metrics only (still included in mc_accuracy).

## Comparison

| Configuration                              | mc_accuracy_over_all |
|--------------------------------------------|----------------------|
| v8b — Haiku 4.5, original prompt           | 0.327 |
| v9 — Haiku 4.5, MC options + tightened prompt | 0.554 |
| v9 + matcher tier 1+2                      | 0.774 |
| v9 + matcher tier 1+2+3 (NFKD + fuzzy)     | 0.849 |
| v9 + null-ideal handling                   | 0.866 |
| **This report — anthropic/claude-haiku-4-5 (raw)**    | **0.866** |
| **This report — anthropic/claude-haiku-4-5 (cleaned)** | **0.870** |
| PaperQA2 (reported, full agentic, multi-doc) | ~0.85 |

This is a single-turn pipeline (no agentic loop, no multi-turn query reformulation) over a shared multi-document index containing all 174 successfully-ingested papers.

## Reproducibility

```bash
python -m verifiable_rag.eval \
    --benchmark litqa2 \
    --model anthropic/claude-haiku-4-5 \
    --embedder cohere \
    --reranker cohere \
    --top-k-retrieve 100 \
    --top-k-rerank 10 \
    --index-dir .verifiable_rag_cache/indexes/eval_lance_cohere_full \
    --delay 6
```

Prerequisite: `python scripts/fetch_litqa2.py` to download papers and run key-passage alignment.
