"""Bundled demo document — a small public-domain overview of penicillin.

Lets users run the examples (and any quick test) with zero setup, no
external PDFs, no API keys for retrieval (only the generator). The
document is authored by the verifiable-rag project for demonstration
purposes; no third-party copyright applies.

Usage::

    from verifiable_rag.demo import sample_paper_path, load_sample_document

    # Path to the bundled PDF — pass to Pipeline.ingest() or ask()
    pdf = sample_paper_path()

    # Or: skip parsing entirely and use the pre-parsed Document directly
    document = load_sample_document()

Contents
--------
A ~3-page summary covering penicillin's discovery, mechanism of action,
resistance, and clinical use. Designed to have rich factoid claims
(names, dates, mechanisms) so citation behavior is easy to inspect.
"""

from __future__ import annotations

from importlib import resources
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from verifiable_rag.models.document import Document


def _resource(name: str) -> Path:
    """Return the absolute path to a bundled data file.

    Uses ``importlib.resources`` so the lookup works in editable installs
    (where files live under ``examples/data/`` via hatch force-include) as
    well as installed wheels (where they live in
    ``site-packages/verifiable_rag/_data/``).
    """
    # The hatch wheel build force-includes examples/data/* at the package
    # path verifiable_rag/_data/. We resolve through importlib.resources so
    # the import target (_data) is what matters, not the filesystem layout.
    res = resources.files("verifiable_rag") / "_data" / name
    p = Path(str(res))
    if p.exists():
        return p
    # Fallback for editable installs where _data isn't materialized — read
    # straight from the source examples/data/ directory.
    fallback = Path(__file__).resolve().parent.parent.parent / "examples" / "data" / name
    if fallback.exists():
        return fallback
    raise FileNotFoundError(
        f"Bundled data file {name!r} not found in either packaged location "
        f"({p}) or source location ({fallback})."
    )


def sample_paper_path() -> Path:
    """Absolute path to the bundled sample PDF.

    Returns the same path on every call. Works for both editable installs
    (resolves to ``examples/data/sample.pdf``) and wheel installs (resolves
    to the in-package ``_data/sample.pdf``).
    """
    return _resource("sample.pdf")


def sample_paper_text() -> str:
    """The raw text content of the bundled sample, for non-PDF flows."""
    return _resource("sample.txt").read_text()


def load_sample_document() -> "Document":
    """Return the pre-parsed :class:`Document` for the bundled sample.

    Skips the parse step entirely — first-run cost drops from ~5 sec
    (PyMuPDF parse) to ~50 ms (JSON load). Useful for testing
    chunker/embedder/generator changes without re-paying parse cost.
    """
    from verifiable_rag.parsers._serde import load_document

    return load_document(_resource("sample.parsed.json"))


__all__ = [
    "load_sample_document",
    "sample_paper_path",
    "sample_paper_text",
]
