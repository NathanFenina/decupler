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
PHOTOS = os.path.join(SKILL, "references", "photos.json")
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


def photo(cle):
    """Un visuel du registre references/photos.json.

    Registre unique, et reserve aux photos REELLES : Wikimedia Commons avec
    credit, ou photos de Nathan. Le 23/09, une image generee de deux
    personnes inventees etait presentee comme « deux experts SEO de
    Decupler » dans quatre brouillons. Passer par ce registre rend ce cas
    impossible a reproduire par inadvertance.
    """
    reg = json.load(open(PHOTOS, encoding="utf-8"))["photos"]
    if cle not in reg:
        raise SystemExit(f"❌ visuel « {cle} » absent de references/photos.json")
    return reg[cle]


def resout_visuels(b):
    """Traduit les cles de visuels du contenu en tuples pour le gabarit."""
    if b.get("visuel_photo"):
        ph = photo(b["visuel_photo"])
        k, v = b["visuel_badge"]
        b["visuel"] = (ph["url"], b.get("visuel_alt") or ph["alt"], ph["w"], ph["h"], k, v)
        b["visuel_credit"] = ph.get("credit")
    if b.get("bandeau_photo") and b.get("bandeau"):
        ph = photo(b["bandeau_photo"])
        titre, paras, _ancien = b["bandeau"]
        b["bandeau"] = (titre, paras, (ph["url"], b.get("bandeau_alt") or ph["alt"],
                                       ph["w"], ph["h"], b.get("bandeau_cap") or ph["alt"]))
        b["bandeau_detoure"] = ph.get("detoure", False)
        b["bandeau_credit"] = ph.get("credit")
    if isinstance(b.get("photo_ville"), dict) and b["photo_ville"].get("cle"):
        ph = photo(b["photo_ville"]["cle"])
        b["photo_ville"].update({"src": ph["url"], "w": ph["w"], "h": ph["h"]})
        b["photo_ville"].setdefault("alt", ph["alt"])
        b["photo_ville"].setdefault("credit", ph["credit"])
    return b


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


def css_pour_la_page():
    """Le CSS du skin, sans ses commentaires.

    Le fichier source est abondamment commente : chaque regle bizarre dit
    quel incident l'a rendue necessaire, et c'est ce qui evite de la retirer
    six mois plus tard. Mais ces commentaires n'ont rien a faire dans le HTML
    servi au visiteur — ils y pesaient plus de 13 Ko par page. On les retire
    ici, a l'assemblage, et seulement ici.
    """
    brut = open(CSS, encoding="utf-8").read()
    sans = re.sub(r"/\*.*?\*/", "", brut, flags=re.S)
    # Les lignes devenues vides, et les espaces de fin : le fichier reste
    # lisible, simplement sans la prose.
    lignes = [l.rstrip() for l in sans.split("\n")]
    return "\n".join(l for l in lignes if l.strip())


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
    ".vgrid>a,.steps>div,.decupler-faq-item,.fig,.mock,.tw,"
    ".livr>div,.duo>div,.bl-dk .ed,.bphoto .ovin');"
    "for(var i=0;i<c.length;i++){c[i].classList.add('dcp-att');}"
    "var o=new IntersectionObserver(function(es){es.forEach(function(e){"
    "if(e.isIntersecting){e.target.classList.add('dcp-vu');o.unobserve(e.target);}"
    "});},{rootMargin:'0px 0px -12% 0px',threshold:0.08});"
    "for(var j=0;j<c.length;j++){o.observe(c[j]);}})();"
)


