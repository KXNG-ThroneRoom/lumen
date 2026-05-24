import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Lumen Static Intelligence Dashboard',
  description: 'Transparent claim, evidence, narrative, contradiction, briefing, and audit scaffold.',
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
