"""File-based JSON cache for parsed Documents.

Each Document is keyed by SHA-256 of its source file's content.  Renaming or
moving a source file does NOT invalidate its cache entry; changing the content
does.  Cache files include a serde version — mismatched versions are silently
discarded and re-parsed.

CachingParser implements the Parser Protocol so it drops in anywhere a Parser
is expected.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import TYPE_CHECKING

from verifiable_rag.models.document import Document
from verifiable_rag.parsers._serde import load_document, save_document

if TYPE_CHECKING:
    from verifiable_rag.parsers import Parser

DEFAULT_CACHE_DIR = Path(".verifiable_rag_cache") / "documents"
_HASH_CHUNK = 64 * 1024


def file_content_hash(path: Path) -> str:
    """SHA-256 of file content as a hex string."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        while chunk := f.read(_HASH_CHUNK):
            h.update(chunk)
    return h.hexdigest()


class DocumentCache:
    """Low-level cache: get/put Documents keyed by source-file content hash.

    Caches both successes (the parsed Document) and failures (the error
    message). Negative caching is what stops us from re-OCRing the same
    broken PDF every run — a failed parse leaves a ``.failed.json`` marker
    that subsequent calls check first.
    """

    def __init__(self, cache_dir: Path = DEFAULT_CACHE_DIR) -> None:
        self._dir = cache_dir

    def _cache_path(self, source_path: Path) -> Path:
        return self._dir / f"{file_content_hash(source_path)}.json"

    def _failure_path(self, source_path: Path) -> Path:
        return self._dir / f"{file_content_hash(source_path)}.failed.json"

    def get(self, source_path: Path) -> Document | None:
        cache_file = self._cache_path(source_path)
        if not cache_file.exists():
            return None
        try:
            return load_document(cache_file)
        except (ValueError, KeyError, json.JSONDecodeError):
            # Stale version, missing key, or corrupt JSON — drop and re-parse.
            cache_file.unlink(missing_ok=True)
            return None

    def get_failure(self, source_path: Path) -> str | None:
        """Return the cached error string for *source_path*, or None."""
        f = self._failure_path(source_path)
        if not f.exists():
            return None
        try:
            data = json.loads(f.read_text())
            error = data.get("error")
            return error if isinstance(error, str) else None
        except (OSError, json.JSONDecodeError):
            return None

    def put(self, source_path: Path, doc: Document) -> None:
        save_document(doc, self._cache_path(source_path))
        # Successful parse supersedes any prior failure marker.
        self._failure_path(source_path).unlink(missing_ok=True)

    def put_failure(self, source_path: Path, error: str) -> None:
        """Record that parsing *source_path* failed with *error*."""
        self._dir.mkdir(parents=True, exist_ok=True)
        self._failure_path(source_path).write_text(
            json.dumps({"error": error}, ensure_ascii=False)
        )

    def invalidate(self, source_path: Path) -> None:
        self._cache_path(source_path).unlink(missing_ok=True)
        self._failure_path(source_path).unlink(missing_ok=True)

    def clear(self) -> None:
        if self._dir.exists():
            for f in self._dir.glob("*.json"):
                f.unlink(missing_ok=True)


class CachingParser:
    """Wraps any Parser with a transparent file-based Document cache.

    First call to parse(path) runs the underlying parser and writes the result
    to the cache.  Subsequent calls on the same content return the cached
    Document — typically <100ms vs. several seconds for docling.
    """

    def __init__(
        self,
        parser: Parser,
        cache_dir: Path = DEFAULT_CACHE_DIR,
    ) -> None:
        self._parser = parser
        self._cache = DocumentCache(cache_dir)

    def parse(self, path: Path) -> Document:
        if not path.exists():
            raise FileNotFoundError(f"No file at {path}")
        cached = self._cache.get(path)
        if cached is not None:
            return cached
        cached_failure = self._cache.get_failure(path)
        if cached_failure is not None:
            # Skip the expensive re-parse — we already know it fails.
            raise ValueError(f"Cached parse failure for {path}: {cached_failure}")
        try:
            doc = self._parser.parse(path)
        except (ValueError, AssertionError) as exc:
            # Record the failure so future runs short-circuit instead of
            # re-running the entire parser (which on Docling means re-OCR).
            self._cache.put_failure(path, f"{type(exc).__name__}: {exc}")
            raise
        self._cache.put(path, doc)
        return doc

    @property
    def cache(self) -> DocumentCache:
        return self._cache
