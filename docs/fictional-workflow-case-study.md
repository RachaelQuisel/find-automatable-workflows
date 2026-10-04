# From weekly exports to a scoped draft report

This is a fictional example of how Find Automatable Workflows moves from a reported pain point to a reviewable proposal. It is not a client result or a deployed automation.

## Starting point

Lena says she exports active orders each week and copies their details into a report. That statement identifies repeated work, but it does not establish how many orders exist, how long the task takes, or whether another automation already covers it. No live source was connected for this example.

## Decisions made during the interview

Lena chooses a manual request that produces one Markdown draft in the conversation. She confirms the inclusion rule, sort field, displayed fields, and what to do when a required value is missing or no orders qualify. She also rules out sending messages and changing source records.

The proposal keeps the live table and field mappings, sort type, date format, existing automation coverage, and operational retry policy unresolved. Those choices must be checked before anyone builds it. The [fictional specification and evaluation](example-handoff.md) records the confirmed rules and open decisions.

## How the proposal is checked

The proposed checks compare the draft against a source snapshot: include exactly the qualifying orders, preserve each displayed value, sort as agreed, name missing data, handle an empty result, and confirm that no extra action occurred. A person still needs to judge whether the draft is useful.

The [verification record](verification.md) describes restricted Claude Code sessions using fictional inputs. The current version asked a short sequence of questions, accepted a corrected status rule, resumed after a pause, and produced a specification with outcome checks. These checks establish observed behavior in those sessions. They do not establish live GitHub, Airtable, Slack, or email access, construction, deployment, or time saved.

## Result

The shareable result is a specification marked **Needs review** and **Not run**. It shows what is known, what must be decided, and what evidence a future implementation would need. No automation was built or run for this example.
