from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from pyrax.models import OperationalFact


@dataclass(frozen=True)
class OperationalState:
    state_id: str
    observed_at: str
    facts: tuple[OperationalFact, ...]
    metadata: dict[str, Any] = field(default_factory=dict)

    def get(self, fact_id: str) -> OperationalFact | None:
        return next((fact for fact in self.facts if fact.fact_id == fact_id), None)
