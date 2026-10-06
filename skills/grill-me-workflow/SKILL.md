---
name: grill-me-workflow
description: 'Ask two to four questions about a selected workflow or automation before it is built. Use when someone says "interview me about this workflow", "grill me on this workflow", "poke holes in this automation", "stress-test this workflow before we build it", or selects an automation opportunity. Use known answers and keep the interview short. Not a deep review of a pricing plan or any plan outside a workflow.'
---

# Grill Me Workflow

Help the user resolve the important choices in a workflow before it is built.

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

If the user asks to “go deeper” or stress-test the workflow, explore the relevant topics in more detail. Continue to ask one question at a time. Stop when the important choices are clear or the user is done.

## Finish or pause

For a selected automation opportunity, preserve its ID, evidence, existing coverage, and confirmed rules. Read [the specification format](references/handoff-format.md) to write the specification. Read the bundled [Eval Creation skill](../eval-creation/SKILL.md) and include its outcome checks. If Eval Creation is not available, write outcome checks for the known goal and confirmed rules.

If the user pauses or stops, return the selected workflow, confirmed decisions, unresolved choices, current topic, and next question with a suggestion if available. Resume from that point. An unresolved choice stays unresolved.

Choosing an option does not authorize building, deploying, changing records, or sending messages. The user defines business rules and the proposed automation's stop and retry behavior.
