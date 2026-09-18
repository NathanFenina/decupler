// Controle mecanique d'une page avant publication : debordement horizontal,
// contraste reel (alpha composite), hierarchie des titres.
//
//     node scripts/rendu/controle.mjs content/articles/<page>.html [largeur]
//
// A lancer aux deux largeurs qui comptent : 1440 et 390. Le detecteur
// d'anti-patterns d'Impeccable raisonne sur le source ; celui-ci mesure le
// rendu, et c'est lui qui tranche quand les deux ne disent pas la meme chose.
import puppeteer from 'puppeteer';
import fs from 'node:fs';
const html = fs.readFileSync(process.argv[2], 'utf8');
const W = Number(process.argv[3] || 390);
const shell = `<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>html,body{margin:0;padding:0;background:#fff;font-family:system-ui}.ast-container{max-width:1280px;margin:0 auto}.entry-content{margin:0 20px}/* Astra peint les <pre> en clair : sans cette regle le harnais
   valide un terminal sombre que la production affiche blanc. */pre{background:#f4f4f6;border:1px solid #e3e3e8;border-radius:4px;padding:12px}</style><div class="ast-container"><div class="site-content"><main><article class="ast-article-single"><div class="entry-content">${html}</div></article></main></div></div>`;
const b = await puppeteer.launch({headless:true, executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--no-sandbox','--disable-dev-shm-usage']});
const p = await b.newPage();
await p.setViewport({width:W, height:900});
await p.setContent(shell,{waitUntil:'domcontentloaded'});
await new Promise(r=>setTimeout(r,2500));
const r = await p.evaluate((W)=>{
  const res = {scrollW: document.documentElement.scrollWidth, viewport: W, debord: [], contraste: [], etats: {}};
  // Un bloc large qui defile dans son propre conteneur overflow-x:auto est
  // le comportement voulu, pas un debordement : ses enfants depassent le
  // viewport par construction. Sans cette exception, tout bloc de code fait
  // crier le controle et on finit par ne plus le lire.
  const dansUnDefilement = e => {
    for (let n = e.parentElement; n; n = n.parentElement) {
      const ox = getComputedStyle(n).overflowX;
      if (ox === 'auto' || ox === 'scroll') return true;
      if (n.classList && n.classList.contains('dcp')) return false;
    }
    return false;
  };
  document.querySelectorAll('.dcp, .dcp *').forEach(e=>{
    const b = e.getBoundingClientRect();
    if (b.right > W + 1 && !dansUnDefilement(e))
      res.debord.push(`${e.tagName.toLowerCase()}.${(e.className||'').toString().slice(0,34)} w=${Math.round(b.width)} right=${Math.round(b.right)}`);
  });
  res.debord = res.debord.slice(0, 8);
  // contraste texte
  const lum = c => { const [r,g,b] = c.match(/\d+/g).map(Number).map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)}); return .2126*r+.7152*g+.0722*b; };
  // Les fonds teintes sont semi-transparents : sans compositer l'alpha sur
  // ce qu'il y a derriere, tout tint clair passe pour un fond noir et le
  // controle crie au faux positif. On empile donc les couches.
  const rgba = c => { const v=(c.match(/[\d.]+/g)||[]).map(Number); return {r:v[0]||0,g:v[1]||0,b:v[2]||0,a:v.length>3?v[3]:1}; };
  const fond = e => {
    const couches=[]; let n=e;
    while(n){ const c=rgba(getComputedStyle(n).backgroundColor); if(c.a>0) couches.push(c); if(c.a===1) break; n=n.parentElement; }
    couches.push({r:255,g:255,b:255,a:1});
    let out=couches.pop();
    while(couches.length){ const c=couches.pop();
      out={r:c.r*c.a+out.r*(1-c.a), g:c.g*c.a+out.g*(1-c.a), b:c.b*c.a+out.b*(1-c.a), a:1}; }
    return `rgb(${Math.round(out.r)}, ${Math.round(out.g)}, ${Math.round(out.b)})`; };
  const vus = new Set();
  document.querySelectorAll('.dcp p,.dcp li,.dcp small,.dcp h1,.dcp h2,.dcp h3,.dcp h4,.dcp summary,.dcp .p-txt,.dcp .band-p').forEach(e=>{
    const cs = getComputedStyle(e), col = cs.color, bg = fond(e);
    const k = col+'|'+bg; if (vus.has(k)) return; vus.add(k);
    const L1 = lum(col), L2 = lum(bg);
    const ratio = (Math.max(L1,L2)+.05)/(Math.min(L1,L2)+.05);
    const gros = parseFloat(cs.fontSize) >= 24 || (parseFloat(cs.fontSize) >= 18.66 && +cs.fontWeight >= 700);
    if (ratio < (gros ? 3 : 4.5)) res.contraste.push(`${ratio.toFixed(2)}:1  ${col} sur ${bg}  (${e.tagName.toLowerCase()}.${(e.className||'').toString().slice(0,24)})`);
  });
  res.etats.details = document.querySelectorAll('.dcp details').length;
  res.etats.liensSansTexte = [...document.querySelectorAll('.dcp a')].filter(a=>!a.textContent.trim()).length;
  res.etats.h1 = document.querySelectorAll('.dcp h1').length;
  res.etats.ordreTitres = [...document.querySelectorAll('.dcp h1,.dcp h2,.dcp h3,.dcp h4')].map(h=>h.tagName).join(' ');
  return res;
}, W);
console.log(JSON.stringify(r, null, 1));
await b.close();