def bande_photo(b):
    """Bande photo pleine largeur, texte en surimpression.

    Nathan : « il manque des photos », « pas assez de banniere differente ».
    Les photos sont de vraies vues de la ville, prises sur Wikimedia Commons
    sous licence CC — pas des images generees. Le credit et la licence sont
    affiches dans la bande : c'est la condition de la licence, et une photo
    reelle creditee vaut mieux qu'une ville plausible mais fausse.

    Aucune balise inline en debut de ligne (regle 5 du skill design) : l'img
    et le lien de credit partent sur la ligne de leur conteneur.
    """
    ph = b["photo_ville"]
    o = ['<div class="bphoto">']
    o.append(f'<div><img src="{ph["src"]}" alt="{ph["alt"]}" '
             f'width="{ph["w"]}" height="{ph["h"]}" loading="lazy"></div>')
    o.append('<div class="voile"></div>')
    o.append('<div class="ov">')
    o.append('<div class="ovin">')
    # Pas de sur-titre au-dessus du H2 : le couple « petite etiquette en
    # capitales + gros titre » est le signal « kicker-above-heading ». Les
    # pastilles sous le texte portent deja l'information.
    o.append(f'<h2>{ph["h2"]}</h2>')
    o.append(f'<p class="ovp">{ph["p"]}</p>')
    if ph.get("chips"):
        o.append('<div class="ovf">')
        for c in ph["chips"]:
            o.append(f'<div>{c}</div>')
        o.append('</div>')
    o.append('</div>')
    o.append('</div>')
    o.append(f'<div class="cred" data-dcp="chrome">{ph["credit"]}</div>')
    o.append('</div>')
    return o


def ruban(b):
    """Bande fine et sombre entre deux grandes sections.

    Son role est rythmique : sans elle la page enchaine blanc / lavande /
    blanc sur toute sa hauteur, ce qui est exactement ce que Nathan a
    appele « trop claude comme page ».
    """
    o = ['<div class="ruban" data-dcp="chrome">', '<div class="rin">']
    for val, lib in b["ruban"]:
        o.append(f'<div class="f"><div class="p"></div><div><b>{val}</b> {lib}</div></div>')
    return o + ['</div>', '</div>']


def livrables(b):
    """Ce qui arrive concretement chaque mois.

    « Pas assez de matiere » : la matiere la plus utile sur une page de
    prestation n'est pas un paragraphe de plus sur l'importance du SEO local,
    c'est la liste de ce que le client recoit et a quelle cadence.
    """
    o = ['<div class="bl">', '<div class="in st-s">',
         f'<h2>{b["h2_livrables"]}</h2>',
         f'<p class="lead nr">{b["livrables_intro"]}</p>', '<div class="livr">']
    # Pas de numerotation « 01 … 06 » : ces livrables ne sont pas une
    # sequence, et une petite etiquette numerotee au-dessus de chaque titre
    # est l'echafaudage editorial que le detecteur d'Impeccable signale
    # (« numbered-section-labels »). L'etiquette porte la cadence, qui est
    # l'information utile : le lecteur voit d'abord QUAND il recoit quoi.
    for _rang, titre, detail, cadence in b["livrables"]:
        o.append(f'<div><div class="rg">{cadence}</div><h3>{titre}</h3>'
                 f'<div class="d">{detail}</div></div>')
    o += ['</div>']
    if b.get("livrables_note"):
        o.append(f'<p class="sub" style="margin-top:16px">{b["livrables_note"]}</p>')
    return o + ['</div>', '</div>']


def duo(b):
    """Ce qu'on fait / ce qu'on ne fait pas.

    Le bloc le plus differenciant de la page, et le moins imitable : dire
    non est concret et verifiable. C'est aussi ce qui fait qu'une page ne se
    lit pas comme un texte produit en serie.
    """
    oui_t, oui, non_t, non = b["duo"]
    o = ['<div class="bl bl-lav">', '<div class="in st-s">',
         f'<h2>{b["h2_duo"]}</h2>',
         f'<p class="lead nr">{b["duo_intro"]}</p>', '<div class="duo">']
    for titre, items, cls, marque in ((oui_t, oui, "col", "\u2713"),
                                      (non_t, non, "col non", "\u2715")):
        o.append(f'<div class="{cls}">')
        o.append(f'<div class="ct"><div class="s">{marque}</div><div>{titre}</div></div>')
        o.append('<ul>')
        for it in items:
            o.append(f'<li>{it}</li>')
        o.append('</ul>')
        o.append('</div>')
    return o + ['</div>', '</div>', '</div>']


