// Repère les <p> vides VISIBLES qu'injecte wpautop dans une page servie en local
// (miroir.py + python3 -m http.server). Un <p> vide dans une grille ou un flex
// prend une case : carte qui passe à la ligne, bannière avec un grand vide.
//   node scripts/rendu/paragraphes_vides.mjs http://127.0.0.1:8230/<slug>/page.html
// Cible : 0. La règle `.lm-mcp p:empty{display:none}` (en-tête 2762 et
// lm-mcp-leadmagnet.css) les masque ; la source doit quand même éviter une
// balise courte (span, i, b…) suivie d'un bloc sur la même ligne.
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const pw = require(process.env.PLAYWRIGHT_MODULE || '/opt/node22/lib/node_modules/playwright');
const b = await pw.chromium.launch({ args: ['--no-sandbox'] });
let total = 0;
for (const url of process.argv.slice(2)) {
  const p = await b.newPage({ viewport: { width: 1440, height: 900 } });
  const base = new URL(url).origin;
  await p.route(u => !u.href.startsWith(base), r => r.abort());
  await p.goto(url, { waitUntil: 'domcontentloaded' });
  const r = await p.evaluate(() => [...document.querySelectorAll('.lm-mcp p, .entry-content p')]
    .filter(x => getComputedStyle(x).display !== 'none' && !x.textContent.trim() && !x.querySelector('img,svg,iframe,input,form,button,video'))
    .map(x => (x.parentElement.className || x.parentElement.tagName) + ' > <p> vide'));
  console.log(url, r.length); r.slice(0, 15).forEach(x => console.log('   ', x));
  total += r.length; await p.close();
}
await b.close();
process.exit(total ? 1 : 0);
