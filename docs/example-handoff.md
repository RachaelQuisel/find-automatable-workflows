# Fictional specification and evaluation

This example uses fictional answers from an earlier Claude Code check. It does not describe a live client workflow. Its wording has been shortened. The rules and unresolved choices remain.

## 1. ID, goal, and audience

- **ID:** OPP-007.
- **Title:** Prepare an active-order draft report. This is a working title. The original card title was not supplied.
- **Goal:** Lena receives an accurate draft without copying order details.
- **Audience:** Lena.

## 2. Evidence and coverage

- Lena reports repeated weekly exports. This is fictional user evidence. No records, files, or counts were inspected.
- The rules below are confirmed fictional interview answers.
- Live source data and table structure were not reviewed. The source tool is unknown.
- Order counts, time spent, and error frequency are unknown.

## 3. Current work and existing coverage

Lena reports exporting order data and copying details into a report each week. The proposed automation would read the selected records and produce a draft on request.

Existing automation coverage is unknown. Check it before construction. Missing access does not prove no automation exists.

## 4. Confirmed rules

1. Include only status `Active`.
2. Sort by Order ID.
3. Preserve Priority exactly as recorded. Do not calculate or replace it.
4. Show **Order ID, Priority, Assignee, Due Date** in that order.
5. Lena starts the process manually.
6. Produce one Markdown draft in the conversation.
7. Send nothing to Slack or email. Change no source records.
8. If a required field is missing, name it and label the draft **Incomplete**.
9. If no orders qualify, produce an explicit empty report.

There are no unconfirmed suggestions. The sort type, Due Date format, and operational retry policy are unresolved.

## 5. Inputs and identifiers

| Data needed | Supplied display name | Live mapping |
|---|---|---|
| Source table | Orders is an assumed role. | Unresolved. |
| Inclusion rule | Status | Unresolved. |
| Display and sort value | Order ID | Unresolved. |
| Display value | Priority | Unresolved. |
| Display value | Assignee | Unresolved. |
| Display value | Due Date | Unresolved. |

These names come from the confirmed rules. They are not verified source names or identifiers. A mapping identifies the actual source for each value.

## 6. Trigger and how it would run

Lena requests the draft manually. A supported reading connection supplies the records. The process filters the records, sorts them, and builds the draft. No schedule or cloud routine is included.

## 7. Intended actions and outputs

- Read Status, Order ID, Priority, Assignee, and Due Date from the selected table.
- Produce one Markdown draft in the conversation.
- Send no messages. Change no records or table structure.

Writing this specification does not authorize construction, execution, or deployment.

## 8. Dependencies and exceptions

- Resolve live table and field mappings. Confirm a reading connection.
- Include only status `Active`.
- List missing required fields and affected orders. Label the draft **Incomplete**.
- When no orders qualify, say “No orders with status Active.”
- Stop if the source is unavailable or a required mapping is unknown.
- Leave the operational stop and retry policy unresolved until the user chooses it.

## 9. Evaluation

### Purpose

Give Lena an accurate Markdown draft of every Active order. Keep the rows in Order ID order.

### Evidence reviewed

The fictional report of weekly exports and confirmed interview rules support these checks. No real source records, exports, completed runs, or failed runs were available.

### What to check

1. Does the draft contain exactly the source orders with status `Active`, without duplicates?
2. Does each row show Order ID, Priority, Assignee, and Due Date in that order?
3. Do displayed values match the source? Is Priority preserved exactly?
4. Are rows sorted by Order ID? Text or numeric sorting must be chosen before this can be checked.
5. Does missing required data produce the affected orders and fields with the label **Incomplete**?
6. Does an empty source produce an explicit empty report?
7. Did the process create only the draft, without sending messages or changing records?

### What success looks like

Every check passes against the source snapshot taken for the run. Lena reviews usefulness. No invented score replaces her judgment.

### When the work is done

All required orders and values match the source. Lena has the draft. Every check passes. No extra action occurred. Unresolved mappings or missing access prevent a completion claim.

### When to stop

Stop if the source cannot be read, a required mapping is unknown, or continuing would change Lena's rules. Stop if any step would send a message or change a source record. Report the problem.

### What to do after a failed run

Find and correct the cause before another complete attempt. Do not repeat an unchanged failed action. Evaluation allows at most ten complete attempts. Stop sooner when continuing could cause harm.

After a tenth failed attempt, report the failure, completed work, remaining work, and help needed. This evaluation limit does not set the automation's retry policy.

### Final result

- **Result:** Needs review.
- **Run number:** Not run. There have been zero runs.
- **Completed work:** The specification and proposed evaluation are written.
- **Unfinished work:** Resolve live mappings, the reading connection, sort type, Due Date format, and retry policy. Check existing automations. Complete implementation, source comparisons, and user review.
- **Problems found:** None were observed. Missing run evidence is not an observed failure.
- **First failed step:** None.
- **Reason for stopping:** This is a proposed specification.

## 10. Remaining choices and status

Construction requires the dependencies and choices listed above. Nothing has been built, run, sent, or edited for this fictional workflow.
