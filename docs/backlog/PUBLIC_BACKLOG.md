# Lumen Public Backlog

Purpose: capture public-facing follow-up work without expanding the v0.6 controlled manual/local input layer. Items here are deferred until separately scoped, implemented, and verified. Nothing in this backlog is a current launch promise.

## Current boundary

v0.6 remains a controlled local/manual demo around one contested claim story: "When does the regulation start?" The public UI is the Story / Evidence / Why uncertain / Audit tabbed view. Manual input is an assertion container, not truth; articles and submitted text are containers of claims, not facts. Lumen does not determine truth, ingest live events, fetch URLs, crawl, poll RSS, call paid APIs or LLMs, collect telemetry, require secrets, create accounts, persist production data, or provide production intelligence reliability.

## Ingestion

- Add a local file-ingestion fixture path that preserves originals as immutable evidence.
  - Why: broaden demo inputs without live crawling or network dependency.
  - Gate: original text preserved, transformation audit events emitted, no source mutation.
- Keep the current manual/local text input path explicitly labeled as an assertion container.
  - Why: user-supplied text proves only that a claim was supplied, not that the claim is true.
  - Gate: `/analyze` returns local-input provenance, visible limitations, audit references, and no external retrieval claims.
- Define a future URL-ingestion threat model before any URL fetching is implemented.
  - Why: live fetching introduces provenance, freshness, safety, and privacy risks.
  - Gate: governance approval, network boundary tests, clear limitation language.
- Add fixture packs for non-breaking edge cases such as ambiguous dates, nested claims, translations, and stale source timestamps.
  - Why: improve eval coverage while staying controlled and deterministic.
  - Gate: fixture provenance documented and no claim of global coverage.

## Source graph

- Model source-dependency uncertainty for copied, syndicated, circular, and common-origin reporting.
  - Why: repeated claims should not be counted as independent support by default.
  - Gate: visible dependency caveats and capped confidence when independence is unclear.
- Add explainable source-role labels for official filing, news report, commentary, and unknown origin.
  - Why: users need to see why one source changes method confidence differently from another.
  - Gate: labels have documented rules and no hidden weighting.
- Create source-graph golden cases for anonymous-source laundering and circular citation.
  - Why: prevent false confidence from source repetition.
  - Gate: golden cases include expected caps and limitation notes.

## Contradiction

- Expand contradiction fixtures beyond date disagreement to amount, attribution, location, and scope conflicts.
  - Why: test the contested-state method across common claim shapes.
  - Gate: outputs preserve uncertainty and avoid final verdict language.
- Add deterministic contradiction-reason codes with human-readable explanations.
  - Why: make contested outputs auditable without exposing machine labels in the public UI.
  - Gate: public copy stays plain-language; internal codes remain inspectable in API/evals.
- Add regression tests for unsupported, unresolved, contradicted, and contested states.
  - Why: keep non-answer states valid and visible.
  - Gate: tests assert no state is coerced into true/false.

## Narrative

- Build a fixture-backed narrative-map explainer that shows how a claim travels between sources.
  - Why: teach users to inspect spread without claiming intent or propaganda detection.
  - Gate: no inference of motive, coordination, or deception without evidence.
- Add copy-review rules for public announcement language.
  - Why: launch copy can overstate capability even when product code is bounded.
  - Gate: reviewed against `docs/checklists/PUBLIC_ANNOUNCEMENT_CHECKLIST.md`.
- Add challenge examples showing how a user can dispute evidence, limitations, or wording.
  - Why: make adversarial review usable by non-maintainers.
  - Gate: examples point to `ADVERSARIAL_REVIEW.md` and avoid live-case claims.

## Evals

- Add golden cases for simplified UI expectations, manual/local input containment, and public-copy boundaries.
  - Why: prevent stale dense-dashboard language from returning as the launch surface and prevent manual input from being mistaken for truth.
  - Gate: static verifier and docs scans catch public UI drift; API contract tests assert local-input provenance and limitations.
- Add no-secret/no-network evals for the default local demo path.
  - Why: auditability is a release blocker and external dependency creep is easy to miss.
  - Gate: tests fail on credential requirements, telemetry, paid API calls, or hidden network calls.
- Track fixture coverage by claim type and limitation type.
  - Why: expose what the eval suite covers and what it does not.
  - Gate: coverage report says "fixture coverage," not real-world verification coverage.

## UX

- Preserve the simplified black/white tabbed public demo until a separate UX scope is approved.
  - Why: launch clarity matters more than analytical surface area for v0.5.
  - Gate: public page still uses Story, Evidence, Why uncertain, and Audit tabs.
- Add optional disclosure affordances for method detail without making the main view dense.
  - Why: experts need audit detail, but public launch users need plain language first.
  - Gate: no raw hashes, audit IDs, `.md` references, underscores, or provenance strings in the main public view.
- Test color/tone accessibility for contested, support, and conflict states.
  - Why: yellow/blue/red should not be the only carrier of meaning.
  - Gate: text labels remain visible and screen-reader friendly.

## Infrastructure

- Add a dedicated launch-hygiene scan command if `scripts/verify_lumen.sh` becomes too broad.
  - Why: separate release-copy checks from normal developer tests when needed.
  - Gate: both commands are documented and deterministic.
- Add CI wiring for the aggregate verifier once dependency installation is stable.
  - Why: local-only gates can drift if not run consistently.
  - Gate: CI does not require secrets, paid services, telemetry, or live network calls beyond dependency install.
- Add generated-artifact cleanup guidance.
  - Why: avoid accidental deletion of evidence, fixtures, `.venv`, or `node_modules`.
  - Gate: cleanup candidates are reviewed before removal.

## Governance

- Define the approval process for any future live ingestion or external model dependency.
  - Why: those changes alter the trust model and public claim surface.
  - Gate: governance doc update, threat model, tests, and public limitation update land together.
- Add a public claim-language review checklist to every release packet.
  - Why: no fake capability claims, final verdict wording, or hidden scoring claims should pass review.
  - Gate: release packet links exact scan commands and reviewer outcome.
- Maintain institutional-memory AARs for launch swarms and postmortems only for real failures, near-misses, or non-obvious fixes.
  - Why: memory should preserve decisions and risks, not create ceremonial artifacts.
  - Gate: `python3 scripts/regen_indexes.py --check --strict` passes.
