// Capture des vignettes de sites pour la page « site gratuit ».
// Source = une URL ou un fichier HTML local (artefact enregistre).
//     node scripts/rendu/vignettes.mjs <source> <sortie.png> [largeur] [hauteur]
import puppeteer from 'puppeteer';
import fs from 'node:fs';
const [src, out, W = 1440, H = 1000, DPR = 1.4] = process.argv.slice(2);
const b = await puppeteer.launch({headless:true, executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args:['--no-sandbox','--disable-dev-shm-usage','--hide-scrollbars']});
const p = await b.newPage();
await p.setViewport({width:+W, height:+H, deviceScaleFactor:+DPR});
try {
  if (fs.existsSync(src)) await p.goto('file://' + fs.realpathSync(src), {waitUntil:'networkidle2', timeout:60000});
  else await p.goto(src, {waitUntil:'networkidle2', timeout:60000});
} catch (e) { console.log('nav:', e.message.slice(0,80)); }
await new Promise(r => setTimeout(r, 4000));
// Les bandeaux cookies mangent le haut de page : on retire ce qui flotte.
await p.evaluate(() => {
  document.querySelectorAll('*').forEach(e => {
    const s = getComputedStyle(e);
    if ((s.position === 'fixed' || s.position === 'sticky') && e.getBoundingClientRect().height > 90) e.remove();
  });
  window.scrollTo(0, 0);
});
await new Promise(r => setTimeout(r, 800));
await p.screenshot({path: out, type: out.endsWith('.jpg') ? 'jpeg' : 'png', quality: out.endsWith('.jpg') ? 80 : undefined});
console.log('→', out, fs.statSync(out).size, 'octets');
await b.close();
