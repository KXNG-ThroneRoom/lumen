import type { Evidence, Source } from '../lib/api-contract';
import { evidenceCanRender } from '../lib/api-contract';

function sourceLabel(item: Evidence, sources: Source[]) {
  const source = sources.find((candidate) => candidate.id === item.source_id);
  return source ? `${source.name} / ${source.source_type}` : item.source_id ?? 'source metadata missing';
}

export function EvidenceTrail({ evidence, sources }: { evidence: Evidence[]; sources: Source[] }) {
  return (
    <section className="panel" aria-labelledby="evidence-heading">
      <div className="panel-kicker">Evidence trail</div>
      <h2 id="evidence-heading">Provenance, limits, and source proximity</h2>
      <div className="evidence-grid">
        {evidence.map((item) => (
          <article className={`evidence-card ${item.primary ? 'primary' : 'secondary'} ${evidenceCanRender(item) ? '' : 'missing'}`} key={item.id}>
            <div className="evidence-meta">
              <span>{item.id}</span>
              <span>{item.evidence_type.replaceAll('_', ' ')}</span>
            </div>
            <h3>{sourceLabel(item, sources)}</h3>
            <blockquote>{item.quote ?? item.summary}</blockquote>
            <dl>
              <div>
                <dt>Provenance</dt>
                <dd>{item.provenance}</dd>
              </div>
              <div>
                <dt>Proximity</dt>
                <dd>{item.proximity}; timestamp quality: {item.timestamp_quality}</dd>
              </div>
              <div>
                <dt>Limitations</dt>
                <dd>{item.limitations.join(' ') || 'No limitation recorded; treat as incomplete metadata.'} Ref: {item.limitations_ref || 'missing'}.</dd>
              </div>
              <div>
                <dt>Audit reference</dt>
                <dd>{item.audit_reference || 'missing — evidence should be treated as withheld'}</dd>
              </div>
            </dl>
          </article>
        ))}
      </div>
    </section>
  );
}
