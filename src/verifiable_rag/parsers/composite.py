"""CompositeParser: try a primary parser, fall back on specified exceptions.

Order matters: primary first, then fallbacks in order. The first parser that
produces a Document wins. If every parser raises one of the ``catch``
exceptions, the *last* exception is re-raised so the caller still gets a
meaningful error (typically the most lenient parser's failure mode).

This is the wiring CLAUDE.md §5 calls for:
    "PDF parsing: docling (primary), PyMuPDF (fallback), MinerU (academic),
     Nougat (math)"

Only Docling → PyMuPDF is wired for now. Adding more is a one-liner.
"""
from __future__ import annotations

from pathlib import Path

from verifiable_rag.models.document import Document
from verifiable_rag.parsers import Parser


class CompositeParser:
    """Chain of parsers tried in order; falls through on *catch* exceptions.

    Other exceptions (e.g. FileNotFoundError) propagate immediately — fallback
    is reserved for parser-internal failures, not for missing files.
    """

    def __init__(
        self,
        primary: Parser,
        fallbacks: list[Parser],
        catch: tuple[type[BaseException], ...] = (ValueError, AssertionError),
    ) -> None:
        if not fallbacks:
            raise ValueError(
                "CompositeParser needs at least one fallback. "
                "Use the primary parser directly if you have nothing to fall back to."
            )
        self._primary = primary
        self._fallbacks = list(fallbacks)
        self._catch = catch

    def parse(self, path: Path) -> Document:
        chain: list[Parser] = [self._primary, *self._fallbacks]
        last_exc: BaseException | None = None
        for parser in chain:
            try:
                return parser.parse(path)
            except self._catch as exc:
                last_exc = exc
                continue
        assert last_exc is not None
        raise last_exc
