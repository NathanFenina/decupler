#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble une page ville a partir de blocs rediges ville par ville.

Le CSS et la charpente sont communs — c'est du design, pas du contenu. Ce qui
doit etre unique par ville, ce sont les blocs de `contenu/{slug}.py` : accroche,
contexte local, points de ranking, etapes, preuves, zone, budget, FAQ. C'est la
separation exigee par le §6 du SKILL, celle qui evite les 40 % de phrases
communes d'un premier jet naif.

Deux registres (cf. _registres dans villes.json) :
  agence      — entite Decupler, voix « nous », schema ProfessionalService
  consultant  — entite Nathan Fenina, voix « je », schema Person

    python3 build_ville.py --slug agence-seo-toulon --sortie build/
"""
import argparse
import html
import importlib.util
import json
import os
import re

ICI = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(ICI)
CSS = os.path.join(SKILL, "assets", "skin-ville.css")
VILLES = os.path.join(SKILL, "references", "villes.json")
CONTENU = os.path.join(SKILL, "contenu")

CAL = "https://calendly.com/fenina-nathan/consultationstrategique"
LI = "https://www.linkedin.com/in/nathan-fenina/"
PHOTO_NATHAN = ("https://decupler.com/wp-content/uploads/2026/09/nathan-fenina-portrait.jpg")
PHOTO_NATHAN_LARGE = ("https://decupler.com/wp-content/uploads/2026/09/nathan-fenina-nice.jpg")
# Bande des moteurs : Google, Perplexity, Claude, OpenAI. Actif deja en
# ligne et deja utilise sur la home — on ne cree pas d'exposition de
# marque supplementaire, et le visuel reste coherent avec le reste du site.
MOTEURS = ("https://decupler.com/wp-content/uploads/2025/10/Sans-titre-200-x-70-px-2.png")
LOGOS = [
    ("decathlon.png", "Decathlon", 376, 126),
    ("le-point.png", "Le Point", 378, 138),
    ("sg.png", "Société Générale", 226, 223),
    ("Capture-decran-2025-10-29-084038.png", "Cdiscount", 314, 90),
    ("kazidomi.png", "Kazidomi", 432, 132),
    ("outdoorsy-.png", "Outdoorsy", 444, 132),
    ("Capture-decran-2025-10-29-084247.png", "Atoo Énergie", 342, 134),
]


def charge_contenu(slug):
    chemin = os.path.join(CONTENU, slug.replace("-", "_") + ".py")
    if not os.path.exists(chemin):
        raise SystemExit(f"❌ blocs rediges manquants : {chemin}\n"
                         "   Les ecrire ville par ville — ne jamais dupliquer.")
    spec = importlib.util.spec_from_file_location("blocs_" + slug, chemin)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.BLOCS


def fiche(slug):
    d = json.load(open(VILLES, encoding="utf-8"))
    for v in d["villes"]:
        if v["slug"] == slug:
            return v, d
    raise SystemExit(f"❌ {slug} absent de villes.json — y ajouter sa fiche "
                     "(codes postaux, communes, secteurs) avant de rediger.")


def txt(x):
    """Texte nu pour le JSON-LD : entites decodees, balises retirees."""
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()


def bloc_logos():
    sortie = ['<div class="logos" data-dcp="chrome">',
              '<div class="lb">Elles nous font confiance</div>', '<div class="gr">']
    for f, alt, w, h in LOGOS:
        sortie.append(
            f'<div class="cell"><img src="https://decupler.com/wp-content/uploads/'
            f'2025/10/{f}" alt="{alt}" width="{w}" height="{h}" loading="lazy"></div>')
    return sortie + ["</div>", "</div>"]


# Observateur d'apparition. Deux garde-fous : on ne touche a l'opacite nulle
# part, et on n'ajoute la classe d'attente qu'en JS — donc un crawler sans JS
# voit la page a sa place definitive.
REVEAL = (
    "(function(){var r=document.querySelector('.dcp-v');if(!r)return;"
    "if(window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)')"
    ".matches)return;"
    "if(!('IntersectionObserver' in window))return;"
    "var c=r.querySelectorAll('.num2>div,.grid2>div,.bud>div,.comm>div,"
    ".vgrid>a,.steps>div,.decupler-faq-item,.fig,.mock,.tw');"
    "for(var i=0;i<c.length;i++){c[i].classList.add('dcp-att');}"
    "var o=new IntersectionObserver(function(es){es.forEach(function(e){"
    "if(e.isIntersecting){e.target.classList.add('dcp-vu');o.unobserve(e.target);}"
    "});},{rootMargin:'0px 0px -12% 0px',threshold:0.08});"
    "for(var j=0;j<c.length;j++){o.observe(c[j]);}})();"
)


def construis(slug):
    v, base = fiche(slug)
    b = charge_contenu(slug)
    reg = v.get("registre", "agence")
    ville = v["ville"]
    siege = base["_siege"]
    o = []
    a = o.append

    a('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
      'family=Sora:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap">')
    a("<style>")
    a(open(CSS, encoding="utf-8").read().rstrip())
    # La grille de logos est en flex dans le skin d'origine ; en grille elle
    # s'aligne vraiment, ce que le releve du 22/09 a montre preferable.
    a(".dcp-v .logos .gr{display:grid;grid-template-columns:repeat(7,1fr);"
      "gap:clamp(14px,2vw,28px);align-items:center}")
    a(".dcp-v .logos .lb{margin-bottom:18px}")
    a("@media (max-width:920px){.dcp-v .logos .gr{grid-template-columns:repeat(4,1fr);"
      "row-gap:22px}}")
    a("@media (max-width:520px){.dcp-v .logos .gr{grid-template-columns:repeat(3,1fr)}}")
    a("</style>")

    # ── hero ───────────────────────────────────────────────────────────────
    a('<div class="dcp-v">')
    a('<div class="hero">')
    a('<div class="in">')
    a('<div class="hgrid">')
    a('<div class="st">')
    a(f'<div><span class="pill a1">{b["pill"]}</span></div>')
    a(f'<h1 class="a2">{b["h1"]}</h1>')
    for p in b["lead"]:
        a(f'<p class="lead nr a2">{p}</p>')
    a(f'<div class="row a3"><a class="btn" href="{CAL}">{b["cta1"]}</a>'
      f'<a class="btn-o" href="{b["cta2_url"]}">{b["cta2"]}</a></div>')
    a(f'<p class="sub a3">{b["micro"]}</p>')
    a("</div>")
    if b.get("visuel"):
        src, alt, w, h, bk, bv = b["visuel"]
        a('<div class="hvis a3">')
        # Le rapport du cadre suit celui de la source : forcer une photo
        # paysage dans un cadre portrait la charcute (premier essai : le
        # visage sortait du cadre). Portrait -> 4/5, paysage -> 4/3.
        classe = "ph2" if h > w else "ph2 pay"
        a(f'<div class="{classe}"><img src="{src}" alt="{alt}" '
          f'width="{w}" height="{h}">')
        a(f'<div class="bdg"><div class="k">{bk}</div><div class="v">{bv}</div></div>')
        a("</div>")
        a('<div class="mot">')
        a('<div class="l">Moteurs suivis</div>')
        a(f'<div class="mi"><img src="{MOTEURS}" alt="Google, Perplexity, Claude '
          f'et ChatGPT" width="400" height="140" loading="lazy"></div>')
        a("</div>")
        # La colonne de droite laissait un vide sous la bande des moteurs. On
        # le remplit avec une preuve chiffree et sourcee plutot qu'avec de
        # l'air : un chiffre attribue, haut dans la page, qui mene a l'etude.
        if b.get("hero_preuve"):
            chiffre, libelle, url = b["hero_preuve"]
            a(f'<div class="hcell"><a class="hpr" href="{url}">')
            a(f'<div class="n">{chiffre}</div>')
            a(f'<div class="l">{libelle}</div>')
            a('<div class="f">Voir l\'étude de cas</div>')
            a("</a>")
            a("</div>")
        a("</div>")
    else:
        a('<div class="cards a3">')
        for k, val in b["cards"]:
            a(f'<div class="card"><div class="k">{k}</div>'
              f'<div class="v">{val}</div></div>')
        a("</div>")
    a("</div>")
    a('<div class="trust">')
    for n, l in b["trust"]:
        a(f'<div><div class="n">{n}</div><div class="l">{l}</div></div>')
    a("</div>")
    for x in bloc_logos():
        a(x)
    a("</div>")
    a("</div>")

    # ── 1. pourquoi ────────────────────────────────────────────────────────
    a('<div class="bl">')
    a('<div class="in st-s">')
    a(f'<h2>{b["h2_pourquoi"]}</h2>')
    for p in b["pourquoi"]:
        a(f'<p class="lead nr">{p}</p>')
    a(f'<div class="row" style="margin-top:8px"><a class="btn" href="{CAL}">'
      f'{b["cta_pourquoi"]}</a></div>')
    a("</div>")
    a("</div>")

    # ── 2. ce qui fait ranker ──────────────────────────────────────────────
    a('<div class="bl bl-lav">')
    a('<div class="in st-s">')
    a(f'<h2>{b["h2_ranker"]}</h2>')
    a(f'<p class="lead nr">{b["ranker_intro"]}</p>')
    a('<div class="num2">')
    for i, (t, d) in enumerate(b["ranker"], 1):
        a(f'<div><div class="b">{i}</div><h3>{t}</h3><div class="d">{d}</div></div>')
    a("</div>")
    a("</div>")
    a("</div>")

    # ── 3. methode ─────────────────────────────────────────────────────────
    a('<div class="bl">')
    a('<div class="in">')
    a('<div class="split">')
    a('<div class="st-s">')
    a(f'<h2>{b["h2_methode"]}</h2>')
    a(f'<p class="lead nr">{b["methode_intro"]}</p>')
    a('<div class="steps">')
    for i, (t, d) in enumerate(b["methode"], 1):
        a(f'<div><div class="b">{i}</div><div class="t"><b>{t}</b> {d}</div></div>')
    a("</div>")
    a("</div>")
    if b.get("image"):
        src, alt, w, h, cap = b["image"]
        a(f'<div class="fig"><img src="{src}" alt="{alt}" width="{w}" height="{h}" '
          f'loading="lazy"><div class="cap">{cap}</div></div>')
    else:
        a('<div class="mock">')
        a(f'<div class="k">{b["mock_k"]}</div>')
        a(f'<div class="q">{b["mock_q"]}</div>')
        a('<div class="ans">')
        for on, t in b["mock_ans"]:
            a(f'<div class="{"on" if on else "off"}"><div class="dot"></div>'
              f'<div><span>{t}</span></div></div>')
        a("</div>")
        a(f'<div class="ft">{b["mock_ft"]}</div>')
        a("</div>")
    a("</div>")
    a("</div>")
    a("</div>")

    # ── 4. resultats ───────────────────────────────────────────────────────
    a('<div class="bl bl-lav">')
    a('<div class="in st-s">')
    a(f'<h2>{b["h2_preuve"]}</h2>')
    a(f'<p class="lead nr">{b["preuve_intro"]}</p>')
    # Grille a 2 colonnes : les blocs de preuve vont par 4, et en 3 colonnes la
    # quatrieme carte reste seule sur sa ligne — le defaut que le skill design
    # signale (« mettre un multiple du nombre de colonnes »).
    a('<div class="grid2 preuves">')
    for t, d, url, ancre in b["preuves"]:
        a(f'<div><h3>{t}</h3><div class="d">{d}</div>'
          f'<div style="margin-top:12px"><a class="lnk" href="{url}">{ancre}</a></div></div>')
    a("</div>")
    a(f'<p class="sub" style="margin-top:14px">{b["preuve_note"]}</p>')
    a("</div>")
    a("</div>")

    # ── 5. zone d'intervention ─────────────────────────────────────────────
    a('<div class="bl">')
    a('<div class="in st-s">')
    a(f'<h2>{b["h2_zone"]}</h2>')
    a(f'<p class="lead nr">{b["zone_intro"]}</p>')
    cp = " · ".join(v["codes_postaux"])
    a(f'<p class="lead nr">Codes postaux couverts : <span class="cp">{cp}</span>.</p>')
    a('<div class="comm">')
    # Le nom du departement repete sous chaque commune etait du bruit : il est
    # deja dit dans l'intro de la section et dans les codes postaux.
    for c in v["communes"]:
        a(f'<div><div class="n">{c}</div></div>')
    a("</div>")
    a(f'<p class="sub" style="margin-top:18px">{b["zone_note"]}</p>')
    a("</div>")
    a("</div>")

    # ── 6. budget ──────────────────────────────────────────────────────────
    a('<div class="bl bl-lav">')
    a('<div class="in st-s">')
    a(f'<h2>{b["h2_budget"]}</h2>')
    a(f'<p class="lead nr">{b["budget_intro"]}</p>')
    a('<div class="bud">')
    for f, q in b["budget"]:
        a(f'<div><div class="f">{f}</div><div class="q">{q}</div></div>')
    a("</div>")
    a(f'<p class="lead nr" style="margin-top:22px">{b["budget_note"]}</p>')
    a("</div>")
    a("</div>")

    # ── bandeau photo. Nathan : « il manque des photos ». Une photo reelle
    #    d'une personne identifiable vaut tous les visuels generes.
    if b.get("bandeau"):
        titre, paras, img = b["bandeau"]
        a('<div class="bl">')
        a('<div class="in">')
        a('<div class="band">')
        a('<div class="st-s">')
        a(f'<h2>{titre}</h2>')
        for pp in paras:
            a(f'<p class="lead nr">{pp}</p>')
        a(f'<div class="row"><a class="btn" href="{CAL}">{b["cta1"]}</a></div>')
        a("</div>")
        src, alt, w, h, cap = img
        a(f'<div class="fig"><img src="{src}" alt="{alt}" width="{w}" height="{h}" '
          f'loading="lazy"><div class="cap" data-dcp="chrome">{cap}</div></div>')
        a("</div>")
        a("</div>")
        a("</div>")

    # ── 7. le bloc qui absorbe les variantes de requete ────────────────────
    a('<div class="bl">')
    a('<div class="in st-s">')
    a(f'<h2>{b["h2_variantes"]}</h2>')
    for p in b["variantes"]:
        a(f'<p class="lead nr">{p}</p>')
    a("</div>")
    a("</div>")

    # ── 8. FAQ ─────────────────────────────────────────────────────────────
    a('<div class="bl bl-lav">')
    a('<div class="in st-s">')
    a(f'<h2>{b["h2_faq"]}</h2>')
    a('<div class="faq">')
    for q, r in b["faq"]:
        a('<div class="decupler-faq-item">')
        a(f'<h3 class="decupler-faq-question">{q}</h3>')
        a('<div class="decupler-faq-answer"><div class="decupler-faq-answer-inner">'
          f'{r}</div></div>')
        a("</div>")
    a("</div>")
    a("</div>")
    a("</div>")

    # ── villes voisines, cliquables ────────────────────────────────────────
    if b.get("voisines"):
        a('<div class="bl">')
        a('<div class="in st-s">')
        a(f'<h2>{b["h2_voisines"]}</h2>')
        a(f'<p class="lead nr">{b["voisines_intro"]}</p>')
        a('<div class="vgrid" data-dcp="chrome">')
        for titre, sous, url in b["voisines"]:
            a(f'<div class="vcell"><a class="vcard" href="{url}">'
              f'<div class="vt">{titre}</div>'
              f'<div class="vs">{sous}</div>'
              f'<div class="vf">Voir la page</div></a></div>')
        a("</div>")
        a("</div>")
        a("</div>")

    # ── E-E-A-T ────────────────────────────────────────────────────────────
    a('<div class="bl">')
    a('<div class="in st-s">')
    a('<div class="eeat" data-dcp="chrome">')
    alt_nathan = b.get("photo_alt", "Nathan Fenina, fondateur de Décupler")
    a(f'<div class="av"><img src="{PHOTO_NATHAN}" alt="{alt_nathan}" '
      f'width="200" height="200" loading="lazy"></div>')
    a('<div class="nf">')
    a('<div class="n">Nathan Fenina</div>')
    a(f'<div class="r">{b["eeat"]}</div>')
    a(f'<div class="row" style="margin-top:8px"><a class="btn-o" href="{LI}">'
      f'Profil LinkedIn</a><a class="btn-o" href="{CAL}">Échanger 30 minutes</a></div>')
    a("</div>")
    a("</div>")
    a(f'<p class="sub" data-dcp="chrome">Décupler — {siege["adresse"]}, '
      f'{siege["code_postal"]} {siege["ville"]}.</p>')
    a("</div>")
    a("</div>")

    # ── CTA final ──────────────────────────────────────────────────────────
    a('<div class="bl final" data-dcp="chrome">')
    a('<div class="in st-s">')
    a(f'<h2>{b["h2_final"]}</h2>')
    a(f'<p class="lead nr">{b["final"]}</p>')
    f_url, f_ancre = b.get("final_lien",
                            ("https://decupler.com/cas-clients/",
                             "Voir les études de cas"))
    a(f'<div class="row"><a class="btn" href="{CAL}">{b["cta1"]}</a>'
      f'<a class="btn-o" href="{f_url}">{f_ancre}</a></div>')
    a("</div>")
    a("</div>")

    # ── JSON-LD. Encapsule dans un <div> : un <script> frere d'un <div> se
    #    fait envelopper par wpautop dans un <p> parasite.
    faq_ld = {"@context": "https://schema.org", "@type": "FAQPage",
              "mainEntity": [{"@type": "Question", "name": txt(q),
                              "acceptedAnswer": {"@type": "Answer", "text": txt(r)}}
                             for q, r in b["faq"]]}
    if reg == "consultant":
        ent = {"@context": "https://schema.org", "@type": "Person",
               "name": "Nathan Fenina", "jobTitle": f"Consultant SEO à {ville}",
               "url": f"https://decupler.com/{slug}/", "image": PHOTO_NATHAN,
               "sameAs": [LI],
               "worksFor": {"@type": "ProfessionalService", "name": "Décupler",
                            "url": "https://decupler.com/"},
               "knowsAbout": ["Référencement naturel", "SEO local",
                              "Generative Engine Optimization"],
               "areaServed": {"@type": "City", "name": ville,
                              "containedInPlace": {"@type": "AdministrativeArea",
                                                   "name": v["departement"]}}}
    else:
        ent = {"@context": "https://schema.org", "@type": "ProfessionalService",
               "name": "Décupler", "url": f"https://decupler.com/{slug}/",
               "image": PHOTO_NATHAN,
               "address": {"@type": "PostalAddress",
                           "streetAddress": siege["adresse"],
                           "postalCode": siege["code_postal"],
                           "addressLocality": siege["ville"],
                           "addressRegion": siege["region"],
                           "addressCountry": siege["pays"]},
               "areaServed": {"@type": "City", "name": ville,
                              "containedInPlace": {"@type": "AdministrativeArea",
                                                   "name": v["departement"]}},
               "founder": {"@type": "Person", "name": "Nathan Fenina",
                           "sameAs": LI}}
    a('<div class="ldjson">')
    a('<script type="application/ld+json">'
      + json.dumps(faq_ld, ensure_ascii=False) + "</script>")
    a('<script type="application/ld+json">'
      + json.dumps(ent, ensure_ascii=False) + "</script>")
    a("</div>")
    a("</div>")

    a('<div class="ldjson">')
    a("<script>" + REVEAL + "</script>")
    a("</div>")

    page = "\n".join(o)
    # Regle 4 du skill design : aucune ligne vide hors du <style>, wpautop en
    # fait un <p></p> parasite, parfois au milieu d'une grille flex.
    tete, _, queue = page.partition("</style>")
    queue = "\n".join(l for l in queue.split("\n") if l.strip())
    return tete + "</style>\n" + queue


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--sortie", default="build")
    a = ap.parse_args()
    os.makedirs(a.sortie, exist_ok=True)
    chemin = os.path.join(a.sortie, a.slug + ".html")
    open(chemin, "w", encoding="utf-8").write(construis(a.slug))
    print(f"✅ {chemin}  ({os.path.getsize(chemin)} octets)")


if __name__ == "__main__":
    main()
