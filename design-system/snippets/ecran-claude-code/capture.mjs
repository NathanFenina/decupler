import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);
const pw = require('/opt/node22/lib/node_modules/playwright');
const b = await pw.chromium.launch({args:['--no-sandbox']});
for (const f of process.argv.slice(2)) {
  const p = await b.newPage({viewport:{width:1112,height:800},deviceScaleFactor:1.5});
  await p.goto('file://'+process.cwd()+'/'+f+'.html');
  await p.screenshot({path:f+'.png',fullPage:true}); await p.close();
}
await b.close();
