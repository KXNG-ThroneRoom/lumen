# Lumen Limitations

Version: v0.5.2-public-framing

## Summary

Lumen is an inspection tool for claims, evidence, uncertainty, provenance, and audit trails. It does not decide what users must believe.

The current MVP release packet is local, deterministic, fixture-backed, and limited. It should be read as a methods demonstration, not a production intelligence system or live claim-verification service.

Related public references:

- Demo flow and required visible disclosures: `docs/architecture/DEMO_FLOW.md`.
- API response limitation fields: `docs/architecture/API_CONTRACT.md`.
- Governance rules for limitation placement: `docs/governance/GOVERNANCE_RULES.md`.
- Public challenge path: `ADVERSARIAL_REVIEW.md`.

## Current MVP Limits

- No real-time ingestion.
- No paid APIs.
- No LLM calls.
- No production-scale retrieval.
- No global source coverage.
- No user accounts.
- No telemetry.
- No blockchain anchoring.
- No claim of complete real-world verification.
- Controlled fixture data may not represent live information complexity.
- The current public UI demonstrates one simplified claim story, not a broad analytical product surface.
- Legacy/internal components may exist in the repository but are not current public demo promises.

## Demo Flow Disclosure Requirements

Every local demo flow, API sample response, and public UI path must display or link this limitations reference close to the output it qualifies.

Demo documentation, README/run instructions, screenshots, and public walkthroughs must link this file when showing analytical output. A polished interface without visible uncertainty, limitations, and audit references is not demo-ready.

Required demo disclosures:

- The response is controlled fixture output unless explicitly labeled otherwise.
- The demo does not ingest live events, paid sources, or external network data.
- Confidence bands describe the documented method-state of available inputs; they are not reality verdicts.
- The current public demo is a simplified tabbed claim story: Story, Evidence, Why uncertain, and Audit.
- Old multi-panel interface language must not be presented as the current public UI.
- Audit references explain how the displayed output was produced; they do not prove the underlying claim.

## Analytical Limits

Lumen may fail or underperform when:

- source coverage is incomplete;
- primary evidence is missing;
- source metadata is unavailable;
- claims are ambiguous or nested;
- translation is required;
- images/video lack provenance;
- timestamps are unclear;
- adversaries seed coordinated narratives;
- sources cite each other circularly;
- anonymous claims are laundered through multiple outlets;
- events evolve after sample data is created;
- evidence is forged, selective, or taken out of context.

## Confidence Limits

Confidence bands are method explanations, not commands to believe.

A high confidence band means the documented rules found stronger support in available inputs. It does not eliminate uncertainty.

A low or unknown band does not prove a claim is false. It means Lumen lacks adequate support under its documented rules.

## Source-Independence Limits

MVP source-dependency detection is limited. It may miss shared ownership, undisclosed funding, copied reporting, syndicated material, or common anonymous origin.

When independence is unclear, Lumen should disclose uncertainty rather than inflate confidence.

## Audit Limits

MVP audit logs are tamper-evident, not tamper-proof.

Hash-chain verification can detect inconsistent modification but cannot prevent deletion, replacement, or full-regeneration by an attacker with filesystem access.

## User Responsibility

Users should inspect sources, limitations, uncertainty notes, audit references, and confidence reasons. Lumen is designed to support judgment, not replace it.

Users may challenge limitation disclosure, confidence reasons, audit completeness, or interface wording through the process in `ADVERSARIAL_REVIEW.md`.
