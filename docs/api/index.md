# API reference

Auto-generated from the live docstrings in [src/verifiable_rag/](https://github.com/firish/rag-rack/tree/main/src/verifiable_rag). Use the sidebar to jump to a module, or browse the highlights:

## Top-level entry points

- [`Pipeline`](pipeline.md) — the core orchestration class
- [`ask()`](ask.md) — single-shot one-liner for the simple case
- [Presets](presets.md) — `hybrid_balanced`, `local_minimal`, etc.

## Data model

- [Models](models.md) — `Document`, `Sentence`, `Chunk`, `Answer`, `CitedSentence`, `VerificationResult`, `Span`

## Components (alphabetical)

- [Chunkers](chunkers.md) — `ParentChildChunker`, `ContextualChunker`, the `Chunker` protocol
- [Config](config.md) — YAML loader, registry, `register()` extension hook
- [Demo](demo.md) — bundled sample document helpers
- [Embedders](embedders.md) — BGE / Cohere / Voyage
- [Generators](generators.md) — `PromptedCitedGenerator`, `ConstrainedCitedGenerator`, `SAFECitedGenerator`
- [Indexers](indexers.md) — `HybridIndex`, `LanceDBIndex`, `BM25Index`
- [Parsers](parsers.md) — `DoclingParser`, `PyMuPDFParser`, composite + caching wrappers
- [Rerankers](rerankers.md) — Cohere / BGE
- [Report](report.md) — HTML audit report renderer
- [Verifiers](verifiers.md) — `DualNLIVerifier`, `HHEMVerifier`, `MiniCheckVerifier`, `LLMJudgeVerifier`

## Protocols

Every component is defined by a `Protocol` — swap implementations freely:

| Protocol | Defined in | What it does |
|---|---|---|
| `Parser` | `verifiable_rag.parsers` | PDF → `Document` |
| `Chunker` | `verifiable_rag.chunkers` | `Document` → `list[Chunk]` |
| `Embedder` | `verifiable_rag.embedders` | `list[str]` → `list[list[float]]` |
| `Reranker` | `verifiable_rag.rerankers` | Rerank `list[RetrievedChunk]` |
| `Generator` | `verifiable_rag.generators` | Query + chunks → `list[CitedSentence]` |
| `Verifier` | `verifiable_rag.verifiers` | `list[CitedSentence]` + `Document` → `list[VerificationResult]` |
| `NLIScorer` | `verifiable_rag.verifiers` | `list[(premise, hypothesis)]` → `list[float]` |
