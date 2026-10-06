---
name: eval-creation
description: 'Write short pass or fail checks for whether a business process or automation meets its goal. Use for outcome checks, success criteria, stop conditions, retry limits, or a definition of done for that process or automation. Base the checks on real examples and confirmed rules. Do not use this for a vendor comparison, an employee performance review, or a model evaluation.'
---

# Evaluation Creation

Write checks that someone unfamiliar with the process can use. Apply [the writing guide](references/writing-guide.md) to every response.

Follow Hamel Husain's method. Inspect real work. Find problems that matter to users. Create focused checks for those problems.

## Start with evidence

1. State the user's goal in one sentence.
2. Review completed work, failed work, and user complaints. After a significant change, review about 20 to 50 examples when available.
3. Use the confirmed definition of a good result. Ask someone who understands the work only when that definition is missing.
4. Give each serious or repeated problem a plain, specific name.
5. Create checks for important observed problems. A confirmed rule can be checked before a failure when the required result is exact.
6. Fix an obvious problem directly when a separate check adds little value.

If real examples are unavailable, say so. Use the stated goal, known rules, and clear safety requirements. Mark judgments as needing review. Do not present guesses as facts.

## Write focused checks

- Check the final outcome first. Ask whether it meets the user's goal.
- Make each check one question with a Pass or Fail answer.
- Split broad qualities into facts that can be checked. Use a one-to-five score only when requested.
- Use simple rules or programs for exact fields, counts, dates, formats, and matching values.
- Use a knowledgeable person for decisions that require judgment.
- Use an artificial intelligence reviewer only for a narrow judgment. Give it clear instructions and examples. Compare its decisions with a knowledgeable person's decisions before trusting it.
- Record the first failed step in a process with several steps. Add checks of individual steps only for repeated problems that need diagnosis.
- Turn real failures into simple test cases. Preserve the cause of the failure.

## Include eight sections

1. **Purpose:** State what the process should accomplish.
2. **Evidence reviewed:** Name the examples, failures, rules, and expert decisions used. State what evidence was unavailable.
3. **What to check:** List the few Pass or Fail questions needed to verify the final result.
4. **What success looks like:** State the exact required result.
5. **When the work is done:** Require every success check to pass. Require the result to match the authoritative source.
6. **When to stop:** State the problems that require an immediate stop.
7. **What to do after a failed run:** Require the cause to be understood and corrected before another attempt. Allow no more than ten complete evaluation attempts. Past ten full runs, repeated retries usually hide a design problem. After a tenth failure, report the failure, completed work, remaining work, and help needed.
8. **Final result:** Report the result, run number, completed work, unfinished work, problems, first failed step, and reason for stopping.

## Count attempts correctly

One complete attempt to perform and check the process is one run. A simple inspection or correction is not another complete run.

Do not repeat an unchanged failed action. Stop before ten runs when continuing could create duplicates, lose information, change the wrong records, or make recovery harder. Stop when a check disagrees with a knowledgeable person's decision until the disagreement is resolved.

Add important new failures when found. Run the evaluation again after a meaningful change. If verification is difficult, explain what output or process change would make success easier to check.

Read [the Hamel Husain references](references/hamel-husain-evaluation-practices.md) when the user asks about the method or its sources.

## Final structure

```text
[Process name] evaluation

Purpose
[The required outcome.]

Evidence reviewed
[The evidence used and missing evidence.]

What to check
1. [A question with a Pass or Fail answer.]
2. [A question with a Pass or Fail answer.]

What success looks like
[The exact successful result.]

When the work is done
[The required completion evidence.]

When to stop
[Immediate stop conditions.]

What to do after a failed run
[The correction rule and limit of ten complete evaluation attempts.]

Final result
Result: Successful, Unsuccessful, or Needs review.
Run number: [Number out of ten, or Not run.]
Completed work: [What is complete.]
Unfinished work: [What remains.]
Problems found: [Observed problems, or None.]
First failed step: [The step, or None.]
Reason for stopping: [The reason.]
```

When a selected automation opportunity or its specification is already in the conversation, read [the automation handoff](references/automation-handoff.md) before writing the checks.
