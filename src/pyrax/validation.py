from __future__ import annotations

import json
from importlib.resources import files
from pathlib import Path

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


def validate_domain_pack(pack: dict, schema: dict | None = None) -> list[str]:
    validator = Draft202012Validator(schema or load_canonical_schema())
    errors = sorted(validator.iter_errors(pack), key=lambda error: list(error.path))
    rendered: list[str] = []
    for error in errors:
        location = ".".join(str(part) for part in error.path) or "root"
        rendered.append(f"{location}: {error.message}")
    return rendered
