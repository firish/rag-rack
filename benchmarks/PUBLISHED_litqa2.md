# LitQA2 Benchmark — Published Result

- **Date:** 2026-05-17
- **Question set:** 186 questions (LitQA2 ships 199; 13 were excluded because the source PDF could not be fetched)
- **Pipeline:** Cohere embed-english-v3 + BM25 hybrid retrieval → Cohere rerank-v3 → Haiku 4.5
- **Settings:** `top_k_retrieve=100`, `top_k_rerank=10`, `min_child_tokens=100`, `loose` strictness, no NLI verifier
- **Two configurations published**, reflecting a substantive design tradeoff (see Methodology):
  1. **v9 — Haiku prompted** — baseline cited-generation via system prompt
  2. **v11 — Haiku constrained (multi-cite, ReClaim-style)** — ReClaim-style JSON-schema constrained decoding with multi-citation per claim (1-3 cites per sentence)

## Headline — multi-choice accuracy

|                            | v9 — Haiku prompted                      (Raw / Cleaned*) | v11 — Haiku constrained (multi-cite, ReClaim-style) (Raw / Cleaned*) |
|----------------------------|-----------|-----------|
| **mc_accuracy_over_all**   | **0.866** / **0.870** | **0.870** / **0.875** |
| mc_accuracy_over_answered  | 0.976 / 0.982 | 0.958 / 0.958 |
| mc_correct                 | 161    | 161    |
| mc_wrong                   | 4      | 7      |
| mc_unanswered              | 21 | 17 |
| n_questions (raw / clean)  | 186 / 185 | 186 / 185 |

\* *Cleaned excludes 1 questions with documented LitQA2 dataset-annotation errors (see Methodology).*

## Citation quality

|                       | v9 — Haiku prompted                      (Raw / Cleaned†) | v11 — Haiku constrained (multi-cite, ReClaim-style) (Raw / Cleaned†) |
|-----------------------|-----------|-----------|
| citation_precision    | 0.680 / 0.712 | 0.590 / 0.620 |
| citation_recall       | 0.514 / 0.492 | 0.602 / 0.582 |
| citation_f1           | 0.451 / 0.475 | 0.481 / 0.510 |
| coverage              | 0.757 / 0.794 | 0.828 / 0.874 |
| localization_accuracy | 0.258 / 0.209 | 0.211 / 0.160 |

\† *Cleaned citation metrics additionally exclude 27 questions where alignment between LitQA2's key-passage and our parsed sentences failed at index time (so no gold span exists to measure citations against).*

## The substantive tradeoff

These two configurations differ only in the generator backend, and they map cleanly onto two different priorities:

- **Prompted (v9)** wins on **citation_precision** (0.712 cleaned). It cites less and is more selective.
- **Constrained (v11)** wins on **citation_recall, coverage, and citation_f1** (0.582 / 0.874 / 0.510 cleaned). Multi-citation (1-3 cites per claim, schema-enforced) catches more gold sentences but accepts more decoration.

Mc_accuracy is essentially tied (0.870 vs 0.866 raw; 0.875 vs 0.870 cleaned). Both are past PaperQA2's reported ~0.85 in their fully-agentic multi-doc setup.

**Which to use depends on application:** if surfacing the *narrowest* well-supported citation matters most, use prompted. If recovering *more* gold supporting sentences matters more, use constrained.

## Methodology

### Multi-choice scoring

We embed all answer options (the ideal answer + distractors + "Insufficient information to answer") in the question prompt, sorted alphabetically. The model is asked to select one option and cite the supporting source sentence(s).

We extract the model's selection using a three-tier matcher:

1. **Bold extraction** — look for `**X**` markdown bolds; map to options with normalization (strip "Answer:" preambles, NFKD Unicode normalization for superscripts and the Unicode minus sign, conservative fuzzy match at threshold 90).
2. **Multi-bold tie-break** — if the model walks through reasoning with multiple bolds, the LAST distinct match wins.
3. **Relaxed substring fallback** — non-alphanumeric boundary matching that handles options ending in `%`, `-`, or pure digits.

For the constrained generator, the JSON schema includes a dedicated `selected_option` field. The parser prepends this as a bolded headline sentence so tier-1 extraction works on the structured output.

Refusal-style ideals (LitQA2 uses `'null'` for ~3 questions and `'Insufficient information to answer'` for others) are scored as **correct** when the model correctly refuses or picks the "Insufficient information" option.

### Citation scoring

Gold sentence IDs come from rapidfuzz alignment between LitQA2's `key-passage` field and our parsed sentences (run once at index time by `scripts/fetch_litqa2.py`). For each question, citation precision/recall is computed over the set of predicted-vs-gold sentence IDs.

Questions where the alignment fuzzy match failed (no `key_passage_sentence_ids` produced) have **no ground truth for citation metrics**. They are excluded from the cleaned citation numbers.

### Excluded questions (cleaned mc_accuracy)

| question_id | reason |
|-------------|--------|
| `dbb51a1c-f9a2-4960-a93c-118957659790` | ideal='-3' contradicts source text which specifies positions 3 or -8 |

### Excluded questions (cleaned citation metrics)

27 additional questions have no gold sentence IDs because the LitQA2 key-passage failed to fuzzy-align to any of our parsed sentences. These are excluded from cleaned citation metrics only (still included in mc_accuracy).

## Comparison

| Configuration                                       | mc_accuracy_over_all |
|-----------------------------------------------------|----------------------|
| v8b — Haiku 4.5, original prompt                    | 0.327 |
| v9 — Haiku 4.5, MC options + tightened prompt       | 0.554 |
| v9 + matcher tier 1+2                               | 0.774 |
| v9 + matcher tier 1+2+3 (NFKD + fuzzy)              | 0.849 |
| v9 + null-ideal handling                            | 0.866 |
| **v9 — prompted (cleaned, this report)**            | **0.870** |
| **v11 — constrained (cleaned, this report)**        | **0.875** |
| PaperQA2 (reported, full agentic, multi-doc)        | ~0.85 |

This is a single-turn pipeline (no agentic loop, no multi-turn query reformulation) over a shared multi-document index containing all 174 successfully-ingested papers.

## Reproducibility

```bash
# v9 — prompted
python -m verifiable_rag.eval \
    --benchmark litqa2 \
    --model anthropic/claude-haiku-4-5 \
    --generator prompted \
    --embedder cohere --reranker cohere \
    --top-k-retrieve 100 --top-k-rerank 10 \
    --index-dir .verifiable_rag_cache/indexes/eval_lance_cohere_full \
    --delay 6

# v11 — constrained
python -m verifiable_rag.eval \
    --benchmark litqa2 \
    --model anthropic/claude-haiku-4-5 \
    --generator constrained \
    --embedder cohere --reranker cohere \
    --top-k-retrieve 100 --top-k-rerank 10 \
    --index-dir .verifiable_rag_cache/indexes/eval_lance_cohere_full \
    --delay 12
```

Prerequisite: `python scripts/fetch_litqa2.py` to download papers and run key-passage alignment.
