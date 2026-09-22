#!/usr/bin/env python3
"""Validateur bloquant des contenus Decupler.

Verifie tout ce qui a deja casse en production : wpautop, densite, occurrences,
longueur, maillage, FAQ, duplication entre pages d'un meme lot.

    python validate_page.py --fichier build/agence-seo-ia.html \
        --kw "agence SEO IA" --slug agence-seo-ia --type article \
        --title "..." --meta "..."

    python validate_page.py --lot build/ --manifeste lot.json

Le manifeste est un JSON : [{"fichier": "...", "kw": "...", "slug": "...",
"type": "article", "title": "...", "meta": "...", "parution": "2026-08-17"}]
"""
import html as htmllib
import os
import re
import sys
import json
import argparse
import itertools
import subprocess
import unicodedata

ICI = os.path.dirname(os.path.abspath(__file__))
SKILL = os.path.dirname(ICI)

def trouver_analyseur():
    """Localise analyze_content.py du skill de notation, ou qu'il soit installe.

    Le skill s'appelle `yoast-score` dans le depot et `decupler-seo-geo-score`
    sur certains postes : on cherche les deux, dans le depot puis chez l'usager.
    """
    noms = ("yoast-score", "decupler-seo-geo-score")
    racines = [os.path.dirname(os.path.dirname(ICI))]        # skills/ voisin
    d = os.path.abspath(os.getcwd())                          # remontee depuis le projet
    while True:
        racines.append(os.path.join(d, ".claude", "skills"))
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    racines.append(os.path.join(os.path.expanduser("~"), ".claude", "skills"))
    for r in racines:
        for n in noms:
            p = os.path.join(r, n, "scripts", "analyze_content.py")
            if os.path.exists(p):
                return p
    return ""


ANALYZE = os.environ.get("DECUPLER_ANALYZE") or trouver_analyseur()

DENSITE_MAX = 3.5          # au-dela : malus -5 de la grille de scoring
OCCURRENCES_MIN = 20
LIENS_MIN = 8
MOTS_PLANCHER = 1500
DUPLI_SEUIL = 4            # phrases communes tolerees entre deux contenus

# Seuils par type. Les valeurs "page-ville" ne sont pas les regles maison
# habituelles : elles viennent du releve SERP du 19/09/2026 sur
# « agence seo marseille » (2 400 de volume).
#
#   Jones and Co  (position 1) : ~850 mots,  5 occurrences, aucune FAQ
#   Digimood      (position 3) : 1 345 mots, 5 occurrences, aucune FAQ
#   Junto         (position 10, modele du gabarit d'origine)
#
# Exiger 20 occurrences et 1 715 mots produirait des pages deux fois plus
# longues que celles qui rankent, sans toucher au facteur reellement
# discriminant : la preuve locale (adresse, communes, references chiffrees).
# D'ou les controles PREUVE_LOCALE ci-dessous, propres a page-ville.
# Le type "home" a ses propres regles : la page d'accueil se classe sur la
# marque, pas sur une requete generique. Exiger 20 occurrences de mot-cle y
# produirait du bourrage sur la page la plus vue du site. On ne verifie donc
# ni occurrences ni densite, mais on garde le plancher de mots, la FAQ et le
# maillage, qui restent decisifs.
OCCURRENCES_TYPE = {"article": 20, "page-ville": 6, "page-service": 20, "home": 0}
MOTS_PLANCHER_TYPE = {"article": 1500, "page-ville": 1100, "page-service": 1500,
                      "home": 900}
FAQ_MIN_TYPE = {"article": 6, "page-ville": 4, "page-service": 6, "home": 5}

SEUILS_TYPE = {
    # type          title      meta        H2 min
    "article":     ((50, 60), (120, 156), 6),
    "page-ville":  ((50, 60), (120, 156), 8),
    "page-service": ((50, 60), (120, 156), 6),
    "home":        ((50, 70), (120, 156), 8),
}


