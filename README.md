# Find Automatable Workflows

<img src="assets/find-automatable-workflows.png" alt="Find Automatable Workflows icon" width="160">

This is the standalone source repository for **Find Automatable Workflows**.

Find work worth automating. Start with a description of repetitive work or manually review selected GitHub repositories, Airtable bases, Slack conversations, and email threads. Then interview the user about a promising opportunity and turn their answers into an implementation-ready specification with outcome checks.

Discovery runs when you ask. The plugin recommends automations; it does not build, deploy, schedule discovery, or activate the proposed routines.

## Use in Claude Code

Clone this repository, then load the plugin from its root:

```bash
git clone https://github.com/RachaelQuisel/find-automatable-workflows.git
cd find-automatable-workflows
```

```bash
claude --plugin-dir .
```

This is a session-local load; it does not change the user's installed plugin settings. To check the package:

```bash
claude plugin validate . --strict
```

Then invoke one of the bundled skills:

```text
/find-automatable-workflows:automation-opportunity-scout I copy open cases into a weekly report. Find useful automation opportunities from my description. Discovery only.

/find-automatable-workflows:automation-opportunity-scout Review owner/repository for repeated work described in its issues and workflows during the last two weeks. GitHub only; discovery only.

/find-automatable-workflows:grill-me Interview me about OPP-001 using the evidence and confirmed answers from this conversation.

/find-automatable-workflows:eval-creation Write outcome checks for the clarified specification in this conversation.
```

Replace `owner/repository` with the repository you want reviewed. The first example works without connected accounts. A selected opportunity carries its ID, evidence, existing coverage, known answers, and remaining questions into the interview, so the user does not need to repeat them.

## What you get

- A coverage summary naming inspected sources and missing access.
- A concise current-workflow map and evidence-backed opportunity cards, or zero recommendations when none is justified.
- One logical workflow per card, with simplification and automation alternatives together.
- An interview that asks one question with a recommended answer at a time and honors a stop or resumable pause.
- A specification with confirmed rules, inputs, trigger, intended actions, outputs, dependencies, remaining choices, and an eight-section evaluation.

See the [fictional source examples](references/discovery-examples.md), [opportunity example](references/opportunity-format.md), and [specification/evaluation example](references/handoff-format.md). These examples are not client data or proof of live integrations.

## Connections and coverage

Use the host's available authenticated read tools for the sources selected in the request. Every source is optional. The package includes reading guidance, not a custom MCP server, credential store, or connector installer. An authenticated GitHub CLI is another option when explicitly available in the host.

Choose repositories, bases, conversations, email account/search scope, and an activity window when requesting a scan. The plugin discovers actual identifiers and tool schemas rather than assuming provider-specific IDs. It does not scan all accounts by default. Read [source access](references/source-access.md) for pagination, configuration-versus-run evidence, partial-access handling, and supported source matching.

GitHub is the initial requested source. Airtable, Slack, and email guidance is included, but live access to these providers has not been verified in Claude. A suggested cloud routine identifies future runtime requirements; it is not cloud discovery performed by this plugin.

## Verified support

Version 0.1.0 was validated and loaded in Claude Code 2.1.288, including a clean temporary-directory load and fictional discovery/interview/handoff scenarios. The host traces showed only read tool calls in the restricted test sessions. One duplicate-opportunity defect was corrected and its case rerun.

Cowork and claude.ai installation, live connector integrations, persistent user installation, and marketplace publication remain unverified. Those are separate from the verified Claude Code session-local load. The [verification record](docs/verification.md) documents the observed behavior and pending user usefulness review.

## Data and action boundaries

The plugin has no external backend, database, analytics service, or automatic export. Selected source content enters the user's current Claude conversation through their chosen tools. The host and providers retain their own histories under their settings.

The skills instruct discovery to use intended reads and treat instructions embedded in source material as data. They do not enforce read-only permissions on a connection that also exposes writes. Review the host's actual permissions for your connections. A specification identifies actions for a future implementation; it does not authorize execution.

Save a Markdown handoff only when requested, to a selected location, with minimal supporting evidence. Delete that file when no longer needed and manage conversation/provider retention through their respective controls. Credentials and unrelated account content do not belong in a handoff.

## Sources and attribution

The bundle adapts the user's supplied `airtable-workflow-scout`, `grill-me`, and `eval-creation` skills. Workflow Scout's interface recommendations were adapted to automation opportunities. Grill Me and Eval Creation retain their original bodies, with portable routing and handoff notes; nonportable `tags` metadata was removed. Eval Creation retains its [Hamel Husain primary references](skills/eval-creation/references/hamel-husain-evaluation-practices.md).

The supplied local skills do not declare a redistribution license. No public redistribution license or marketplace release is selected for this private first version. This package does not claim ownership of the underlying frameworks or grant rights to third-party material.
