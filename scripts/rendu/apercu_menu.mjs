import fs from 'fs';
import puppeteer from 'puppeteer';
const html = fs.readFileSync('content/header/header.html','utf8');
const page_html = `<!doctype html><html lang="fr"><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap">
<style>body{margin:0;background:#fff;font-family:'DM Sans',sans-serif}</style></head>
<body>${html}<div style="height:520px"></div></body></html>`;
const b = await puppeteer.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args:['--no-sandbox','--disable-dev-shm-usage']});
const p = await b.newPage();
await p.setViewport({width:1440,height:900,deviceScaleFactor:1});
await p.setContent(page_html,{waitUntil:'load'});
await new Promise(r=>setTimeout(r,600));
await p.screenshot({path:'/tmp/menu-ferme.png'});
// ouvrir « Site offert »
await p.evaluate(()=>{
  const box=document.querySelectorAll('.d-has-mega')[0].querySelector('.d-mega-box');
  box.style.display='flex';
  box.querySelectorAll('.d-side-item').forEach(e=>e.classList.remove('active'));
  box.querySelectorAll('.d-tab-content').forEach(e=>e.classList.remove('d-active'));
  box.querySelector('[data-target="tab-offre"]').classList.add('active');
  box.querySelector('#tab-offre').classList.add('d-active');
});
await new Promise(r=>setTimeout(r,300));
await p.screenshot({path:'/tmp/menu-offre.png'});
// onglet SEO, pour verifier que les autres colonnes n'ont pas bouge
await p.evaluate(()=>{
  const box=document.querySelectorAll('.d-has-mega')[0].querySelector('.d-mega-box');
  box.querySelectorAll('.d-side-item').forEach(e=>e.classList.remove('active'));
  box.querySelectorAll('.d-tab-content').forEach(e=>e.classList.remove('d-active'));
  box.querySelector('[data-target="tab-seo"]').classList.add('active');
  box.querySelector('#tab-seo').classList.add('d-active');
});
await new Promise(r=>setTimeout(r,300));
await p.screenshot({path:'/tmp/menu-seo.png'});
const w = await p.evaluate(()=>document.documentElement.scrollWidth);
console.log('scrollWidth', w);
await b.close();
