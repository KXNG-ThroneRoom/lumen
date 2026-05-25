# Implementation Postmortem Template

## Purpose

This template is for technical implementation postmortems.

Use this when documenting:

- bugs
- failed assumptions
- schema drift
- architecture drift
- integration failures
- verifier failures
- test failures
- production-risk discoveries
- implementation tradeoffs
- remediation work

This document is the technical cognition memory of the project.

It answers:

```text
What broke?
Why did it break?
What did we change?
What did we learn?
How do we prevent recurrence?
```

It is separate from the swarm after-action report.

A single incident may produce both a postmortem and an after-action report.
The postmortem captures the technical cause and fix.
The after-action report captures the multi-agent execution context.

---

## Reporting Rules

- Machine-first, human-readable second.
- Do not write empty sections. Omit sections that do not apply.
- Do not add blame.
- Do not bury root cause.
- Distinguish symptoms from causes.
- Distinguish bugs from intentional deferrals.
- Record prevention mechanisms, not just fixes.
- Record prevention status (none | proposed | filed | implemented | verified).
- Link to commits, tests, task IDs, and affected files where possible.
- If no code changed, say so explicitly.
- If root cause is unknown, say "unknown" and explain why investigation stopped.
- Keep the canonical postmortem under 200 lines. Link raw logs separately.
- Use only the failure_classes listed below. To add a new class, update the SOP first.
- Resolved postmortems require fix/prevention evidence and `prevention_status` other than `none`.
- Placeholder text is invalid in canonical cards and will be rejected by `regen_indexes.py`.

---

## When to Write One

Write an implementation postmortem when any of the following occur:

- a verifier or test failure required remediation
- schema, contract, or architecture drift was discovered
- an assumption embedded in code or docs turned out to be false
- a near-miss exposed a latent risk worth recording
- a fix was applied whose reasoning would not be obvious six months later

Do NOT write one for trivial fixes whose cause and prevention are self-evident from the diff.

---

## File Naming

`docs/postmortems/<YYYY-MM-DD>_<short-slug>.md`

Example: `docs/postmortems/2026-05-24_api-contract-schema-drift.md`

---

## Canonical Template

### Frontmatter (required)

```yaml
---
schema_version: 1
doc_type: implementation_postmortem
project: Lumen
phase: ""
sprint: ""
date: ""
detected_at: ""           # when the issue was noticed
introduced_at: ""         # best estimate of when it entered the codebase, or "unknown"
resolved_at: ""
detection_method: human_review | verifier | test | user_report | grep | runtime | other
repo_path: ""
repo_commit_before: ""
repo_commit_after: ""
branch: ""
status: resolved | partially_resolved | unresolved
severity: low | medium | high | critical
prevention_status: none | proposed | filed | implemented | verified
failure_classes:          # closed enum — use only these values
  - schema_drift
  - test_failure
  - orchestration_failure
  - integration_failure
  - architecture_drift
  - governance_risk
  - documentation_gap
  - dependency_issue
affected_modules:
  - ""
affected_files:
  - ""
related_tasks:
  - ""
related_swarms:
  - ""
related_postmortems:
  - ""
constitution_articles_at_risk: []   # optional, only when the incident threatened a constitutional invariant
supersedes: ""            # prior postmortem this replaces or extends
tags:
  - ""
retrieval_keywords:
  - ""
related_docs:
  - ""
forensic_log: ""          # path under docs/forensics/postmortems/ if a raw log exists
index_record: "docs/postmortems/index.jsonl"
line_ceiling_exception: false
line_ceiling_exception_reason: ""
---
```

### Narrative body (required sections in this order)

```markdown
## Summary
One paragraph. What broke and what it cost.

## Symptom
What was observed. Surface-level only — what a human or test saw.
Not what caused it.

## Root cause
The underlying reason, not the surface failure.
If unknown, say "unknown" and explain why the investigation stopped.

## Causal chain
Symptom → intermediate cause → root cause.
As many steps as needed, no more.
Each step should be a single line.

## Fix
What was changed. Link commits, PRs, or specific file paths and line ranges.
If no code changed (e.g., documentation-only or config-only), state that explicitly.

## Prevention
What change makes recurrence harder or impossible.
State the prevention status (proposed | filed | implemented | verified).
If status is "none," explain why no prevention is feasible.
If the postmortem status is "resolved," link the prevention evidence or rationale.

## What we learned
One or two sentences.
The transferable lesson, not the specific bug.
Should be useful to a future contributor who has never seen this incident.

## Open questions
What we still do not know.
Required if root cause is "unknown" or prevention status is "none."
Omit if neither applies.
```

---

## Hard Limits

- Canonical postmortem: 200 lines maximum.
- Raw logs, transcripts, and forensic detail: link via `forensic_log`, do not inline.
- Frontmatter fields: use the closed enums exactly. Do not invent values.
- Over-ceiling cards require `line_ceiling_exception: true` and a substantive `line_ceiling_exception_reason`.

---

## Index Regeneration

Every postmortem must register in `docs/postmortems/index.jsonl`.

The index is regenerated automatically from frontmatter via `scripts/regen_indexes.py`.

Do not hand-edit the index.

If frontmatter changes, rerun the regeneration script:

```bash
python3 scripts/regen_indexes.py --check --strict
python3 scripts/regen_indexes.py
```