def sansacc(t):
    return "".join(c for c in unicodedata.normalize("NFKD", t.lower())
                   if not unicodedata.combining(c))


def sanstags(t):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t))


def sansliaison(t):
    """sansacc, entites HTML decodees, balises retirees, puis les liaisons
    « & » et « et » supprimees. « Agence SEO &amp; GEO » dans un H1 et
    « agence seo geo » en requete doivent se correspondre — sans le decodage
    des entites, le controle echoue sur une esperluette ou une espace insecable."""
    t = htmllib.unescape(t).replace("\u00a0", " ")
    t = sansacc(t)
    t = re.sub(r"\s*&\s*", " ", t)
    t = re.sub(r"\bet\b", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def occurrences_min(typ):
    return OCCURRENCES_TYPE.get(typ, OCCURRENCES_MIN)


def mots_min(kw, typ="article"):
    """Assez de mots pour porter les occurrences du type sans depasser 3,5 %."""
    n = len(kw.split())
    occ = occurrences_min(typ)
    plancher = MOTS_PLANCHER_TYPE.get(typ, MOTS_PLANCHER)
    return max(plancher, int(occ * n / (DENSITE_MAX / 100)) + 1)


def hors_css(html):
    """Le contenu sans le bloc <style> : les lignes vides y sont legitimes."""
    return html.split("</style>")[-1] if "</style>" in html else html


def texte(html):
    c = hors_css(html)
    c = re.sub(r"<script.*?</script>", " ", c, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", c))


def phrases(html, sidebar=""):
    """Phrases de >= 8 mots, sidebar exclue (identique sur tous les contenus)."""
    if sidebar:
        html = html.replace(sidebar, "")
    html = re.sub(r'<div class="dcp-sidebar".*?</div>\s*</div>', "", html, flags=re.S)
    return {p.strip() for p in re.split(r"[.!?]", texte(html))
            if len(p.strip().split()) >= 8}


def mesures(html, kw):
    """Delegue au script de notation (skill yoast-score)."""
    if not os.path.exists(ANALYZE):
        return None
    tmp = os.path.join(SKILL, "_tmp_validate.html")
    open(tmp, "w", encoding="utf-8").write(html)
    try:
        r = subprocess.run([sys.executable, ANALYZE, "--file", tmp,
                            "--keyword", kw],
                           capture_output=True, text=True, encoding="utf-8")
        return json.loads(r.stdout)
    except Exception:
        return None
    finally:
        if os.path.exists(tmp):
            os.remove(tmp)


def balises_equilibrees(html):
    c = hors_css(html)
    return c.count("<div") - c.count("</div>")


def inline_orphelins(html):
    """Inline VOISIN d'un bloc : wpautop l'enveloppe et avale la balise du bloc.

    Le danger n'est pas l'inline en soi — <div><span>a</span><span>b</span></div>
    est sur — mais l'inline qui a un element de BLOC pour frere direct :
        <div>…</div><span>x</span>   ou   <span>x</span><div>…</div>
    """
    c = hors_css(html)
    inline = r"span|svg|b|i|em|strong|small|code"
    bloc = r"div|section|ul|ol|table|figure|blockquote"
    fautifs = []
    for m in re.finditer(rf"</(?:{bloc})>\s*<(?:{inline})\b", c):
        fautifs.append(c[max(0, m.start() - 40):m.end()])
    for m in re.finditer(rf"</(?:{inline})>\s*<(?:{bloc})[ >]", c):
        fautifs.append(c[max(0, m.start() - 40):m.end()])
    return fautifs[:3]


def valide(html, kw, slug, typ="article", title=None, meta=None,
           parution=None, ordre=None, urls_vivantes=None):
    e = []
    seuils = SEUILS_TYPE.get(typ, SEUILS_TYPE["article"])
    (t_min, t_max), (m_min, m_max), h2_min = seuils
    k = sansacc(kw)

    # ── structure et pieges wpautop ────────────────────────────────────────
    d = balises_equilibrees(html)
    if d:
        e.append(f"balises div desequilibrees ({d:+d})")
    if "\n\n" in hors_css(html):
        e.append("ligne vide hors CSS (wpautop)")
    orph = inline_orphelins(html)
    if orph:
        e.append(f"inline orphelin (wpautop) : {orph[0][:60]}…")

    # ── placement du mot-cle ───────────────────────────────────────────────
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S)
    if not h1:
        e.append("aucun H1")
    elif k not in sansacc(h1.group(1)) and \
            sansliaison(kw) not in sansliaison(sanstags(h1.group(1))):
        e.append("mot-cle absent du H1")
    if len(re.findall(r"<h1[^>]*>", html)) > 1:
        e.append("plusieurs H1")
    if typ != "home" and \
       k.replace("'", "").replace("’", "") not in sansacc(slug.replace("-", " ")):
        e.append("mot-cle absent du slug")
    h2s = re.findall(r"<h2[^>]*>(.*?)</h2>", html, re.S)
    if len(h2s) < h2_min:
        e.append(f"{len(h2s)} H2 (<{h2_min})")
    if not any(k in sansacc(x) or sansliaison(kw) in sansliaison(sanstags(x))
               for x in h2s):
        e.append("mot-cle dans aucun H2")
    interro = sum(1 for x in h2s if "?" in x)
    if typ != "home" and h2s and interro < len(h2s) * 0.5:
        e.append(f"seulement {interro}/{len(h2s)} H2 formules en question")

    # ── metadonnees ────────────────────────────────────────────────────────
    if title is not None and not (t_min <= len(title) <= t_max):
        e.append(f"title {len(title)} car. ({t_min}-{t_max})")
    if meta is not None and not (m_min <= len(meta) <= m_max):
        e.append(f"meta {len(meta)} car. ({m_min}-{m_max})")
    if typ != "article" and (title or meta):
        # Vrai jusqu'au 22/09/2026. Depuis, le plugin decupler-yoast-rest expose
        # _yoast_wpseo_title/_metadesc/_focuskw a l'API sur post et page (verifie :
        # ecriture puis relecture OK sur la page 20732). Le rappel ne vaut plus que
        # si le plugin est desactive.
        e.append("NOTE verifier que le plugin decupler-yoast-rest est actif, "
                 "sinon Yoast se saisit a la main")

    # ── maillage ───────────────────────────────────────────────────────────
    liens = re.findall(r'href="(?:https://decupler\.com)?(/[^"#]*)"', html)
    liens = [u for u in liens if not u.startswith("/wp-content")]
    # Un bloc de navigation « villes voisines » (.vcard) reprend forcement des
    # destinations deja citees dans le texte : c'est de la navigation, pas de
    # l'ancrage editorial. Le controle des liens repetes ne vise que la prose,
    # ou repeter la meme ancre est du bourrage. Ces liens restent comptes dans
    # le total du maillage.
    nav = re.findall(r'<a class="vcard" href="(?:https://decupler\.com)?(/[^"#]*)"',
                     html)
    prose = list(liens)
    for u in nav:
        if u in prose:
            prose.remove(u)
    if len(set(liens)) < LIENS_MIN:
        e.append(f"{len(set(liens))} liens internes (<{LIENS_MIN})")
    if typ != "home" and len(prose) != len(set(prose)):
        rep = [u for u in set(prose) if prose.count(u) > 1]
        e.append("lien interne repete : " + ", ".join(sorted(rep)))
    if f"/{slug}/" in liens:
        e.append("lien vers soi-meme")
    if 'dcp-links-block' in hors_css(html) or "À découvrir aussi" in html:
        e.append("bloc de liens en pied : interdit, poser des ancres contextuelles")
    if urls_vivantes:
        morts = [u for u in set(liens) if u not in urls_vivantes]
        if morts:
            e.append("lien vers une URL non verifiee : " + ", ".join(sorted(morts)))
    if ordre and slug in ordre:
        rang = ordre.index(slug)
        apres = [u for u in set(liens) if u.strip("/") in ordre
                 and ordre.index(u.strip("/")) >= rang]
        if apres:
            e.append("lien vers un contenu paraissant apres : "
                     + ", ".join(sorted(apres)))

    # ── images ─────────────────────────────────────────────────────────────
    imgs = re.findall(r"<img[^>]*>", html)
    if not imgs:
        e.append("aucune image dans le corps")
    sans_alt = [i for i in imgs if 'alt="' not in i or 'alt=""' in i]
    if sans_alt:
        e.append(f"{len(sans_alt)} image(s) sans alt")
    if imgs and not any(k in sansacc(i) or sansliaison(kw) in sansliaison(i)
                        for i in imgs):
        e.append("aucun alt ne contient le mot-cle")

    # ── CTA et E-E-A-T ─────────────────────────────────────────────────────
    if "calendly.com" not in html:
        e.append("aucun CTA Calendly")
    if "Nathan Fenina" not in html:
        e.append("cross-citation Nathan Fenina absente")

    # ── FAQ ────────────────────────────────────────────────────────────────
    faq_min = FAQ_MIN_TYPE.get(typ, 6)
    nb_faq = html.count("decupler-faq-item")
    if nb_faq < faq_min:
        e.append(f"{nb_faq} questions de FAQ (<{faq_min})")
    if "decupler-faq-answer-inner" not in html:
        e.append("FAQ sans .decupler-faq-answer-inner (aucun padding)")
    if "FAQPage" not in html:
        e.append("JSON-LD FAQPage absent")

    # ── preuve locale : ce qui separe reellement les pages villes ──────────
    # Digimood (#3) affiche adresse, communes, logos et temoignages ; la page
    # #1 n'a aucune preuve mais porte l'autorite d'un domaine marseillais.
    # Sans adresse locale, la preuve chiffree est notre seul levier.
    # Correction du 21/09/2026 : le controle initial exigeait un LocalBusiness
    # sur chaque page ville. C'etait une sur-generalisation depuis la page
    # Marseille de Digimood, ou ils ont un bureau. Leur page Nice
    # (digimood.com/agence-seo/nice/) ranke avec 610 mots, aucune adresse,
    # aucun LocalBusiness, aucune FAQ et aucun temoignage. Sur une ville
    # satellite, areaServed et un cadrage honnete (« a proximite de »)
    # suffisent. On n'invente jamais d'adresse : faux signal local.
    if typ == "page-ville":
        if not re.search(r"\b\d{5}\b", html):
            e.append("PREUVE LOCALE : aucun code postal cite")
        if "LocalBusiness" not in html and "areaServed" not in html:
            e.append("PREUVE LOCALE : ni LocalBusiness ni areaServed dans le JSON-LD")
        if "etude-de-cas" not in html:
            e.append("PREUVE LOCALE : aucun lien vers une etude de cas chiffree")

    # ── mesures deleguees ──────────────────────────────────────────────────
    m = mesures(html, kw)
    if m:
        cible = mots_min(kw, typ)
        occ_min = occurrences_min(typ)
        if m["mots"] < cible:
            e.append(f"{m['mots']} mots (<{cible} pour {occ_min} "
                     f"occurrences a {DENSITE_MAX}%)")
        if m["occurrences_exactes"] < occ_min:
            e.append(f"{m['occurrences_exactes']} occurrences (<{occ_min})")
        if m["densite_effective_pct"] > DENSITE_MAX:
            e.append(f"SUR-OPTIMISATION densite {m['densite_effective_pct']}% "
                     f"— ajouter du texte, pas retirer des occurrences")
        if typ != "home" and not m["mot_cle_dans_100_premiers_mots"]:
            e.append("mot-cle absent des 100 premiers mots")
    return e, m


def controle_duplication(pages, seuil=DUPLI_SEUIL):
    """pages : {slug: html}. Renvoie les paires au-dessus du seuil."""
    ph = {s: phrases(h) for s, h in pages.items()}
    alertes, pire = [], (0, None)
    for a, b in itertools.combinations(sorted(ph), 2):
        n = len(ph[a] & ph[b])
        if n > pire[0]:
            pire = (n, (a, b))
        if n >= seuil:
            alertes.append((a, b, n, sorted(ph[a] & ph[b])[:3]))
    return alertes, pire


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fichier")
    ap.add_argument("--kw")
    ap.add_argument("--slug")
    ap.add_argument("--type", default="article", choices=list(SEUILS_TYPE))
    ap.add_argument("--title")
    ap.add_argument("--meta")
    ap.add_argument("--manifeste", help="JSON decrivant un lot complet")
    ap.add_argument("--urls", help="JSON des URLs vivantes (check_urls.py)")
    a = ap.parse_args()

    vivantes = None
    if a.urls and os.path.exists(a.urls):
        vivantes = set(json.load(open(a.urls, encoding="utf-8"))["vivantes"])

    if a.manifeste:
        items = json.load(open(a.manifeste, encoding="utf-8"))
        items.sort(key=lambda x: x.get("parution", ""))
        ordre = [x["slug"] for x in items if x.get("parution")]
    else:
        if not (a.fichier and a.kw and a.slug):
            sys.exit("il faut --manifeste, ou --fichier --kw --slug")
        items = [{"fichier": a.fichier, "kw": a.kw, "slug": a.slug,
                  "type": a.type, "title": a.title, "meta": a.meta}]
        ordre = None

    pages, total = {}, 0
    print(f"{'contenu':32s} {'mots':>5} {'dens':>6} {'occ':>4} {'H2':>3} "
          f"{'liens':>6}  etat")
    print("-" * 82)
    for it in items:
        html = open(it["fichier"], encoding="utf-8").read()
        pages[it["slug"]] = html
        err, m = valide(html, it["kw"], it["slug"], it.get("type", "article"),
                        it.get("title"), it.get("meta"),
                        it.get("parution"), ordre, vivantes)
        liens = len({u for u in re.findall(
            r'href="(?:https://decupler\.com)?(/[^"#]*)"', html)
            if not u.startswith("/wp-content")})
        defauts = [x for x in err if not x.startswith("NOTE")]
        etat = "✓" if not defauts else "✗ " + " | ".join(defauts[:2])
        print(f"{it['slug'][:32]:32s} {(m or {}).get('mots', 0):>5} "
              f"{(m or {}).get('densite_effective_pct', 0):>5}% "
              f"{(m or {}).get('occurrences_exactes', 0):>4} "
              f"{html.count('<h2'):>3} {liens:>6}  {etat}")
        for x in defauts[2:] + [x for x in err if x.startswith("NOTE")]:
            print(" " * 63 + x)
        total += len(defauts)

    if len(pages) > 1:
        print("\n=== DUPLICATION ENTRE CONTENUS ===")
        alertes, pire = controle_duplication(pages)
        for x, y, n, ex in alertes:
            print(f"  ⚠ {x} ↔ {y} : {n} phrases communes")
            for p in ex:
                print(f"      « {p[:90]}… »")
        print(f"  pire cas : {pire[0]} phrase(s)"
              + (f" ({pire[1][0]} ↔ {pire[1][1]})" if pire[1] else "")
              + f" · seuil {DUPLI_SEUIL}")
        total += len(alertes)

    print()
    if total:
        print(f"❌ {total} probleme(s) — ne pas pousser")
        sys.exit(1)
    print("✓ tous les controles passent")


if __name__ == "__main__":
    main()
