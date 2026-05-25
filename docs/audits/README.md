# Historical Audits

`docs/audits/` is historical-only for pre-institutional-memory audit artifacts and point-in-time audit outputs.

New canonical institutional-memory records belong in:

- `docs/swarms/` for Hermes swarm after-action reports.
- `docs/postmortems/` for implementation postmortems.
- `docs/forensics/` for unbounded raw logs that back canonical cards.

## Backfill Rules

- Do not delete historical audit files just because a canonical card now exists.
- When a historical audit contains forensic detail for a canonical card, copy or move that detail into `docs/forensics/<type>/` and link it from the canonical card's `forensic_log` frontmatter field.
- Keep the canonical card short, queryable, and evidence-linked.
- Do not hand-edit `docs/swarms/index.jsonl` or `docs/postmortems/index.jsonl`; regenerate them with `python3 scripts/regen_indexes.py`.
