#!/usr/bin/env python3
"""
analyze_content.py — mesures objectives pour l'audit seo-geo-score.

But : donner au skill des CHIFFRES RÉELS (densité, longueur des phrases, liens,
images/alt, présence FAQ/schema) au lieu d'estimations « à l'œil ». C'est ce qui
rend le score réaliste et reproductible : deux audits du même contenu donnent les
mêmes mesures.

Usage :
    python3 analyze_content.py --keyword "content marketing" --file article.html
    cat article.html | python3 analyze_content.py --keyword "content marketing"

Sortie : un bloc JSON avec les mesures. Le skill lit ces chiffres, applique la
grille (references/criteres-scoring.md) et le malus sur-optimisation, puis rédige
le rapport. Le jugement qualitatif (pertinence, ton, intention) reste au modèle ;
le script ne fait que le quantitatif fiable.
"""
import argparse
import json
import re
import sys

# Mots de transition FR (liste indicative, pour estimer la fluidité façon Yoast).
TRANSITIONS = {
    "d'abord", "ensuite", "enfin", "puis", "donc", "ainsi", "car", "parce que",
    "cependant", "toutefois", "néanmoins", "pourtant", "en effet", "par ailleurs",
    "de plus", "en outre", "par exemple", "notamment", "surtout", "en revanche",
    "au contraire", "tandis que", "alors que", "par conséquent", "c'est pourquoi",
    "grâce à", "afin de", "pour", "malgré", "puisque", "désormais", "aujourd'hui",
    "plutôt que", "en résumé", "pour conclure", "d'une part", "d'autre part",
}


def strip_noise(html: str):
    """Retire commentaires, <script>, <style> ; renvoie (texte_visible, html_brut)."""
    raw = html
    no_comment = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    no_script = re.sub(r"<script.*?</script>", " ", no_comment, flags=re.S | re.I)
    no_style = re.sub(r"<style.*?</style>", " ", no_script, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", no_style)
    text = re.sub(r"\s+", " ", text).strip()
    return text, raw


def word_tokens(text: str):
    return re.findall(r"[0-9a-zàâäéèêëïîôöùûüçœ]+", text.lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--keyword", required=True, help="Mot-clé principal ciblé")
    ap.add_argument("--file", help="Fichier contenu (HTML ou texte). Sinon: stdin")
    args = ap.parse_args()

    html = open(args.file, encoding="utf-8").read() if args.file else sys.stdin.read()
    text, raw = strip_noise(html)
    low = text.lower()
    kw = args.keyword.lower().strip()
    kw_wordlen = len(kw.split())

    words = word_tokens(text)
    n = len(words) or 1

    # Densité du mot-clé exact.
    occ = len(re.findall(re.escape(kw), low))
    density = occ * kw_wordlen / n * 100

    # Phrases + longueur.
    sentences = [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    long_sents = [s for s in sentences if len(word_tokens(s)) > 20]
    pct_long = (len(long_sents) / len(sentences) * 100) if sentences else 0

    # Mots de transition (part des phrases qui en contiennent au moins un).
    with_trans = sum(1 for s in sentences if any(t in s.lower() for t in TRANSITIONS))
    pct_trans = (with_trans / len(sentences) * 100) if sentences else 0

    # Liens (sur le HTML brut).
    hrefs = re.findall(r'href=["\']([^"\']+)["\']', raw, flags=re.I)
    external = [h for h in hrefs if re.match(r"https?://", h, flags=re.I)]
    internal = [h for h in hrefs if h.startswith("/") or h.startswith("#")]

    # Images + alt.
    imgs = re.findall(r"<img\b[^>]*>", raw, flags=re.I)
    imgs_with_alt = [t for t in imgs if re.search(r'alt=["\'][^"\']+["\']', t, flags=re.I)]

    # Titres.
    headings = {f"h{i}": len(re.findall(rf"<h{i}\b", raw, flags=re.I)) for i in range(1, 5)}

    # Signaux GEO.
    has_faq_schema = bool(re.search(r'"@type"\s*:\s*"FAQPage"', raw, flags=re.I))
    has_any_schema = bool(re.search(r"application/ld\+json", raw, flags=re.I))
    kw_in_first_100 = kw in " ".join(words[:100])

    out = {
        "mot_cle": args.keyword,
        "mots": n,
        "occurrences_mot_cle": occ,
        "densite_pct": round(density, 2),
        "densite_verdict": (
            "OK" if density <= 2.5 else
            "un peu haute" if density <= 3.5 else
            "SUR-OPTIMISATION"
        ),
        "malus_suroptimisation": (
            0 if density <= 3.5 else
            5 if density <= 5 else
            8 if density <= 6.5 else 12
        ),
        "mot_cle_dans_100_premiers_mots": kw_in_first_100,
        "phrases": len(sentences),
        "phrases_longues_pct": round(pct_long, 1),
        "mots_transition_pct": round(pct_trans, 1),
        "liens_internes": len(internal),
        "liens_externes": len(external),
        "images": len(imgs),
        "images_avec_alt": len(imgs_with_alt),
        "titres": headings,
        "faq_schema": has_faq_schema,
        "schema_present": has_any_schema,
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
