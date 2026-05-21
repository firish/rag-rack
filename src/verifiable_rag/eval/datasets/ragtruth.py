"""RAGTruth — word-span hallucination annotations on real RAG outputs.

RAGTruth (Niu et al., NAACL 2024) ships ~18K LLM responses across QA,
Data2txt, and Summary tasks from 6 different LLMs, each with manual
word-level hallucination annotations. It's the canonical benchmark for
faithfulness verifiers because it has *gold span-level* labels, not just
response-level booleans.

Architectural note
------------------
RAGTruth examples are pre-generated: the dataset gives us
``(query, context, response)`` tuples where the response is already
produced by some upstream LLM. Our pipeline's parser/chunker/retriever/
generator are therefore *not* exercised — only the verifier is. Hence
RAGTruth is exposed via a distinct :class:`RAGTruthBench` /
:class:`RAGTruthExample` shape rather than ``EvalQuestion``; it gets
its own verifier-only runner (Phase 4).

Files
-----
After ``scripts/fetch_faithfulness_benches.py``, the parquet shards live
under ``.verifiable_rag_cache/ragtruth/data/{train,test}-00000-of-00001.parquet``.
Schema (from wandb/RAGTruth-processed):

    id, query, context, output, task_type, quality, model, temperature,
    hallucination_labels, hallucination_labels_processed, input_str

Encoding gotcha
---------------
``hallucination_labels`` is stored as a numpy array of strings where the
JSON span list has been *split character-by-character* across array
elements. We rejoin and ``json.loads``.

Test split: 2700 rows (900 per task × 3 tasks, balanced across 6 models).
~35 % are hallucinated (943/2700) — a healthy positive-class base rate.
"""

from __future__ import annotations

import json
from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import Any

_CACHE_ROOT = Path(".verifiable_rag_cache/ragtruth")
_TASK_TYPES = frozenset({"QA", "Data2txt", "Summary"})
_LABEL_TYPES = frozenset(
    {
        "Evident Conflict",
        "Subtle Conflict",
        "Evident Baseless Info",
        "Subtle Baseless Info",
    }
)


@dataclass(frozen=True)
class HallucinationSpan:
    """One annotated hallucination span within a model output."""

    start: int  # char offset in ``response``
    end: int  # exclusive char offset
    text: str  # the hallucinated text
    label_type: str  # one of the four RAGTruth labels (Evident/Subtle × Conflict/Baseless)


@dataclass(frozen=True)
class RAGTruthExample:
    """One verifier-benchmark example: pre-generated response + gold spans."""

    id: str
    task_type: str  # "QA" | "Data2txt" | "Summary"
    model: str  # upstream LLM that produced ``response``
    query: str  # task prompt
    context: str  # source passages the response should be grounded in
    response: str  # pre-generated LLM output (the thing we verify)
    hallucination_spans: tuple[HallucinationSpan, ...]

    @property
    def is_hallucinated(self) -> bool:
        return len(self.hallucination_spans) > 0


class RAGTruthBench:
    """RAGTruth adapter for the verifier-only runner.

    Parameters
    ----------
    split:
        ``"test"`` (2700 rows) or ``"train"``.
    task_filter:
        Optional subset of task types: any subset of
        ``{"QA", "Data2txt", "Summary"}``.
    model_filter:
        Optional subset of generating LLMs (e.g. ``{"gpt-4-0613"}``).
    max_examples:
        Optional row cap (applied after task/model filters, before
        iteration). Used for smoke tests.
    stratify_by_task:
        If True, ``max_examples`` is split evenly across the three task
        types (rounded down per task). Use this for balanced subsampling
        so per-task metrics are computed on equal-sized subsets.
    random_seed:
        Seed for deterministic shuffling when ``max_examples`` is set.
        ``None`` (default) means no shuffle — take rows in dataset order,
        matching the original parquet's row-by-row layout.
    cache_root:
        Directory containing ``data/{split}-00000-of-00001.parquet``.
        Defaults to the path ``scripts/fetch_faithfulness_benches.py``
        writes to.
    """

    name = "ragtruth"

    def __init__(
        self,
        split: str = "test",
        task_filter: frozenset[str] | None = None,
        model_filter: frozenset[str] | None = None,
        max_examples: int | None = None,
        stratify_by_task: bool = False,
        random_seed: int | None = None,
        cache_root: Path = _CACHE_ROOT,
    ) -> None:
        if split not in {"train", "test"}:
            raise ValueError(f"split must be 'train' or 'test', got {split!r}")
        if task_filter is not None:
            bad = task_filter - _TASK_TYPES
            if bad:
                raise ValueError(
                    f"unknown task_type(s): {sorted(bad)}; "
                    f"choose from {sorted(_TASK_TYPES)}"
                )

        self._split = split
        self._task_filter = task_filter
        self._model_filter = model_filter
        self._max_examples = max_examples
        self._path = Path(cache_root) / "data" / f"{split}-00000-of-00001.parquet"

        if not self._path.exists():
            raise FileNotFoundError(
                f"RAGTruth {split} parquet not found at {self._path}. "
                f"Run `python scripts/fetch_faithfulness_benches.py` first."
            )

        import pandas as pd  # lazy: keeps the module importable without pandas

        df = pd.read_parquet(self._path)
        if task_filter is not None:
            df = df[df["task_type"].isin(task_filter)]
        if model_filter is not None:
            df = df[df["model"].isin(model_filter)]
        if max_examples is not None:
            if stratify_by_task:
                # Per-task quota; balanced if max_examples is divisible by 3.
                tasks = sorted(df["task_type"].unique())
                per_task = max_examples // max(len(tasks), 1)
                parts: list[pd.DataFrame] = []
                for t in tasks:
                    sub = df[df["task_type"] == t]
                    if random_seed is not None:
                        sub = sub.sample(
                            n=min(per_task, len(sub)),
                            random_state=random_seed,
                        )
                    else:
                        sub = sub.iloc[:per_task]
                    parts.append(sub)
                df = pd.concat(parts, ignore_index=True)
            elif random_seed is not None:
                df = df.sample(
                    n=min(max_examples, len(df)),
                    random_state=random_seed,
                )
            else:
                df = df.iloc[:max_examples]
        self._df = df.reset_index(drop=True)

    def __len__(self) -> int:
        return len(self._df)

    def examples(self) -> Iterator[RAGTruthExample]:
        for _, row in self._df.iterrows():
            yield RAGTruthExample(
                id=str(row["id"]),
                task_type=str(row["task_type"]),
                model=str(row["model"]),
                query=str(row["query"]),
                context=str(row["context"]),
                response=str(row["output"]),
                hallucination_spans=_parse_spans(row["hallucination_labels"]),
            )


def _parse_spans(raw: Any) -> tuple[HallucinationSpan, ...]:
    """Decode wandb/RAGTruth-processed's char-chunked JSON encoding."""
    if raw is None:
        return ()
    if hasattr(raw, "__iter__") and not isinstance(raw, str):
        s = "".join(raw)
    else:
        s = str(raw)
    if not s or s == "[]":
        return ()
    try:
        items = json.loads(s)
    except json.JSONDecodeError:
        return ()
    if not items:
        return ()
    out: list[HallucinationSpan] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        label_type = str(item.get("label_type", ""))
        out.append(
            HallucinationSpan(
                start=int(item["start"]),
                end=int(item["end"]),
                text=str(item.get("text", "")),
                label_type=label_type,
            )
        )
    return tuple(out)


__all__ = [
    "HallucinationSpan",
    "RAGTruthBench",
    "RAGTruthExample",
]
