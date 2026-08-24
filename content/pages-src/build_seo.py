# -*- coding: utf-8 -*-
"""Construit la page « Mini-analyse GEO gratuite » pour freelances et
agences SEO — decupler.com/mini-analyse-geo-seo.

    python3 content/pages-src/build_seo.py

Sort content/articles/mini-analyse-geo-seo.html, prêt pour wp_publish.py.
Formulaire dédié (voir form_seo.py), écrit dans Supabase (projet
« LinkedIn App », table `candidatures_seo`).
"""
import sys, re, json
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
for d in ('content/components', 'scripts/lib'):
    sys.path.insert(0, str(RACINE / d))
import form_seo as FORM
import wpcss

SKIN = open(RACINE / 'content/skins/dcp.css', encoding='utf-8').read()
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Syne:wght@700;800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700'
         '&family=JetBrains+Mono:wght@400;700&display=swap">')

CLOTURE = FORM.CLOTURE
PLACES = FORM.PLACES

TEASER_CSS = """<style>
.rt-trust{font-family:var(--mono);font-size:.78rem;letter-spacing:.04em;color:var(--faint);margin:14px 0 0}
.rt-trust b{color:var(--ink);font-weight:700}
</style>"""

CALENDRIER = [
    ("Vous candidatez", "Deux minutes, quelques questions sur votre activité et ce que vous avez déjà essayé."),
    (f"On sélectionne {PLACES} profils", f"On regarde le fit réel, pas qui a répondu en premier. Clôture {CLOTURE}."),
    ("On vous appelle", "Retenu : on vous appelle pour caler la suite et vous envoyer la mini-analyse. Pas retenu cette fois&nbsp;: on vous prévient quand même."),
]
calendrier_html = "".join(
    f'<div class="et-l rise"><div class="num"></div><div><h3>{h}</h3><p>{p}</p></div></div>'
    for h, p in CALENDRIER)

FAQ = [
    ("C'est vraiment gratuit&nbsp;? Où est le piège&nbsp;?",
     "Il n'y en a pas, et ce n'est pas un cadeau&nbsp;: c'est un échange. On lance une nouvelle offre d'infrastructure GEO et on a besoin de retours honnêtes de la part de freelances et d'agences qui vivent le SEO au quotidien. En échange de la mini-analyse offerte pour un de vos clients, on vous demande ce retour."),
    ("La mini-analyse, c'est quoi exactement&nbsp;?",
     "Une analyse GEO ciblée sur le domaine de votre client&nbsp;: les prompts où ses concurrents apparaissent dans ChatGPT/Perplexity et lui non, et ses angles morts. Prête à envoyer, à votre marque."),
    ("Je n'ai pas envie de vous revendre quoi que ce soit, je peux quand même candidater&nbsp;?",
     "Oui. L'option « la mini-analyse gratuite, pour voir » n'engage à rien derrière."),
    ("Pourquoi la question sur ce que j'ai déjà payé ces 12 derniers mois&nbsp;?",
     "Parce que c'est plus honnête que ce qu'on déclare être prêt à payer. Ça nous aide à savoir à qui on parle, pas à vous juger."),
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
    <div class="eyebrow rise">Candidatures ouvertes · {PLACES} places · clôture {CLOTURE}</div>
    <h1 class="rise">Une mini-analyse GEO <em>offerte</em>, à votre marque, aux freelances et agences SEO qui candidatent.</h1>
    <p class="lead rise">On lance une nouvelle offre d'infrastructure GEO. Pour la faire connaître, on offre à {PLACES} freelances et agences une mini-analyse GEO pour l'un de leurs clients — prête à envoyer, à leur nom — en échange d'un retour honnête sur ce qu'ils en pensent.</p>
    <p class="lead rise">Deux minutes pour candidater. On répond à tout le monde avant le {CLOTURE}.</p>
    <div class="dcp-act rise"><a class="dcp-cta" href="#candidature-form" data-open-form rel="noopener">Candidater</a></div>
    <p class="rt-trust rise">On a aussi travaillé avec <b>Sodexo</b> · <b>Décathlon</b> · <b>Société Générale</b></p>
  </div>
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
