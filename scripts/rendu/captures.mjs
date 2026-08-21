import puppeteer from 'puppeteer';
import fs from 'node:fs';
const html = fs.readFileSync(process.argv[2], 'utf8');
const shell = `<!doctype html><meta charset="utf-8"><style>
html,body{margin:0;padding:0;background:#fff;font-family:system-ui}
#masthead{height:92px;background:#fff;border-bottom:1px solid #eee}
.ast-container{max-width:1280px;margin:0 auto}.entry-content{margin:0 20px}
#colophon{height:260px;background:#14152b}
</style><div id="masthead"></div><div class="ast-container"><div class="site-content"><main><article class="ast-article-single"><header class="entry-header"><h1 class="entry-title">Titre du theme</h1></header><div class="entry-content">${html}</div></article></main></div></div><div id="colophon"></div>`;
const W = Number(process.argv[4] || 1440);
const b = await puppeteer.launch({ headless: true, executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox','--disable-dev-shm-usage'] });
const p = await b.newPage();
await p.setViewport({ width: W, height: 1000, deviceScaleFactor: 1 });
await p.setContent(shell, { waitUntil: 'domcontentloaded' });
await new Promise(r => setTimeout(r, 3000));
const H = await p.evaluate(() => document.documentElement.scrollHeight);
console.log('DEBUG', await p.evaluate(() => {
  const st = getComputedStyle(document.documentElement);
  const alt = document.querySelector('.dcp-sec.alt'), r = alt.getBoundingClientRect();
  return JSON.stringify({bl: st.getPropertyValue('--dcp-bl'), altX: Math.round(r.x), altW: Math.round(r.width), ml: getComputedStyle(alt).marginLeft, nbStyle: document.querySelectorAll('style').length});
}));
console.log('hauteur', H, 'scrollW', await p.evaluate(() => document.documentElement.scrollWidth));
// Instrumentation de capture uniquement : Puppeteer re-emule les metriques
// pendant screenshot(), ce qui declenche un resize et fait recalculer la
// gouttiere sur une largeur factice. On fige donc les marges avant capture.
await p.evaluate(() => {
  const st = getComputedStyle(document.documentElement);
  const l = st.getPropertyValue('--dcp-bl').trim(), r = st.getPropertyValue('--dcp-br').trim();
  document.querySelectorAll('.dcp-sec,.dcp-band,.pcta').forEach(e => {
    e.style.marginLeft = 'calc(-1 * ' + l + ')'; e.style.marginRight = 'calc(-1 * ' + r + ')';
  });
});
let n = 0;
for (let y = 0; y < H - 200; y += 950) {
  await p.evaluate(v => scrollTo(0, v), y);
  await new Promise(r => setTimeout(r, 900));
  await p.screenshot({ path: `${process.argv[3]}-${String(n).padStart(2,'0')}.png` });
  n++;
}
console.log('captures', n);
await b.close();
