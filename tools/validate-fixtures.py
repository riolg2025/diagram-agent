#!/usr/bin/env python3
"""Validate V0.1 examples and benchmark fixtures against draft schemas."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

try:
    import jsonschema
except ImportError:
    print("Missing dependency: jsonschema")
    print("Install it with: python3 -m pip install jsonschema")
    sys.exit(2)


ROOT = Path(__file__).resolve().parents[1]


SCHEMAS = {
    "evidence": ROOT / "schemas/evidence.schema.json",
    "semantic": ROOT / "schemas/semantic.schema.json",
    "intent": ROOT / "schemas/intent.schema.json",
    "question": ROOT / "schemas/question.schema.json",
    "diagram_ir": ROOT / "schemas/diagram-ir.schema.json",
    "validation": ROOT / "schemas/validation.schema.json",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def validator_for(schema_name: str) -> jsonschema.Draft202012Validator:
    schema = load_json(SCHEMAS[schema_name])
    return jsonschema.Draft202012Validator(schema)


def validate_item(schema_name: str, item: Any, label: str) -> list[str]:
    validator = validator_for(schema_name)
    errors = sorted(validator.iter_errors(item), key=lambda error: list(error.path))
    messages = []
    for error in errors:
        path = ".".join(str(part) for part in error.path) or "<root>"
        messages.append(f"{label}: {path}: {error.message}")
    return messages


def validate_many(schema_name: str, items: list[Any], label: str) -> list[str]:
    messages = []
    for index, item in enumerate(items):
        item_id = item.get("id", index) if isinstance(item, dict) else index
        messages.extend(validate_item(schema_name, item, f"{label}[{item_id}]"))
    return messages


def validate_minimal_flow() -> list[str]:
    path = ROOT / "examples/minimal-flow.json"
    data = load_json(path)
    messages = []
    messages.extend(validate_many("evidence", data["evidence"], str(path)))
    messages.extend(validate_many("semantic", data["semantic_claims"], str(path)))
    messages.extend(validate_many("intent", data["intent_claims"], str(path)))
    messages.extend(validate_many("question", data["questions"], str(path)))
    messages.extend(validate_item("diagram_ir", data["diagram_ir"], str(path)))
    messages.extend(validate_many("validation", data["validation"], str(path)))
    return messages


def validate_benchmark_case(case_dir: Path) -> list[str]:
    messages = []
    checks = [
        ("evidence", "expected-evidence.json", True),
        ("semantic", "expected-semantic.json", True),
        ("intent", "expected-intent.json", True),
        ("question", "expected-question.json", True),
        ("diagram_ir", "expected-diagram-ir.json", False),
        ("validation", "expected-validation.json", True),
    ]

    for schema_name, filename, is_array in checks:
        path = case_dir / filename
        data = load_json(path)
        if is_array:
            messages.extend(validate_many(schema_name, data, str(path)))
        else:
            messages.extend(validate_item(schema_name, data, str(path)))

    return messages


def validate_benchmark_cases() -> list[str]:
    cases_root = ROOT / "benchmark/cases"
    if not cases_root.exists():
        return []

    messages = []
    for case_dir in sorted(path for path in cases_root.iterdir() if path.is_dir()):
        messages.extend(validate_benchmark_case(case_dir))
    return messages


def main() -> int:
    messages = []
    messages.extend(validate_minimal_flow())
    messages.extend(validate_benchmark_cases())

    if messages:
        print("Fixture validation failed:")
        for message in messages:
            print(f"- {message}")
        return 1

    print("All fixtures validate against draft schemas.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

