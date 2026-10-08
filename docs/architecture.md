# Architecture

V0.1 defines the project as a schema-centered system.

The stable core is not a model, prompt, or rendering library. The stable core is the set of schemas that describe evidence, semantic claims, intent, questions, diagram IR, and validation results.

## High-Level Layers

```text
Source Material
  ↓
Evidence Extraction
  ↓
Semantic and Intent Inference
  ↓
Confidence Gate and Clarification Protocol
  ↓
Diagram IR
  ↓
Renderers
  ↓
Validation and Repair
```

## Schema Core

Schemas are the contracts between system parts.

Expected schema areas:

- evidence
- semantic
- intent
- question
- diagram-ir
- validation

V0.1 starts with the smallest useful chain:

```text
Evidence -> Semantic Claim -> Intent Claim -> Diagram IR -> Validation Result
```

The draft schemas are intentionally minimal and may change as benchmark cases reveal missing structure.

## Agents

Agents consume and produce schema-shaped data.

They may observe, infer, validate, ask questions, compile, render, and repair. The current design treats agent behavior as replaceable as long as the schema contracts remain stable.

## Skills

Skills are named capabilities.

Initial skill areas discussed:

- understand-diagram
- reconstruct-diagram
- generate-diagram
- transform-diagram
- render-diagram

V0.1 records these as conceptual capabilities, not implemented modules.

## Domain Knowledge

Domain knowledge is separated from the core agent loop.

This lets the system start with generic diagram understanding and later add domain-specific interpretation packs.

## Renderers

Renderers compile Diagram IR into concrete outputs.

Potential output formats include SVG and PPTX, but V0.1 does not choose or implement a renderer.

## Validation

Validation is part of the architecture, not an optional finishing step.

The result should be checked against evidence, semantic claims, intent, and rendering expectations.
