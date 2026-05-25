# Swarm After-Action Reports

Canonical Hermes/Kanban swarm after-action reports live here.

One file per swarm run: `YYYY-MM-DD_swarm-id.md`

## Rules

- Use the template: `docs/sops/SWARM_AFTER_ACTION_REPORT_TEMPLATE.md`
- Governed by: `docs/sops/SOP_INSTITUTIONAL_MEMORY.md`
- Hard ceiling: 250 lines per card. Raw logs go in `docs/forensics/swarms/`.
- Cards are indexed automatically into `index.jsonl` by `scripts/regen_indexes.py`.
- Every swarm produces one report, regardless of outcome (pass | partial | fail).

## Create a new report

```bash
python3 scripts/new_report.py --type swarm \
  --swarm-id lumen-v0-4-ingestion --board lumen-build-server --root-task t_abc123 \
  --status partial
```

## Regenerate the index after editing

```bash
python3 scripts/regen_indexes.py
```

## Query the index

```bash
# All failed swarms in phase v0.3:
jq -c 'select(.status=="fail" and .phase=="v0.3")' index.jsonl

# Every swarm that engaged constitutional Article XXV:
grep '"XXV"' index.jsonl
```

## Historical artifacts

Pre-SOP swarm summaries (prior to 2026-05-24) live under `docs/audits/` as
historical reference. They predate the canonical card schema and are not
indexed.

## Do not

- Hand-edit `index.jsonl`.
- Dump per-agent forensic detail into the canonical card. Link via `forensic_log`.
- Claim a `pass` status without `verification_evidence` linking to commands or transcripts.
