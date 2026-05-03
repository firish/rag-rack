from __future__ import annotations

from pathlib import Path
from typing import Protocol, runtime_checkable

from verifiable_rag.models.document import Document


@runtime_checkable
class Parser(Protocol):
    """Convert a document file into a span-preserving Document model.

    Implementations must preserve character offsets through the full parsing
    pipeline so every Sentence can be traced back to its source location.
    """

    def parse(self, path: Path) -> Document:
        """Parse the file at *path* and return a Document.

        Raises:
            FileNotFoundError: if *path* does not exist.
            ValueError: if the file format is unsupported.
        """
        ...
