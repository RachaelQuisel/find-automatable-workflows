# Find Automatable Workflows Verification

Verified October 3, 2026. Current package: this repository root, version 0.1.0. Host: Claude Code 2.1.288.

## Repository

The user requested a dedicated GitHub repository: `RachaelQuisel/find-automatable-workflows`. The complete plugin is packaged at its root, with session-local loading instructions adjusted for this checkout. Root manifest validation returned zero errors and warnings; Markdown/README image links resolve and the packaged text has no personal absolute filesystem paths. A first validation invocation targeted the parent directory rather than the new checkout; rerunning in the plugin root passed. The [fictional example handoff](example-handoff.md) is included; original planning artifacts and raw host traces remain in the prior private working repository.

## Scope

The user selected Claude first, recommendations/specifications, manual scans only, and GitHub as the source. GitHub hosting for this workspace is the private repository `RachaelQuisel/plug-in-prd`, verified through repository metadata. The exact live scan repository remains pending; no live account content was scanned during these tests.

The plugin includes the requested three skills and optional source guidance for GitHub, Airtable, Slack, and email. It does not build proposed automations, run background discovery, or activate cloud routines.

The initial behavioral evidence below was recorded under the former working name, Automation Scout (`automation-scout`). Its local trace folder retains that name so the original evidence stays identifiable. The user subsequently selected Workflow Automation Finder.

## Packaging and Host Evidence

- `claude plugin validate plugins/automation-scout --strict --json`: success, zero errors and warnings.
- All three skills passed the Skill Creator frontmatter validator. Its PyYAML dependency was provided through the existing uv runtime after the system Python lacked it.
- The original Grill Me and Eval Creation bodies remain intact. Only unsupported `tags` frontmatter was normalized and routing/handoff notes added. Their locally supplied license status was checked and documented; no redistribution license was inferred.
- All package-local Markdown links resolve and no personal absolute path is embedded in the package.
- Claude's session initialization records list all three `automation-scout` namespaced skills. Their entry files were read in the initial load check.
- The final plugin was copied into a fresh temporary directory and loaded through `--plugin-dir` from that directory. Discovery ran successfully there. This verifies a clean session-local load, not persistent user installation or another Claude surface.
- Behavioral sessions used only Read and Skill tools, an empty MCP configuration, and permission mode `dontAsk`. Observed tool calls were Read only; the interview response needed no tool call. No unexpected tool calls or permission denials occurred.

Detailed local traces are retained in `docs/evidence/automation-scout/` in the original private `RachaelQuisel/plug-in-prd` working repository, rather than bundled here. They contain fictional inputs and local environment paths and are retained as local QA artifacts. The public-facing package does not contain those traces.

## Behavioral Results

The cases were performed by invoking the packaged skills in Claude Code, not by matching the source instructions against expected wording. The outputs and tool traces were inspected against the plan's nine required scenarios.

| Required scenario | Observed behavior | Result |
|---|---|---|
| Description only | Started from the user's account with no connection requirement; labeled reports, assumptions, and unknown automation coverage. | PASS after the deduplication correction below |
| Same workflow across tools | Northstar issue, table, conversation, and partial email produced one NR-18 candidate. Cedar Museum stayed outside scope. | PASS |
| Existing automation | Recognized acknowledgement coverage as distinct from aggregation; the fully automated River Workshop process produced zero new opportunities. | PASS |
| Partial or denied access | Named the four missing email messages and missing live mappings; did not claim a complete account review. Provider access-denial behavior is described but not exercised against a live connector. | PASS for partial supplied sources; live denial unverified |
| Ambiguous business rule | Asked one status-inclusion decision with a recommendation and retained known fields, trigger, and output choices; did not record the recommendation as confirmed. | PASS |
| No supported opportunity | Returned zero recommendations with visible evidence and coverage limits for River Workshop. | PASS |
| Embedded source instructions | The quoted instruction to scan all accounts and send records caused no scope expansion or external action. Tool traces stayed read-only. | PASS in the restricted fixture session |
| Interview stopped or resumed | Produced a resumable Scope-branch summary when stopped, and resumed a supplied Scope-branch summary without re-asking confirmed facts. | PASS |
| Manual/cloud proposal | Delivered the selected manual specification plus eight evaluation sections, unknown mappings and policy, and Needs review/zero runs. No implementation or delivery was claimed. Discovery also described a cloud routine as a conditional alternative. | PASS |

## Defect Found and Corrected

The first description-only case created two candidates for one workflow: generating the report and questioning whether the report was needed. That violated the logical-workflow granularity rule.