def parti_pris(b, photo):
    """Bande sombre editoriale : la prise de parole de Nathan.

    Une page de ville se termine partout pareil — FAQ, villes voisines, CTA.
    Cette bande casse la serie : fond sombre, texte plus grand, premiere
    personne, signature avec la photo. C'est la ou se dit ce qu'une page
    generique ne dit jamais.
    """
    o = ['<div class="bl bl-dk">', '<div class="in">', '<div class="edit">']
    o.append('<div class="st-s">')
    o.append(f'<div><span class="pill">{b["parti_pill"]}</span></div>')
    o.append(f'<h2>{b["h2_parti"]}</h2>')
    o.append('<div class="sig">')
    o.append(f'<div class="av"><img src="{photo}" alt="Nathan Fenina, '
             f'fondateur de Décupler" width="200" height="200" loading="lazy"></div>')
    o.append('<div><div class="nn">Nathan Fenina</div>'
             f'<div class="rr">{b["parti_role"]}</div></div>')
    o.append('</div>')
    o.append('</div>')
    o.append('<div class="ed">')
    for pp in b["parti_pris"]:
        o.append(f'<p>{pp}</p>')
    o.append('</div>')
    return o + ['</div>', '</div>', '</div>']


# U+202F, espace fine insecable : la ponctuation haute francaise s'y accroche.
FINE = " "


def _ponctue(texte):
    """Colle : ; ! ? et les guillemets francais au mot qui precede."""
    texte = re.sub(r"[  ]+([:;!?])", FINE + r"\g<1>", texte)
    texte = re.sub(r"«[  ]+", "«" + FINE, texte)
    texte = re.sub(r"[  ]+»", FINE + "»", texte)
    return texte


def typo_fr(page):
    """Applique la ponctuation francaise aux seuls titres de la page.

    Releve du 22/09 sur la page de Cannes : le H1 se cassait en « Agence SEO
    Cannes / : ranker avant le / salon » — le deux-points ouvrait une ligne.
    Une espace fine insecable avant la ponctuation haute est de toute facon
    la regle en francais, et c'est precisement ce qui empeche ce rejet.

    Limite aux h1/h2/h3 : c'est la que la casse se voit, et ca evite de
    toucher au corps du texte comme au contenu des attributs.

    Piege paye ici : dans une chaine NON brute, "\\1" n'est pas un renvoi de
    groupe mais le caractere U+0001. Le premier jet a donc remplace les
    points d'interrogation des titres par un caractere de controle — et le
    validateur a eu raison de signaler 0 H2 formule en question.
    """
    return re.sub(
        r"(<h([123])\b[^>]*>)(.*?)(</h\2>)",
        lambda m: m.group(1) + _ponctue(m.group(3)) + m.group(4),
        page, flags=re.S)


# ── Carte de la zone ─────────────────────────────────────────────────────
# Coordonnees reelles (latitude, longitude) des communes du reseau. La carte
# n'est pas une illustration : chaque point est a sa place, et la distance
# affichee est calculee depuis Nice, pas estimee.
COORDS = {
    "Toulon": (43.1242, 5.9280), "Fréjus": (43.4331, 6.7370),
    "Grasse": (43.6580, 6.9225), "Cannes": (43.5528, 7.0174),
    "Le Cannet": (43.5769, 7.0191), "Antibes": (43.5808, 7.1251),
    "Cagnes-sur-Mer": (43.6640, 7.1489), "Nice": (43.7102, 7.2620),
    "Monaco": (43.7384, 7.4246), "Menton": (43.7747, 7.4975),
}
# Trait de cote simplifie, d'ouest en est : La Seyne, les caps, les golfes.
# C'est un schema — assez fidele pour situer, sans pretendre au cadastre.
COTE = [(43.095, 5.86), (43.108, 5.93), (43.075, 6.02), (43.09, 6.13),
        (43.14, 6.37), (43.17, 6.53), (43.26, 6.66), (43.31, 6.64),
        (43.42, 6.77), (43.435, 6.86), (43.505, 6.94), (43.548, 7.02),
        (43.565, 7.075), (43.545, 7.13), (43.585, 7.135), (43.655, 7.165),
        (43.695, 7.27), (43.68, 7.33), (43.735, 7.425), (43.775, 7.51),
        (43.79, 7.56), (43.785, 7.63), (43.775, 7.70), (43.76, 7.80)]
