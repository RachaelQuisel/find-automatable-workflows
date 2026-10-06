---
name: grill-me
description: Ask a few questions about a workflow or plan before it is built. Use when the user asks to be interviewed, selects an automation opportunity, or wants important gaps resolved. Use known answers and evidence to keep the interview short. Ask more when the user requests a deeper review.
---

# Grill Me

Help the user resolve the important choices in a workflow or plan.

Read [the conversation guide](references/conversation-guide.md). Apply [the writing guide](references/writing-guide.md) to every response.

## Ask and respond

- Start from the selected recommendation and earlier answers. Read supplied evidence before asking factual questions.
- Ask one question at a time. Wait for the answer.
- Usually ask two to four questions about important unanswered decisions. Do not ask a fixed number in each topic.
- Offer a recommended answer when the evidence supports one. Label it as a suggestion until the user chooses it.
- Use each answer to update the proposal. Replace earlier answers when corrected.
- Mark an unknown answer as unknown. Keep required choices visible.
- Ask an extra question only when a missing choice prevents an accurate specification. Explain why it matters.

Consider the problem, approach, required tools, scope, likely failures, and success. These are topics to check against what is already known. They are not a required questionnaire.

If the user asks to “go deeper” or stress-test the full plan, explore the relevant topics in more detail. Continue to ask one question at a time. Stop when the important choices are clear or the user is done.

## Finish or pause

For a selected automation opportunity, preserve its ID, evidence, existing coverage, and confirmed rules. Read [the specification format](references/handoff-format.md) to write the specification. Read the bundled [Eval Creation skill](../eval-creation/SKILL.md) and include its outcome checks.

If the user pauses or stops, return the selected workflow, confirmed decisions, unresolved choices, current topic, and next question with a suggestion if available. Resume from that point. An unresolved choice stays unresolved.

Choosing an option does not authorize building, deploying, changing records, or sending messages. The user defines business rules and the proposed automation's stop and retry behavior.
