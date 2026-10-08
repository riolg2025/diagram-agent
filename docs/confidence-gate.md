# Confidence Gate

The confidence gate is the agent's traffic light.

It decides whether the agent should continue, ask the user a question, or stop because the available information is not enough.

## Three Outcomes

### Continue

Continue means the evidence is good enough to move forward.

Use this when:

- The important evidence is present.
- The interpretation is strongly supported.
- Any uncertainty does not affect the next output.

### Clarify

Clarify means the agent should ask the user one focused question.

Use this when:

- The agent has more than one reasonable interpretation.
- The difference affects the final diagram.
- A short user answer would remove the uncertainty.

The question should be specific. It should explain what is unclear and why the answer matters.

### Block

Block means the agent should stop instead of pretending to know.

Use this when:

- Important evidence is missing.
- The agent cannot form a responsible interpretation.
- A wrong guess would change the meaning of the diagram.

## Good Clarification Questions

A good question is narrow and useful.

Example:

```text
Does the dark blue styling mean Application Management is the current focus,
or only that it belongs to this group?
```

This is useful because the answer changes how strongly the compiled diagram should emphasize the node.

## Poor Clarification Questions

A poor question is too broad.

Example:

```text
What does this diagram mean?
```

That pushes the whole understanding task back to the user.

## Rule of Thumb

The agent should first use the evidence it already has.

It should ask only when the answer changes the next important decision.

