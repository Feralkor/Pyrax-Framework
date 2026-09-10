from __future__ import annotations

import json
from importlib.resources import files
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator


def load_document(path: str | Path) -> dict:
    file_path = Path(path)
    text = file_path.read_text(encoding="utf-8")
    if file_path.suffix.lower() in {".yaml", ".yml"}:
        data = yaml.safe_load(text)
    else:
        data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("Domain Pack must be a mapping/object")
    return data


def load_schema(schema_path: str | Path) -> dict:
    return json.loads(Path(schema_path).read_text(encoding="utf-8"))


def load_canonical_schema() -> dict:
    resource = files("pyrax").joinpath("resources/domain-pack.schema.json")
    return json.loads(resource.read_text(encoding="utf-8"))


def _duplicates(values: list[str]) -> set[str]:
    seen: set[str] = set()
    duplicates: set[str] = set()
    for value in values:
        if value in seen:
            duplicates.add(value)
        seen.add(value)
    return duplicates


def _ids(items: Any, key: str = "id") -> list[str]:
    if not isinstance(items, list):
        return []
    return [str(item[key]) for item in items if isinstance(item, dict) and item.get(key)]


def validate_integrity(pack: dict) -> list[str]:
    errors: list[str] = []

    source_ids = _ids(pack.get("sources"))
    signal_ids = _ids(pack.get("signals"))
    decision_ids = _ids(pack.get("decisions"))
    entity_names = _ids(pack.get("entities"), key="name")

    for label, values in (
        ("source", source_ids),
        ("signal", signal_ids),
        ("decision", decision_ids),
        ("entity", entity_names),
    ):
        for duplicate in sorted(_duplicates(values)):
            errors.append(f"integrity.{label}: duplicate identifier '{duplicate}'")

    known_sources = set(source_ids)
    for signal in pack.get("signals", []):
        if not isinstance(signal, dict):
            continue
        signal_id = signal.get("id", "<unknown>")
        for source_id in signal.get("evidence_required", []):
            if source_id not in known_sources:
                errors.append(
                    f"integrity.signal.{signal_id}: evidence source '{source_id}' is not declared"
                )

    known_signals = set(signal_ids)
    for decision in pack.get("decisions", []):
        if not isinstance(decision, dict):
            continue
        decision_id = decision.get("id", "<unknown>")
        for signal_id in decision.get("triggered_by", []):
            if signal_id not in known_signals:
                errors.append(
                    f"integrity.decision.{decision_id}: trigger signal '{signal_id}' is not declared"
                )

    semantics = pack.get("semantics", {})
    if isinstance(semantics, dict):
        certified = set(semantics.get("certified", []))
        candidates = set(semantics.get("candidates", []))
        unknowns = set(semantics.get("unknowns", []))
        for value in sorted(certified & candidates):
            errors.append(f"integrity.semantics: '{value}' cannot be CERTIFIED and CANDIDATE")
        for value in sorted(certified & unknowns):
            errors.append(f"integrity.semantics: '{value}' cannot be CERTIFIED and UNKNOWN")
        for value in sorted(candidates & unknowns):
            errors.append(f"integrity.semantics: '{value}' cannot be CANDIDATE and UNKNOWN")

    return errors


def validate_domain_pack(pack: dict, schema: dict | None = None) -> list[str]:
    validator = Draft202012Validator(schema or load_canonical_schema())
    schema_errors = sorted(validator.iter_errors(pack), key=lambda error: list(error.path))
    rendered: list[str] = []
    for error in schema_errors:
        location = ".".join(str(part) for part in error.path) or "root"
        rendered.append(f"{location}: {error.message}")
    rendered.extend(validate_integrity(pack))
    return rendered