# La cote continue en Italie (Vintimille, Bordighera) : sans ces trois points
# elle s'arretait apres Menton et la mer remontait en mur vertical sur le
# bord droit — la ou il y a de la terre. Constate au rendu du 23/09.
FRONTIERE = [(43.785, 7.530), (43.815, 7.515), (43.86, 7.52)]


# Deux cadrages. Le reseau s'etend de Toulon a Menton, mais tout se joue
# entre Frejus et Menton : cadrer sur Toulon ecrasait le 06 dans un coin
# (premier rendu du 23/09, etiquettes empilees entre Cannes et Monaco).
CADRE_06 = (6.60, 7.62, 43.36, 43.84)     # lon min, lon max, lat min, lat max
CADRE_LARGE = (5.80, 7.62, 43.02, 43.84)
LARGEUR, HAUTEUR = 600, 380


def _projection(cadre):
    """Equirectangulaire corrigee du cosinus : isotrope a cette echelle."""
    import math
    lo0, lo1, la0, la1 = cadre
    k = math.cos(math.radians((la0 + la1) / 2))
    ech = min(LARGEUR / ((lo1 - lo0) * k), HAUTEUR / (la1 - la0))
    ox = (LARGEUR - (lo1 - lo0) * k * ech) / 2
    oy = (HAUTEUR - (la1 - la0) * ech) / 2

    def proj(lat, lon):
        return (round(ox + (lon - lo0) * k * ech, 1),
                round(oy + (la1 - lat) * ech, 1))
    return proj, ech


def _km(a, b):
    import math
    (la1, lo1), (la2, lo2) = a, b
    p1, p2 = math.radians(la1), math.radians(la2)
    d = (math.sin((p2 - p1) / 2) ** 2
         + math.cos(p1) * math.cos(p2) * math.sin(math.radians(lo2 - lo1) / 2) ** 2)
    return round(2 * 6371 * math.asin(math.sqrt(d)))


def _place_etiquettes(points, taille):
    """Place chaque etiquette sans chevaucher les autres ni les points.

    Glouton : pour chaque point, essaie droite, gauche, dessus, dessous, et
    garde la premiere position libre et dans le cadre. Largeur estimee a
    0,58 em par caractere — une surestimation prudente pour Inter.
    """
    boites = [(x - 6, y - 6, x + 6, y + 6) for _, x, y, _ in points]
    sortie = []
    # Les points mis en avant se placent en premier : ils gardent la
    # meilleure position.
    for nom, x, y, fort in sorted(points, key=lambda p: not p[3]):
        t = taille + (1.5 if fort else 0)
        w, h = len(nom) * t * 0.58, t
        essais = [(x + 10, y + h * 0.35, "start", (x + 9, y - h * 0.65, x + 11 + w, y + h * 0.45)),
                  (x - 10, y + h * 0.35, "end", (x - 11 - w, y - h * 0.65, x - 9, y + h * 0.45)),
                  (x, y - 11, "middle", (x - w / 2, y - 11 - h, x + w / 2, y - 9)),
                  (x, y + 11 + h * 0.8, "middle", (x - w / 2, y + 9, x + w / 2, y + 13 + h))]
        choix = essais[0]
        for e in essais:
            bx0, by0, bx1, by1 = e[3]
            dedans = bx0 > 2 and bx1 < LARGEUR - 2 and by0 > 2 and by1 < HAUTEUR - 2
            libre = all(bx1 < a0 or bx0 > a1 or by1 < b0 or by0 > b1
                        for a0, b0, a1, b1 in boites)
            if dedans and libre:
                choix = e
                break
        boites.append(choix[3])
        sortie.append((nom, choix[0], choix[1], choix[2], fort))
    return sortie


