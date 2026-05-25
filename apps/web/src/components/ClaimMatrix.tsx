import type { Claim } from '../lib/api-contract';
import { claimAuditReference, claimRenderState } from '../lib/api-contract';

function label(value: string) {
  return value.replaceAll('_', ' ');
}

export function ClaimMatrix({ claims, auditReference }: { claims: Claim[]; auditReference: string }) {
  return (
    <section className="panel" aria-labelledby="claims-heading">
      <div className="panel-kicker">Claim matrix</div>
      <h2 id="claims-heading">Atomic claims with visible uncertainty gates</h2>
      <div className="matrix">
        {claims.map((claim) => {
          const renderState = claimRenderState(claim, auditReference);
          const visibleAuditReference = claimAuditReference(claim, auditReference);

          if (!renderState.canRender) {
            return (
              <article className="claim-row" key={renderState.claimId}>
                <div className="claim-id">{renderState.claimId}</div>
                <div>
                  <div className="claim-type">Quarantined claim</div>
                  <h3>Claim withheld by uncertainty guard</h3>
                  <p>
                    Missing required display fields: {renderState.reasons.join(', ')}. Lumen does not render claim text without status,
                    confidence reason, evidence reference, and audit reference.
                  </p>
                </div>
                <div className="status-chip unknown">withheld</div>
                <div className="confidence-cell">withheld</div>
              </article>
            );
          }

          return (
            <article className="claim-row" key={claim.id}>
              <div className="claim-id">{claim.id}</div>
              <div>
                <div className="claim-type">{label(claim.claim_type)}</div>
                <h3>{claim.normalized_claim}</h3>
                <p>{claim.limitations.join(' ') || 'No extra limitation recorded for this claim.'}</p>
                <div className="reason-list" aria-label={`Confidence reasons for ${claim.id}`}>
                  {claim.confidence_reason.map((reason) => (
                    <span key={reason}>{reason}</span>
                  ))}
                </div>
                <p>
                  Evidence refs: {claim.evidence_refs.join(', ')}. Contradiction refs:{' '}
                  {claim.contradiction_refs.length > 0 ? claim.contradiction_refs.join(', ') : 'none recorded'}. Claim audit ref: {visibleAuditReference}.
                  Limitations ref: {claim.limitations_ref}.
                </p>
              </div>
              <div className={`status-chip ${claim.status}`}>{label(claim.status)}</div>
              <div className="confidence-cell">{Math.round(claim.confidence_score * 100)}% method signal</div>
            </article>
          );
        })}
      </div>
    </section>
  );
}
