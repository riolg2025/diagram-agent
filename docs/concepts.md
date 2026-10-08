# Core Concepts

This document captures the current V0.1 conceptual vocabulary for the Diagram Understanding & Compilation Agent.

## Evidence

Evidence is information that can be observed, extracted, or explicitly obtained from the source material.

Possible sources include:

- Native presentation or document structure.
- OCR.
- Visual model output.
- Geometry analysis.
- Color and style analysis.
- Connector and line analysis.
- User answers.
- External context supplied to the agent.

Evidence describes what is present. It does not describe what the material means.

Example:

```yaml
id: e-001
type: text
source: ppt_native
content: "Application Management"
confidence: 0.99
```

## Visual Grammar

Visual Grammar records how diagram elements communicate through visual form.

Examples:

- Fill color.
- Border style.
- Emphasis.
- Grouping.
- Containers.
- Relative position.
- Alignment.
- Connection style.

The purpose is to preserve signals such as "this node is highlighted", "these nodes belong to a dashed group", or "this item is visually central".

## Context

Context is first-class evidence.

For diagram intent understanding, page-level and document-level context can be as important as the diagram itself.

Context may include:

- Page title.
- Subtitle.
- Explanatory text.
- Bullets.
- Captions.
- Tables.
- Footer.
- Other shapes on the same page.
- Previous and following pages.
- Section title.
- Document title.

## Semantic

Semantic information describes what evidence is likely to mean.

Semantic claims must remain tied to evidence and confidence. A semantic claim without evidence is only an unsupported guess.

## Intent

Intent describes what the author likely wanted the diagram to communicate.

Intent should be inferred explicitly and validated against evidence, context, and domain knowledge.

## Hypothesis

A hypothesis is a provisional interpretation.

Hypotheses are allowed, but they must be marked as hypotheses and should move through validation before they become accepted semantic or intent claims.

## Confidence

Confidence expresses how strongly the agent can rely on a piece of evidence, semantic claim, or intent claim.

Confidence is used by the agent loop to decide whether to continue, ask a clarifying question, or stop because progress is blocked.

## Provenance

Provenance records where a claim came from.

Every important semantic and intent claim should be traceable back to evidence, user input, or domain knowledge.

## Domain Knowledge

Domain knowledge helps interpret diagram meaning within a specific field.

Examples discussed for future knowledge packs include:

- Generic.
- IT operations.
- Banking.
- Telecom.
- Manufacturing.

V0.1 only names this layer. It does not define domain-specific rules yet.

## Understanding Depth

Understanding depth describes how far the agent has moved from surface recognition toward intent.

At minimum, V0.1 distinguishes:

- Surface evidence: what is visible.
- Visual structure: how elements are arranged and emphasized.
- Semantic interpretation: what elements likely represent.
- Intent interpretation: what the diagram is trying to communicate.

