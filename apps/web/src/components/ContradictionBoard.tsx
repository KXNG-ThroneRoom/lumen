import type { Contradiction } from '../data/lumenSample';

export function ContradictionBoard({ contradictions, auditReference }: { contradictions: Contradiction[]; auditReference: string }) {
  if (!auditReference) {
    return (
      <section className="panel" aria-labelledby="contradictions-heading">
        <div className="panel-kicker">Contradiction board</div>
        <h2 id="contradictions-heading">Contradiction analysis withheld</h2>
        <p>Audit reference is required before contradiction analysis can be rendered.</p>
      </section>
    );
  }

  return (
    <section className="panel" aria-labelledby="contradictions-heading">
      <div className="panel-kicker">Contradiction board</div>
      <h2 id="contradictions-heading">Conflicts stay visible until resolved</h2>
      <p>Audit reference: {auditReference}. Contradictions are fixture-scoped unresolved disputes, not final findings.</p>
      <div className="contradiction-list">
        {contradictions.map((item) => (
          <article className="contradiction-card" key={item.id}>
            <div className="contradiction-topline">
              <span>{item.id}</span>
              <strong>{item.status}</strong>
            </div>
            <h3>{item.conflict}</h3>
            <p>{item.evidenceGap}</p>
            <div className="claim-links">Linked claims: {item.claims.join(', ')}</div>
          </article>
        ))}
      </div>
    </section>
  );
}
