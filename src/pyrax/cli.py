from __future__ import annotations

import argparse
import json
from pathlib import Path

from pyrax.readiness import assess_domain_pack
from pyrax.scaffold import scaffold_project
from pyrax.validation import load_document, load_schema, validate_domain_pack


def _schema_path() -> Path:
    return Path(__file__).resolve().parents[2] / "schemas" / "domain-pack.schema.json"


def cmd_validate(args: argparse.Namespace) -> int:
    pack = load_document(args.domain_pack)
    errors = validate_domain_pack(pack, load_schema(args.schema or _schema_path()))
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALID")
    return 0


def cmd_assess(args: argparse.Namespace) -> int:
    pack = load_document(args.domain_pack)
    report = assess_domain_pack(pack)
    payload = {
        "production_ready": report.production_ready,
        "items": [
            {"area": item.area, "status": item.status.value, "reason": item.reason}
            for item in report.items
        ],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if report.production_ready else 2


def cmd_scaffold(args: argparse.Namespace) -> int:
    root = scaffold_project(args.name, args.destination, force=args.force)
    print(root)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pyrax", description="Pyrax Framework CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    validate = sub.add_parser("validate", help="Validate a Domain Pack against the canonical schema")
    validate.add_argument("domain_pack")
    validate.add_argument("--schema")
    validate.set_defaults(func=cmd_validate)

    assess = sub.add_parser("assess", help="Assess framework readiness for a Domain Pack")
    assess.add_argument("domain_pack")
    assess.set_defaults(func=cmd_assess)

    scaffold = sub.add_parser("scaffold", help="Generate a new Pyrax-based solution skeleton")
    scaffold.add_argument("name")
    scaffold.add_argument("--destination", default=".")
    scaffold.add_argument("--force", action="store_true")
    scaffold.set_defaults(func=cmd_scaffold)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
