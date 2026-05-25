# SOP & Template Changelog

All changes to institutional-memory templates and SOPs are recorded here.

The current schema version is reflected in each template's `schema_version` frontmatter field.

When the schema bumps, prior cards remain valid at their original schema version.
The regen script handles multiple schema versions in parallel.

---

## schema_version: 1 — 2026-05-24

Initial release.

### Enforcement hardening — 2026-05-25

- `scripts/regen_indexes.py` now validates before writes and refuses to update indexes when any canonical card is invalid.
- `--strict` is validation-only and non-mutating.
- Placeholder/scaffold body text is rejected for canonical cards.
- `pass` swarm status now requires verification evidence with at least one command/check and result.
- Resolved postmortems now require fix/prevention evidence and `prevention_status` other than `none`.
- Canonical line ceilings are enforced, with explicit exception fields for rare justified cases.
- `forensic_log` paths are validated when present.
- `decision.reversibility` values are validated when decisions are present.

### Templates introduced

- `IMPLEMENTATION_POSTMORTEM_TEMPLATE.md`
- `SWARM_AFTER_ACTION_REPORT_TEMPLATE.md`

### SOP introduced

- `SOP_INSTITUTIONAL_MEMORY.md` — governing doc for both artifact types.

### Tooling introduced

- `scripts/regen_indexes.py` — rebuilds `docs/postmortems/index.jsonl` and `docs/swarms/index.jsonl`.
- `scripts/new_report.py` — scaffolds a new card with pre-populated frontmatter.

### Folder structure introduced

- `docs/sops/` — templates and governing SOPs.
- `docs/postmortems/` — canonical postmortem cards + index.
- `docs/swarms/` — canonical swarm AAR cards + index.
- `docs/forensics/postmortems/` and `docs/forensics/swarms/` — unbounded raw logs.

### Closed enums established

- `failure_classes`: schema_drift, test_failure, orchestration_failure, integration_failure, architecture_drift, governance_risk, documentation_gap, dependency_issue
- `status` (postmortem): resolved, partially_resolved, unresolved
- `status` (swarm): pass, partial, fail
- `severity`: low, medium, high, critical
- `prevention_status`: none, proposed, filed, implemented, verified
- `detection_method`: human_review, verifier, test, user_report, grep, runtime, other
- `worker.status`: done, blocked, abandoned, replaced
- `decision.reversibility`: easy, moderate, hard
