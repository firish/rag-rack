---
hide:
  - navigation
  - toc
---

# verifiable-rag

> Document-grounded Q&A with sentence-level citations, NLI verification, and calibrated refusal.

[![PyPI](https://img.shields.io/pypi/v/verifiable-rag.svg)](https://pypi.org/project/verifiable-rag/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/firish/rag-rack/blob/main/LICENSE)
[![Python](https://img.shields.io/pypi/pyversions/verifiable-rag.svg)](https://pypi.org/project/verifiable-rag/)

A Python library for building RAG pipelines that **actually verify** what they say. Every generated sentence carries a tight pointer to the source span that supports it; every claim is NLI-checked against its cite; the system refuses cleanly when it isn't confident.

## The one finding that drives the design

On RAGTruth (the canonical 2,700-example RAG hallucination benchmark), a dual NLI ensemble of two small open-source models matches a Claude Sonnet 4.6 LLM-judge — **AUROC 0.844 vs 0.846 — at >100× lower per-call cost**.

That number is the whole pitch: you don't need a frontier-LLM judge to verify your RAG outputs. Two small NLI models, calibrated honestly, ensembled correctly, get you there for free per call.

[See the full result →](benchmarks/index.md){ .md-button .md-button--primary }
[Read the blog post →](blog/03_verified_rag.md){ .md-button }
[All posts →](blog/index.md){ .md-button }

## Quickstart

```python
import verifiable_rag
from verifiable_rag.demo import sample_paper_path

answer = verifiable_rag.ask(
    "What is the mechanism of action of penicillin?",
    docs=sample_paper_path(),
)
print(answer.text)
```

For the full audit trail in a browser:

```python
verifiable_rag.ask(
    "What is the mechanism of action of penicillin?",
    docs=sample_paper_path(),
    output_html="audit.html",
)
```

[Full quickstart →](getting-started/quickstart.md){ .md-button }

## Why this exists

Every shipping "chat with your documents" product (NotebookLM, ChatPDF, Humata, Adobe Acrobat AI) stops at **chunk-level** citations and **prompt-conditioned** grounding. The 2024–2026 research literature — ReClaim, SAFE, HALT-RAG, MiniCheck — has solved sentence-span attribution and post-hoc faithfulness verification.

None of it has shipped in a usable library. That's the gap.

## What this library does that others don't

<div class="grid cards" markdown>

-   **Sentence-level citations**

    ---

    Every generated sentence traces back to exact source spans `(doc_id, page, char_start, char_end)` — not a chunk-level handwave. Citation granularity is decoupled from chunk granularity.

    [Read more →](concepts/citation-flow.md)

-   **NLI-verified claims**

    ---

    Each generated sentence is fact-checked against its cited span by a dual NLI ensemble (HHEM + MiniCheck). The verifier is calibrated on RAGTruth and matches a Sonnet-judge baseline.

    [Read more →](concepts/verification.md)

-   **Calibrated refusal**

    ---

    The strictness slider (`loose` / `balanced` / `strict` / `paranoid`) maps to honest thresholds — not "say I don't know" prompting. Unsupported sentences get flagged or surgically removed; truly uncertain answers get refused.

    [Read more →](concepts/strictness.md)

-   **Fully auditable**

    ---

    Every `Answer` exposes its full audit trail programmatically (`unsupported_sentences`, `audit_trail()`, per-sentence NLI scores) and renders a self-contained HTML report on demand.

    [Read more →](how-to/render-audit-html.md)

</div>

## Published benchmark results

| Benchmark | Headline |
|---|---|
| [ALCE](benchmarks/index.md) | Constrained decoding beats prompted by +4–7 F1 under dual-LLM-judge cross-validation |
| [RAGTruth](benchmarks/index.md) | **Dual NLI ensemble = Sonnet 4.6 judge at less than 1/100th the per-call cost** |
| [LitQA2](benchmarks/index.md) | Constrained decoding lifts MC accuracy; contextual retrieval is a null result on saturated retrieval |

## Status

`v0.5` — alpha. Public API stabilizing; interfaces still reserve the right to change in `0.x` releases. The library is usable end-to-end with five presets, YAML config, a top-level `ask()` one-liner, and a full audit-trail UX.

[Roadmap & status →](https://github.com/firish/rag-rack#roadmap){ .md-button }
[GitHub →](https://github.com/firish/rag-rack){ .md-button }
