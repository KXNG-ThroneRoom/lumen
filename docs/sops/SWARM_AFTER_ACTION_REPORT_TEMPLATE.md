# Swarm After-Action Report Template

## Purpose

This template is for Hermes/Kanban swarm after-action reports.

Use this when documenting a multi-agent run involving:

- worker cards
- verifier card
- synthesizer card
- Kanban board execution
- multi-lane implementation or planning

This report is the canonical retrieval card for institutional memory.

It is not the full forensic log.

If a longer raw log exists, link it under `forensic_log`.

A single swarm may also produce one or more implementation postmortems.
This report captures the multi-agent execution context.
Postmortems capture technical causes and fixes.

---

## Reporting Rules

- Machine-first, human-readable second.
- Keep the canonical report under 250 lines.
- Do not include empty sections. Omit sections that do not apply.
- Do not add ceremonial filler.
- Do not claim success without verification evidence.
- Every `pass` status must link to the commands or transcripts that prove it.
- `status: pass` or `gate_status: pass` requires at least one verification command/check with a result.
- Separate what was completed from what was deferred.
- Distinguish "deferred intentionally" from "forgotten" — always.
- Record decisions, not just outputs.
- Record constitutional pressure points only when they were actually stressed, challenged, changed, or reaffirmed. Do not list "all articles passed."
- Link full logs instead of dumping raw logs into this report.
- Use only the listed enums for status, gate_status, and lane status.
- Placeholder text is invalid in canonical cards and will be rejected by `regen_indexes.py`.

---

## When to Write One

Write a swarm after-action report for every multi-agent swarm run, regardless of outcome.

If the swarm produced or revealed technical failures requiring root-cause analysis, also write an implementation postmortem and cross-link it under `related_postmortems`.

---

## File Naming

`docs/swarms/<YYYY-MM-DD>_<swarm-id>.md`

Example: `docs/swarms/2026-05-24_lumen-v0-3-contract-demo.md`

---

## Canonical Template

### Frontmatter (required)

```yaml
---
schema_version: 1
doc_type: swarm_after_action_report
project: Lumen
phase: ""
sprint: ""
date: ""
repo_path: ""
repo_commit_before: ""
repo_commit_after: ""
branch: ""
board: ""
tenant: ""
root_task: ""
verifier_task: ""
synthesizer_task: ""
status: pass | partial | fail
gate_status: pass | partial | fail
duration_hours: 0
files_changed_count: 0
tests_passed: 0
tests_failed: 0
blockers_resolved: 0
blockers_unresolved: 0
modules_touched:
  - ""
constitution_articles_engaged: []   # only articles actually stressed or reaffirmed this sprint
workers:
  - profile: ""
    task_id: ""
    lane: ""
    status: done | blocked | abandoned | replaced
    files_owned: []
    key_deliverable: ""             # one line
supersedes: ""
related_postmortems:
  - ""
related_swarms:
  - ""
tags:
  - ""
retrieval_keywords:
  - ""
related_docs:
  - ""
forensic_log: ""          # path under docs/forensics/swarms/ if a raw log exists
index_record: "docs/swarms/index.jsonl"
line_ceiling_exception: false
line_ceiling_exception_reason: ""
---
```

### Operational metadata (optional, separated from retrieval frontmatter)

These are Hermes-runtime fields. Useful for forensics, noise for retrieval.
Include only when relevant to reconstructing the run.

```yaml
operational:
  idempotency_key: ""
  write_authorized: true | false
  write_authorization_phrase_present: true | false
```

### Narrative body (required sections in this order)

```markdown
## Sprint goal
One sentence. What this swarm was supposed to accomplish.

## Outcome
One paragraph. What actually shipped vs. what was attempted.

## Decisions
For each significant decision made during the swarm:

### D<n>: <short name>
- Decision: what was chosen
- Reason: why
- Tradeoff: what was given up
- Reversibility: easy | moderate | hard
- Article reference: (if constitutional)
- Evidence: file path, commit, or task ID

This section is the highest-value content in the report.
Do not skip it. If no significant decisions were made, state that explicitly.

## Deferred intentionally
Bulleted list. Each item:
- what was deferred
- why
- when to revisit (or "indefinite")

Required if anything was cut from scope, even verbally.
Distinguishes intentional scope cuts from forgotten work.

## Blockers & resolutions
For each real blocker (something that stopped progress):

- Blocker: what
- Root cause: the underlying reason, not the surface failure
- Resolution: what fixed it
- Prevention: link to filed issue/PR/postmortem, or "none"

Omit this section entirely if no blockers occurred.

## Constitutional pressure points
Only list articles that were stressed, challenged, nearly violated, or reaffirmed under pressure this sprint.
Do NOT list "all articles passed."
Omit the section entirely if nothing was pressured.

## Verification evidence
Commands run, results, and links to transcripts or log lines.
Required for any `pass` status.

Example:
- `python3 -m pytest apps/api/tests -q` → 17 passed (link)
- `npm run verify:static --prefix apps/web` → pass (link)
- `npm run typecheck --prefix apps/web` → pass (link)
- forbidden legacy-name scan → clean (link)
- certainty-overclaim scan → clean (link)

## Risks carried forward
What is still fragile. Link to where each risk is tracked (issue, postmortem, next-sprint card).

## Next sprint recommendation
One paragraph. What logically follows from this swarm.
```

---

## Hard Limits

- Canonical report: 250 lines maximum.
- Agent-by-agent forensic detail: link via `forensic_log`, do not inline.
- Frontmatter fields: use the closed enums exactly. Do not invent values.
- Over-ceiling cards require `line_ceiling_exception: true` and a substantive `line_ceiling_exception_reason`.

---

## Index Regeneration

Every after-action report must register in `docs/swarms/index.jsonl`.

The index is regenerated automatically from frontmatter via `scripts/regen_indexes.py`.

Do not hand-edit the index.

If frontmatter changes, rerun the regeneration script:

```bash
python3 scripts/regen_indexes.py --check --strict
python3 scripts/regen_indexes.py
```

---

## Cross-Linking

If this swarm produced or revealed technical failures requiring root-cause analysis:

1. Write a separate implementation postmortem using `IMPLEMENTATION_POSTMORTEM_TEMPLATE.md`.
2. Cross-link it here under `related_postmortems`.
3. Cross-link this report from the postmortem under `related_swarms`.

Bidirectional linking is required. It is what turns isolated documents into a retrievable graph.
