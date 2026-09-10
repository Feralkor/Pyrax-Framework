from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class RuntimeEvent:
    event_type: str
    run_id: str
    occurred_at: str
    component: str
    status: str
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class EventCollector:
    events: list[RuntimeEvent] = field(default_factory=list)

    def emit(self, event: RuntimeEvent) -> None:
        self.events.append(event)

    def by_run(self, run_id: str) -> tuple[RuntimeEvent, ...]:
        return tuple(event for event in self.events if event.run_id == run_id)
