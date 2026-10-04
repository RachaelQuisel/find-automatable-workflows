# Selected Opportunity Handoff

Read this when carrying a selected candidate into Grill Me or producing its specification and evaluation. Use the conversation's existing answers and evidence. Do not require a new database, account connection, or saved file to continue.

## Interview context and resumption

Carry the candidate ID/title, workflow/audience, source scope and coverage, evidence locators, existing automation coverage, proposed approach, confirmed answers, and unresolved questions. Mark a suggested answer as proposed until the user selects it.

Conduct the bundled Grill Me interview one question with a recommended answer at a time. Preserve its branch order and stopping rules. Read evidence before asking factual questions it can answer. If the user stops or a blocker needs offline resolution, return:

- the candidate and goal;
- confirmed decisions and their basis;
- remaining questions and any offline blocker;
- current branch;
- next question and recommended answer.

Resume from this summary rather than repeating the interview. The user's stop is not approval of unresolved choices.

## Specification fields

Use a concise Markdown specification with these fields:

1. **Candidate ID, title, goal, and audience.** Preserve the candidate's identity and intended outcome.
2. **Evidence and coverage.** Include minimal source support and all material access gaps; distinguish observations, user reports, fictional examples, and inferences.
3. **Current workflow and existing coverage.** Identify what changes and what existing automations already handle.
4. **Confirmed decisions and business rules.** Record only user-selected rules or authoritative rules actually supplied. List proposals and unresolved choices separately.
5. **Inputs and identifiers.** Name data roles, actual confirmed mappings when available, and unresolved field/repository/account mappings. Do not invent IDs.
6. **Trigger and execution fit.** Explain a manual invocation, deterministic event, or asynchronous cloud routine, including runtime requirements. No routine activation is implied.
7. **Permitted actions and outputs.** Describe exactly the intended reads/writes and destination. Record execution authorization separately; a recommendation does not grant permission to implement, send, or deploy.
8. **Dependencies and exceptions.** State required connections, unavailable evidence, inclusion/exclusion behavior, and the user's selected stop/retry policy. Unknown policies remain unresolved.
9. **Evaluation and completion evidence.** Attach Eval Creation's eight-section evaluation; identify source-of-truth comparisons and user judgments. A proposed evaluation is not a completed-run result.
10. **Remaining choices and implementation status.** State whether the handoff is ready for construction or requires specific decisions/mappings first. Do not call an unverified execution path runnable.

Deliver the specification and evaluation together in the conversation. Save a portable Markdown copy only if requested. Keep credentials, unrelated records, and full private archives out of the handoff.

## Fictional clarified example

This extends the [Acorn opportunity](opportunity-format.md#example-one-workflow-several-sources). The following answers are fictional example answers, not this user's business decisions.

**OPP-001 — Prepare an open-case summary**

- **Goal/audience:** Mira can request an accurate draft without manually copying case details.
- **Evidence/coverage:** the supplied SUP-42 discussion, case schema, and Slack request support the draft-report job. Email is partial and real connector access is unverified. Existing acknowledgement automation covers a different job.
- **Confirmed example answers:** include statuses `New` and `In progress`; include case ID, description, owner, classification tag, and last update; sort by case ID. Preserve source classification tags. Produce a Markdown draft in the current conversation. Do not send it to Slack or email. Missing required fields should be identified and left for Mira to resolve before the draft is considered complete. Zero qualifying cases produces an explicit empty report. No automatic rerun was requested.
- **Inputs:** selected Support Cases table and the five report fields plus status. Exact live base/table/field mappings are not supplied and must be resolved before construction. These display names are fictional examples, not universal Airtable field names.
- **Trigger/execution:** Mira manually requests the draft. A supported read connection supplies the selected records; this could later be implemented as a manual action. No cloud schedule is part of this example.
- **Permitted output:** one draft in the conversation. Construction and external delivery have not been authorized.
- **Exceptions/dependencies:** unavailable source data or unresolved mappings are explicit dependencies. Preserve the confirmed inclusion rule; do not substitute a different status. Identify incomplete cases without silently declaring the full draft complete.
- **Implementation status:** proposed handoff; live mappings and connection remain unresolved. See the evaluation example below for how completion would be checked.

## Evaluation for the fictional draft

### Purpose

Produce a complete, correctly ordered draft of the cases Mira has chosen to include.

### Evidence reviewed

Fictional Acorn source excerpts and the confirmed example answers above. No actual automation execution, live case set, or delivery evidence exists.

### What to check

1. Does the draft contain exactly the source cases whose status is `New` or `In progress`, with no duplicates or excluded cases?
2. Do the five displayed values match the selected source records, preserving classification tags and sorting by case ID?
3. Are missing required fields or source access clearly reported, with the draft labeled incomplete when they prevent verification?
4. Does a zero-case source produce an explicit empty report?
5. Is the output limited to the requested draft, with no Slack/email send or source-record change?

### What success looks like

All outcome checks pass against the selected source snapshot. Mira reviews the result's usefulness; that judgment is not replaced with an invented numeric score.

### When the work is done

Every required source case and value is reconciled, no unsupported action occurred, and Mira has the requested draft. Unresolved mappings and missing evidence prevent an actual completion claim.

### When to stop

Stop construction or evaluation that requires unavailable source access, unknown required mappings, or a change to Mira's confirmed business rules. Report the dependency instead of guessing.

### What to do after a failed run

Understand and correct the cause before another complete evaluation attempt. Eval Creation caps its evaluation workflow at ten complete attempts and stops sooner where continuing could create harm. This does not configure the proposed automation's operational retries; the fictional user requested no automatic rerun.

### Final result

Result: Needs review. Run number: not run; zero execution attempts. Completed work: specification and proposed evaluation. Unfinished work: live mappings, implementation, source reconciliation, and user review. Problems/first failed step: no run observed, so none established. Reason for stopping: this deliverable is a proposed handoff, not an executed workflow.
