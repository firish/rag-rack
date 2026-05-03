"""Sentence segmentation with span tracking.

Wraps wtpsplit's SaT model.  The key contract is split_with_offsets():
it returns sentences with character offsets *into the input text* such that
``input_text[span.start:span.end] == span.text`` always holds.

This invariant is what makes downstream span tracking possible.  Any deviation
(e.g. wtpsplit returns text not present in the input) results in skipping that
sentence rather than emitting a wrong-but-plausible span.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SentenceSpan:
    """One sentence with its character offsets in the input text."""

    text: str
    start: int  # inclusive char offset within the input string
    end: int    # exclusive


class SentenceSplitter:
    """wtpsplit-backed sentence segmenter, lazily loaded."""

    def __init__(self, model: str = "sat-3l", language: str = "en") -> None:
        self._model_name = model
        self._language = language
        self._sat: Any = None  # wtpsplit.SaT — lazy

    def _load(self) -> Any:
        if self._sat is None:
            try:
                from wtpsplit import SaT
            except ImportError as exc:
                raise ImportError(
                    "wtpsplit is required for sentence segmentation. "
                    "Install it with: pip install 'verifiable-rag[wtpsplit]'"
                ) from exc
            self._sat = SaT(self._model_name)
        return self._sat

    def split_with_offsets(self, text: str) -> list[SentenceSpan]:
        """Split *text* into sentences with character offsets.

        Invariant: for every returned span s, ``text[s.start:s.end] == s.text``.
        Sentences that wtpsplit returns but cannot be located in *text* are
        silently skipped — emitting a wrong span would corrupt downstream citations.
        """
        if not text.strip():
            return []

        sat = self._load()
        try:
            raw_sentences: list[str] = list(sat.split(text, lang_code=self._language))
        except TypeError:
            # Older wtpsplit versions don't accept lang_code; fall back to default segmentation.
            raw_sentences = list(sat.split(text))

        result: list[SentenceSpan] = []
        cursor = 0
        for raw in raw_sentences:
            stripped = raw.strip()
            if not stripped:
                cursor += len(raw)
                continue

            idx = text.find(stripped, cursor)
            if idx == -1:
                # wtpsplit returned a sentence not present in the input — skip it.
                # In practice this is extremely rare (would indicate a model bug).
                continue

            end = idx + len(stripped)
            # Always read the actual substring back from text — guarantees the invariant
            result.append(SentenceSpan(text=text[idx:end], start=idx, end=end))
            cursor = end
        return result
