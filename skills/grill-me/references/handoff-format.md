# Selected workflow specification

Use this when a user selects a recommendation or when writing its specification and evaluation. Use the conversation's existing answers and evidence. Continuing requires no new database, connection, or saved file.

## Interview and resumption

Follow [the conversation guide](conversation-guide.md) and the bundled Grill Me skill. Carry forward the ID, title, goal, audience, source limits, evidence, existing automation coverage, confirmed answers, and open questions.

A suggested answer stays proposed until the user chooses it. Ask only important unanswered questions. The default interview is short. It does not require a question count for each topic.

If the user pauses or stops, provide the selected workflow, confirmed decisions and their basis, unresolved choices, any offline blocker, current topic, and next question. Include a suggested answer when supported. Resume from there. Stopping does not approve unresolved choices.

## Specification fields

1. **ID, title, goal, and audience.** Preserve the recommendation's identity and intended result.
2. **Evidence and coverage.** Include minimal support and material access gaps. Separate observations, user reports, fictional examples, and inferences.
3. **Current work and existing coverage.** Explain what would change and what existing automations handle.
4. **Confirmed rules.** Record only user-selected rules or supplied authoritative rules. Separate suggestions and unresolved choices.
5. **Inputs and identifiers.** Name the data needed and confirmed source mappings. A mapping identifies which source supplies a value. Mark unresolved fields, repositories, and accounts. Do not invent IDs.
6. **Trigger and how it would run.** Describe the manual request, event, or cloud routine. State the required tools and connections. Nothing is activated.
7. **Intended actions and outputs.** Name the reads, writes, and destinations proposed for the future automation. Record execution permission separately.
8. **Dependencies and exceptions.** State missing connections or evidence, inclusion rules, exceptions, and user-selected stop and retry behavior. Leave unknown policies unresolved.
9. **Evaluation.** Include Eval Creation's eight sections. Identify source comparisons and user judgments. A proposed check is not a completed run.
10. **Remaining choices and status.** State what is ready and what must be resolved before construction. Do not call an unverified path runnable.

Deliver the specification and evaluation in the conversation. Save a Markdown copy only when requested. Exclude credentials, unrelated records, and complete private archives.

## Fictional clarified example

This extends the [Acorn recommendation](opportunity-format.md#example-one-workflow-across-several-sources). These are fictional answers. They are not this user's business rules.

**OPP-001: Prepare an open-case summary**

- **Goal:** Mira can request an accurate draft without copying case details.
- **Evidence:** SUP-42, the table structure, and the Slack request support the reporting task. Email is partial. Live connections are unverified. Acknowledgement automation serves a different purpose.
- **Confirmed example rules:** Include statuses `New` and `In progress`. Include case ID, description, owner, classification tag, and last update. Sort by case ID. Preserve classification tags. Produce a Markdown draft in the conversation. Send nothing to Slack or email. Identify missing required fields. Mira must resolve them before the draft is complete. Report explicitly when zero cases qualify. No automatic rerun was requested.
- **Inputs:** Use the selected Support Cases table, the five report fields, and status. Live base, table, and field mappings remain unknown. These display names are fictional.
- **Trigger:** Mira requests a draft manually. A supported connection reads the selected records. No schedule is included.
- **Output and permission:** Produce one draft in the conversation. Construction and external delivery have not been authorized.
- **Exceptions:** Report unavailable data or unresolved mappings. Preserve the inclusion rule. Identify incomplete cases without declaring the whole draft complete.
- **Status:** This is a proposed specification. Live mappings and a connection are still required.

## Evaluation for the fictional draft

### Purpose

Produce a complete draft of the cases Mira selected. Keep them in the correct order.

### Evidence reviewed

The fictional Acorn sources and confirmed example answers support these checks. No actual run, live case set, or delivery evidence exists.

### What to check

1. Does the draft contain exactly the cases with status `New` or `In progress`, without duplicates?
2. Do the five displayed values match the source records?
3. Are classification tags preserved and cases sorted by case ID?
4. Are missing fields and source access reported? Is the draft labeled incomplete when they prevent verification?
5. Does a zero-case source produce an explicit empty report?
6. Did the process produce only the requested draft, without sending messages or changing source records?

### What success looks like

All checks pass against the selected source snapshot. Mira decides whether the result is useful. No invented score replaces her judgment.

### When the work is done

Every required case and value matches the source. Mira has the requested draft. No extra action occurred. Missing mappings or evidence prevent an actual completion claim.

### When to stop

Stop construction or evaluation that needs unavailable source access or unknown required mappings. Stop if continuing would change Mira's confirmed rules. Report what is missing.

### What to do after a failed run

Understand and correct the cause before another complete evaluation attempt. Eval Creation allows no more than ten complete attempts. Stop sooner when continuing could cause harm. This does not set retries for the proposed automation. The fictional user requested no automatic rerun.

### Final result

- **Result:** Needs review.
- **Run number:** Not run. There have been zero execution attempts.
- **Completed work:** The specification and proposed evaluation are written.
- **Unfinished work:** Live mappings, implementation, source comparisons, and user review remain.
- **Problems and first failed step:** None are established because no run was observed.
- **Reason for stopping:** The deliverable is a proposal. It has not been executed.