def _decoupe_polygone(pts, w, h):
    """Sutherland-Hodgman : le polygone de la mer, coupe au cadre.

    Sans decoupe, la mer et la cote debordaient geometriquement du SVG
    (masquees a l'ecran, mais la sonde DOM les comptait comme debordements
    a 505 px, et c'est de la geometrie sale). Constate le 23/09.
    """
    def coupe(pts, dedans, inter):
        out = []
        for i, cur in enumerate(pts):
            prev = pts[i - 1]
            if dedans(cur):
                if not dedans(prev):
                    out.append(inter(prev, cur))
                out.append(cur)
            elif dedans(prev):
                out.append(inter(prev, cur))
        return out

    def ix(x0):
        return lambda a, b: (x0, a[1] + (b[1] - a[1]) * (x0 - a[0]) / ((b[0] - a[0]) or 1e-9))

    def iy(y0):
        return lambda a, b: (a[0] + (b[0] - a[0]) * (y0 - a[1]) / ((b[1] - a[1]) or 1e-9), y0)

    for dedans, inter in ((lambda p: p[0] >= 0, ix(0)), (lambda p: p[0] <= w, ix(w)),
                          (lambda p: p[1] >= 0, iy(0)), (lambda p: p[1] <= h, iy(h))):
        pts = coupe(pts, dedans, inter)
        if not pts:
            break
    return [(round(x, 1), round(y, 1)) for x, y in pts]


def _decoupe_ligne(pts, w, h):
    """Liang-Barsky segment par segment : le trait de cote, coupe au cadre.
    Renvoie une liste de polylignes (un trait peut sortir puis rentrer)."""
    traits, cur = [], []
    for (x0, y0), (x1, y1) in zip(pts, pts[1:]):
        dx, dy = x1 - x0, y1 - y0
        t0, t1, ok = 0.0, 1.0, True
        for p, q in ((-dx, x0), (dx, w - x0), (-dy, y0), (dy, h - y0)):
            if p == 0:
                if q < 0:
                    ok = False
                    break
            else:
                r = q / p
                if p < 0:
                    t0 = max(t0, r)
                else:
                    t1 = min(t1, r)
        if not ok or t0 > t1:
            if cur:
                traits.append(cur)
                cur = []
            continue
        a = (round(x0 + t0 * dx, 1), round(y0 + t0 * dy, 1))
        b = (round(x0 + t1 * dx, 1), round(y0 + t1 * dy, 1))
        if not cur or cur[-1] != a:
            if cur:
                traits.append(cur)
            cur = [a]
        cur.append(b)
        if t1 < 1:
            traits.append(cur)
            cur = []
    if cur:
        traits.append(cur)
    return traits


