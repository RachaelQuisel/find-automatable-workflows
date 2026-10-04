---
name: grill-me
description: Stress-test a plan or design through a relentless, branch-by-branch interview until every load-bearing decision is resolved. Use when the user says "grill me", "interview me on this", "stress-test this plan", "find the holes", or wants someone to find the gaps before they commit. The point is to surface unanswered questions early so they get answered on a whiteboard, not in production.
---

# Grill Me

Interview the user about every load-bearing decision in their plan or design until shared understanding is reached. The user wants the holes found — be useful by finding them.

## How to run

Ask one question at a time. Wait for the answer before the next question. Don't dump a list.

For each question, provide your **recommended answer** alongside the question — not as the final word, but as a Schelling point that makes "yes/no/different" cheap to answer. A bare question costs the user thinking time; a question + recommendation costs them a reaction.

If a question can be answered by reading the codebase, read the codebase instead of asking.

## Branches to walk

Walk these branches in order. Inside each branch, ask 3-5 probing questions before moving on. Skip a branch only if the plan genuinely has nothing in it (e.g., a refactor has no new users).

1. **Problem.** What's the actual problem? Who has it? How do you know? What's the cost of not solving it? What happens if we wait six months?
2. **Approach.** Why this approach over the obvious alternatives? What did you rule out and why? What's the simplest version that could work?
3. **Architecture.** Where does this live? What does it depend on? What depends on it? Where are the seams? What's the rollback?
4. **Scope.** What's in / out / explicitly deferred? What's the smallest shippable slice? What's the biggest thing that could expand scope mid-build?
5. **Risk.** What's the most likely way this breaks? What's the worst case? What signals would tell you it's going wrong before it does?
6. **Success.** How will you know it worked? What metric / behavior / outcome? When do you check?

## When to stop

Stop when:
- The user signals they're done, OR
- Every branch has been walked and recommended answers are committed, OR
- A blocking ambiguity has surfaced that needs offline resolution (name it, log it, stop).

Don't keep grinding past clarity. The point is to surface what was missing, not to fill the conversation.

## Find Automatable Workflows handoff

When invoked from Find Automatable Workflows, begin with the selected candidate, its evidence, workflow map, existing automation coverage, confirmed answers, and unresolved questions. Read the bundled [handoff format](../../references/handoff-format.md) when recording decisions. Check supplied evidence before asking a question the sources can answer. Never ask the user to repeat an answer already in the handoff; probe the remaining load-bearing decisions.

Record each answer as a confirmed decision, user report, or unresolved choice as appropriate. A recommended answer remains a proposal until the user selects it. Do not widen business rules or infer authorization to build, deploy, or send anything.

When the user stops or an offline blocker appears, return the candidate ID, known decisions, remaining questions, current branch, and next question with its recommended answer. Resume from that summary rather than restarting the interview.

When clarity is reached, produce the specification using the handoff format and read the bundled [Eval Creation skill](../eval-creation/SKILL.md) to attach outcome checks. Read the bundled skill even if another installed skill has the same name.
