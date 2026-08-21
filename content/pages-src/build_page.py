# -*- coding: utf-8 -*-
"""Assemble une page Décupler à partir d'une liste de sections déclarées.

    python3 content/pages-src/build_page.py agent-vocal-ia

Les pages métier ont leur propre générateur (build_metier.py) parce qu'elles
suivent toutes exactement la même trame. Ici, chaque page décrit ses sections :
c'est ce qu'il faut pour un guide (intention informationnelle) et pour une page
agent (intention commerciale), qui n'ont pas la même architecture.

Skin, icônes et catalogue d'agents sont ceux de la page pilier : une page du
cluster ne réinvente rien. Les audits wpcss sont des assertions.
"""
import sys, re, json
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
for d in ('content/data', 'content/components', 'scripts/lib'):
    sys.path.insert(0, str(RACINE / d))
sys.path.insert(0, str(Path(__file__).resolve().parent))
import agents_locaux as A
import pages_cluster as PC
import cta_prompts as CTA
import wpcss
import icones as I
sys.path.insert(0, str(RACINE / 'content/components'))
from visuels import VIZ

SKIN = open(RACINE / 'content/skins/dcp.css', encoding='utf-8').read()
FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Syne:wght@700;800&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700'
         '&family=JetBrains+Mono:wght@400;700&display=swap">')
PAR_SLUG = {s: (n, p) for s, n, _, p, _, _ in A.AGENTS}


# ── Blocs ────────────────────────────────────────────────────────────────────

def _cartes(items, balise='h3', classe=''):
    """Grille de cartes (icône, titre, texte). Enfants tous block : wpautop
    n'a aucune ligne vide ni enfant inline où glisser un </p> orphelin."""
    out = ''
    for ic, titre, txt in items:
        out += (f'<div class="ag2 {classe} rise">{I.bloc(ic, "ag2-ic")}'
                f'<div class="ag2-tx"><{balise}>{titre}</{balise}><p>{txt}</p></div></div>')
    return f'<div class="ag-grille">{out}</div>'


def hero(d, page):
    visuel = ''
    if d.get('image'):
        img, alt = d['image']
        visuel = (f'<div class="photo"><img src="{img}" alt="{alt}" width="1536" height="1024" '
                  f'loading="eager" decoding="async"></div>')
    elif d.get('viz'):
        visuel = VIZ[d['viz']].replace(' rise', '')
    tel = ''
    if d.get('phone'):
        lignes = ''
        for e in d['phone']:
            tag = f'<span class="evt-tag">{e[3]}</span>' if len(e) > 3 else ''
            lignes += f'<div class="evt evt-{e[0]}"><b>{e[1]}</b><span>{e[2]}</span>{tag}</div>'
        tel = ('<div class="phone"><div class="phone-scr">'
               '<div class="phone-top"><div class="phone-notch"></div></div>'
               f'<div class="phone-body">{lignes}</div></div></div>')
    leads = ''.join(f'<p class="lead">{t}</p>' for t in d['leads'])
    return f"""<section class="dcp-hero"><div class="in dcp-grid">
  <div>
    <h1><span class="k">{d['kicker']}</span>{d['h1']}</h1>
    {leads}
    <div class="dcp-act"><a class="dcp-cta" href="{PC.RDV}" rel="noopener">{d.get('cta', 'Voir mon site avant de décider')}</a></div>
    <p class="dcp-under">{d.get('sous_cta', 'Site 0&nbsp;€ · puis dès 199&nbsp;€/mois')}</p>
  </div>
  <div class="hero-visuel{' seul' if not d.get('image') else ''}">
    {visuel}
    {tel}
  </div>
</div></section>"""


def bande(d, page):
    g, gc, dr, dc = d['cnt']
    return f"""<section class="dcp-band"><div class="in">
  <div class="cnt lost">{I.bloc(d.get('ic_g', 'sms-appel-manque'), "cnt-ic")}<p class="lbl">{d['lbl_g']}</p><p class="num">{g}</p><p class="cap">{gc}</p></div>
  <div class="arrow">→</div>
  <div class="cnt won">{I.bloc(d.get('ic_d', 'sms-formulaire'), "cnt-ic")}<p class="lbl">{d['lbl_d']}</p><p class="num">{dr}</p><p class="cap">{dc}</p></div>
</div></section>"""


