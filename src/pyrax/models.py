from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum
from typing import Any


class ConfidenceLevel(StrEnum):
    CERTIFIED = "CERTIFIED"
    ASSISTED = "ASSISTED"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"


class ReadinessStatus(StrEnum):
    PASS = "PASS"
    PARTIAL = "PARTIAL"
    BLOCKED = "BLOCKED"
    NOT_STARTED = "NOT_STARTED"


@dataclass(frozen=True)
class Evidence:
    source: str
    grain: str
    observed_at: str | None = None
    rule_version: str | None = None
    quality: str | None = None
    lineage: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class OperationalFact:
    fact_id: str
    value: Any
    confidence: ConfidenceLevel
    evidence: tuple[Evidence, ...] = ()
    unknown_reason: str | None = None

    def __post_init__(self) -> None:
        if self.value is None and not self.unknown_reason:
            raise ValueError("Unknown facts must explain why the value is unavailable")


@dataclass(frozen=True)
class Signal:
    signal_id: str
    severity: str
    facts: tuple[OperationalFact, ...]
    confidence: ConfidenceLevel


@dataclass(frozen=True)
class Recommendation:
    decision_id: str
    action: str
    confidence: ConfidenceLevel
    evidence: tuple[Evidence, ...]
    human_approval_required: bool = True


@dataclass(frozen=True)
class ReadinessItem:
    area: str
    status: ReadinessStatus
    reason: str


@dataclass(frozen=True)
class ReadinessReport:
    items: tuple[ReadinessItem, ...]

    @property
    def production_ready(self) -> bool:
        return bool(self.items) and all(item.status == ReadinessStatus.PASS for item in self.items)