def carte_zone(ville):
    """La carte SVG de la zone, ville courante mise en avant.

    Tout sur UNE ligne : wpautop transforme un saut de ligne dans un SVG en
    <br> ou en <p>, et une ligne qui commence par <svg> se fait envelopper
    (regle 5 du skill design). Les etiquettes restent du texte.
    """
    cadre = CADRE_06
    if ville in COORDS:
        la, lo = COORDS[ville]
        if not (cadre[0] <= lo <= cadre[1] and cadre[2] <= la <= cadre[3]):
            cadre = CADRE_LARGE
    proj, ech = _projection(cadre)
    nice = COORDS["Nice"]
    cote = [proj(*c) for c in COTE]
    poly = _decoupe_polygone(cote + [(LARGEUR + 40, HAUTEUR + 40), (-40, HAUTEUR + 40)],
                             LARGEUR, HAUTEUR)
    mer = " ".join(f"{x},{y}" for x, y in poly)
    traits = _decoupe_ligne(cote, LARGEUR, HAUTEUR)
    o = [f'<svg class="cz" viewBox="0 0 {LARGEUR} {HAUTEUR}" role="img" '
         f'aria-label="Carte : {ville} et les communes suivies depuis le bureau de Nice">']
    o.append(f'<polygon class="cz-mer" points="{mer}"/>')
    for t in traits:
        o.append('<polyline class="cz-cote" points="'
                 + " ".join(f"{x},{y}" for x, y in t) + '"/>')
    o.append(f'<text class="cz-mer-lb" x="{LARGEUR * 0.56}" y="{HAUTEUR - 34}">Mer Méditerranée</text>')
    # La frontiere italienne : c'est elle, plus que le trait de cote, qui
    # fait lire le dessin comme une carte et non comme un graphique.
    fr = [proj(*c) for c in FRONTIERE]
    if any(0 <= x <= LARGEUR for x, _ in fr):
        for t in _decoupe_ligne(fr, LARGEUR, HAUTEUR):
            o.append('<polyline class="cz-front" points="'
                     + " ".join(f"{x},{y}" for x, y in t) + '"/>')
        fx, fy = proj(43.83, 7.585)
        if fx < LARGEUR - 20:
            o.append(f'<text class="cz-pays" x="{fx}" y="{fy}" text-anchor="middle">ITALIE</text>')
        gx, gy = proj(43.74, 6.76) if cadre == CADRE_06 else proj(43.62, 6.25)
        o.append(f'<text class="cz-pays" x="{gx}" y="{gy}" text-anchor="middle">FRANCE</text>')

    ici = COORDS.get(ville)
    if ici and ville != "Nice":
        (x1, y1), (x2, y2) = proj(*nice), proj(*ici)
        o.append(f'<line class="cz-trajet" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')

    points, hors = [], []
    for nom, c in COORDS.items():
        x, y = proj(*c)
        if not (0 <= x <= LARGEUR and 0 <= y <= HAUTEUR):
            hors.append((nom, c))
            continue
        cls = "cz-pt" + (" on" if nom == ville else "") + (" siege" if nom == "Nice" else "")
        o.append(f'<circle class="{cls}" cx="{x}" cy="{y}" r="{6.5 if nom == ville else 4.2}"/>')
        points.append((nom + (" · bureau" if nom == "Nice" else ""), x, y,
                       nom in (ville, "Nice")))
    for nom, x, y, ancre, fort in _place_etiquettes(points, 12.5):
        o.append(f'<text class="cz-lb{" on" if fort else ""}" x="{round(x, 1)}" '
                 f'y="{round(y, 1)}" text-anchor="{ancre}">{nom}</text>')
    # Les communes hors cadre (Toulon, vue du 06) : un repere au bord, avec
    # la distance. Elles existent, mais les dessiner ecraserait le reste.
    for nom, c in hors:
        o.append(f'<text class="cz-hors" x="10" y="{HAUTEUR - 14}">← {nom} · '
                 f'{_km(nice, c)} km</text>')
    # Echelle : 10 km.
    L = round(10 * ech / 111.2, 1)
    o.append(f'<line class="cz-ech" x1="16" y1="22" x2="{16 + L}" y2="22"/>'
             f'<text class="cz-ech-lb" x="{22 + L}" y="26">10 km</text>')
    o.append("</svg>")
    if ici and ville != "Nice":
        legende = (f"{ville} est à {_km(nice, ici)} km à vol d'oiseau de notre "
                   "bureau, 10 avenue Lympia privée à Nice.")
    else:
        legende = ("Notre bureau, 10 avenue Lympia privée. Chaque point est une "
                   "commune où nous suivons des clients depuis Nice.")
    # Le <svg> dans son propre <div> : frere direct du <div> de legende, il
    # se faisait signaler par le garde-fou wpautop (regle 5) — WordPress
    # l'aurait enveloppe dans un <p>.
    return ('<div class="carte" data-dcp="chrome"><div class="czw">' + "".join(o)
            + f'</div><div class="cz-leg">{legende}</div></div>')


