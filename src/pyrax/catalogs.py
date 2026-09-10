from __future__ import annotations

from copy import deepcopy


SOLUTION_PROFILES: dict[str, dict] = {
    "fleet-intelligence": {
        "description": "Fleet, route, driver and transportation decision intelligence.",
        "blocks": ["dead-reckoning", "constraint-propagation", "capacity-risk", "rate-of-change", "outcome-feedback"],
        "adapters": ["sql", "rest-api", "telemetry"],
        "ui_components": ["control-tower", "object-360", "timeline", "evidence-drawer", "scenario-panel", "decision-card"],
        "maturity_target": "P4_PREDICTIVE_OPERATIONS",
    },
    "asset-radar": {
        "description": "Last-known-state, telemetry reconciliation and asset visibility.",
        "blocks": ["dead-reckoning", "coverage", "baseline-deviation", "outcome-feedback"],
        "adapters": ["telemetry", "rest-api", "sql"],
        "ui_components": ["control-tower", "object-360", "timeline", "evidence-drawer"],
        "maturity_target": "P3_ASSISTED_INTELLIGENCE",
    },
    "predictive-maintenance": {
        "description": "Condition, degradation and maintenance-priority intelligence.",
        "blocks": ["baseline-deviation", "rate-of-change", "capacity-risk", "outcome-feedback"],
        "adapters": ["telemetry", "sql", "files"],
        "ui_components": ["object-360", "timeline", "scenario-panel", "evidence-drawer", "decision-card"],
        "maturity_target": "P4_PREDICTIVE_OPERATIONS",
    },
    "industrial-performance": {
        "description": "OEE, flow, losses, bottlenecks and industrial performance.",
        "blocks": ["coverage", "bottleneck-detection", "baseline-deviation", "rate-of-change", "capacity-risk"],
        "adapters": ["sql", "telemetry", "files"],
        "ui_components": ["control-tower", "andon", "heatmap", "timeline", "evidence-drawer"],
        "maturity_target": "P3_ASSISTED_INTELLIGENCE",
    },
    "decision-intelligence": {
        "description": "General evidence-backed signals, scenarios and decision support.",
        "blocks": ["baseline-deviation", "rate-of-change", "constraint-propagation", "outcome-feedback"],
        "adapters": ["sql", "rest-api", "files"],
        "ui_components": ["decision-card", "scenario-panel", "evidence-drawer", "timeline", "object-360"],
        "maturity_target": "P4_PREDICTIVE_OPERATIONS",
    },
}

BUILDING_BLOCKS: dict[str, dict] = {
    "aging": {"kind": "anticipation", "unknown_policy": "abstain", "requires_evidence": True},
    "coverage": {"kind": "truth/anticipation", "unknown_policy": "preserve", "requires_evidence": True},
    "deficit-propagation": {"kind": "anticipation", "unknown_policy": "preserve", "requires_evidence": True},
    "dead-reckoning": {"kind": "anticipation", "unknown_policy": "abstain", "requires_evidence": True},
    "constraint-propagation": {"kind": "decision", "unknown_policy": "preserve", "requires_evidence": True},
    "baseline-deviation": {"kind": "anticipation", "unknown_policy": "abstain", "requires_evidence": True},
    "rate-of-change": {"kind": "anticipation", "unknown_policy": "abstain", "requires_evidence": True},
    "bottleneck-detection": {"kind": "anticipation", "unknown_policy": "preserve", "requires_evidence": True},
    "capacity-risk": {"kind": "decision", "unknown_policy": "abstain", "requires_evidence": True},
    "outcome-feedback": {"kind": "memory", "unknown_policy": "preserve", "requires_evidence": True},
}

ADAPTER_CATALOG: dict[str, dict] = {
    "sql": {"mode": "read", "examples": ["PostgreSQL", "Oracle", "SQL Server", "MySQL"]},
    "rest-api": {"mode": "read", "examples": ["REST/JSON APIs"]},
    "telemetry": {"mode": "read", "examples": ["IoT", "GPS", "machine telemetry", "vehicle telemetry"]},
    "files": {"mode": "read", "examples": ["CSV", "Excel", "JSON", "Parquet"]},
    "event-stream": {"mode": "read", "examples": ["Kafka", "queues", "event buses"]},
}

UI_COMPONENTS: dict[str, dict] = {
    "control-tower": {"purpose": "exception-first operational overview"},
    "andon": {"purpose": "severity-based visual management"},
    "heatmap": {"purpose": "spatial or categorical concentration of operational pressure"},
    "timeline": {"purpose": "state and event history"},
    "object-360": {"purpose": "entity-centered operational context"},
    "evidence-drawer": {"purpose": "source, lineage, confidence and rule inspection"},
    "scenario-panel": {"purpose": "compare hypothetical states without mutating canonical state"},
    "decision-card": {"purpose": "signal, recommendation, constraints, confidence and approval"},
}


def get_solution_profile(profile_id: str) -> dict:
    if profile_id not in SOLUTION_PROFILES:
        raise KeyError(f"Unknown solution profile: {profile_id}")
    return deepcopy(SOLUTION_PROFILES[profile_id])
