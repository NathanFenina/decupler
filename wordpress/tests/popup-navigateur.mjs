// Vérifie la pop-up dans un vrai navigateur, sur le banc WordPress.
// Horloge simulée (page.clock) : les 15 s du délai passent instantanément.
// Chaque cas s'ouvre dans un contexte neuf, donc un localStorage vide.
//
//   node wordpress/tests/popup-navigateur.mjs http://127.0.0.1:8123
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
let pw;
try { pw = require('playwright'); } catch { pw = require('/opt/node22/lib/node_modules/playwright'); }

const B = process.argv[2] || 'http://127.0.0.1:8123';
const nav = await pw.chromium.launch({ args: ['--no-sandbox'] });
const lignes = [];
let ko = 0;
const t = (nom, ok, detail = '') => { lignes.push(`${ok ? 'OK' : 'KO'}|${nom}${ok ? '' : ' — ' + detail}`); if (!ok) ko++; };

async function ouvre(chemin, largeur = 1440, avance = 0, contexte = null, heure = null) {
  const ctx = contexte || await nav.newContext({ viewport: { width: largeur, height: 900 } });
  const p = await ctx.newPage();
  await p.clock.install(heure ? { time: heure } : {});
  // Rien d'externe : polices et emoji ne doivent pas ralentir le banc.
  await p.route(u => !u.href.startsWith(B), r => r.abort());
  await p.goto(B + chemin, { waitUntil: 'domcontentloaded' });
  if (avance) await p.clock.runFor(avance);
  return { p, ctx };
}
const pop = p => p.evaluate(() => {
  const w = document.getElementById('dcp-pop');
  if (!w) return null;
  const go = w.querySelector('.dcp-go');
  return { cls: w.className, titre: (w.querySelector('.dcp-t, .dcp-mt') || {}).textContent,
    href: go && go.href, target: go && go.target, rel: go && go.rel,
    focus: w.contains(document.activeElement), role: w.querySelector('[role=dialog]') !== null };
});

// 1. Délai
let { p, ctx } = await ouvre('/', 1440, 14000);
t('rien à 14 s', (await pop(p)) === null);
await p.clock.runFor(2000);
let r = await pop(p);
t('affichée à 16 s', r !== null);
t('fenêtre au centre sur ordinateur', r && r.cls === '', r && r.cls);
t('titre du workshop', r && /Claude\sCode/.test(r.titre), r && r.titre);
t('bouton vers l’événement, nouvel onglet, noopener',
  r && r.href === 'https://www.linkedin.com/events/7508143909210910720' && r.target === '_blank' && r.rel === 'noopener', JSON.stringify(r));
t('focus dans la fenêtre, dialogue accessible', r && r.focus && r.role);

// 2. Fermeture et mémoire
await p.keyboard.press('Escape');
t('Échap ferme', (await pop(p)) === null);
const mem = await p.evaluate(() => JSON.parse(localStorage.getItem('dcp_popup_workshop-2026-10-08') || 'null'));
t('fermeture mémorisée', !!(mem && mem.ferme));
await p.close();
({ p } = await ouvre('/agence-geo/', 1440, 20000, ctx));
t('ne revient pas sur la page suivante', (await pop(p)) === null);
await p.close();
({ p } = await ouvre('/', 1440, 0, ctx));
await p.evaluate(() => localStorage.setItem('dcp_popup_workshop-2026-10-08', JSON.stringify({ ferme: Date.now() - 8 * 864e5 })));
await p.reload({ waitUntil: 'domcontentloaded' }); await p.clock.runFor(16000);
t('revient après 7 jours', (await pop(p)) !== null);
await ctx.close();

// 3. Clic sur le bouton : plus jamais pour cette campagne
({ p, ctx } = await ouvre('/', 1440, 16000));
await p.evaluate(() => { const a = document.querySelector('#dcp-pop .dcp-go'); a.target = ''; a.href = '#'; a.click(); });
await p.clock.runFor(200);
t('cliquée : fermée', (await pop(p)) === null);
const mem2 = await p.evaluate(() => JSON.parse(localStorage.getItem('dcp_popup_workshop-2026-10-08') || 'null'));
t('cliquée : mémorisée', !!(mem2 && mem2.clic));
await ctx.close();

// 4. Clic à côté et « Non merci »
({ p, ctx } = await ouvre('/', 1440, 16000));
await p.mouse.click(20, 20);
t('clic à côté ferme', (await pop(p)) === null);
await ctx.close();
({ p, ctx } = await ouvre('/', 1440, 16000));
await p.click('#dcp-pop .dcp-no');
t('« Non merci » ferme', (await pop(p)) === null);
await ctx.close();

// 5. Mobile
({ p, ctx } = await ouvre('/', 390, 16000));
r = await pop(p);
t('bandeau sur mobile', r && r.cls === 'dcp-mob', r && r.cls);
const geo = await p.evaluate(() => { const c = document.querySelector('#dcp-pop .dcp-c').getBoundingClientRect();
  return { bas: Math.round(innerHeight - c.bottom), haut: Math.round(c.height), deborde: document.documentElement.scrollWidth > innerWidth }; });
t('bandeau collé en bas, ne couvre pas la page', geo.bas <= 12 && geo.haut < 120 && !geo.deborde, JSON.stringify(geo));
await ctx.close();

// 6. Pages lead magnet, aperçu, blocage
({ p, ctx } = await ouvre('/guide-lm/', 1440, 20000));
t('pas de doublon sur une page lead magnet', (await pop(p)) === null);
await ctx.close();
({ p, ctx } = await ouvre('/?dcp_popup=1', 1440, 600));
t('aperçu ?dcp_popup=1 en 0,5 s', (await pop(p)) !== null);
await ctx.close();
({ p, ctx } = await ouvre('/?dcp_popup=0', 1440, 20000));
t('?dcp_popup=0 la bloque', (await pop(p)) === null);
await ctx.close();

// 7. Date de fin dépassée dans le navigateur (page restée en cache)
({ p, ctx } = await ouvre('/', 1440, 16000, null, new Date('2026-10-08T12:31:00+02:00')));
t('après la fin, même une page en cache ne l’affiche pas', (await pop(p)) === null);
await ctx.close();

await nav.close();
console.log(lignes.join('\n'));
process.exit(ko ? 1 : 0);
