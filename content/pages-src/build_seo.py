# -*- coding: utf-8 -*-
"""Construit la page fusionnée « Cartographie / mini-analyse GEO gratuite »
— sert à la fois les PME/ETI et les freelances/agences SEO (fusion des 2
anciennes pages séparées ; l'URL survivante est mini-analyse-geo-seo).

    python3 content/pages-src/build_seo.py

Sort content/articles/mini-analyse-geo-seo.html, prêt pour wp_publish.py
(publier avec --id 20716 pour mettre à jour la page existante en place).
Formulaire dédié (voir form_seo_pme.py) : Q0 route vers 3 branches (SEO /
PME-ETI / Autre), chacune vers sa propre table Supabase.
"""
import sys, re, json
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
for d in ('content/components', 'scripts/lib'):
    sys.path.insert(0, str(RACINE / d))
import form_seo_pme as FORM
import wpcss

SKIN = open(RACINE / 'content/skins/dcp.css', encoding='utf-8').read()
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Syne:wght@700;800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700'
         '&family=JetBrains+Mono:wght@400;700&display=swap">')

CLOTURE = FORM.CLOTURE

TEASER_CSS = """<style>
.rt-trust{font-family:var(--mono);font-size:.78rem;letter-spacing:.04em;color:var(--faint);margin:14px 0 0}
.rt-trust b{color:var(--ink);font-weight:700}
.rt-tri{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:26px 0 4px}
.rt-c{background:#fff;border:1px solid var(--edge);border-radius:14px;padding:22px 20px 24px;transition:transform .22s,box-shadow .22s,border-color .22s}
.rt-c:hover{transform:translateY(-3px);border-color:var(--vio);box-shadow:0 18px 36px -18px rgba(123,92,250,.35)}
.rt-c .eyebrow{margin:0 0 12px}
.rt-c h3{font-family:var(--display);font-size:1.05rem;font-weight:800;color:var(--ink);margin:0 0 8px;line-height:1.3}
.rt-c p{font-size:.88rem;line-height:1.55;color:var(--soft);margin:0}
@media(max-width:820px){.rt-tri{grid-template-columns:1fr}}
</style>"""

TEASERS = [
    ("Agence / freelance SEO", "Mini-analyse GEO, à votre marque",
     "Une analyse GEO prête à envoyer à l'un de vos clients, sous votre nom — zéro effort de votre côté."),
    ("PME / ETI", "Cartographie GEO de votre marché",
     "Les prompts où vos concurrents sortent et vous non, vos angles morts, vos pages qui ne convertissent pas."),
    ("Autre profil", "On regarde quand même",
     "Association, indépendant, startup… le formulaire s'adapte, précisez simplement votre situation."),
]
teaser_html = "".join(
    f'<div class="rt-c rise"><div class="eyebrow">{eb}</div><h3>{h}</h3><p>{p}</p></div>'
    for eb, h, p in TEASERS)

CALENDRIER = [
    ("Vous candidatez", "Le formulaire route automatiquement selon votre profil — deux minutes, pas plus."),
    ("On sélectionne", "On regarde le fit réel, pas qui a répondu en premier. Clôture " + CLOTURE + "."),
    ("On vous appelle", "Retenu : on vous appelle pour caler la suite. Pas retenu cette fois&nbsp;: on vous prévient quand même."),
]
calendrier_html = "".join(
    f'<div class="et-l rise"><div class="num"></div><div><h3>{h}</h3><p>{p}</p></div></div>'
    for h, p in CALENDRIER)

FAQ = [
    ("C'est vraiment gratuit&nbsp;? Où est le piège&nbsp;?",
     "Il n'y en a pas, et ce n'est pas un cadeau&nbsp;: c'est un échange. On lance une nouvelle offre d'infrastructure GEO et on a besoin de retours honnêtes, de la part de PME comme de freelances et d'agences SEO. En échange de l'analyse offerte, on vous demande ce retour."),
    ("La cartographie / mini-analyse, c'est quoi exactement&nbsp;?",
     "Les prompts où vos concurrents (ou ceux de votre client) apparaissent dans ChatGPT, Perplexity et les AI&nbsp;Overviews et vous non, et les angles morts sur votre marché. Prête à utiliser, ou à envoyer si vous êtes une agence."),
    ("Pourquoi un formulaire et pas juste premier arrivé, premier servi&nbsp;?",
     "Parce que les places sont limitées et réparties par profil, et qu'on préfère les donner là où l'impact sera le plus net&nbsp;— pas aux plus rapides à cliquer."),
    ("Je ne suis pas retenu&nbsp;: je repars les mains vides&nbsp;?",
     "Non. Chaque candidature reçoit une réponse, que vous soyez sélectionné ou non."),
]
faq_html = ''.join(f'<details class="rise"><summary>{q}</summary><p>{a}</p></details>' for q, a in FAQ)
faq_ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": re.sub(r'&nbsp;|<[^>]+>', ' ', q).strip(),
     "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'&nbsp;|<[^>]+>', ' ', a).strip()}} for q, a in FAQ
]}, ensure_ascii=False)

