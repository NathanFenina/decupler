#!/usr/bin/env python3
"""CSS du gabarit d'article Decupler (dcp-post).

Version de reference fournie par Nathan (article « Classement agences GEO 2026 »).
Contient les blocs absents de la version precedente : .dcp-numbered-list,
.dcp-rank-item, .dcp-pillar-label, .dcp-pillar-avis, .decupler-faq-answer-inner.
Le correctif sticky natif est inclus (remplace l'ancien sticky JS).
"""

CSS = r"""
  .dcp-post * { box-sizing: border-box; }
  .dcp-post {
    font-family: 'Inter', 'DM Sans', sans-serif !important;
    color: #1a1a2e !important;
    max-width: 1320px;
    margin: 0 auto !important;
    padding: 0 24px 80px !important;
    line-height: 1.7;
  }
  /* ---------- HEADER / H1 ---------- */
  .dcp-post-header {
    max-width: 900px;
    margin: 0 auto 56px !important;
    text-align: center;
    padding-top: 56px;
  }
  .dcp-eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.1));
    border: 1px solid rgba(118,75,162,0.25);
    color: #764ba2 !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 12.5px;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    font-weight: 600;
    padding: 7px 16px;
    border-radius: 100px;
    margin-bottom: 24px;
  }
  .dcp-post-header h1 {
    font-family: 'Sora', sans-serif !important;
    font-size: clamp(30px, 4.2vw, 48px) !important;
    line-height: 1.15 !important;
    font-weight: 700 !important;
    margin: 0 0 20px !important;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: #764ba2 !important;
  }
  .dcp-post-header .dcp-subtitle {
    font-size: 17px;
    color: #55556b !important;
    max-width: 680px;
    margin: 0 auto !important;
  }
  .dcp-post-header .dcp-divider {
    width: 72px;
    height: 4px;
    margin: 28px auto 0 !important;
    border-radius: 4px;
    background: linear-gradient(135deg, #667eea, #764ba2);
  }
  /* ---------- LAYOUT 2 COLONNES ---------- */
  .dcp-layout {
    display: grid;
    grid-template-columns: 1fr 320px;
    gap: 56px;
    align-items: start;
  }
  /* ---------- CONTENU ---------- */
  .dcp-content h2 {
    font-family: 'Sora', sans-serif !important;
    font-size: 27px !important;
    font-weight: 700 !important;
    color: #1a1a2e !important;
    margin: 48px 0 18px !important;
    padding-left: 16px;
    border-left: 4px solid #764ba2;
  }
  .dcp-content h3 {
    font-family: 'Sora', sans-serif !important;
    font-size: 21px !important;
    font-weight: 700 !important;
    color: #2d2d44 !important;
    margin: 32px 0 14px !important;
  }
  .dcp-content p { font-size: 16px; color: #33334a; margin: 0 0 18px !important; }
  .dcp-content ul, .dcp-content ol { margin: 0 0 20px !important; padding-left: 22px; }
  .dcp-content li { margin-bottom: 10px; font-size: 15.5px; color: #33334a; }
  .dcp-content a {
    color: #764ba2 !important;
    font-weight: 600;
    text-decoration: underline;
    text-decoration-color: rgba(118,75,162,0.35);
    text-underline-offset: 3px;
  }
  .dcp-content a:hover { text-decoration-color: #764ba2; }
  .dcp-lead {
    font-size: 18.5px !important;
    color: #1a1a2e !important;
    font-weight: 500;
  }
  /* ---------- BLOCS SPÉCIAUX (conseil / avertissement) ---------- */
  .dcp-callout {
    border-radius: 14px;
    padding: 20px 22px;
    margin: 28px 0 !important;
    font-size: 15.5px;
    border-left: 4px solid;
  }
  .dcp-callout.dcp-tip {
    background: linear-gradient(135deg, rgba(102,126,234,0.07), rgba(118,75,162,0.07));
    border-color: #764ba2;
    color: #3a2d5c !important;
  }
  .dcp-callout.dcp-warning {
    background: #fff6ed;
    border-color: #e8912f;
    color: #6b4718 !important;
  }
  .dcp-callout strong { color: inherit !important; }
  /* ---------- TABLEAUX ---------- */
  .dcp-table-wrap { overflow-x: auto; margin: 28px 0 !important; border-radius: 14px; box-shadow: 0 4px 20px rgba(30,20,60,0.08); }
  .dcp-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 14px;
    min-width: 640px;
  }
  .dcp-table thead th {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: #fff !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 600;
    text-align: left;
    padding: 14px 16px;
  }
  .dcp-table tbody td {
    padding: 12px 16px;
    border-bottom: 1px solid #ececf4;
    color: #2d2d44 !important;
    font-size: 13.5px;
  }
  .dcp-table tbody tr:nth-child(even) { background: #f7f6fc; }
  .dcp-table tbody td:first-child { font-weight: 700; color: #5b3d8a !important; }
  /* ---------- BLOCS PILIER ---------- */
  .dcp-pillar {
    background: #fff;
    border: 1px solid #ececf4;
    border-radius: 16px;
    padding: 26px 28px;
    margin: 28px 0 !important;
    box-shadow: 0 4px 16px rgba(30,20,60,0.05);
  }
  .dcp-pillar-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 36px; height: 36px;
    border-radius: 10px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: #fff !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 700;
    font-size: 15px;
    margin-bottom: 14px;
  }
  .dcp-pillar h3 { margin-top: 0 !important; }
  .dcp-pillar-label {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    color: #764ba2 !important;
    margin: 14px 0 4px !important;
  }
  .dcp-pillar-avis {
    background: #f7f6fc;
    border-radius: 10px;
    padding: 14px 16px;
    margin-top: 10px !important;
    font-size: 14.5px;
    color: #3a2d5c !important;
  }
  /* ---------- ITEMS NUMÉROTÉS ---------- */
  .dcp-rank-item {
    display: flex;
    gap: 18px;
    align-items: flex-start;
    background: #fff;
    border: 1px solid #ececf4;
    border-radius: 14px;
    padding: 18px 20px;
    margin-bottom: 12px !important;
  }
  .dcp-rank-num {
    flex-shrink: 0;
    width: 30px; height: 30px;
    border-radius: 8px;
    background: rgba(118,75,162,0.1);
    color: #764ba2 !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 700;
    font-size: 13.5px;
    display: flex; align-items: center; justify-content: center;
  }
  .dcp-rank-body h4 {
    font-family: 'Sora', sans-serif !important;
    font-size: 16.5px !important;
    font-weight: 700;
    color: #1a1a2e !important;
    margin: 0 0 6px !important;
  }
  .dcp-rank-body p { font-size: 14.5px; margin: 0 !important; color: #4a4a60; }
  /* ---------- LISTE NUMÉROTÉE STYLISÉE ---------- */
  .dcp-numbered-list { list-style: none; padding-left: 0 !important; margin: 24px 0 !important; counter-reset: dcp-counter; }
  .dcp-numbered-list li {
    position: relative;
    padding: 4px 0 4px 46px;
    margin-bottom: 18px !important;
    counter-increment: dcp-counter;
  }
  .dcp-numbered-list li::before {
    content: counter(dcp-counter);
    position: absolute;
    left: 0; top: 0;
    width: 32px; height: 32px;
    border-radius: 9px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: #fff !important;
    font-family: 'Sora', sans-serif !important;
    font-weight: 700;
    font-size: 14px;
    display: flex; align-items: center; justify-content: center;
  }
  /* ---------- RÉCAP / TAKEAWAYS ---------- */
  .dcp-recap {
    background: #0a0e1a !important;
    border-radius: 18px;
    padding: 34px 30px;
    margin: 36px 0 !important;
  }
  .dcp-recap h2 { color: #fff !important; border-left-color: #a78bfa; margin-top: 0 !important; }
  .dcp-recap p { color: #e4e4f0 !important; }
  .dcp-recap p.dcp-recap-final { color: #b8b8d0 !important; margin-top: 8px !important; margin-bottom: 0 !important; font-style: italic; }
  /* ---------- MAILLAGE INTERNE ---------- */
  .dcp-links-block {
    margin: 44px 0 8px !important;
    padding: 26px;
    border-radius: 16px;
    background: #fff;
    border: 1px solid #ececf4;
  }
  .dcp-links-block h4 {
    font-family: 'Sora', sans-serif !important;
    font-size: 15px !important;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: #764ba2 !important;
    margin: 0 0 16px !important;
  }
  .dcp-links-grid { display: flex; flex-wrap: wrap; gap: 10px; }
  .dcp-links-grid a {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: linear-gradient(135deg, rgba(102,126,234,0.08), rgba(118,75,162,0.08));
    border: 1px solid rgba(118,75,162,0.2);
    color: #5b3d8a !important;
    font-size: 13.5px;
    font-weight: 600;
    text-decoration: none !important;
    padding: 9px 15px;
    border-radius: 100px;
    transition: all 0.2s ease;
  }
  .dcp-links-grid a:hover {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: #fff !important;
    border-color: transparent;
  }
  /* ---------- SIDEBAR CTA ---------- */
  .dcp-sidebar { position: relative; }
  .dcp-cta-sticky {
    background: transparent !important;
    border: 1.5px solid rgba(118,75,162,0.25);
    border-radius: 20px;
    padding: 28px 24px;
    box-shadow: 0 10px 30px rgba(60,30,110,0.08);
  }
  .dcp-cta-badge {
    display: inline-block;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 11px;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: #764ba2 !important;
    background: rgba(118,75,162,0.1);
    padding: 5px 12px;
    border-radius: 100px;
    margin-bottom: 14px;
  }
  .dcp-cta-sticky h3 {
    font-family: 'Sora', sans-serif !important;
    font-size: 20px !important;
    font-weight: 700 !important;
    color: #1a1a2e !important;
    margin: 0 0 10px !important;
  }
  .dcp-cta-sticky p {
    font-size: 14px;
    color: #55556b !important;
    margin: 0 0 20px !important;
  }
  .dcp-cta-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 100%;
    background: linear-gradient(135deg, #667eea, #764ba2) !important;
    color: #fff !important;
    font-weight: 700;
    font-size: 14.5px;
    text-decoration: none !important;
    padding: 14px 18px;
    border-radius: 12px;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
  }
  .dcp-cta-btn:hover { transform: translateY(-2px); box-shadow: 0 10px 24px rgba(118,75,162,0.35); }
  .dcp-cta-meta {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-top: 16px;
    font-size: 12px;
    color: #8888a0 !important;
  }
  .dcp-cta-dot { width: 7px; height: 7px; border-radius: 50%; background: #4ade80; flex-shrink: 0; }
  @media (max-width: 900px) {
    .dcp-layout { grid-template-columns: 1fr; }
    .dcp-sidebar { order: 2; width: 100% !important; }
    .dcp-cta-sticky {
      position: relative !important;
      top: 0 !important;
      left: 0 !important;
      width: 100% !important;
      margin: 12px 0 40px;
    }
    .dcp-post-header { padding-top: 32px; }
  }
  /* ---------- FAQ ---------- */
  .dcp-faq-section { max-width: 900px; margin: 64px auto 0 !important; }
  .dcp-faq-section > h2 {
    font-family: 'Sora', sans-serif !important;
    font-size: 28px !important;
    text-align: center;
    background: linear-gradient(135deg, #667eea, #764ba2);
    -webkit-background-clip: text;
    background-clip: text;
    -webkit-text-fill-color: transparent;
    color: #764ba2 !important;
    margin: 0 0 30px !important;
    border-left: none !important;
    padding-left: 0 !important;
  }
  .decupler-faq-item {
    background: #fff;
    border: 1px solid #ececf4;
    border-radius: 14px;
    margin-bottom: 14px;
    overflow: hidden;
    opacity: 0;
    transform: translateY(16px);
    transition: opacity 0.5s ease, transform 0.5s ease, box-shadow 0.2s ease;
  }
  .decupler-faq-item.dcp-in-view { opacity: 1; transform: translateY(0); }
  .decupler-faq-item:hover { box-shadow: 0 8px 24px rgba(60,30,110,0.1); }
  .decupler-faq-question {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    padding: 18px 22px;
    cursor: pointer;
    background: #fff;
  }
  .decupler-faq-item.dcp-open .decupler-faq-question {
    background: linear-gradient(135deg, #667eea, #764ba2);
  }
  .decupler-faq-question span.dcp-q-text {
    font-family: 'Sora', sans-serif !important;
    font-weight: 600;
    font-size: 15.5px;
    color: #1a1a2e !important;
  }
  .decupler-faq-item.dcp-open .dcp-q-text { color: #fff !important; }
  .decupler-faq-icon {
    flex-shrink: 0;
    width: 26px; height: 26px;
    border-radius: 50%;
    background: rgba(118,75,162,0.1);
    color: #764ba2 !important;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; font-weight: 700;
    transition: transform 0.3s ease, background 0.3s ease, color 0.3s ease;
  }
  .decupler-faq-item.dcp-open .decupler-faq-icon {
    background: rgba(255,255,255,0.2);
    color: #fff !important;
    transform: rotate(45deg);
  }
  .decupler-faq-answer { max-height: 0; overflow: hidden; transition: max-height 0.35s ease; }
  .decupler-faq-answer-inner { padding: 4px 22px 20px; font-size: 15px; color: #4a4a60 !important; }
  @media (max-width: 600px) {
    .dcp-post { padding: 0 16px 60px !important; }
    .dcp-rank-item { flex-direction: column; }
  }
  /* ---------- STICKY NATIF ---------- */
  @media (min-width: 901px) {
    .dcp-post .dcp-sidebar { align-self: stretch; height: auto !important; }
    .dcp-post .dcp-cta-sticky {
      position: sticky !important;
      top: 24px !important;
      left: auto !important;
      width: auto !important;
    }
  }
  .dcp-post .dcp-faq-section { max-width: 100% !important; margin: 64px 0 0 !important; }

.dcp-post .dcp-screen-figure{margin:30px 0 6px;padding:0;border-radius:16px;
 line-height:0;background:#0a0e1a;overflow:hidden;
 box-shadow:0 16px 40px rgba(15,18,45,.16)}
.dcp-post .dcp-screen-figure img{display:block;width:100%;height:auto;border-radius:16px}
.dcp-post .dcp-screen-figure figcaption{line-height:1.55;font-size:14px;color:#6b7280;
 background:#fff;padding:12px 4px 0;text-align:center;font-style:italic}
@media(max-width:768px){.dcp-post .dcp-screen-figure{margin:22px 0 4px;border-radius:12px}
 .dcp-post .dcp-screen-figure img{border-radius:12px}
 .dcp-post .dcp-screen-figure figcaption{font-size:13px}}
"""
