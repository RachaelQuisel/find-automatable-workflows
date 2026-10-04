# Fictional Claude Host Verification Output

This is a generated example using fictional user answers, not a live client workflow.

# OPP-007: Specification and evaluation

**Status:** Proposed handoff. Nothing has been built, run or authorized. Two things must be settled before construction: the live table and field mappings, and the read connection.

---

## 1. Candidate, goal and audience

- **Candidate:** OPP-007. The original card's title wasn't in the arguments, so this working title is only descriptive: *Prepare an active-order draft report*.
- **Goal:** Lena stops copying order details by hand. She gets an accurate draft of the active orders.
- **Audience:** Lena.

## 2. Evidence and coverage

| Item | Type | Notes |
|---|---|---|
| Lena repeats the same exports every week | User report (fictional evidence) | No observed records, export files or counts support this. |
| Business rules in section 4 | Confirmed by the user | Selected in the interview. |
| Source records, schema, live data | **Not reviewed** | No read connection has been set up. |
| Number of orders, time spent, how often errors happen | **Unknown** | Not estimated or invented. |

**Access gaps:** I did not inspect any live source, and I have not confirmed which tool the source table lives in.

## 3. Current workflow and existing coverage

- **Current workflow (as reported):** Every week, Lena exports order data and copies the relevant details into a report by hand.
- **What changes:** When Lena asks, the system reads the source records and produces the draft. Lena no longer copies anything by hand.
- **Existing automation coverage:** **Unknown.** No existing automations were checked for this handoff. That is not proof that none exist, and it should be checked before construction.

## 4. Confirmed decisions and business rules

1. Include only orders whose status is exactly `Active`.
2. Sort by Order ID.
3. Keep Priority exactly as recorded. Don't recalculate, reword or fill it in.
4. Show these columns, in this order: **Order ID, Priority, Assignee, Due Date**.
5. Lena starts it manually.
6. The output is one Markdown draft in the conversation.
7. Don't send anything to Slack or email, and don't edit any source records.
8. If a required source field is missing, report it and label the draft **Incomplete**.
9. If no orders qualify, produce an explicit empty report. Don't return blank output.

**Proposed, not confirmed:** none.

**Unresolved:**
- How to sort by Order ID: as text or as numbers. This matters if IDs look like `ORD-9` and `ORD-10`.
- What format to show Due Date in.
- Whether any operational retry policy is needed (see section 8).

## 5. Inputs and identifiers

| Data role | Display name | Live mapping |
|---|---|---|
| Source table | Orders (assumed role) | **Unresolved** |
| Inclusion filter | Status | **Unresolved** |
| Display / sort key | Order ID | **Unresolved** |
| Display | Priority | **Unresolved** |
| Display | Assignee | **Unresolved** |
| Display | Due Date | **Unresolved** |

These display names come from the confirmed rules. They are not verified field names or IDs, and I have not invented any.

## 6. Trigger and execution fit

- **Trigger:** Lena asks for the draft by hand.
- **Best fit:** A manually triggered action that reads the source, filters, sorts and builds the Markdown output. Each run is self-contained and deterministic.
- **Runtime requirement:** A supported, read-only connection to the source table.
- **Not included:** No schedule, cloud routine or event trigger. Nothing is activated.

## 7. Permitted actions and outputs

- **Reads:** Only the Status, Order ID, Priority, Assignee and Due Date fields from the selected source table.
- **Writes:** None.
- **Output:** One Markdown draft in the current conversation.
- **Not permitted:** Sending to Slack or email, editing records, or changing the schema.
- **Execution authorization:** **Not granted.** Selecting OPP-007 and writing this handoff do not authorize building, running or deploying anything.

## 8. Dependencies and exceptions

- **Required before construction:** The live table and field mappings, and a read connection.
- **Inclusion:** Only status `Active` counts. Don't substitute or add other statuses.
- **Missing required fields:** List the affected orders and fields, and label the draft **Incomplete**. Never present it as complete.
- **No qualifying orders:** Produce an explicit empty report, such as "No orders with status Active."
- **Source unavailable or mapping unknown:** Stop and report what is missing. Don't guess.
- **Operational stop/retry policy:** **Unresolved.** The user hasn't chosen one, so none is assumed.

## 9. Evaluation

### Active-order draft evaluation

**Purpose**
Give Lena an accurate Markdown draft of every Active order, in Order ID order, without any manual copying.

**Evidence reviewed**
I reviewed Lena's report of repeated weekly exports (fictional evidence) and the business rules confirmed in the interview. No real source records, past exports, completed runs or failed runs were available. These checks therefore come from the confirmed rules, not from failures anyone has observed.

**What to check**
1. Does the draft contain exactly the source orders with status `Active`, with no duplicates and no other statuses? *(Pass/Fail: compare with a source snapshot.)*
2. Does each row show Order ID, Priority, Assignee and Due Date in that order, with values matching the source record? *(Pass/Fail: compare field by field.)*
3. Does each Priority value exactly match the recorded value? *(Pass/Fail)*
4. Are the rows sorted by Order ID? *(Pass/Fail. Text versus number sorting is still unresolved.)*
5. If any required field is missing, does the draft name the affected orders and fields and carry the label **Incomplete**? *(Pass/Fail)*
6. If no orders are Active, does the output say so explicitly? *(Pass/Fail)*
7. Did the run produce only the one draft in the conversation, with no Slack or email send and no source edits? *(Pass/Fail)*

**What success looks like**
Every check passes against a snapshot of the source taken at the time of the run. Lena then reviews whether the draft is useful. That is her judgment, and no invented score replaces it.

**When the work is done**
The work is done when all checks pass, every Active order and its values match the source snapshot, nothing outside the permitted actions happened, and Lena has the draft. While the mappings and connection are unresolved, completion can't be claimed.

**When to stop**
Stop immediately in any of these cases:
- The source can't be read.
- A required field mapping is unknown.
- Continuing would require changing Lena's confirmed rules.
- Any step would send a message or edit a source record.

Report the problem instead of guessing.

**What to do after a failed run**
Find and fix the cause before trying another complete run. Don't repeat a failed action unless something has been corrected. This evaluation allows no more than 10 complete runs, and you should stop sooner if continuing could cause harm. If the tenth run fails, report what failed, what was finished, what remains and what help is needed. This limit applies to evaluating the process. It is not an operational retry policy for the automation, which is still unresolved.

**Final result**
- Result: Needs review
- Run number: Not run (zero runs)
- Completed work: The specification and the proposed evaluation
- Unfinished work: Live mappings, read connection, Order ID sort type, Due Date format, operational retry policy, existing automation check, implementation, checking the output against the source, and Lena's review
- Problems found: None observed. There is no run evidence, which is different from a failure.
- First failed step: None
- Reason for stopping: This is a proposed handoff, not a run.

## 10. Remaining choices and implementation status

**Not ready for construction.** Still needed:
1. The live source table and field mappings
2. A read-only connection to the source
3. Whether Order IDs sort as text or as numbers
4. The Due Date display format
5. An operational retry or stop policy, or explicit confirmation that none is needed
6. A check for existing automations that already cover this job

Nothing was built, run, sent or edited, and there is no evidence of a completed run.
