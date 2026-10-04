## Trigger

- You ask Find Automatable Workflows to find repeated work that could be automated.
- A connected scan starts after you identify the sources and activity window to review.

## Inputs

- Your description explains the task, who does it, and the result they need.
- Your answers supply missing details and confirmed business rules.
- Selected source files, records, discussions, or messages provide supporting evidence when access is available.
- Existing automation definitions and results show what is already covered when they can be read.

## What happens

1. The plugin reads your request and earlier answers.
2. If important details are missing, it asks a few questions. It asks one question at a time and waits for your answer.
3. If you request a connected scan, it confirms the source limits. It reads the selected material through tools available in Claude. If access is missing or results are incomplete, it reports that gap.
4. It describes the current work and checks available existing automations.
5. It looks for work that could be removed, simplified, or automated. If no useful opportunity is supported, it returns zero recommendations.
6. It presents one card per workflow. Each card can include simplification and automation options.
7. If you requested discovery only, it ends after the findings. Otherwise it invites you to choose a workflow.
8. After you choose, it asks a few questions about important unresolved choices. Each answer updates the proposal. A correction replaces the earlier answer. An unknown answer remains visible.
9. If you pause or stop, it ends the questions and provides enough context to resume later. If a required choice remains unresolved, it marks the specification as needing that decision.
10. When enough is known, it writes the specification and checks for deciding whether the proposed automation succeeds. Missing live evidence prevents a claim that it has run successfully.

## Outputs

- The conversation contains the source coverage, current workflow, and supported recommendations.
- A selected workflow produces a specification with confirmed rules, intended actions, required connections, and remaining choices.
- The specification includes outcome checks. It can describe a manual action or a routine that runs in the cloud.
- A pause produces a summary of confirmed answers and the next unanswered question.
- A requested saved copy uses Markdown, which is plain text with formatting marks. It goes to the location you choose. The plugin does not build, activate, or schedule the proposed automation.
