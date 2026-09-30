#!/usr/bin/env bash
# Assemble /jev-seo/ (page 21035) : injecte la FAQ dans le gabarit, puis build_article.py.
# Usage : bash scripts/lead_magnet_jev_seo.sh   -> content/articles/jev-seo.html
set -e
cd /home/user/decupler && python3 - <<'PY'
import json,html
faq=json.load(open('content/articles/jev-seo.faq.json',encoding='utf-8'))
f='\n'.join(f'      <details><summary>{html.escape(q["question"])}</summary><p>{html.escape(q["answer"])}</p></details>' for q in faq)
req=html.escape(open('content/lead-magnets/kit-jev-seo-geo/requete-page.json',encoding='utf-8').read().rstrip(),quote=False)
t=open('content/articles/jev-seo.body.tpl.html',encoding='utf-8').read().replace('__FAQ__',f).replace('__REQ__',req)
assert '__' not in t.replace('__IMG','')
open('content/articles/jev-seo.body.html','w',encoding='utf-8').write(t)
PY
python3 scripts/build_article.py --body content/articles/jev-seo.body.html \
 --title "Jev SEO : l'audit SEO et GEO avec Jev (playbook gratuit)" \
 --description "Jev SEO : comment auditer ton site en SEO et GEO avec Jev et le skill jev-seo, lire les résultats et corriger dans le bon ordre. Testé sur notre site." \
 --faq content/articles/jev-seo.faq.json \
 --extra-css design-system/landing/lm-mcp-light.css design-system/landing/lm-mcp-decupler.css design-system/landing/lm-mcp-leadmagnet.css \
 --gate "https://decupler.substack.com" --gate-title "Accède au playbook Jev" \
 --gate-desc "Laisse ton email : tu débloques le playbook complet et tu reçois les prochains guides SEO et GEO." \
 --gate-delay 6000 --gate-param acces=linkedin --gate-soft-delay 25000 --out content/articles/jev-seo.html
