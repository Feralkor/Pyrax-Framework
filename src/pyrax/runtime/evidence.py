from __future__ import annotations

from pyrax.models import Evidence


def build_evidence(*, source: str, grain: str, observed_at: str | None = None, rule_version: str | None = None, quality: str | None = None, lineage: dict | None = None) -> Evidence:
    return Evidence(
        source=source,
        grain=grain,
        observed_at=observed_at,
        rule_version=rule_version,
        quality=quality,
        lineage=lineage or {},
    )
