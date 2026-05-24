import auditFixture from '../../../../examples/sample_audit_trail.json';
import briefingFixture from '../../../../examples/sample_briefing.json';
import claimMatrixFixture from '../../../../examples/sample_claim_matrix.json';

export type ClaimStatus = 'plausible' | 'contested' | 'unknown' | 'unsupported' | 'unresolved';
export type ConfidenceBand = 'low' | 'limited' | 'guarded' | 'moderate';

export type EvidenceItem = {
  id: string;
  label: string;
  sourceType: string;
  provenance: string;
  independence: string;
  quality: 'primary' | 'direct' | 'secondary' | 'anonymous' | 'missing' | 'interested';
  quote: string;
};

export type Claim = {
  id: string;
  text: string;
  type: string;
  status: ClaimStatus;
  confidence: ConfidenceBand;
  confidenceLogic: string[];
  supports: string[];
  contradicts: string[];
  unresolved: string;
};

export type NarrativeFrame = {
  role: string;
  observedFrame: string;
  evidence: string;
  caution: string;
};

export type Contradiction = {
  id: string;
  conflict: string;
  claims: string[];
  evidenceGap: string;
  status: 'unresolved' | 'contested';
};

export type AuditEvent = {
  id: string;
  operation: string;
  actor: string;
  inputHash: string;
  outputHash: string;
  previousHash: string;
  ruleVersion: string;
  note: string;
};

type RawEvidence = (typeof claimMatrixFixture.evidence)[number];
type RawClaim = (typeof claimMatrixFixture.claims)[number];

function evidenceQuality(item: RawEvidence): EvidenceItem['quality'] {
  if ('missing' in item && item.missing && item.missing.length > 0) return 'missing';
  if (item.type.includes('anonymous')) return 'anonymous';
  if (item.proximity.includes('primary_interested') || item.type.includes('interested')) return 'interested';
  if (item.proximity.includes('secondary')) return 'secondary';
  return 'direct';
}

function statusFromFixture(status: RawClaim['status']): ClaimStatus {
  if (status === 'plausible' || status === 'contested' || status === 'unsupported' || status === 'unresolved') return status;
  return 'unknown';
}

function confidenceFromFixture(label: string): ConfidenceBand {
  if (label === 'moderate' || label === 'limited' || label === 'low' || label === 'guarded') return label;
  return 'guarded';
}

export const briefing = {
  topic: briefingFixture.topic,
  bottomLine: `${briefingFixture.bottom_line} Fixture notice: ${briefingFixture.fixture_notice}`,
  confidence: `${briefingFixture.confidence.label} (${briefingFixture.confidence.explanation})`,
  watchIndicators: briefingFixture.watch_indicators,
  unresolvedQuestions: briefingFixture.unresolved_questions,
};

export const evidence: EvidenceItem[] = claimMatrixFixture.evidence.map((item) => ({
  id: item.id,
  label: `${item.source} / ${item.type}`,
  sourceType: item.type,
  provenance: item.proximity,
  independence: item.proximity.includes('secondary')
    ? 'Requires source graph review before treating as independent.'
    : 'Single visible fixture source; independence is not assumed beyond the sample record.',
  quality: evidenceQuality(item),
  quote: 'Sample evidence reference from canonical example JSON; inspect source, proximity, and missing fields before raising confidence.',
}));

export const claims: Claim[] = claimMatrixFixture.claims.map((claim) => ({
  id: claim.id,
  text: claim.normalized_claim,
  type: claim.claim_type,
  status: statusFromFixture(claim.status),
  confidence: confidenceFromFixture(claim.confidence_label),
  confidenceLogic: claim.confidence_reasons,
  supports: claim.evidence_refs,
  contradicts: claim.contradiction_refs,
  unresolved: claim.uncertainty.length > 0 ? claim.uncertainty.join('; ') : 'No explicit uncertainty recorded in fixture.',
}));

const narrative = claimMatrixFixture.narrative_map;
export const narrativeFrames: NarrativeFrame[] = [
  {
    role: 'Hero',
    observedFrame: narrative.hero.length ? narrative.hero.join(', ') : 'No explicit hero frame recorded.',
    evidence: 'Derived from canonical sample claim matrix narrative_map.hero.',
    caution: narrative.analysis_label,
  },
  {
    role: 'Victim',
    observedFrame: narrative.victim.length ? narrative.victim.join(', ') : 'No explicit victim frame recorded.',
    evidence: 'Derived from canonical sample claim matrix narrative_map.victim.',
    caution: narrative.analysis_label,
  },
  {
    role: 'Threat',
    observedFrame: narrative.threat.length ? narrative.threat.join(', ') : 'No explicit threat frame recorded.',
    evidence: 'Derived from canonical sample claim matrix narrative_map.threat.',
    caution: narrative.analysis_label,
  },
  {
    role: 'Omitted context',
    observedFrame: narrative.omitted_context.join(', '),
    evidence: 'Missing context remains visible rather than filled by assumption.',
    caution: narrative.analysis_label,
  },
];

export const contradictions: Contradiction[] = briefingFixture.contradictions.map((item, index) => ({
  id: `CON-${String(index + 1).padStart(3, '0')}`,
  conflict: item.note,
  claims: item.claims,
  evidenceGap: `${item.type}; inspect missing information: ${briefingFixture.missing_information.join(', ')}`,
  status: 'unresolved',
}));

export const auditTrail: AuditEvent[] = auditFixture.events.map((event) => ({
  id: event.event_id,
  operation: event.operation,
  actor: `${event.actor_type}:${event.actor_id}`,
  inputHash: event.input_hash ?? 'GENESIS',
  outputHash: event.output_hash,
  previousHash: event.previous_event_hash ?? 'GENESIS',
  ruleVersion: event.rule_version,
  note: `${event.reason} ${auditFixture.hash_chain_notice}`,
}));
