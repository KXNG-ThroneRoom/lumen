# scripts/

Project tooling for institutional memory and build hygiene.

## Institutional memory

| Script              | Purpose                                                         |
| ------------------- | --------------------------------------------------------------- |
| `regen_indexes.py`  | Validate canonical memory cards and rebuild `docs/postmortems/index.jsonl` and `docs/swarms/index.jsonl` from valid frontmatter. |
| `new_report.py`     | Scaffold a new postmortem or swarm AAR with pre-populated frontmatter. |

### Typical workflow

```bash
# 1. Scaffold a new swarm after-action report.
python3 scripts/new_report.py --type swarm \
  --swarm-id lumen-v0-4-ingestion --board lumen-build-server \
  --root-task t_abc123 --status pass

# 2. Fill in the narrative body using docs/sops/SWARM_AFTER_ACTION_REPORT_TEMPLATE.md.

# 3. Regenerate indexes before committing.
python3 scripts/regen_indexes.py

# 4. Validate without writing (useful in CI / pre-commit).
python3 scripts/regen_indexes.py --check --strict
```

`--strict` is validation-only and never writes index files. `--check` compares
the regenerated output with the checked-in indexes and exits 2 if they differ.
The default `python3 scripts/regen_indexes.py` path validates first and aborts
without writing if any card is invalid.

### Postmortem workflow

```bash
python3 scripts/new_report.py --type postmortem \
  --slug api-contract-schema-drift --severity high
# fill in body
python3 scripts/regen_indexes.py
```

## Hermes integration

Hermes synthesizer cards should invoke `new_report.py` at the end of every
swarm run, fill in the body, then call `regen_indexes.py`.

See `docs/sops/SOP_INSTITUTIONAL_MEMORY.md` for the full workflow.

## Conventions

- All scripts are Python 3, no external dependencies (uses only the stdlib).
- Scripts must be runnable from the repo root: `python3 scripts/<name>.py`.
- New scripts should follow the same zero-dep, stdlib-only convention.