def construis(slug):
    v, base = fiche(slug)
    b = resout_visuels(charge_contenu(slug))
    reg = v.get("registre", "agence")
    ville = v["ville"]
    siege = base["_siege"]
    o = []
    a = o.append

    a('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
      'family=Sora:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap">')
    a("<style>")
    a(css_pour_la_page())
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
        if b.get("visuel_credit"):
            # Condition de la licence CC : attribution visible, pas en note.
            a(f'<div class="hcred">{b["visuel_credit"]}</div>')
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

    # ── bande photo de la ville, pleine largeur ────────────────────────────
    if b.get("photo_ville"):
        for x in bande_photo(b):
            a(x)

    # ── 5. zone d'intervention ─────────────────────────────────────────────
    a('<div class="bl">')
    a('<div class="in">')
    a('<div class="zsplit">')
    a('<div class="st-s">')
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
    a(carte_zone(ville))
    a("</div>")
    a("</div>")
    a("</div>")

    # ── ruban de faits ─────────────────────────────────────────────────────
    if b.get("ruban"):
        for x in ruban(b):
            a(x)

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

    # ── livrables ──────────────────────────────────────────────────────────
    if b.get("livrables"):
        for x in livrables(b):
            a(x)

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
        cls = "fig det" if b.get("bandeau_detoure") else "fig"
        if b.get("bandeau_credit"):
            cap = f'{cap} — {b["bandeau_credit"]}'
        a(f'<div class="{cls}"><img src="{src}" alt="{alt}" width="{w}" height="{h}" '
          f'loading="lazy"><div class="cap" data-dcp="chrome">{cap}</div></div>')
        a("</div>")
        a("</div>")
        a("</div>")

    # ── ce qu'on fait / ce qu'on ne fait pas ───────────────────────────────
    if b.get("duo"):
        for x in duo(b):
            a(x)

    # ── bande sombre editoriale ────────────────────────────────────────────
    if b.get("parti_pris"):
        for x in parti_pris(b, PHOTO_NATHAN):
            a(x)

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

    # ── bande auteur (E-E-A-T) ─────────────────────────────────────────────
    #    Version precedente : un avatar de 60 px dans un filet blanc, coince
    #    entre deux bandes sans fond — 180 px de vide au-dessus et en dessous.
    #    C'est ce que Nathan a vu en disant « regarde le bas, y'a pas de
    #    photo, y'a pas assez de matiere ». Desormais : fond lavande, grande
    #    photo verticale, biographie, et la signature d'auteur que Google
    #    comme les moteurs IA cherchent en fin de page.
    alt_nathan = b.get("photo_alt", "Nathan Fenina, fondateur de Décupler")
    # La page consultant de Nice affichait trois fois la meme photo (hero,
    # bandeau, bande auteur). On prend la premiere photo de Nathan qui n'est
    # pas deja utilisee sur la page.
    deja = {x[0] for x in (b.get("visuel"), (b.get("bandeau") or (0, 0, (None,)))[2]) if x}
    choix = [photo("nathan-nice"), photo("nathan-bras"), photo("nathan-portrait")]
    aut_ph = next((p for p in choix if p["url"] not in deja), choix[0])
    a('<div class="bl bl-lav">')
    a('<div class="in">')
    a('<div class="aut" data-dcp="chrome">')
    a(f'<div class="ph{" det" if aut_ph.get("detoure") else ""}"><img src="{aut_ph["url"]}" '
      f'alt="{alt_nathan}" width="{aut_ph["w"]}" height="{aut_ph["h"]}" loading="lazy"></div>')
    a('<div class="tx">')
    a('<div><span class="pill">Qui écrit et qui exécute</span></div>')
    a('<div class="nm">Nathan Fenina</div>')
    a(f'<div class="rl">{b["parti_role"]}</div>')
    a(f'<p class="lead nr">{b["eeat"]}</p>')
    if b.get("eeat_plus"):
        for pp in b["eeat_plus"]:
            a(f'<p class="lead nr">{pp}</p>')
    a('<div class="row"><a class="btn-o" href="' + LI + '">Profil LinkedIn</a>'
      f'<a class="btn" href="{CAL}">Échanger 30 minutes</a></div>')
    a(f'<p class="sub">Décupler — {siege["adresse"]}, '
      f'{siege["code_postal"]} {siege["ville"]}. '
      f'Zone d\'intervention : {ville} et {v["departement"]}.</p>')
    a("</div>")
    a("</div>")
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
    # La ponctuation haute des titres est collee en dernier : sur le HTML
    # final, donc une seule fois, et sans risque de toucher le <style>.
    return tete + "</style>\n" + typo_fr(queue)


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
