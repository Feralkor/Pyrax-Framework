from __future__ import annotations

import json
import os
import time
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Callable

from pyrax import __version__
from pyrax.api import API_VERSION

AUDIT_ENV = "PYRAX_MCP_AUDIT_LOG"


def _result_summary(result: object) -> dict[str, Any]:
    if not isinstance(result, dict):
        return {"result_type": type(result).__name__}

    summary: dict[str, Any] = {}
    for key in ("valid", "found", "production_ready", "level", "kind", "profile_id"):
        if key in result and isinstance(result[key], (str, int, float, bool, type(None))):
            summary[key] = result[key]
    return summary


def _write_record(record: dict[str, Any]) -> None:
    destination = os.getenv(AUDIT_ENV)
    if not destination:
        return

    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True))
        handle.write("\n")


def audited_call(tool_name: str, operation: Callable[..., dict[str, Any]], *args: Any, **kwargs: Any) -> dict[str, Any]:
    """Run one MCP operation and optionally append a metadata-only local audit record.

    Audit records intentionally exclude tool arguments, Domain Packs, manifests and full
    results. The feature is disabled unless PYRAX_MCP_AUDIT_LOG is explicitly configured.
    """
    started = time.perf_counter_ns()
    timestamp = datetime.now(UTC).isoformat()
    try:
        result = operation(*args, **kwargs)
    except Exception as exc:
        duration_ms = (time.perf_counter_ns() - started) / 1_000_000
        _write_record(
            {
                "timestamp": timestamp,
                "tool": tool_name,
                "framework_version": __version__,
                "api_version": API_VERSION,
                "duration_ms": round(duration_ms, 3),
                "outcome": "error",
                "error_type": exc.__class__.__name__,
            }
        )
        raise

    duration_ms = (time.perf_counter_ns() - started) / 1_000_000
    _write_record(
        {
            "timestamp": timestamp,
            "tool": tool_name,
            "framework_version": __version__,
            "api_version": API_VERSION,
            "duration_ms": round(duration_ms, 3),
            "outcome": "success",
            "summary": _result_summary(result),
        }
    )
    return result
