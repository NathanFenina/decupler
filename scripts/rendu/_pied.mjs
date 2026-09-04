import puppeteer from 'puppeteer'; import fs from 'node:fs';
const html=fs.readFileSync(process.argv[2],'utf8');
const shell=`<!doctype html><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:#fff;font-family:system-ui}#masthead{height:92px;background:#fff}.ast-container{max-width:1280px;margin:0 auto}.entry-content{margin:0 20px}/* Astra peint les <pre> en clair : sans cette regle le harnais
   valide un terminal sombre que la production affiche blanc. */pre{background:#f4f4f6;border:1px solid #e3e3e8;border-radius:4px;padding:12px}.site-content{padding-bottom:60px}article.ast-article-single{padding-bottom:40px}#colophon{height:260px;background:#14152b}</style><div id="masthead"></div><div class="ast-container"><div class="site-content"><main><article class="ast-article-single"><div class="entry-content">${html}</div></article></main></div></div><div id="colophon"></div>`;
const b=await puppeteer.launch({headless:true,executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox','--disable-dev-shm-usage']});
const p=await b.newPage(); await p.setViewport({width:1440,height:900});
await p.setContent(shell,{waitUntil:'domcontentloaded'}); await new Promise(r=>setTimeout(r,3000));
console.log(await p.evaluate(()=>{
  const band=[...document.querySelectorAll('.dcp-band')].pop();
  const foot=document.querySelector('#colophon');
  return `bas de la derniere bande : ${Math.round(band.getBoundingClientRect().bottom)}\nhaut du footer          : ${Math.round(foot.getBoundingClientRect().top)}\nECART                   : ${Math.round(foot.getBoundingClientRect().top-band.getBoundingClientRect().bottom)}px`;
}));
await b.close();
