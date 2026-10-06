# Opportunity cards

Use this format for recommendations. Describe the work and evidence before the proposed automation. Label a description as a user report when no source was inspected.

## Source coverage and current work

State the selected project and accounts, inspected sources, date window, and configuration versions. Report missing access, omitted results, and relevant existing automations. Include coverage even when there are zero recommendations. Do not call a partial review complete.

Describe the trigger, person doing the work, steps, decisions, and completed outcome. Name who benefits. Distinguish required controls from habitual steps. Leave unknown business rules as questions.

## Card fields

- **ID and title:** Use a short stable identifier such as `OPP-001`. Keep it through selection, interview, specification, and evaluation. It identifies a recommendation in the scan, not a provider record. Preserve supplied IDs when resuming.
- **Workflow and audience:** State the job and who benefits.
- **Problem:** Describe the repeated effort or delay. State what supports the claim.
- **Evidence:** Include source identifiers or links, known dates, and minimal excerpts. Label observations, fictional sources, user reports, and inferences. Keep gaps visible.
- **Existing coverage:** State what the inspected automations handle. Separate configuration from successful results. Mark unavailable external coverage unknown.
- **Improvement:** Consider removing or simplifying work first. If automation is useful, describe its trigger, steps, and outcome.
- **How it would run:** Recommend a manual action, an event-based automation, or a routine in the cloud. Explain the fit and unverified requirements. Nothing is activated.
- **Dependencies:** Name required source access, confirmed rules, permissions, identifiers, and tools. Include only the providers needed.
- **Priority:** Explain likely benefit, feasibility, and uncertainty. Do not invent savings or a return on investment.
- **Open questions:** Include only questions that change the proposal. Separate missing evidence from choices the user must make.

Recommend a small useful set. Give a first choice when justified. There is no minimum number of cards. Keep simplification and automation options for one workflow in one card. Keep unrelated projects separate.

Unless discovery only was requested, invite the user to choose a card. Wait for their answer. Use [the conversation guide](conversation-guide.md) to continue.

## Example: one workflow across several sources

This uses the [fictional Acorn sources](discovery-examples.md#example-scope).

**Coverage:** The supplied sources include a GitHub discussion, an acknowledgement workflow and run log, an Airtable table structure, a Slack request, and two of five email messages. No live sources were read. Other automation coverage is incomplete. Maple Clinic is excluded.

**Current work:** Mira copies open cases and their classification tags for the Friday review. She formats a summary and sends it to the support lead. The sources do not prove delivery or define every status.

**OPP-001: Prepare the open-case summary**

- **Audience and problem:** Mira reports repeated copying and formatting in SUP-42.
- **Evidence:** The [discussion](discovery-examples.md#github-reporting-discussion), [table structure](discovery-examples.md#airtable-case-structure), and [Slack request](discovery-examples.md#slack-report-request) share SUP-42. These sources are fictional. Email coverage is partial. Delivery is unknown.
- **Existing coverage:** [Case acknowledgements](discovery-examples.md#existing-acknowledgement-automation) handle new-case responses. They do not build the summary. Other coverage is unknown.
- **Improvement:** First ask whether a saved view could replace the report. If a report is needed, a manual action could read the selected cases and prepare a draft. Use the user's confirmed inclusion rule.
- **How it would run:** A manual action lets Mira review the draft. A recurring cloud routine is another option if the user chooses a schedule and suitable connections exist.
- **Dependencies:** Resolve the table and fields. Confirm inclusion and classification rules. Confirm a supported reading connection. A draft requires no Slack or email write.
- **Priority:** This is the first recommendation because repeated effort is reported and the data structure is supplied. Savings and complete feasibility are unmeasured.
- **Open questions:** Confirm which cases count as open, the required fields and order, and whether the result stays a draft or is delivered.

The acknowledgement workflow serves a different purpose. Maple Clinic belongs to a different project. Neither becomes another recommendation for this reporting job.
