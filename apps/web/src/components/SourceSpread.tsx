import type { EvidenceItem } from '../data/lumenSample';

type SourceSpreadItem = {
  source: string;
  sourceType: string;
  provenance: string;
  independence: string;
  evidenceIds: string[];
};

function sourceName(label: string) {
  return label.split(' / ')[0] ?? label;
}

function groupSources(evidence: EvidenceItem[]): SourceSpreadItem[] {
  const grouped = new Map<string, SourceSpreadItem>();

  for (const item of evidence) {
    const key = `${sourceName(item.label)}|${item.sourceType}|${item.provenance}`;
    const existing = grouped.get(key);
    if (existing) {
      existing.evidenceIds.push(item.id);
      continue;
    }

    grouped.set(key, {
      source: sourceName(item.label),
      sourceType: item.sourceType,
      provenance: item.provenance,
      independence: item.independence,
      evidenceIds: [item.id],
    });
  }

  return Array.from(grouped.values());
}

export function SourceSpread({ evidence, auditReference }: { evidence: EvidenceItem[]; auditReference: string }) {
  const sources = groupSources(evidence);

  return (
    <section className="panel" aria-labelledby="source-spread-heading">
      <div className="panel-kicker">Source spread</div>
      <h2 id="source-spread-heading">Source independence is deferred, not assumed</h2>
      <p>
        Explicit stub/deferred panel. The current UI groups fixture evidence by visible source metadata only; it does not infer ownership, geography,
        political leaning, or real independence. Audit reference: {auditReference || 'missing — analysis withheld'}.
      </p>
      <div className="evidence-grid">
        {sources.map((source) => (
          <article className="evidence-card" key={`${source.source}-${source.sourceType}-${source.provenance}`}>
            <div className="evidence-meta">
              <span>{source.sourceType}</span>
              <span>{source.evidenceIds.join(', ')}</span>
            </div>
            <h3>{source.source}</h3>
            <dl>
              <div>
                <dt>Provenance</dt>
                <dd>{source.provenance}</dd>
              </div>
              <div>
                <dt>Independence note</dt>
                <dd>{source.independence}</dd>
              </div>
              <div>
                <dt>Deferred fields</dt>
                <dd>ownership, geography, affiliation, and source graph validation</dd>
              </div>
            </dl>
          </article>
        ))}
      </div>
    </section>
  );
}
