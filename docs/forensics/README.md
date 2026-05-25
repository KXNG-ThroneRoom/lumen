# Forensics

Raw, unbounded logs that back the canonical cards in `docs/postmortems/` and `docs/swarms/`.

## Layout

```
forensics/
  postmortems/<YYYY-MM-DD>_<slug>.log.md
  swarms/<YYYY-MM-DD>_<swarm-id>.log.md
```

## Purpose

Canonical cards are capped at 200–250 lines for retrieval.
Forensic logs are unbounded for reconstruction.

Most readers will never open these files. When something breaks six months later, they are invaluable.

## What belongs here

- Per-agent execution traces
- Verbatim verifier output
- Full command transcripts
- Raw tool outputs
- Step-by-step remediation logs
- Diff dumps
- Any narrative detail that exceeds the canonical card ceiling

## What does not belong here

- Decisions and tradeoffs (those go in the canonical card under `## Decisions`)
- Root cause analysis (canonical card under `## Root cause` / `## Causal chain`)
- Prevention mechanisms (canonical card under `## Prevention`)

The canonical card is the *interpretation*. The forensic log is the *raw evidence*.

## Linking

Every forensic log is referenced from its canonical card's `forensic_log` frontmatter field.

If a canonical card exists without a forensic log, that field is empty — that is fine.

## Not indexed

Forensic logs are intentionally excluded from `index.jsonl`. They are read only when a canonical card points to them.
