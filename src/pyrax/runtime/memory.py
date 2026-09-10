from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class OperationalMemory:
    events: list[dict[str, Any]] = field(default_factory=list)

    def append(self, event: dict[str, Any]) -> None:
        self.events.append(dict(event))

    def by_decision(self, decision_id: str) -> list[dict[str, Any]]:
        return [event for event in self.events if event.get("decision_id") == decision_id]
