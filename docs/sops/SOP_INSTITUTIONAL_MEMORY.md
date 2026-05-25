# SOP — Institutional Memory

## Purpose

This SOP defines how Lumen captures, stores, and retrieves the cognition behind every build.

It is the foundation of the project's institutional memory layer.

It governs two artifact types:

1. **Swarm After-Action Reports** — one per Hermes/Kanban swarm run.
2. **Implementation Postmortems** — one per technical failure, near-miss, or non-obvious fix.

Both feed a queryable index that survives contributor turnover, model upgrades, and project scaling.

---

## Core Principles

1. **Machine-first.** Every artifact starts with structured frontmatter so it can be indexed, queried, and graphed without re-reading the prose.
2. **Two-tier structure.** A short canonical card (≤200–250 lines) for retrieval + an optional unbounded forensic log for forensics.
3. **Capture the *why*, not just the *what*.** Decisions, tradeoffs, and intentional deferrals are the highest-value content. They decay the fastest if not written down.
4. **No empty sections.** If a section does not apply, omit it. Empty headers train writers to fill them with garbage.
5. **Evidence over assertion.** Every `pass`, every "compliance" claim must link to the file, command, or commit that proves it. The indexer rejects pass records without verification evidence.
6. **Intentional vs. forgotten — always distinguish.** Deferred work and forgotten work look identical six months later unless you label them now.
7. **Closed vocabularies.** Status, severity, failure_classes, and other enums are fixed. To add a new value, update this SOP first.

---

## When to Write What

| Situation                                       | Swarm AAR | Postmortem |
| ----------------------------------------------- | --------- | ---------- |
| Any multi-agent swarm run completes             | Yes       | If failures occurred |
| Verifier blocker required remediation           | (in AAR)  | Yes        |
| Schema, contract, or architecture drift found   | (link)    | Yes        |
| Embedded assumption proved false                | (link)    | Yes        |
| Near-miss exposed latent risk                   | (link)    | Yes        |
| Non-obvious fix whose reasoning will fade       | —         | Yes        |
| Trivial fix obvious from the diff               | —         | No         |
| Solo contributor commits without a swarm run    | —         | If failure |

If both apply, write both and cross-link them bidirectionally.

---

## File Layout

```
docs/
  sops/                                       # this folder — templates + SOPs
    SOP_INSTITUTIONAL_MEMORY.md               # this file
    IMPLEMENTATION_POSTMORTEM_TEMPLATE.md
    SWARM_AFTER_ACTION_REPORT_TEMPLATE.md
    CHANGELOG.md                              # template version history

  postmortems/                                # canonical postmortem cards
    README.md
    index.jsonl                               # auto-generated
    <YYYY-MM-DD>_<slug>.md                    # one per postmortem

  swarms/                                     # canonical swarm AARs
    README.md
    index.jsonl                               # auto-generated
    <YYYY-MM-DD>_<swarm-id>.md                # one per swarm

  forensics/                                  # unbounded raw logs
    postmortems/
      <YYYY-MM-DD>_<slug>.log.md
    swarms/
      <YYYY-MM-DD>_<swarm-id>.log.md

scripts/
  regen_indexes.py                            # rebuilds index.jsonl files
  new_report.py                               # scaffolds a new card from a template
```

---

## File Naming

- Postmortems: `docs/postmortems/<YYYY-MM-DD>_<short-slug>.md`
  - Example: `2026-05-24_api-contract-schema-drift.md`
- Swarm AARs: `docs/swarms/<YYYY-MM-DD>_<swarm-id>.md`
  - Example: `2026-05-24_lumen-v0-3-contract-demo.md`
- Forensic logs: same filename as the canonical card, with `.log.md` suffix, under `docs/forensics/<type>/`.

---

## Workflow

### For Hermes swarms (automatic)

After every swarm completes:

1. The synthesizer card invokes:
   ```bash
   python3 scripts/new_report.py --type swarm \
     --swarm-id <id> --board <board> --root-task <id> \
     --status <pass|partial|fail>
   ```
   This creates `docs/swarms/<date>_<swarm-id>.md` pre-populated with frontmatter.

2. The synthesizer fills in the narrative body using `SWARM_AFTER_ACTION_REPORT_TEMPLATE.md`.

