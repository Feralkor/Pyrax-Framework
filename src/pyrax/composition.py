from __future__ import annotations

import json
from copy import deepcopy
from importlib.resources import files
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

from pyrax.catalogs import ADAPTER_CATALOG, BUILDING_BLOCKS, UI_COMPONENTS, get_solution_profile


def deep_merge(base: dict[str, Any], overlay: dict[str, Any]) -> dict[str, Any]:
    """Recursively merge dictionaries. Lists/scalars are replaced by the overlay."""
    result = deepcopy(base)
    for key, value in overlay.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = deepcopy(value)
    return result


def compose_domain_pack(base: dict, *overlays: dict) -> dict:
    """Compose an explicit base Domain Pack with ordered organization/domain overlays."""
    result = deepcopy(base)
    for overlay in overlays:
        result = deep_merge(result, overlay)
    return result


def load_solution_manifest_schema() -> dict:
    resource = files("pyrax").joinpath("resources/solution-manifest.schema.json")
    return json.loads(resource.read_text(encoding="utf-8"))


def _schema_errors(manifest: dict) -> list[str]:
    validator = Draft202012Validator(load_solution_manifest_schema())
    errors = sorted(validator.iter_errors(manifest), key=lambda error: list(error.path))
    rendered: list[str] = []
    for error in errors:
        location = ".".join(str(part) for part in error.path) or "root"
        rendered.append(f"{location}: {error.message}")
    return rendered


def validate_solution_manifest(manifest: dict) -> list[str]:
    errors = _schema_errors(manifest)
    if errors:
        return errors

    profile_id = manifest["profile"]
    try:
        profile = get_solution_profile(profile_id)
    except KeyError as exc:
        return [str(exc)]

    blocks = manifest.get("blocks", profile.get("blocks", []))
    adapters = manifest.get("adapters", profile.get("adapters", []))
    ui_components = manifest.get("ui_components", profile.get("ui_components", []))
    for block in blocks:
        if block not in BUILDING_BLOCKS:
            errors.append(f"unknown building block: {block}")
    for adapter in adapters:
        if adapter not in ADAPTER_CATALOG:
            errors.append(f"unknown adapter: {adapter}")
    for component in ui_components:
        if component not in UI_COMPONENTS:
            errors.append(f"unknown UI component: {component}")
    return errors


def materialize_solution_manifest(manifest: dict) -> dict:
    errors = validate_solution_manifest(manifest)
    if errors:
        raise ValueError("; ".join(errors))
    profile = get_solution_profile(manifest["profile"])
    return {
        "profile": manifest["profile"],
        "description": manifest.get("description") or profile.get("description", ""),
        "blocks": manifest.get("blocks", profile.get("blocks", [])),
        "adapters": manifest.get("adapters", profile.get("adapters", [])),
        "ui_components": manifest.get("ui_components", profile.get("ui_components", [])),
        "maturity_target": manifest.get("maturity_target", profile.get("maturity_target")),
        "technology_profile": manifest.get("technology_profile", "not-selected"),
        "domain_pack": manifest.get("domain_pack"),
        "overrides": manifest.get("overrides", {}),
    }


def load_solution_manifest(path: str | Path) -> dict:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle) or {}
    if not isinstance(data, dict):
        raise ValueError("Solution Manifest must be a mapping")
    return data