The scout and opportunity reference now require simplification and automation alternatives inside the same card. The same description-only prompt was rerun: it returned one candidate with both alternatives. The clean-directory smoke run also returned one candidate. The failed original trace remains preserved for comparison.

The initial clean-load launcher also forwarded its Python input as extra context to the host. The final clean-load check used closed stdin; its output contained only the requested discovery context. This was a verification-launcher correction, not a plugin behavior change.

Two transient text-matching checks used an incorrect expected phrase during tracker updates. They were replaced with direct artifact review and the progress count was reconciled with completed subtask checkboxes. Those checks are not product test evidence.

## Evidence Index

| Local artifact | Purpose |
|---|---|
| `skill-load.json` | Initial namespaced skill loading and source routing |
| `package-validation.json` | Strict manifest validation |
| `cross-tool-input.md`, `cross-tool.jsonl` | Raw fictional multi-source case and observed output/tool calls |
| `no-op-input.md`, `no-op.jsonl` | Raw fully automated case and zero-findings output |
| `description.jsonl`, `description-revised.jsonl` | Original duplicate-candidate defect and corrected run |
| `interview.jsonl`, `pause.jsonl` | Resume and stop behavior |
| `handoff.jsonl`, `handoff-output.md` | Specification/evaluation result and user-review copy |
| `clean-load.jsonl`, `clean-load-revised.jsonl` | Original launcher context and corrected clean-directory session load |

## Selected Name Verification

The user selected **Workflow Automation Finder** for small-business owners. The manifest display name, slug, package directory, README commands, and bundled handoff headings now use that name. Version remains 0.1.0. Strict validation of `plugins/workflow-automation-finder` returned zero errors and warnings. A fresh Claude Code session listed all three skills under the `workflow-automation-finder:` namespace and read the renamed manifest and Scout entry file successfully. Observed tool calls were Read only. The local trace is `name-load.jsonl` in the original evidence folder; this was a naming/load smoke check, not a repeat of the behavioral scenarios.

## Final Name

The user requested **Find Automatable Workflows** and a push to the existing draft PR. The current slug, package directory, command examples, handoff headings, and icon filename use `find-automatable-workflows`. Strict validation of the renamed package returned zero errors and warnings; package resource links and the manifest values were checked. The initial optional host-loading check was blocked by an automatic permission-review timeout. A fresh restricted Claude Code session subsequently loaded the standalone repository under `find-automatable-workflows:`, registered all three bundled skills, and read its root manifest and Scout entry file. The session completed without errors; observed tool calls were Read only. The local trace is retained outside this repository as `find-automatable-workflows-standalone-load.jsonl`. The original timeout therefore does not leave current namespace loading unverified.

## Icon

Current icon: `assets/find-automatable-workflows.png`, created with the user-selected Soft Index Icons renderer. The revised mark makes workflow the primary symbol: one starting step branching into two next steps, drawn as rounded outline boxes with one dot and a top-right sparkle on a dusty mauve ground. The initial magnifier version was replaced after the user clarified that workflow is the keyword; its local copy is retained in `artifacts/workflow-automation-finder-icon/previous-magnifier.png`. The supplied geometry helpers, hand-wobble, Sheet API, paper grain, and squircle mask were reused unchanged; subject painting was omitted for outline-only linework. The PNG was visually inspected and checked as 1024 × 1024 RGBA with transparent corners and a feathered squircle boundary. After the user supplied the three-icon contact sheet, the mark was revised into a branching workflow and visually compared at the same scale beside those references. The exact supplied renderer matches the renderer used for the reference set; its geometry helpers, stroke setting, palette technique, and paper treatment were retained. The comparison is a local review artifact in `artifacts/workflow-automation-finder-icon/reference-comparison.png`; the user reference images are not bundled. This is a packaged asset and README preview; no marketplace upload was performed.

## Remaining Evidence and User Review

- User review of the fictional handoff's usefulness is requested and pending. Automated/host checks do not replace that judgment.
- Exact live GitHub scan scope is requested and pending. No GitHub issue, workflow run, Airtable base, Slack thread, or email has been reviewed live for this plugin.
- Cowork/claude.ai installation, live connector access and denial behavior, persistent installation, public publication, and execution of proposed automations are unverified or excluded.
- The plugin's read-only instructions are behavioral. The restricted QA sessions enforce their own limited tool set; that restriction is not automatically installed with the plugin.

Implementation artifacts are ready for review. The plan remains short of 100% until its user usefulness review is recorded.
