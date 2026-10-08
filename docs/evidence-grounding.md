# Evidence Grounding

Evidence grounding is the discipline that keeps the agent from silently guessing.

## Principle

Evidence describes what is present.

Semantic and intent claims describe what the evidence may mean.

The agent must keep those layers separate.

## Claim Types

V0.1 uses three broad claim levels:

- Observed evidence: directly extracted from source material.
- Inferred semantic claim: interpretation based on evidence.
- Inferred intent claim: likely communication purpose.

## Provenance

Every important claim should point back to one or more sources.

Sources may include:

- A native document object.
- OCR output.
- A visual region.
- A geometry or style observation.
- A page-level context element.
- A user answer.
- Domain knowledge.

## Confidence

Confidence is required because not all sources are equally reliable.

Examples:

- Native text extraction may have high confidence.
- OCR from a low-resolution image may have lower confidence.
- Intent inferred from visual emphasis may require validation.

## Clarification

The agent should ask selectively.

Clarifying questions are appropriate when:

- A low-confidence interpretation blocks progress.
- Multiple plausible intents are supported by similar evidence.
- The user can answer a targeted question more cheaply than the agent can infer.

Clarification should not become a substitute for observation. The agent should first use the evidence it already has.

## Blocked State

The agent should be able to stop when it cannot responsibly continue.

A blocked state is preferable to inventing missing meaning.

