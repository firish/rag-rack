"""Local NLIScorer wrappers around the Modal-hosted GPU verifiers.

Each wrapper looks up its deployed Modal class by name and delegates
``score_pairs`` to ``.remote()``. The :class:`NLIScorer` Protocol stays
the same, so the RAGTruth runner doesn't care whether scoring happens
on CPU, MPS, or a Modal T4.

Deploy the Modal app first:

    modal deploy infra/modal_verifiers.py

Then locally:

    from verifiable_rag.verifiers import ModalHHEMScorer
    scorer = ModalHHEMScorer()
    scorer.score_pairs([("p", "h"), ...])

Modal client must be installed and authenticated (``modal token new``)
for these wrappers to function. The import is lazy so the module stays
importable in test environments without modal.
"""

from __future__ import annotations

from typing import Any

_APP_NAME = "verifiable-rag-verifiers"


class _ModalScorer:
    """Shared scaffold — subclasses set ``_class_name``."""

    _class_name: str = ""

    def __init__(self, app_name: str = _APP_NAME) -> None:
        self._app_name = app_name
        self._instance: Any = None

    def _get_instance(self) -> Any:
        if self._instance is not None:
            return self._instance
        try:
            import modal
        except ImportError as exc:
            raise ImportError(
                "modal is required for Modal-hosted verifiers. "
                "Install with: pip install modal"
            ) from exc
        cls = modal.Cls.from_name(self._app_name, self._class_name)
        self._instance = cls()
        return self._instance

    def score_pairs(self, pairs: list[tuple[str, str]]) -> list[float]:
        if not pairs:
            return []
        instance = self._get_instance()
        # Modal's @method() makes score_pairs an object with .remote(); the
        # call returns the list directly (sync over the gRPC channel).
        return list(instance.score_pairs.remote(pairs))


class ModalHHEMScorer(_ModalScorer):
    """HHEM-2.1-open running on a Modal T4."""

    _class_name = "HHEMRemote"


class ModalMiniCheckScorer(_ModalScorer):
    """MiniCheck-Flan-T5-Large running on a Modal T4."""

    _class_name = "MiniCheckRemote"


__all__ = ["ModalHHEMScorer", "ModalMiniCheckScorer"]
