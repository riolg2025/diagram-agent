# Benchmark

The benchmark direction for V0.1 is to evaluate whether the agent can understand and compile diagrams in an evidence-grounded way.

This document records evaluation intent only. It does not define a benchmark dataset yet.

## What To Evaluate

The benchmark should eventually evaluate:

- Evidence extraction accuracy.
- Visual grammar preservation.
- Context usage.
- Semantic interpretation quality.
- Intent interpretation quality.
- Clarification quality.
- Diagram IR correctness.
- Rendered output fidelity.
- Result validation and repair behavior.

## Evidence Grounding Checks

A benchmark should ask whether important claims can be traced back to evidence.

Unsupported claims should be visible as errors or low-confidence hypotheses, not hidden inside fluent output.

## Compilation Checks

Compilation should be evaluated separately from understanding.

Once Diagram IR is fixed, rendering should be deterministic and inspectable.

## Clarification Checks

Questions should be selective and useful.

A good clarification question resolves a specific uncertainty that affects the output.

## Current Status

No benchmark data has been selected for V0.1.