def texte(d, page):
    alt = ' alt' if d.get('alt') else ''
    corps = ''.join(f'<p class="lead rise">{t}</p>' for t in d['paras'])
    photo = ''
    if d.get('image'):
        img, a = d['image']
        photo = (f'<div class="photo rise"><img src="{img}" alt="{a}" width="1536" height="1024" '
                 f'loading="lazy" decoding="async"></div>')
        if d.get('legende'):
            photo += f'<p class="photo-cap rise">{d["legende"]}</p>'
    tip = ''
    if d.get('tip'):
        tip = f'<div class="dcp-tip rise"><div class="ic">{d.get("tip_ic", "💡")}</div><p>{d["tip"]}</p></div>'
    ancre = f' id="{d["id"]}"' if d.get('id') else ''
    return f"""<section class="dcp-sec{alt}"{ancre}><div class="in">
  <div class="eyebrow rise">{d['eyebrow']}</div>
  <h2 class="rise">{d['h2']}</h2>
  {corps}{photo}{tip}
</div></section>"""


def reponse(d, page):
    """Bloc de réponse directe, écrit pour être extrait tel quel par un moteur
    génératif : une question en H2, deux ou trois phrases autonomes."""
    alt = ' alt' if d.get('alt') else ''
    return f"""<section class="dcp-sec{alt}"><div class="in">
  <div class="eyebrow rise">{d['eyebrow']}</div>
  <h2 class="rise">{d['h2']}</h2>
  <div class="dcp-rep rise"><p>{d['reponse']}</p></div>
  {''.join(f'<p class="lead rise">{t}</p>' for t in d.get('paras', []))}
</div></section>"""


def cartes(d, page):
    alt = ' alt' if d.get('alt') else ''
    ancre = f' id="{d["id"]}"' if d.get('id') else ''
    chapo = ''.join(f'<p class="lead rise">{t}</p>' for t in d.get('paras', []))
    src = ''
    if d.get('sources'):
        liens = ', '.join(f'<a href="{u}" rel="nofollow noopener" target="_blank">{t}</a>' for t, u in d['sources'])
        src = f'<p class="dcp-src rise">Sources&nbsp;: {liens}.</p>'
    tip = ''
    if d.get('tip'):
        tip = f'<div class="dcp-tip rise"><div class="ic">{d.get("tip_ic", "💡")}</div><p>{d["tip"]}</p></div>'
    return f"""<section class="dcp-sec{alt}"{ancre}><div class="in">
  <div class="eyebrow rise">{d['eyebrow']}</div>
  <h2 class="rise">{d['h2']}</h2>
  {chapo}{_cartes(d['items'], classe=d.get('classe', ''))}{tip}{src}
</div></section>"""


def etapes(d, page):
    alt = ' alt' if d.get('alt') else ''
    lignes = ''.join(f'<div class="et-l rise"><div class="num"></div><div><h3>{t}</h3><p>{p}</p></div></div>'
                     for t, p in d['items'])
    return f"""<section class="dcp-sec{alt}"><div class="in">
  <div class="eyebrow rise">{d['eyebrow']}</div>
  <h2 class="rise">{d['h2']}</h2>
  {''.join(f'<p class="lead rise">{t}</p>' for t in d.get('paras', []))}
  <div class="etapes">{lignes}</div>
</div></section>"""


def tableau(d, page):
    alt = ' alt' if d.get('alt') else ''
    thead = ''.join(f'<th>{c}</th>' for c in d['colonnes'])
    tbody = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in ligne) + '</tr>' for ligne in d['lignes'])
    return f"""<section class="dcp-sec{alt}"><div class="in">
  <div class="eyebrow rise">{d['eyebrow']}</div>
  <h2 class="rise">{d['h2']}</h2>
  {''.join(f'<p class="lead rise">{t}</p>' for t in d.get('paras', []))}
  <table class="rise"><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>
</div></section>"""


