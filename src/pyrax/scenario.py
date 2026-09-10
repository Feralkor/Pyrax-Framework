from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class ScenarioResult:
    scenario_id: str
    baseline: dict[str, Any]
    assumptions: dict[str, Any]
    projected: dict[str, Any]
    changed_fields: tuple[str, ...]


class ScenarioEngine:
    """Runs deterministic what-if projections without mutating canonical state."""

    @staticmethod
    def project(
        scenario_id: str,
        baseline: dict[str, Any],
        assumptions: dict[str, Any],
        projector: Callable[[dict[str, Any], dict[str, Any]], dict[str, Any]],
    ) -> ScenarioResult:
        baseline_copy = dict(baseline)
        assumption_copy = dict(assumptions)
        projected = projector(dict(baseline_copy), dict(assumption_copy))
        if not isinstance(projected, dict):
            raise TypeError("Scenario projector must return a mapping")
        changed = tuple(
            key
            for key in sorted(set(baseline_copy) | set(projected))
            if baseline_copy.get(key) != projected.get(key)
        )
        return ScenarioResult(
            scenario_id=scenario_id,
            baseline=baseline_copy,
            assumptions=assumption_copy,
            projected=dict(projected),
            changed_fields=changed,
        )
