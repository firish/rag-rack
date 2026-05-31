# Changelog

All notable changes to this project are documented here. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project
adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

`0.x` releases reserve the right to change public APIs without a deprecation
cycle. Once we hit `1.0` the normal semver promises apply.

## [Unreleased]

## [0.5.2] — 2026-05-31

Adds an LLM-as-judge preset for offline ceiling reference + audit-grade
workflows, plus the generic adapter that makes it possible.

### Added

- :class:`verifiable_rag.verifiers.NLIVerifier` — adapter that turns any
  :class:`NLIScorer` (``LLMJudgeVerifier``, ``MiniCheckVerifier``,
  ``ModalHHEMScorer``, …) into a :class:`Verifier`-protocol-compliant
  Pipeline verifier. Mirrors the same premise-building logic the
  library uses internally.
- :func:`verifiable_rag.llm_judge_verified` preset — Cohere retrieval +
  constrained Haiku generator + Sonnet 4.6 LLM-judge verifier (wrapped
  via ``NLIVerifier``). Strictest single-model option; offline ceiling
  reference. ~250x per-call cost vs Dual NLI.
- ``verifiable_rag.ask(..., preset="llm_judge_verified")`` is the
  one-liner equivalent.

### Changed

- :meth:`Answer.audit_trail` field rename: ``verifier_configured`` →
  ``verification_ran``. More accurate — the Pipeline can have a verifier
  attached yet skip verification when the generator produced no
  sentences to check. **Breaking** for any code that read the
  ``verifier_configured`` key from v0.5.1 — update to
  ``verification_ran``.

## [0.5.1] — 2026-05-31

Patch release. Two small bugfixes spotted during the post-launch
sanity check from a fresh PyPI install.

### Fixed

- ``verifiable_rag.__version__`` now matches the PyPI metadata version
  (was stuck at ``"0.1.0"`` in v0.5.0 even though the package was
  published as 0.5.0).
- ``Pipeline.faithfulness_score`` no longer falls back to the raw
  retrieval scalar when no verifier ran. Previously, ``loose``-strictness
  pipelines without a verifier produced misleading-looking sub-0.1
  faithfulness scores (the raw retrieval-model output, not a
  calibrated [0, 1] value). Now defaults to ``1.0`` ("no evidence of
  unfaithfulness") and the audit surfaces include a new
  ``verifier_configured: bool`` flag so downstream consumers know
  whether the score is meaningful.
- ``Answer.to_html()`` now skips the "Faithfulness" card row entirely
  when no verifier was configured, and the header reads "no verifier
  configured" instead of an uninterpretable score.

### Added

- ``Answer.audit_trail()`` includes a new ``verifier_configured`` key.

## [0.5.0] — 2026-05-28

The library is now usable end-to-end. Five preset pipelines, a YAML config
loader, a top-level `ask()` one-liner, a full audit-trail UX (programmatic +
self-contained HTML report), and a bundled demo document.

### Added — public API

- `verifiable_rag.ask(question, docs=...)` — top-level one-liner for the
  "just give me an answer" use case. Optional `output_html=...` writes the
  audit-trail HTML page on the side.
- Preset pipelines exported at the top level:
  `local_minimal`, `local_verified`, `hybrid_balanced` (recommended),
  `hybrid_strict`, `hybrid_paranoid`, plus the parametric `build_pipeline(...)`.
- `Pipeline.from_yaml(path)` — load any pipeline from a YAML config.
  Component types are registered via `verifiable_rag.config.register(...)`
  and listable via `verifiable_rag.config.registered_types()`.
- `DualNLIVerifier` — Pipeline-compatible `Verifier` wrapping two `NLIScorer`s
  (default HHEM + MiniCheck) with min/mean/max aggregation. Default threshold
  `0.0562` is fit on RAGTruth-train.
- `EnsembleScorer` — composable NLIScorer combining N scorers.
- `ContextualChunker` + `LLMContextualizer` — Anthropic 2024 Contextual Retrieval
  recipe. Configurable granularity (`section` | `paragraph` | `chunk`) and an
  optional `group_by` callable for custom document structures.
- `LLMJudgeVerifier` — LLM-as-judge faithfulness scorer with Anthropic prompt
  caching on system + premise.
- `MiniCheckVerifier` — Flan-T5-based NLI verifier.
- `Answer.to_html(title=...)` — self-contained HTML audit report (inline CSS,
  no JS, no external deps).
- Programmatic audit-trail accessors on `Answer`:
  `supported_sentences`, `unsupported_sentences`, `verification_for(idx)`,
  `cited_sentence_ids`, `nli_scores`, `min_nli_score`, `audit_trail()`.
- `verifiable_rag.demo.sample_paper_path()` /
  `sample_paper_text()` / `load_sample_document()` — bundled ~3-page demo
  document about penicillin (authored for the project, no third-party
  copyright) for zero-setup examples and tests.

### Added — eval / benchmarks

- RAGTruth verifier benchmark: `RAGTruthBench` loader, verifier-only runner
  in `verifiable_rag.eval.ragtruth_runner`, calibration script
  (`scripts/compute_calibrated_metrics.py`). Published baseline at
  `benchmarks/PUBLISHED_ragtruth.md` — dual NLI matches Sonnet 4.6 judge at
  ~250× lower per-call cost.
- ALCE benchmark: full reproducibility for prompted vs constrained generators
  with dual-LLM-judge cross-validation. Published at
  `benchmarks/PUBLISHED_alce.md`.
- LitQA2 3×2 ablation (generators × contextual retrieval). Published at
  `benchmarks/PUBLISHED_litqa2.md`.

### Added — infrastructure

- `infra/modal_verifiers.py` — Modal-hosted GPU verifiers
  (`ModalHHEMScorer`, `ModalMiniCheckScorer`) for accelerated benchmark runs.
- YAML config loader with component registry pattern, plus
  `examples/pipeline.yaml` as a copy-paste starting point.
- Runnable examples under `examples/`:
  `01_minimal.py`, `02_audit_html.py`, `03_audit_trail.py`,
  `04_multi_question.py`, `05_yaml_config.py`, plus `inspect_parser.py`.

### Changed

- `Pipeline` ingestion now routes chunks through
  `verifiable_rag.chunkers.embedding_text(chunk)` so contextual preambles
  flow into the embedder transparently when present.
- README rewritten around the new top-level UX (ask one-liner + audit trail
  + presets + benchmark links).
- Bumped Development Status classifier from "Pre-Alpha" → "Alpha".
- Added optional extras: `voyage`, `yaml`, `modal`.

### Hard rules

- Span preservation invariant is unchanged: `chunk.text` and `chunk.span`
  are never mutated. The contextual preamble lives in
  `metadata["contextual_preamble"]` and is only used at embedding time.
- Default thresholds (HHEM 0.3, DualNLI 0.0562) are calibrated on
  RAGTruth-train and frozen. Re-fit for your domain with
  `scripts/compute_calibrated_metrics.py`.

## Earlier work

Phases 0–4 happened pre-public-release and are not individually changelogged.
See `benchmarks/baselines/` for the chronological iteration history.
