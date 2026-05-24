# Lumen Confidence Scoring Methodology

Version: v0.2-local-deterministic

## Purpose

Confidence scoring in Lumen is an explanation mechanism, not a verdict mechanism. It helps users understand why the system assigned a method-state to a claim.

Lumen does not determine what users must believe. It exposes the rule path, evidence quality, uncertainty, and provenance behind a confidence band.

## Required Fields

Every scored claim must include:

- status;
- confidence_band;
- confidence_reason;
- applied_rules;
- evidence_refs;
- source_refs;
- limitation_refs;
- audit_ref.

A claim missing status or confidence_reason is invalid for display.

## Confidence Bands

- high: strong primary or near-primary evidence, strong provenance, independent corroboration, and no material unresolved contradiction.
- medium: meaningful support exists, but some dependency, indirectness, provenance gap, or missing context remains.
- low: weak, indirect, dependent, anonymous, stale, or incomplete evidence dominates.
- capped: a governance cap prevents elevation.
- unknown: confidence cannot be assigned honestly from available inputs.

## Deterministic MVP Rule Order

MVP scoring applies rules in this order:

1. Start at unknown.
2. If no inspectable evidence exists, set unsupported or unresolved with low/unknown confidence.
3. If the item is framing, speculation, or interpretation, set narrative_only unless a factual subclaim is extracted separately.
4. Add support for primary or near-primary evidence with adequate provenance.
5. Add support for independent evidence streams.
6. Reduce or cap confidence for anonymous sourcing.
7. Reduce or cap confidence for wire/citation/source dependency.
8. Reduce or cap confidence for material contradiction.
9. Reduce confidence for missing timestamp, missing origin, stale source, or unclear chain of custody.
10. Emit visible reasons and audit references.

## Anonymous-Source Caps

Default cap rules:

| Source condition | Maximum band without stronger evidence | Required reason |
| --- | --- | --- |
| Unsupported anonymous assertion | low | Anonymous assertion has no inspectable support. |
| Anonymous official / unnamed institutional source | low | Identity and incentives cannot be independently inspected. |
| Anonymous eyewitness | low | Witness cannot be independently assessed. |
| Anonymous expert interpretation | low or narrative_only | Expert basis is not inspectable. |
| Leaked document with weak provenance | capped | Document chain of custody is uncertain. |

Independent primary evidence can raise confidence above the cap, but the reason must explain why.

## Source-Independence Effects

Independent evidence streams can raise confidence. Dependent repetition cannot.

Dependency indicators include:

- same wire origin;
- citation loop;
- repeated language;
- common press release;
- same anonymous briefing;
- unclear origin;
- shared ownership/funding materially relevant to the claim.

When dependency exists, confidence_reason must say that article count was not treated as independent support.

## Primary Evidence Effects

Primary evidence may increase confidence when it is relevant and has adequate provenance.

Primary evidence is not automatically decisive. It can be incomplete, forged, selectively edited, stale, miscaptioned, mistranslated, or context-dependent.

Scoring must distinguish:

- evidence existence;
- evidence authenticity;
- evidence relevance;
- evidence completeness;
- evidence chain of custody.

## Contradiction Effects

Material contradictions usually produce contested or capped status.

Contradiction reasons must identify:

- the conflict type;
- the conflicting source or evidence;
- whether the conflict is direct or indirect;
- why uncertainty remains.

## Unknown / Unresolved Handling

Unknown and unresolved are not failures. They are honest outputs when evidence is inadequate.

Use unknown when the system cannot classify.
Use unresolved when a claim is clear but evidence is insufficient or incomplete.
Use contested when competing evidence or claims materially conflict.

## Anti-Bias Requirements

Confidence must never use hidden ideology, partisan identity, popularity, institution type, or source prestige as a substitute for evidence.

Official, mainstream, alternative, anonymous, activist, corporate, government, and independent sources all remain claim sources requiring context.

## Audit Coupling

Every score assignment must produce or reference an audit event containing:

- rule_version;
- input_hash;
- output_hash;
- applied_rules;
- confidence_reason;
- limitations;
- previous_event_hash;
- event_hash.
