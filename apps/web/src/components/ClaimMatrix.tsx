import type { Claim } from '../data/lumenSample';

const statusLabels: Record<Claim['status'], string> = {
  plausible: 'Plausible',
  contested: 'Contested',
  unknown: 'Unknown',
  unsupported: 'Unsupported',
  unresolved: 'Unresolved',
};

function hasConfidenceReason(claim: Claim) {
  return Array.isArray(claim.confidenceLogic) && claim.confidenceLogic.some((reason) => reason.trim().length > 0);
}

export function ClaimMatrix({ claims }: { claims: Claim[] }) {
  return (
    <section className="panel" aria-labelledby="claims-heading">
      <div className="panel-kicker">Claim matrix</div>
      <h2 id="claims-heading">Atomic claims, not article-level truth</h2>
      <div className="matrix">
        {claims.map((claim) => {
          if (!claim.status) {
            return (
              <article className="claim-row" key={claim.id}>
                <div className="claim-id">{claim.id}</div>
                <div>
                  <div className="claim-type">Quarantined claim</div>
                  <h3>Claim withheld by uncertainty guard</h3>
                  <p>Missing status. Lumen does not render claim text without an explicit status.</p>
                </div>
                <div className="status-chip unknown">Missing status</div>
                <div className="confidence-cell">withheld</div>
              </article>
            );
          }

          const confidenceHasReason = hasConfidenceReason(claim);

          return (
            <article className="claim-row" key={claim.id}>
              <div className="claim-id">{claim.id}</div>
              <div>
                <div className="claim-type">{claim.type}</div>
                <h3>{claim.text}</h3>
                <p>{claim.unresolved}</p>
                <div className="reason-list" aria-label={`Confidence reasons for ${claim.id}`}>
                  {confidenceHasReason ? (
                    claim.confidenceLogic.map((reason) => <span key={reason}>{reason}</span>)
                  ) : (
                    <span>Missing confidence reason — confidence display withheld.</span>
                  )}
                </div>
              </div>
              <div className={`status-chip ${claim.status}`}>{statusLabels[claim.status]}</div>
              <div className="confidence-cell">{confidenceHasReason ? claim.confidence : 'withheld'}</div>
            </article>
          );
        })}
      </div>
    </section>
  );
}
