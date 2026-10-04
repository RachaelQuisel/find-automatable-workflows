---
name: eval-creation
description: Write short, plain-English evaluations for processes and repeated tasks using Hamel Husain's evidence-first practices. Use when the user asks for an eval, a definition of done, success criteria, stop conditions, retry limits, or a clear way to decide whether a process worked.
---

# Evaluation Creation

Write an evaluation that someone unfamiliar with the process can understand and use. Follow Hamel Husain's evidence-first approach: inspect real work, find problems that matter to users, and create focused checks for those problems.

## Start with real evidence

1. State the user's goal in one sentence.
2. Review actual completed work, failed work, and user complaints before deciding what to check. After a significant change, review about 20 to 50 examples when that many are available.
3. Ask a person who understands the work and its users to decide what good work looks like.
4. Give each repeated or serious problem a plain, specific name.
5. Create checks for important problems that have been observed. Do not invent broad checks for problems that might never occur. A known rule may be checked before a failure occurs when success is exact and unambiguous.
6. Fix an obvious problem directly when a separate check would add little value.

If no real examples are available, say so. Use only the user's stated goal, known rules, and clear safety requirements. Mark subjective conclusions as needing review instead of presenting guesses as facts.

## Write focused checks

- Check the final outcome first by asking, “Did this meet the user's goal?”
- Make each check answer one clear question with **Pass** or **Fail**.
- Split broad ideas such as quality, helpfulness, or accuracy into separate facts that can be checked. Do not use a one-to-five score unless the user specifically requires one.
- Use a simple rule or program for exact facts such as required fields, counts, dates, formats, or matching values.
- Use a knowledgeable person when the decision depends on judgment.
- Use an artificial intelligence reviewer only for a narrow judgment question. Give it clear instructions and examples, and compare its decisions with decisions made by a knowledgeable person before trusting it.
- For a process with several steps, record the first step where the process went wrong. Add step-by-step checks only for repeated problems that need diagnosis.
- Turn real failures into test cases. Make each case as simple as possible while preserving the failure.

## Include these sections

1. **Purpose:** Explain what the process is supposed to accomplish.
2. **Evidence reviewed:** State which real examples, failures, rules, and expert decisions were used. State what evidence was unavailable.
3. **What to check:** List the few pass-or-fail questions that prove the final result is correct and safe.
4. **What success looks like:** State the exact result required for success.
5. **When the work is done:** Give a clear definition of done. Require every success check to pass and require the final result to match the source of truth.
6. **When to stop:** State the problems that require an immediate stop before more work is performed.
7. **What to do after a failed run:** Require the cause to be understood and corrected before another run. Never allow more than 10 complete runs. If the tenth run fails, stop and explain what failed, what was completed, what remains, and what help is needed.
8. **Final result:** Report the result, run number, completed work, unfinished work, problems, first failed step, and reason for stopping.

## Use plain language

- Use complete sentences, familiar words, and short sections.
- Keep the evaluation as short as possible without removing important evidence, safety, or success checks.
- Do not use abbreviations, invented terms, vague labels, or unnecessary technical language.
- Give every section and named item a name that explains what it is.
- Explain any necessary specialized term the first time it appears.
- Replace statements such as “verify everything” with facts that can be checked.

## Apply the retry limit correctly

Treat one complete attempt to perform and check the process as one run. Do not count a simple inspection or correction as another run unless the full process is performed again.

Do not repeat the same failed action without a correction. Stop sooner than 10 runs when continuing could create duplicates, lose information, change the wrong records, make recovery harder, or rely on a check that disagrees with a knowledgeable person's decision.

## Keep the evaluation useful

Add important new failures when they are found. Run the evaluation again after a meaningful change. If the result is difficult to verify, say that the process or its output should be changed so success is easier to see.

Read [references/hamel-husain-evaluation-practices.md](references/hamel-husain-evaluation-practices.md) when the user asks why this method is used or wants sources.

## Use this final structure

```text
[Clear process name] evaluation

Purpose
[What the process should accomplish.]

Evidence reviewed
[The real work, failures, rules, and expert decisions used. State missing evidence.]

What to check
1. [One question that can be answered Pass or Fail.]
2. [One question that can be answered Pass or Fail.]

What success looks like
[The exact successful result.]

When the work is done
[The definition of done.]

When to stop
[The immediate stop conditions.]

What to do after a failed run
[The correction rule and the limit of 10 complete runs.]

Final result
Result: Successful, Unsuccessful, or Needs review
Run number: [number out of 10]
Completed work: [plain-English summary]
Unfinished work: [plain-English summary]
Problems found: [plain-English summary]
First failed step: [plain-English description, or None]
Reason for stopping: [plain-English explanation]
```

## Find Automatable Workflows handoff

Read the clarified candidate and specification from the current conversation or the supplied [handoff format](../../references/handoff-format.md). Keep the selected goal, confirmed business rules, source evidence, existing coverage, and unanswered questions intact. Prefer a few observable final-outcome checks to a checklist for every implementation detail.

This plugin produces a proposed evaluation; it does not run the proposed automation. If no actual run evidence exists, label the result Needs review and say the process has not run. Do not count writing or reviewing this evaluation as an execution attempt. Distinguish missing evidence from an observed failure.

The ten-complete-run limit above belongs to this evaluation workflow. It is not a new retry limit for every proposed automation. The user defines that automation's operational stop and retry behavior; flag unresolved policy instead of inventing it.

Deliver the specification and its eight-section evaluation together. Subjective recommendation usefulness and business-rule judgments require user review. Reading complete fields or a successful tool response alone does not prove the business outcome.
