# Opportunity Cards

Use this format for discovery results. Explain the work and the evidence before the proposed implementation. A description-only run may have user reports rather than observed system evidence; label them accurately.

## Start with coverage and the workflow

Record the selected project/accounts, sources actually inspected, activity window and configuration refs, pagination or truncation limits, missing access, and relevant existing automation coverage. A zero-findings result still includes coverage. Do not call a partial review complete.

Summarize the current workflow as:

`trigger → person/steps → handoffs/decisions → completed outcome`

Name the intended audience and distinguish required controls from habitual steps. Unknown business rules remain questions.

## Card fields

- **Candidate ID and title:** a short stable ID within the scan, such as `OPP-001`. Reuse it throughout selection, interview, specification, and evaluation; do not imply that it is a provider record ID. When resuming a prior scan, retain its supplied IDs rather than inventing replacements.
- **Workflow and audience:** the job and the person who benefits.
- **Problem:** the repeated work or avoidable delay and what supports that interpretation.
- **Evidence:** source identifiers/links, dates when known, minimal excerpts, and whether each is observed, supplied fictional evidence, user-reported, or inferred. Preserve unresolved gaps.
- **Existing coverage:** automation inspected, relevant behavior, configuration/runtime distinction, and unknown external coverage.
- **Proposed improvement:** simplify/remove unnecessary work first, then state `trigger → steps → outcome` if automation is useful.
- **Execution fit:** manually triggered action, deterministic automation, or asynchronous cloud routine; explain the fit and identify unverified runtime dependencies. This is a recommendation, not activation.
- **Dependencies:** source reads, confirmed business rules, permissions, identifiers, and tools required. Do not assume all providers are needed.
- **Priority rationale:** explain likely benefit, feasibility, and uncertainty with the evidence available. Do not manufacture numeric savings or a precise return on investment.
- **Unresolved questions:** only the questions that change the proposal. Distinguish missing evidence from a choice the user needs to make.

Recommend a small useful set, with one first choice when justified. Do not force a minimum number. One logical workflow should have one card even if many sources mention it or several improvements are possible. Put a saved-view alternative and an automation alternative inside that card; do not create a separate candidate merely to ask whether the workflow should exist. Keep unrelated projects separate.

## Example: one workflow, several sources

This example uses only the [fictional Acorn sources](discovery-examples.md#example-scope).

**Coverage:** supplied fictional GitHub discussion and current acknowledgement workflow/log, Airtable schema excerpt, Slack request, and two of five email messages. No live connections. External automation coverage is incomplete. Maple Clinic is excluded.

**Current work:** Friday review request → Mira copies open cases and classification tags → Mira formats a summary and sends it to the support lead → lead receives the correct summary. The available sources do not prove delivery or define all relevant status meanings.

**OPP-001 — Prepare the open-case summary**

- **Audience/problem:** Mira repeatedly copies and formats cases for the Friday review, according to the SUP-42 discussion.
- **Evidence:** [GitHub discussion](discovery-examples.md#github-reporting-discussion), [table structure](discovery-examples.md#airtable-case-structure), and [Slack request](discovery-examples.md#slack-report-request) share SUP-42. These are supplied fictional sources. Email coverage is partial; delivery is unknown.
- **Existing coverage:** [case acknowledgements](discovery-examples.md#existing-acknowledgement-automation) cover new-case responses, not summary aggregation. Other automation coverage is unknown.
- **Improvement:** request summary → read the selected cases using the user's confirmed inclusion rule → format a draft for review. Automatic delivery remains a separate choice.
- **Execution fit:** start with a manual summary action so Mira can review its contents. A recurring cloud routine is an alternative if the user later wants a schedule and its connections can support the work.
- **Dependencies:** selected table/fields, confirmed case inclusion and classification rules, and a supported read connection. No new Slack/email write is required for a draft-only option.
- **Priority:** first candidate because repeated copy/format work is reported and the source structure appears available. Time savings and end-to-end feasibility are unmeasured.
- **Questions:** which cases count as open, what fields and order must appear, and whether the output should remain a reviewed draft or be delivered automatically.

This example does not propose duplicate acknowledgement work, count SUP-42's appearances as independent opportunities, or assume Maple Clinic belongs to Acorn Support.
