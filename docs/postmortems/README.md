# Postmortems

Canonical implementation postmortems live here.

One file per postmortem: `YYYY-MM-DD_short-slug.md`

## Rules

- Use the template: `docs/sops/IMPLEMENTATION_POSTMORTEM_TEMPLATE.md`
- Governed by: `docs/sops/SOP_INSTITUTIONAL_MEMORY.md`
- Hard ceiling: 200 lines per card. Raw logs go in `docs/forensics/postmortems/`.
- Cards are indexed automatically into `index.jsonl` by `scripts/regen_indexes.py`.

## Create a new postmortem

```bash
python3 scripts/new_report.py --type postmortem --slug api-contract-schema-drift --severity high
```

## Regenerate the index after editing

```bash
python3 scripts/regen_indexes.py
```

## Query the index

```bash
# Unresolved high-severity postmortems:
jq -c 'select(.status=="unresolved" and .severity=="high")' index.jsonl

# All postmortems touching a specific module:
grep '"audit_ledger"' index.jsonl
```

## Do not

- Hand-edit `index.jsonl`. It is rebuilt from frontmatter on every regen.
- Write empty sections. Omit sections that do not apply.
- Dump raw logs into the canonical card. Link them via `forensic_log`.
