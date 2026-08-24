import fs from 'fs';
import puppeteer from 'puppeteer';
const html = fs.readFileSync('content/header/header.html','utf8');
const doc = `<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&display=swap">
<style>body{margin:0;background:#fff;font-family:'DM Sans',sans-serif}</style></head><body>${html}</body></html>`;
const b = await puppeteer.launch({headless:true, executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args:['--no-sandbox','--disable-dev-shm-usage']});
const p = await b.newPage();
await p.setViewport({width:390,height:844,deviceScaleFactor:2});
await p.setContent(doc,{waitUntil:'load'});
await new Promise(r=>setTimeout(r,600));
await p.click('#d-burger-trigger');
await new Promise(r=>setTimeout(r,400));
await p.evaluate(()=>document.querySelectorAll('.d-mobile-has-sub > .d-mobile-link')[0].click());
await new Promise(r=>setTimeout(r,300));
await p.screenshot({path:'/tmp/menu-mobile.png'});
console.log('scrollWidth', await p.evaluate(()=>document.documentElement.scrollWidth));
await b.close();
