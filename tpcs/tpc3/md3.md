# Support Playbook
This playbook is for support engineers handling tickets for the Report Generator.
It emphasizes *repeatable triage* and **clear communication**.
Inline tags like #support, ref#17, and issue#301 are normal text, not headers.

## Philosophy
Support is a product surface.
We optimize for *speed with accuracy* and **calm escalation**.

- Assume good intent and ask clarifying questions *once*
- Keep notes **structured** and time-stamped
- Avoid copy-paste noise; write the *signal*
- Escalate early when impact is **broad**

# Common Requests
These are the requests we see most often.
Literal asterisks appear in examples like 6*7=42, *.txt, and backup*2026.

## Exports and Formatting
Users commonly report issues with exports.

- “My export is empty” after applying filters
- “The PDF looks different than the preview”
- “The filename contains weird characters”
- “The HTML export is missing **sections** or *emphasis*”

## Performance Questions
Performance complaints can be vague; use a consistent checklist.

1. Ask for dataset size and time range
2. Confirm the user’s version and environment
3. Determine whether the slowdown is *new* or chronic
4. Check if the issue reproduces with **defaults**
5. Collect a minimal reproduction

# First Response Checklist
The first reply should reduce uncertainty for the customer and for us.

1. Restate the issue in one sentence
2. Ask for steps to reproduce, in *plain language*
3. Request logs only if needed, and explain **why**
4. Set expectations for next updates and timelines
5. Confirm priority based on impact

## What Is Not a List
References like version 2.0.1, section 4.2, and item 3.1 may appear in text.
They are not list markers unless they start a line with "1. " and a space.
Also, 1.ThisHasNoSpace should remain literal.

# Troubleshooting Guide
Use these steps in order.
Skip ahead only if you can explain *why*.

## Data and Permissions
Many failures are permissions or data source issues.

- Verify the user has access to the dataset
- Confirm the data source connection is reachable
- Check for recent permission changes and **revocations**
- Ask whether the report template was recently edited

## Templates and Layout
Layout issues usually trace back to template configuration.

1. Ask which template is used
2. Confirm whether the issue affects *all* exports
3. Check if the template contains **required** fields
4. Verify the export settings match the intended output
5. Ask for a screenshot if needed

# Escalation Criteria
Escalate when the issue exceeds routine handling.

1. The issue affects multiple customers or a critical workflow
2. There is evidence of data loss or incorrect calculations
3. Recovery requires changes outside standard procedures
4. The issue persists beyond the *acceptable* window
5. The customer provides logs indicating **system instability**

## Recommended Language
How you write matters.

- Use *empathetic* phrasing and avoid blame
- Summarize the plan with **clear next steps**
- Confirm understanding before closing the ticket
- Include a short recap and *expected* timeline

# Follow-up and Closure
Closing a ticket should increase trust.

1. Document the resolution and any workaround
2. Link internal references like issue#888 and #postmortem
3. Add a brief knowledge base note with **key learnings**
4. Confirm the customer is unblocked
5. Close the loop with a final summary that is *actionable*

- Final reminder: tokens like end*of*word and pre*post are not emphasis
- Final reminder: inline #tags are not headers