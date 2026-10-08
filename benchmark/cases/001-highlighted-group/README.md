# Benchmark Case 001: Highlighted Group

This case tests the smallest useful evidence-grounded chain.

The source material describes a diagram with a dashed container and a highlighted node labeled "Application Management".

## Purpose

This case checks whether the system can represent:

- Text evidence.
- Container evidence.
- Visual style evidence.
- A semantic hypothesis grounded in evidence.
- An intent hypothesis with unresolved uncertainty.
- A clarification question.
- A Diagram IR that preserves evidence links.
- A validation result that distinguishes structural pass from intent warning.

## Expected Chain

```text
input.md
  -> expected-evidence.json
  -> expected-semantic.json
  -> expected-intent.json
  -> expected-diagram-ir.json
  -> expected-validation.json
```

## Scope

This case does not require image parsing, OCR, rendering, or runtime execution.

It is a contract fixture for V0.1 schema and reasoning shape.

