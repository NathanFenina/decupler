// Vérifie le comportement du verrou, pas seulement son rendu.
// L'action du formulaire est détournée vers about:blank : on teste la
// mécanique sans créer d'inscription bidon chez Substack.
import puppeteer from 'puppeteer';
import fs from 'node:fs';
import http from 'node:http';
const html = fs.readFileSync(process.argv[2],'utf8');
const shell=`<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><style>html,body{margin:0;background:#fff;font-family:system-ui}.entry-content{margin:0 20px}</style><div class="entry-content">${html}</div>`;
// setContent donne une origine opaque : ni localStorage ni cookies. Un
// verrou dont la mémoire est la moitié du comportement se teste sur une
// vraie origine, donc on sert la page.
const srv = http.createServer((q,r)=>{r.writeHead(200,{'Content-Type':'text/html; charset=utf-8'});r.end(shell)});
await new Promise(r=>srv.listen(0,'127.0.0.1',r));
const PORT = srv.address().port;
const b=await puppeteer.launch({headless:true,executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args:['--no-sandbox','--disable-dev-shm-usage']});
const p=await b.newPage(); await p.setViewport({width:1280,height:900});
await p.goto(`http://127.0.0.1:${PORT}/`,{waitUntil:'domcontentloaded'}); await new Promise(r=>setTimeout(r,1500));
const ok=[];
const t=async(nom,fn)=>{ try{ ok.push(`${await fn()?'  ok   ':'ECHEC '} ${nom}`);}catch(e){ok.push(`ERREUR ${nom} — ${e.message.slice(0,60)}`);} };

await t('la modale est cachée au chargement', ()=>p.evaluate(()=>document.getElementById('vrl').hidden===true));
await t('cliquer « Ouvrir le dépôt » ouvre la modale et ne navigue pas', async ()=>{
  await p.evaluate(()=>document.querySelector('[data-depot]').click());
  return p.evaluate(()=>{const m=document.getElementById('vrl');return !m.hidden&&m.classList.contains('on')&&location.href!=='https://github.com/NathanFenina/claude-seo';});
});
await t('le focus part dans le champ email', ()=>p.evaluate(()=>document.activeElement&&document.activeElement.id==='vrl-e'));
await t('le défilement de la page est bloqué', ()=>p.evaluate(()=>document.documentElement.style.overflow==='hidden'));
await t('Échap referme et rend le défilement', async ()=>{
  await p.keyboard.press('Escape');
  return p.evaluate(()=>document.getElementById('vrl').hidden===true&&document.documentElement.style.overflow==='');
});
await t('un abonné connu passe sans modale', ()=>p.evaluate(()=>{
  localStorage.setItem('lmg_sub','true');
  let navigue=false; const a=document.querySelector('[data-depot]');
  a.addEventListener('click',e=>{ if(!e.defaultPrevented) navigue=true; e.preventDefault(); },{once:true});
  a.click();
  return navigue && document.getElementById('vrl').hidden===true;
}));
await t('après envoi, le verrou s’ouvre et la clé est posée', async ()=>{
  await p.evaluate(()=>{ localStorage.removeItem('lmg_sub');
    document.cookie='lmg_sub=;path=/;max-age=0';
    document.getElementById('vrl-f').setAttribute('action','about:blank'); });
  await p.evaluate(()=>document.querySelector('[data-depot]').click());
  await p.type('#vrl-e','test@exemple.fr');
  await p.evaluate(()=>document.getElementById('vrl-f').requestSubmit());
  await new Promise(r=>setTimeout(r,1200));
  return p.evaluate(()=>document.getElementById('vrl').classList.contains('done')
    && localStorage.getItem('lmg_sub')==='true');
});
console.log(ok.join('\n'));
console.log('\n' + (ok.every(l=>l.startsWith('  ok')) ? 'TOUS LES CONTROLES PASSENT' : 'AU MOINS UN ECHEC'));
await b.close(); srv.close();