def agents(d, page):
    alt = ' alt' if d.get('alt') else ''
    items = []
    for s in d['slugs']:
        nom, promesse = PAR_SLUG[s]
        titre = f'<a href="{A.LIENS[s]}">{nom}</a>' if s in A.LIENS else nom
        items.append((s, titre, promesse))
    return f"""<section class="dcp-sec{alt}"><div class="in">
  <div class="eyebrow rise">{d['eyebrow']}</div>
  <h2 class="rise">{d['h2']}</h2>
  {''.join(f'<p class="lead rise">{t}</p>' for t in d.get('paras', []))}
  {_cartes(items)}
</div></section>"""


def relance(d, page):
    alt = ' alt' if d.get('alt') else ''
    return f"""<section class="dcp-sec{alt}"><div class="in">
  <div class="dcp-mini rise"><p class="dcp-mini-t">{d['texte']}</p>
  <p class="dcp-mini-a"><a class="dcp-cta" href="{PC.RDV}" rel="noopener">{d.get('libelle', 'Prendre 15 minutes')}</a></p></div>
</div></section>"""


def faq(d, page):
    alt = ' alt' if d.get('alt') else ''
    blocs = ''.join(f'<details class="rise"><summary>{q}</summary><p>{a}</p></details>' for q, a in d['items'])
    return f"""<section class="dcp-sec{alt}"><div class="in">
  <div class="eyebrow rise">{d['eyebrow']}</div>
  <h2 class="rise">{d['h2']}</h2>
  {blocs}
  <div class="dcp-sign rise">
    <p class="dcp-sign-t">Écrit par <strong>Nathan Fenina</strong>, fondateur de <strong>Décupler</strong>, agence SEO et GEO. {page.get('signature', '')} Voir <a href="https://decupler.com/cas-clients/">nos cas clients</a> et <a href="{PC.PILIER}">l'offre site offert</a>.</p>
    <p class="dcp-sign-d">Dernière mise à jour&nbsp;: {PC.MAJ}</p>
  </div>
</div></section>"""


def visuel(d, page):
    alt = ' alt' if d.get('alt') else ''
    return f"""<section class="dcp-sec{alt}"><div class="in">
  <div class="eyebrow rise">{d['eyebrow']}</div>
  <h2 class="rise">{d['h2']}</h2>
  {''.join(f'<p class="lead rise">{t}</p>' for t in d.get('paras', []))}
  <div class="viz-seul rise">{VIZ[d['viz']]}</div>
</div></section>"""


BLOCS = {'hero': hero, 'visuel': visuel, 'bande': bande, 'texte': texte, 'reponse': reponse, 'cartes': cartes,
         'etapes': etapes, 'tableau': tableau, 'agents': agents, 'relance': relance, 'faq': faq}


def construis(slug):
    page = PC.PAGES[slug]
    corps = ''.join(BLOCS[t](d, page) for t, d in page['sections'])

    fq = next((d['items'] for t, d in page['sections'] if t == 'faq'), [])
    ld = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": re.sub(r'&nbsp;|<[^>]+>', ' ', q).strip(),
         "acceptedAnswer": {"@type": "Answer", "text": re.sub(r'&nbsp;|<[^>]+>', ' ', a).strip()}}
        for q, a in fq]}, ensure_ascii=False)

    body = f"""{FONTS}
{SKIN}
<div class="dcp">
{corps}
</div>
{CTA.render('vous', href=PC.RDV)}
<div class="dcp-js"><script type="application/ld+json">{ld}</script></div>
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
</script></div>"""
    return wpcss.harden(body)


if __name__ == '__main__':
    slug = sys.argv[1]
    if slug not in PC.PAGES:
        sys.exit(f"❌ « {slug} » inconnu. Disponibles : {', '.join(PC.PAGES)}")
    body = construis(slug)
    for nom, audit in (('style', wpcss.audit), ('balisage', wpcss.audit_markup), ('structure', wpcss.audit_structure)):
        pb = audit(body)
        assert not pb, f'{nom} : ' + ' | '.join(pb[:5])
    out = RACINE / f'content/articles/{slug}.html'
    out.write_text(body, encoding='utf-8')
    mots = len(re.sub(r'<[^>]+>', ' ', re.sub(r'<style>.*?</style>|<script.*?</script>', '', body, flags=re.S)).split())
    print(f'écrit : {out.name} · {len(body)} octets · {mots} mots')
