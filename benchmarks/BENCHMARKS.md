# Benchmarks

> Eval before optimization. Numbers, not vibes.

This file tracks eval results across pipeline configurations. Updated automatically by CI via `pytest -m eval`.

## Metrics

| Metric | Description |
|--------|-------------|
| `citation_precision` | Of cited spans, fraction that actually support the claim |
| `citation_recall` | Of supporting spans, fraction that were cited |
| `citation_f1` | Harmonic mean |
| `span_tightness` | 1.0 = exact, >1 = over-cited |
| `abstention_precision` | Of refusals, fraction truly unsupported |
| `abstention_recall` | Of unsupported claims, fraction refused |
| `abstention_f1` | Harmonic mean |
| `localization_accuracy` | How closely cited spans match ground-truth spans |

## Results

_No results yet. Run Phase 1 baseline first._

<!--
Example row format (fill in after Phase 1):

| Phase | Dataset | Model | Mode | citation_f1 | abstention_f1 | span_tightness | Notes |
|-------|---------|-------|------|-------------|---------------|----------------|-------|
| 1 | LitQA2 | claude-sonnet-4-6 | prompted | 0.00 | 0.00 | 0.00 | baseline |
-->

## Datasets

- **LitQA2** (FutureHouse) — scientific Q&A with span-level annotations
- **RAGTruth** — hallucination annotations on RAG outputs
- **HaluBench** — faithfulness evaluation benchmark

Data is downloaded on first run and cached in `benchmarks/data/` (gitignored).

## Running

```bash
# Full eval (slow)
pytest -m eval -v

# Fast CI subset
pytest -m eval --ci-subset -v

# Single dataset
pytest -m eval -k litqa2 -v
```