BODY = f"""{FONTS}
{SKIN}
{TEASER_CSS}
<div class="dcp">

<section class="dcp-hero"><div class="in">
  <div style="max-width:680px">
    <div class="eyebrow rise">Candidatures ouvertes · clôture {CLOTURE}</div>
    <h1 class="rise">La cartographie GEO de votre marché, <em>offerte</em>, aux PME/ETI et aux pros du SEO qui candidatent.</h1>
    <p class="lead rise">On lance une nouvelle offre d'infrastructure GEO. Pour la faire connaître, on offre une cartographie ou une mini-analyse GEO à un nombre limité de candidats — en échange d'un retour honnête sur ce que ça change pour vous.</p>
    <p class="lead rise">Un seul formulaire ci-dessous&nbsp;: il s'adapte à votre profil. Deux minutes pour candidater, on répond à tout le monde avant le {CLOTURE}.</p>
    <div class="dcp-act rise"><a class="dcp-cta" href="#candidature-form" data-open-form rel="noopener">Candidater</a></div>
    <p class="rt-trust rise">On a aussi travaillé avec <b>Sodexo</b> · <b>Décathlon</b> · <b>Société Générale</b></p>
  </div>
</div></section>

<section class="dcp-sec"><div class="in">
  <div class="eyebrow rise">Deux portes, un seul formulaire</div>
  <h2 class="rise">Vous candidatez, on ne devine pas à votre place.</h2>
  <p class="lead rise">La première question du formulaire route automatiquement vers ce qui vous concerne&nbsp;: pas besoin de savoir où cliquer.</p>
  <div class="rt-tri">{teaser_html}</div>
</div></section>

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">Comment ça se passe</div>
  <h2 class="rise">Trois étapes, et une place n'est jamais donnée au hasard</h2>
  <div class="etapes">{calendrier_html}</div>
  <div class="dcp-mini rise"><p class="dcp-mini-t">Prêt à candidater&nbsp;? Ça prend deux minutes.</p>
  <p class="dcp-mini-a"><a class="dcp-cta" href="#candidature-form" data-open-form rel="noopener">Candidater</a></p></div>
</div></section>

{FORM.render()}

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">FAQ</div>
  <h2 class="rise">Les questions qu'on nous pose</h2>
  {faq_html}
</div></section>

</div>
<div class="dcp-js"><script type="application/ld+json">{faq_ld}</script></div>
<div class="dcp-js"><noscript><style>.dcp .rise{{opacity:1;transform:none}}.dcp .ic-svg>*{{stroke-dashoffset:0}}</style></noscript></div>
<div class="dcp-js"><script>
(function(){{
  document.querySelectorAll('.entry-header,.entry-title,.ast-single-entry-banner,.page-header')
    .forEach(function(e){{if(e){{if(e.remove){{e.remove()}}}}}});
  function bleed(){{
    var d=document.querySelector('.dcp'); if(!d) return;
    var r=d.getBoundingClientRect(), w=document.documentElement.clientWidth, st=document.documentElement.style;
    st.setProperty('--dcp-bl', Math.min(400,Math.max(0,Math.round(r.left)))+'px');
    st.setProperty('--dcp-br', Math.min(400,Math.max(0,Math.round(w-r.right)))+'px');
  }}
  bleed();
  var t; addEventListener('resize',function(){{clearTimeout(t);t=setTimeout(bleed,120)}});
  addEventListener('load',bleed);
  var els=document.querySelectorAll('.dcp .rise');
  function showAll(){{for(var i=0;i<els.length;i++)els[i].classList.add('vu')}}
  if(!('IntersectionObserver' in window)){{showAll();return}}
  var io=new IntersectionObserver(function(en){{
    en.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('vu');io.unobserve(e.target)}}}})
  }},{{rootMargin:'0px 0px -8% 0px',threshold:.05}});
  for(var i=0;i<els.length;i++)io.observe(els[i]);
  setTimeout(showAll,2500);
}})();
</script></div>
"""

BODY = wpcss.harden(BODY)
probs = wpcss.audit(BODY)
assert not probs, probs
risques = wpcss.audit_markup(BODY)
assert not risques, f'{len(risques)} conteneur(s) que wpautop cassera : {risques[:3]}'
struct = wpcss.audit_structure(BODY)
assert not struct, f'{len(struct)} probleme(s) de structure : {struct[:3]}'
out = str(RACINE / 'content/articles/mini-analyse-geo-seo.html')
open(out, 'w', encoding='utf-8').write(BODY)
txt = re.sub(r'<[^>]+>', ' ', re.sub(r'<style.*?</style>|<script.*?</script>', '', BODY, flags=re.S))
print('écrit :', out, len(BODY), 'octets ·', len(txt.split()), 'mots')