3. Raw per-agent logs are written to `docs/forensics/swarms/<date>_<swarm-id>.log.md` and referenced from the canonical card under `forensic_log`.

4. If failures occurred, the synthesizer (or operator) also generates one or more postmortems:
   ```bash
   python3 scripts/new_report.py --type postmortem \
     --slug <short-slug> --severity <low|medium|high|critical>
   ```

5. Indexes are validated and regenerated:
   ```bash
   python3 scripts/regen_indexes.py --check --strict
   python3 scripts/regen_indexes.py
   ```

6. All new files are committed in the same commit as the code changes they describe.

### For human contributors

Same workflow, manually. Run `scripts/new_report.py` to scaffold, fill in body, run `scripts/regen_indexes.py` before commit.

---

## Hard Limits

| Artifact                     | Max lines | Enforced by      |
| ---------------------------- | --------- | ---------------- |
| Swarm AAR canonical card     | 250       | regen strict + reviewer |
| Postmortem canonical card    | 200       | regen strict + reviewer |
| Forensic logs                | unbounded | —                |
| Frontmatter enum values      | fixed     | regen script validates |

If a canonical card exceeds the ceiling, content moves to the forensic log. A rare exception requires both:

- `line_ceiling_exception: true`
- `line_ceiling_exception_reason: "<why this card cannot be split safely>"`

The reason must be substantive. Empty exception fields are invalid.

---

## Validation Gate

`scripts/regen_indexes.py` is the enforcement gate for canonical cards.

It rejects:

- malformed or missing frontmatter
- `schema_version` values other than `1`
- unknown enum values
- missing required fields
- placeholder body text such as `TBD`, `TODO`, `Fill in`, `<...>`, `[...]`, or scaffold comments
- empty required narrative sections
- `pass` swarm records without at least one verification command/check and result
- resolved postmortems without fix/prevention evidence
- invalid or missing `index_record` values
- invalid `forensic_log` paths when provided
- over-ceiling canonical cards without a valid exception reason

Validation always runs before writes. If validation fails, no index file is updated.

`--strict` is validation-only and never writes indexes. Use this CI-safe command:

```bash
python3 scripts/regen_indexes.py --check --strict
```

---

## Indexes

`docs/postmortems/index.jsonl` and `docs/swarms/index.jsonl` are the queryable retrieval layer.

Each line is one JSON record derived from a card's frontmatter. Example query:

```bash
# Every swarm that touched the audit_ledger module:
grep '"audit_ledger"' docs/swarms/index.jsonl | jq -r '.swarm_id'

# Every unresolved postmortem at high severity:
jq -c 'select(.status=="unresolved" and .severity=="high")' docs/postmortems/index.jsonl
```

Indexes are regenerated, never hand-edited. Validate first, then write:

```bash
python3 scripts/regen_indexes.py --check --strict
python3 scripts/regen_indexes.py
```

The script validates frontmatter, body requirements, evidence rules, forensic links, line ceilings, and closed enums. Malformed cards fail before index writes.

---

## Cross-Linking

Bidirectional references between swarms and postmortems are mandatory.

- Swarm AAR lists related postmortems under `related_postmortems`.
- Postmortem lists related swarms under `related_swarms`.

This is what turns a folder of documents into a navigable graph.

---

## Versioning

The templates themselves are versioned. `schema_version: 1` is the current schema.

Schema changes are recorded in `docs/sops/CHANGELOG.md`.

When the schema bumps, prior cards remain valid only after the SOP, templates, changelog, and regen script explicitly define how that schema version is validated.

---

## Constitutional Alignment

This SOP is the project's enforcement mechanism for several constitutional articles:

- **Article V (Transparency)** — all decisions and tradeoffs are publicly documented.
- **Article XX (Auditability)** — every meaningful transformation produces a traceable record.
- **Article XXI (Reproducibility)** — decisions and prevention mechanisms enable rebuilds.
- **Article XXII (Governance Changes)** — schema changes go through this SOP, not silently.
- **Article XXIV (Limitations)** — postmortems force honesty about what broke and why.

Institutional memory is not a productivity tool. It is a constitutional commitment.
