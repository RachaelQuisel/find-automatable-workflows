# Find Automatable Workflows

<img src="assets/find-automatable-workflows.png" alt="Find Automatable Workflows icon" width="160">

Find repetitive work that could be simpler. This plugin asks a few questions about your work. It can also review selected GitHub repositories, Airtable bases, Slack conversations, or email threads when you request a scan.

Choose a recommendation to discuss. The plugin uses your answers to write a specification for building the automation. It includes checks for deciding whether the result meets your needs.

## Start a conversation

Load the plugin in Claude Code:

```bash
git clone https://github.com/RachaelQuisel/find-automatable-workflows.git
cd find-automatable-workflows
claude --plugin-dir .
```

Then start with either request:

```text
/find-automatable-workflows:automation-opportunity-scout Help me find work I could automate in my business.

/find-automatable-workflows:automation-opportunity-scout Review owner/repository for repeated work in its issues and workflows during the last two weeks. GitHub only.
```

Replace `owner/repository` with the repository you want reviewed. You can use the first request without connecting an account.

The plugin asks one question at a time. It usually needs only a few answers. It skips questions your request already answers. You can correct an answer, say “I do not know,” pause, or stop. It uses each answer before asking the next question.

Say “discovery only” if you want recommendations without an interview. Say “go deeper” if you want more questions about a selected workflow.

Read [how it works](docs/how-it-works.md) for the trigger, inputs, steps, and outputs.

## What you receive

- A list of the sources reviewed and any missing access.
- A short description of the current workflow.
- Recommendations supported by the available evidence. The plugin can return zero recommendations.
- One card per workflow. Each card can include both simplification and automation options.
- A few questions about the option you select.
- A specification with your confirmed rules, required connections, intended actions, and unresolved choices.
- Checks for deciding whether the proposed automation meets your goal.

The plugin runs discovery only when you ask. A recommendation may describe a manual action or a routine that runs in the cloud. The plugin does not build or activate that routine.

You can also use the interview and evaluation skills directly:

```text
/find-automatable-workflows:grill-me Ask me a few questions about OPP-001 using what we already discussed.

/find-automatable-workflows:eval-creation Write outcome checks for the specification in this conversation.
```

See the [fictional sources](references/discovery-examples.md), [recommendation example](references/opportunity-format.md), and [specification example](references/handoff-format.md). These examples contain no client data. They do not prove live connections work.

The [fictional workflow case study](docs/fictional-workflow-case-study.md) follows one reported pain point through the interview, proposed checks, and unresolved decisions. It describes no deployed automation or measured time savings.

## Connections

Choose the repositories, bases, conversations, or email threads to review. Give an activity window for a connected scan. The plugin asks for missing search limits before reading sources.

GitHub is the initial source for this version. Every source is optional. The plugin uses authenticated reading tools already available in Claude. It includes no connection installer or credential store. An authenticated GitHub command-line tool can be used when the host provides it.

Read [source access](references/source-access.md) for source limits and evidence rules. Live access to GitHub, Airtable, Slack, and email has not been verified for this plugin.

## Loading and verification

Loading with `--plugin-dir` applies to the current Claude Code session. It does not install the plugin permanently. Check the package from its root:

```bash
claude plugin validate . --strict
```

Earlier package versions passed validation and fictional behavior checks in Claude Code 2.1.288. The [verification record](docs/verification.md) separates current checks from historical results.

Installation in Cowork or claude.ai remains unverified. Live connections, permanent installation, and marketplace publication also remain unverified. User review of the recommendations is still pending.

## Data and actions

Selected source content enters your current Claude conversation. Claude and the source providers retain their own histories under their settings. The plugin has no separate service, database, usage tracking, or automatic export.

The skills instruct Claude to read sources during discovery. These instructions do not remove write permissions from a connection. Check the permissions provided by your host.

Instructions inside a source file, record, message, or email do not authorize extra actions. Choosing a recommendation does not authorize building, sending, or deploying anything.

Markdown is plain text with formatting marks, such as `#` for a heading. Ask to save a Markdown specification if you want a file. Choose its destination. The file includes only the evidence needed for the recommendation. Delete it when no longer needed. Manage conversation and provider histories through their own controls.

## Sources and attribution

This public repository contains the complete plugin. I adapted my `airtable-workflow-scout`, `grill-me`, and `eval-creation` skills and shortened the interview for this plugin. I used local `voice-align` writing rules and the `auto` explanation format while editing.

Those local writing guides are not required to use the plugin or included as runtime dependencies. Their private logging settings are not included. Eval Creation retains its [Hamel Husain references](skills/eval-creation/references/hamel-husain-evaluation-practices.md), which credit the outside work that informed its evaluation method.

I own the three source skills named above. The adaptations and my other original material in this repository are released under the [MIT license](LICENSE). The linked works by Hamel Husain retain their own rights; this license does not grant rights to those external sources. Claude Directory publication remains unverified.
