"""Top-level :func:`ask` helper — the "just give me an answer" entry point.

For users who don't want to wire a Pipeline by hand. Picks a sensible
preset, ingests the document(s), runs one query, returns the
:class:`Answer`. Optionally writes the audit-trail HTML report on the
side.

For multi-question workloads (asking many questions over the same
corpus), build a Pipeline directly so you only pay the ingest cost once::

    from verifiable_rag import hybrid_balanced
    pipeline = hybrid_balanced()
    pipeline.ingest("paper.pdf")
    a1 = pipeline.ask("Q1")
    a2 = pipeline.ask("Q2")
"""

from __future__ import annotations

from collections.abc import Sequence
from pathlib import Path
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from verifiable_rag.models.answer import Answer


_VALID_PRESETS = (
    "local_minimal",
    "local_verified",
    "hybrid_balanced",
    "hybrid_strict",
    "hybrid_paranoid",
    "llm_judge_verified",
)


def ask(
    question: str,
    docs: str | Path | Sequence[str | Path],
    *,
    preset: str = "hybrid_balanced",
    output_html: str | Path | None = None,
    output_html_title: str | None = None,
    **preset_kwargs: Any,
) -> "Answer":
    """Single-shot ingest + query + answer.

    Parameters
    ----------
    question:
        Natural-language query.
    docs:
        Path or list of paths to document files (PDFs, etc.).
    preset:
        Named preset from :mod:`verifiable_rag.presets`. Default
        ``"hybrid_balanced"`` — Cohere retrieval + Dual NLI + constrained
        Haiku generator. See ``verifiable_rag.presets`` for alternatives.
    output_html:
        Optional path. If given, the audit-trail HTML report is written
        to that path alongside returning the Answer.
    output_html_title:
        Optional title for the HTML report. Default ``"verifiable-rag report"``.
    **preset_kwargs:
        Extra kwargs forwarded to the preset factory (e.g.
        ``generator_model``, ``index_dir``).

    Returns
    -------
    Answer
        The pipeline's full Answer — text via ``answer.text``, audit
        trail via ``answer.verification_results`` /
        ``answer.retrieved_chunks``, HTML report via
        ``answer.to_html()``.

    Examples
    --------
    Simplest::

        import verifiable_rag
        answer = verifiable_rag.ask("What did the authors find?", docs="paper.pdf")
        print(answer.text)

    With an HTML audit report::

        verifiable_rag.ask(
            "What did the authors find?",
            docs="paper.pdf",
            output_html="report.html",
        )

    Switching presets::

        answer = verifiable_rag.ask(
            "What did the authors find?",
            docs=["a.pdf", "b.pdf"],
            preset="hybrid_strict",
        )
    """
    if preset not in _VALID_PRESETS:
        raise ValueError(
            f"Unknown preset {preset!r}; choose from {list(_VALID_PRESETS)}"
        )
    from verifiable_rag import presets

    preset_fn = getattr(presets, preset)
    pipeline = preset_fn(**preset_kwargs)

    doc_paths: list[Path] = (
        [Path(docs)]
        if isinstance(docs, (str, Path))
        else [Path(p) for p in docs]
    )
    for p in doc_paths:
        pipeline.ingest(p)

    answer = pipeline.ask(question)

    if output_html is not None:
        title = output_html_title or "verifiable-rag report"
        Path(output_html).write_text(answer.to_html(title=title))

    return answer


__all__ = ["ask"]
