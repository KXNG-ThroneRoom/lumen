import { AuditTrail } from '../components/AuditTrail';
import { BriefingPanel } from '../components/BriefingPanel';
import { ClaimMatrix } from '../components/ClaimMatrix';
import { ContradictionBoard } from '../components/ContradictionBoard';
import { EvidenceTrail } from '../components/EvidenceTrail';
import { NarrativeMap } from '../components/NarrativeMap';
import { SourceSpread } from '../components/SourceSpread';
import { auditTrail, briefing, claims, contradictions, evidence, narrativeFrames } from '../data/lumenSample';

const doctrine = [
  'Methods over conclusions',
  'More informed humans, not a new oracle',
  'Unknown / unresolved / contested remain valid outputs',
  'No conclusion without an evidence trail',
  'Article volume is not proof; source independence matters',
  'Narrative analysis, not fact',
  'Audit events use a visible hash-chain design',
];

const limitationsReference = 'LIMITATIONS.md / deterministic fixture only; no live ingestion, no LLM calls, no real-world verification claim';
const auditReference = auditTrail[0]?.id ?? 'sample-audit-trail-missing';

export default function Home() {
  return (
    <main className="dashboard-shell">
      <header className="hero-panel">
        <div>
          <p className="eyebrow">Lumen / public intelligence terminal</p>
          <h1>Claim-level analysis scaffold for evidence, uncertainty, and auditability.</h1>
          <p className="hero-copy">
            This static mock uses deterministic sample data. It does not ingest live news, declare final truth, or sell conclusions.
          </p>
        </div>
        <aside className="doctrine-card" aria-label="Lumen doctrine">
          {doctrine.map((item) => (
            <span key={item}>{item}</span>
          ))}
        </aside>
      </header>

      <section className="system-ribbon" aria-label="Visible method chain">
        {['Source', 'Claim', 'Evidence', 'Contradiction', 'Narrative', 'Score logic', 'Audit'].map((step) => (
          <span key={step}>{step}</span>
        ))}
      </section>

      <div className="dashboard-grid">
        <BriefingPanel briefing={briefing} limitationsReference={limitationsReference} auditReference={auditReference} />
        <ClaimMatrix claims={claims} />
        <EvidenceTrail evidence={evidence} />
        <SourceSpread evidence={evidence} auditReference={auditReference} />
        <NarrativeMap frames={narrativeFrames} auditReference={auditReference} />
        <ContradictionBoard contradictions={contradictions} auditReference={auditReference} />
        <AuditTrail events={auditTrail} />
      </div>
    </main>
  );
}
