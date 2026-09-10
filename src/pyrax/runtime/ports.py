from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any, Protocol


class SourceAdapter(Protocol):
    """Boundary implemented by product-specific connectors.

    The framework defines the contract, never the credentials or source semantics.
    """

    source_id: str

    def fetch(self, *, parameters: Mapping[str, Any]) -> Iterable[Mapping[str, Any]]:
        """Return source records for an explicitly bounded request."""
        ...


class SnapshotSink(Protocol):
    """Optional durable boundary for products that persist canonical snapshots."""

    def publish(self, *, snapshot_id: str, payload: Mapping[str, Any]) -> None:
        ...
