from __future__ import annotations

import argparse
import json

from pyrax.bootstrap import bootstrap_discovery
from pyrax.readiness import assess_domain_pack
from pyrax.scaffold import scaffold_project
from pyrax.validation import load_canonical_schema, load_document, load_schema, validate_domain_pack


def cmd_validate(args: argparse.Namespace) -> int:
    pack = load_document(args.domain_pack)
    schema = load_schema(args.schema) if args.schema else load_canonical_schema()
    errors = validate_domain_pack(pack, schema)
    if errors:
        print("INVALID")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALID")
    return 0


def cmd_assess(args: argparse.Namespace) -> int:
    pack = load_document(args.domain_pack)
    errors = validate_domain_pack(pack)
    if errors:
        payload = {
            "valid": False,
            "production_ready": False,
            "validation_errors": errors,
            "items": [],
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 1

    report = assess_domain_pack(pack)
    payload = {
        "valid": True,
        "production_ready": report.production_ready,
        "items": [
            {"area": item.area, "status": item.status.value, "reason": item.reason}
            for item in report.items
        ],
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if report.production_ready else 2


def cmd_bootstrap(args: argparse.Namespace) -> int:
    root = bootstrap_discovery(
        args.organization,
        args.destination,
        archetype=args.archetype,
        force=args.force,
    )
    print(root)
    return 0


def cmd_scaffold(args: argparse.Namespace) -> int:
    pack = load_document(args.domain_pack) if args.domain_pack else None
    if pack:
        errors = validate_domain_pack(pack)
        if errors and not args.allow_invalid:
            print("Domain Pack is invalid; scaffold aborted.")
            for error in errors:
                print(f"- {error}")
            return 1
    root = scaffold_project(
        args.name,
        args.destination,
        domain_pack=pack,
        force=args.force,
    )
    print(root)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="pyrax", description="Pyrax Framework CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    bootstrap = sub.add_parser(
        "bootstrap",
        help="Create a discovery workspace for a new organization before a Domain Pack exists",
    )
    bootstrap.add_argument("organization")
    bootstrap.add_argument("--destination", default=".")
    bootstrap.add_argument("--archetype", default="to-be-discovered")
    bootstrap.add_argument("--force", action="store_true")
    bootstrap.set_defaults(func=cmd_bootstrap)

    validate = sub.add_parser("validate", help="Validate a Domain Pack against canonical contracts")
    validate.add_argument("domain_pack")
    validate.add_argument("--schema")
    validate.set_defaults(func=cmd_validate)

    assess = sub.add_parser("assess", help="Assess framework readiness for a valid Domain Pack")
    assess.add_argument("domain_pack")
    assess.set_defaults(func=cmd_assess)

    scaffold = sub.add_parser("scaffold", help="Generate a new Pyrax-based solution skeleton")
    scaffold.add_argument("name")
    scaffold.add_argument("--destination", default=".")
    scaffold.add_argument("--domain-pack")
    scaffold.add_argument("--allow-invalid", action="store_true")
    scaffold.add_argument("--force", action="store_true")
    scaffold.set_defaults(func=cmd_scaffold)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    raise SystemExit(args.func(args))


if __name__ == "__main__":
    main()
