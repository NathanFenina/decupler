# -*- coding: utf-8 -*-
"""Construit la page « Site gratuit » pour entreprises locales (artisans,
libéraux, médical) — première des 3 pages de la campagne rentrée (locale,
puis PME, puis freelance/agence SEO).

    python3 content/pages-src/build_local.py

Sort content/articles/site-gratuit-local.html, prêt pour wp_publish.py.
Formulaire dédié (voir form_local.py), écrit dans Supabase (projet
« LinkedIn App », table `candidatures_local`).
"""
import sys, re, json
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
for d in ('content/components', 'scripts/lib'):
    sys.path.insert(0, str(RACINE / d))
import form_local as FORM
import wpcss

SKIN = open(RACINE / 'content/skins/dcp.css', encoding='utf-8').read()
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Syne:wght@700;800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700'
         '&family=JetBrains+Mono:wght@400;700&display=swap">')

CLOTURE = FORM.CLOTURE
PLACES = FORM.PLACES
MAJ = '24 août 2026'
# Photo deja en ligne (page /site-internet-offert/), meme recit
# artisan/appel-manque : on la reutilise plutot que d'en regenerer une.
PHOTO_HERO = 'https://decupler.com/wp-content/uploads/2026/08/offre-hero.jpg'
PHOTO_HERO_ALT = "Un artisan en fin de journée regarde son téléphone : le SMS automatique a retenu le client qu'il n'a pas pu prendre"

TEASER_CSS = """<style>
.rt-trust{font-family:var(--mono);font-size:.78rem;letter-spacing:.04em;color:var(--faint);margin:14px 0 0}
.rt-trust b{color:var(--ink);font-weight:700}
</style>"""

CALENDRIER = [
    ("Vous candidatez", "Deux minutes, quelques questions sur votre activité et votre situation actuelle."),
    (f"On sélectionne {PLACES} profils", f"On regarde le besoin réel, pas qui a répondu en premier. Clôture {CLOTURE}."),
    ("On vous appelle", "Retenu : on vous appelle pour caler la suite. Pas retenu cette fois : on vous prévient quand même, par téléphone ou email."),
]
calendrier_html = "".join(
    f'<div class="et-l rise"><div class="num"></div><div><h3>{h}</h3><p>{p}</p></div></div>'
    for h, p in CALENDRIER)

FAQ = [
    ("C'est vraiment gratuit&nbsp;? Où est le piège&nbsp;?",
     "Il n'y en a pas, et ce n'est pas un cadeau&nbsp;: c'est un échange. On lance une nouvelle offre d'agents IA pour les entreprises locales et on a besoin de cas documentés, avec des résultats réels, pour la faire connaître. En échange du site offert, on vous demande un retour honnête sur ce que ça change pour vous."),
    ("Pourquoi un formulaire et pas juste premier arrivé, premier servi&nbsp;?",
     f"Parce qu'on n'a que {PLACES} places pour cette édition, et qu'on préfère les donner aux métiers où le site va vraiment changer quelque chose&nbsp;— pas aux plus rapides à cliquer."),
    ("Je ne suis pas retenu&nbsp;: je repars les mains vides&nbsp;?",
     "Non. Chaque candidature reçoit une réponse, que vous soyez sélectionné ou non."),
    ("Après le site gratuit, je suis obligé de payer quelque chose&nbsp;?",
     "Non. Le site reste à vous, gratuitement. Si vous voulez ensuite qu'on s'occupe des appels manqués, des devis ou de votre visibilité, c'est une option&nbsp;— jamais une obligation."),
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
    <h1 class="rise">Un site moderne, <em>offert</em>, aux artisans, libéraux et professionnels de santé qui candidatent.</h1>
    <p class="lead rise">On lance une nouvelle offre d'agents IA pour les entreprises locales (rattraper les appels manqués, relancer les devis, récolter les avis). Pour la faire connaître, on offre le site à {PLACES} professionnels&nbsp;— en échange d'un retour honnête sur ce que ça change pour vous.</p>
    <p class="lead rise">Deux minutes pour candidater. On répond à tout le monde avant le {CLOTURE}.</p>
    <div class="dcp-act rise"><a class="dcp-cta" href="#candidature-form" rel="noopener">Candidater</a></div>
    <p class="rt-trust rise">Déjà au travail avec <b>Apogea</b> · <b>Pluxee</b> · <b>BeTomorrow</b></p>
  </div>
</div></section>

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">Comment ça se passe</div>
  <h2 class="rise">Trois étapes, et une place n'est jamais donnée au hasard</h2>
  <div class="etapes">{calendrier_html}</div>
</div></section>

<section class="dcp-sec"><div class="in">
  {FORM.render(photo_url=PHOTO_HERO, photo_alt=PHOTO_HERO_ALT)}
</div></section>

<section class="dcp-sec alt"><div class="in">
  <div class="eyebrow rise">FAQ</div>
  <h2 class="rise">Les questions qu'on nous pose</h2>
  {faq_html}
  <div class="dcp-sign rise">
    <p class="dcp-sign-t">Écrit par <strong>Nathan Fenina</strong>, fondateur de <strong>Décupler</strong>, agence SEO et GEO. Voir <a href="https://decupler.com/site-internet-offert/">l'offre site gratuit détaillée</a> et <a href="https://decupler.com/cas-clients/">nos cas clients</a>.</p>
    <p class="dcp-sign-d">Dernière mise à jour&nbsp;: {MAJ}</p>
  </div>
</div></section>

</div>
<div class="dcp-js"><script type="application/ld+json">{faq_ld}</script></div>
<div class="dcp-js"><noscript><style>.dcp .rise{{opacity:1;transform:none}}.dcp .ic-svg>*{{stroke-dashoffset:0}}</style></noscript></div>
<div class="dcp-js"><script>
(function(){{
  document.querySelectorAll('.entry-header,.entry-title,.ast-single-entry-banner,.page-header')
    .forEach(function(e){{e&&e.remove&&e.remove()}});
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
out = str(RACINE / 'content/articles/site-gratuit-local.html')
open(out, 'w', encoding='utf-8').write(BODY)
txt = re.sub(r'<[^>]+>', ' ', re.sub(r'<style.*?</style>|<script.*?</script>', '', BODY, flags=re.S))
print('écrit :', out, len(BODY), 'octets ·', len(txt.split()), 'mots')
