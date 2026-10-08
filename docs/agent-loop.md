# Agent Loop

The agent loop is the core behavior model for V0.1.

The agent should not behave as:

```text
input diagram -> guess -> output diagram
```

It should behave as an evidence-grounded loop:

```text
Observe
  ↓
Extract Evidence
  ↓
Infer
  ↓
Validate
  ↓
Confidence Gate
  ├── Continue
  ├── Clarify
  └── Block
  ↓
Semantic Model
  ↓
Intent Model
  ↓
Diagram IR
  ↓
Compile / Render
  ↓
Validate Result
  ↓
Repair / Done
```

## Observe

Observe the raw material without prematurely interpreting it.

The material may include a diagram image, native presentation structure, OCR text, surrounding slide content, or user-provided context.

## Extract Evidence

Extract observable facts from the source.

Evidence should preserve source, confidence, and provenance.

## Infer

Build explicit hypotheses from evidence.

Inference is allowed, but inferred claims must not be confused with directly observed evidence.

## Validate

Validate hypotheses against the available evidence, visual grammar, context, and domain knowledge.

## Confidence Gate

The confidence gate decides what the agent should do next.

- Continue: confidence is sufficient to keep building the model.
- Clarify: a targeted user question can resolve meaningful ambiguity.
- Block: the agent cannot proceed responsibly with the available information.

## Semantic Model

The semantic model represents interpreted meaning while preserving evidence links.

## Intent Model

The intent model represents the likely communication goal of the diagram.

## Diagram IR

Diagram IR is the structured intermediate representation that downstream renderers can consume.

V0.1 names this layer but does not yet define a complete IR schema.

## Compile / Render

Compilation should be deterministic once the Diagram IR is fixed.

Renderers may eventually target SVG, PPTX, or other formats.

## Validate Result

The loop ends only after result validation, not after generation.

The generated output should be checked against the intended semantic and visual structure.

## Repair / Done

If validation fails, the agent should repair the result and validate again. If validation passes, the task is done.

