from __future__ import annotations

from collections.abc import Callable
from typing import Any


class QualityGate:
    def __init__(self, rules: list[Callable[[dict[str, Any]], bool]] | None = None) -> None:
        self.rules = rules or []

    def evaluate(self, record: dict[str, Any]) -> tuple[bool, list[str]]:
        failures: list[str] = []
        for index, rule in enumerate(self.rules, start=1):
            try:
                passed = bool(rule(record))
            except Exception:
                passed = False
            if not passed:
                failures.append(f"quality_rule_{index}")
        return not failures, failures
