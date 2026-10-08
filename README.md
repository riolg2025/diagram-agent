# diagram-agent

Evidence-Grounded Diagram Understanding & Compilation Agent.

This project explores an agent that can understand, reconstruct, generate, and transform diagrams by grounding every meaningful inference in observable evidence.

The current milestone is **V0.1 Spec**. It is intentionally documentation-first: schemas, concepts, agent loop, and evaluation vocabulary come before implementation.

## Core Philosophy

```text
Observe faithfully -> Infer explicitly -> Ask selectively -> Compile deterministically
```

The agent should not jump from an input diagram directly to a guessed output. It should:

1. Observe the source material faithfully.
2. Extract evidence from text, layout, visual grammar, context, and user-provided information.
3. Make semantic hypotheses explicitly.
4. Validate hypotheses against evidence.
5. Ask the user only when uncertainty blocks meaningful progress.
6. Compile a diagram representation into deterministic renderable outputs.
7. Validate the result and repair it when needed.

## V0.1 Scope

V0.1 defines the stable conceptual foundation:

- Core concepts for evidence-grounded diagram understanding.
- The agent loop and confidence gate.
- The first architecture boundary between schemas, agents, skills, renderers, and domain knowledge.
- Evidence grounding and provenance expectations.
- A benchmark direction for evaluating understanding and compilation quality.

V0.1 does not commit to a specific model provider, rendering engine, storage layer, or runtime architecture.

## Project Structure

```text
.
├── README.md
├── CONTRIBUTING.md
├── LICENSE
├── docs/
│   ├── architecture.md
│   ├── agent-loop.md
│   ├── benchmark.md
│   ├── concepts.md
│   └── evidence-grounding.md
├── examples/
│   └── minimal-flow.json
├── schemas/
├── knowledge/
├── skills/
├── renderers/
└── benchmark/
```

## Design Principle

Schemas are the stable core. Agents, prompts, model providers, skills, renderers, and future tools are producers and consumers of those schemas.

This keeps the project adaptable: the core should survive changes in LLM provider, visual model, rendering backend, or even a partial move away from LLMs.

## Current Status

This repository is at the initial V0.1 skeleton stage.

The first schema drafts now cover the minimum evidence-grounded chain:

```text
Evidence -> Semantic Claim -> Intent Claim -> Diagram IR -> Validation Result
```
