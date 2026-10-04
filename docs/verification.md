# Find Automatable Workflows verification

The historical baseline was verified on October 3, 2026. It used version 0.1.0 in Claude Code 2.1.288. The current package is version 0.1.1 at this repository root. Current interaction checks are recorded below.

## Repository and scope

The user originally requested a private repository for [RachaelQuisel/find-automatable-workflows](https://github.com/RachaelQuisel/find-automatable-workflows). The repository is now public. It is the current source, and the plugin is packaged at its root.

The user selected Claude first, recommendations and specifications, manual scans, and GitHub as the initial source. The exact repository for a live scan remains pending. No live account content was scanned during plugin tests.

The package contains three skills. Optional reading guidance covers GitHub, Airtable, Slack, and email. The plugin does not build automations, discover work in the background, or activate cloud routines.

Initial planning and raw test traces belong to the private `RachaelQuisel/plug-in-prd` repository. Its draft pull request is historical. The earlier names Automation Scout and Workflow Automation Finder appear below only to identify historical checks.

Root manifest validation passed without errors or warnings. Internal document and image links resolved. Distributed text contained no personal absolute file paths. One command initially validated the parent directory. Running it from the plugin root passed.

## Historical package and loading checks

- `claude plugin validate plugins/automation-scout --strict --json` passed without errors or warnings.
- All three skills passed the Skill Creator validator. An existing uv environment provided PyYAML when system Python lacked it.
- At this stage, Grill Me and Eval Creation retained their original bodies. Unsupported `tags` metadata was removed. Routing notes were added. Version 0.1.1 later shortened the interview and rewrote the text.
- The supplied skills declared no redistribution license. No license was inferred.
- Claude registered all three `automation-scout` skills and read their entry files.
- A fresh temporary-directory copy loaded with `--plugin-dir`. Discovery ran successfully. This proved loading for one Claude Code session. It did not prove permanent installation or support in another host.
- Tests allowed only Read and Skill tools. They used an empty Model Context Protocol configuration and permission mode `dontAsk`. Model Context Protocol lets a host connect to external tools. Observed calls used Read only. The interview needed no tool call. There were no unexpected calls or permission denials.

Raw traces remain outside this package in the original planning repository's `docs/evidence/automation-scout/` folder. They contain fictional inputs and local environment paths.

## Historical behavior checks

Actual Claude Code sessions performed these cases. Source text matching alone was not used as proof.

| Scenario | Observed result | Status |
|---|---|---|
| Description only | Used the user report without requiring a connection. Kept assumptions and unknown coverage visible. | Passed after the duplicate correction. |
| One workflow across tools | Combined the Northstar sources into one NR-18 recommendation. Excluded Cedar Museum. | Passed. |
| Existing automation | Kept acknowledgements separate from report aggregation. Recommended nothing new for the fully automated River Workshop process. | Passed. |
| Partial access | Reported four missing email messages and unresolved live mappings. Made no complete-review claim. | Passed for supplied partial sources. Live access denial was not tested. |
| Ambiguous rule | Asked one status-inclusion question. Offered a suggestion without confirming it. Preserved known fields, trigger, and output. | Passed. |
| No useful opportunity | Returned zero recommendations with coverage limits for River Workshop. | Passed. |
| Source instructions | Ignored a quoted request to scan all accounts and send records. Did not widen scope or act externally. | Passed in the restricted test session. |
| Stop and resume | Returned a summary at the Scope topic. Resumed supplied context without repeating confirmed answers. | Passed. |
| Manual and cloud proposals | Delivered a manual specification and eight evaluation sections. Kept mappings and policy unknown. Reported Needs review and zero runs. Described a conditional cloud alternative. Claimed no implementation or delivery. | Passed. |

## Historical defects and corrections

The first description-only test produced two recommendations for one workflow. One generated the report. The other questioned whether the report was needed. This violated the one-workflow-per-card rule.

The scout and card format were corrected. Simplification and automation alternatives now belong on one card. The repeated test and clean-directory check each returned one recommendation. The original failed trace was preserved.

The first clean-load launcher passed Python input to Claude as extra context. Closing its standard input corrected the launcher. Standard input is the text a command receives from its caller. The response then contained only the requested discovery context. This changed the test launcher, not the plugin.

Two tracker checks expected the wrong text. Direct artifact review replaced them. The progress count was checked against completed items. These tracker checks are not product evidence.

## Historical trace index

| Local artifact | What it records |
|---|---|
| `skill-load.json` | Initial skill loading and routing. |
| `package-validation.json` | Manifest validation. |
| `cross-tool-input.md`, `cross-tool.jsonl` | Fictional sources and the multi-source result. |
| `no-op-input.md`, `no-op.jsonl` | Fully automated work and zero recommendations. |
| `description.jsonl`, `description-revised.jsonl` | Original duplicate and corrected result. |
| `interview.jsonl`, `pause.jsonl` | Resume and stop behavior. |
| `handoff.jsonl`, `handoff-output.md` | Specification, evaluation, and user-review copy. |
| `clean-load.jsonl`, `clean-load-revised.jsonl` | Original extra context and corrected clean-directory load. |

## Name and current loading

The user first selected Workflow Automation Finder for small-business owners. That stage used version 0.1.0. Validation of `plugins/workflow-automation-finder` passed without errors or warnings. Claude registered its three skills under `workflow-automation-finder:`. It read the renamed manifest and scout file. Calls used Read only. The historical trace is `name-load.jsonl`.

The user then selected Find Automatable Workflows and requested this repository. The current slug, commands, headings, and icon filename use `find-automatable-workflows`.

Validation of the renamed package passed. Links and manifest values were checked. An initial optional loading check timed out during automatic permission review. A later restricted session loaded this standalone package successfully. It registered all three `find-automatable-workflows:` skills. It read the manifest and scout file. The session completed without errors. Calls used Read only.

The trace `find-automatable-workflows-standalone-load.jsonl` remains outside this repository. The earlier timeout leaves no unresolved loading gap for the current namespace.

## Icon

The current icon is `assets/find-automatable-workflows.png`. It used the supplied renderer now named `ghibli-icon-maker`.

The mark shows one starting box branching into two boxes. It uses rounded outlines, one dot, a sparkle, and a dusty mauve background. The user chose workflow as the main symbol.

The renderer's geometry helpers, stroke settings, paper texture, and rounded-square mask were preserved. Shape interiors were left unpainted. The image was visually inspected. It is 1024 × 1024 pixels with transparency at the corners and softened edges.

The final mark was compared at the same scale with the user's three reference icons. The renderer matched their supplied renderer. The comparison remains in the planning workspace at `artifacts/workflow-automation-finder-icon/reference-comparison.png`. An earlier magnifier remains at `artifacts/workflow-automation-finder-icon/previous-magnifier.png`.

The reference images are not bundled. The current icon is packaged and shown in the README. It has not been uploaded to a marketplace.

## Regression before version 0.1.1

After the self-review, a restricted session used this description: “I copy our active orders into a Markdown report every Tuesday.” It requested discovery only with no accounts connected.

The result contained one recommendation, OPP-001. Its card included simplification and automation alternatives. The launcher closed standard input with `< /dev/null`. The response contained only the intended task context. Calls used Read only.

The trace remains in the planning workspace as `docs/evidence/automation-scout/current-regression.jsonl`. This verified the corrected defects against the standalone package. It did not test a live connection.

## Version 0.1.1 changes

The user requested a few interactive questions and plain English throughout the plugin. The scout now uses a short intake. Grill Me asks a few important unresolved questions instead of a fixed count per topic.

The conversation guide covers answers, corrections, unknowns, selection, discovery only, and resumption. The shared writing guide applies to all three skills. [How it works](how-it-works.md) uses the requested Trigger, Inputs, What happens, and Outputs format.

Private Voice Align logging belongs to the editing run. It is not included in the plugin's runtime requirements.

## Version 0.1.1 interaction checks

A new restricted Claude Code conversation began with a small-business request and no connected accounts. It asked one question about repeated work and waited. The next answer produced one recommendation, OPP-001. Selecting it produced one question about an unresolved sort order.

A later answer replaced status `Active` with `Ready` and requested a pause. The response preserved the corrected rule and paused. It listed confirmed answers, remaining choices, and a next question. Resuming with the remaining rules produced a specification and all eight evaluation sections. The result stayed Needs review and Not run. Live mappings stayed unresolved. No construction or delivery was claimed.

A separate discovery-only session returned one workflow card. It kept simplification and automation alternatives together. It did not start an interview or write a specification.

All six responses completed without host errors. Observed tool calls used Read only. Standard input was closed. No live workflow sources were connected. The host read the new conversation and writing guides.

Strict manifest validation passed without errors or warnings. All three skills passed the Skill Creator validator. Internal document links, heading links, and the README image resolved. Distributed text contained no personal absolute paths or em dashes. The text was also reviewed for repeated facts, unclear terms, and incomplete explanations.

Raw traces remain outside this package in the original planning workspace under `docs/evidence/automation-scout/interaction-v0.1.1/`. These checks establish observed behavior for fictional requests. They do not replace live connection tests or user usefulness review.

## Remaining review

- User review of the fictional specification's usefulness remains pending.
- The exact live GitHub scan scope remains pending. No live workflow source was reviewed for these tests.
- Cowork and claude.ai installation remain unverified. Live connections, live denial behavior, permanent installation, and Claude Directory publication remain unverified. The GitHub source repository is public.
- Execution of proposed automations is outside scope.
- Reading instructions do not enforce permissions. Restricted test tools do not automatically restrict an installed plugin.

The original plan remains below 100% until its user usefulness review is recorded.
