#!/usr/bin/env python3
"""Publication WordPress qui ne casse rien.

Trois protections, chacune correspondant a un incident reel :

  1. cherche le contenu par SLUG avant d'ecrire, sinon WordPress cree un
     doublon suffixe « -2 » ;
  2. PRESERVE le statut existant : un POST avec status=draft deprogramme
     silencieusement un article planifie ;
  3. reutilise le media existant par slug, sinon WordPress empile des fichiers
     « -1 », « -2 » et decale le slug de l'original.

    python push_wp.py --manifeste lot.json --dry-run     # OBLIGATOIRE d'abord
    python push_wp.py --manifeste lot.json

Manifeste : [{"fichier": "...", "slug": "...", "titre": "...", "kw": "...",
"type": "article", "title": "...", "meta": "...", "une": "img.png",
"une_alt": "...", "ecran": "ecran.jpg", "ecran_alt": "..."}]
"""
import os
import re
import sys
import json
import argparse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wp_client import WP, load_env  # noqa: E402

POST_TYPE = {"article": "posts", "page-ville": "pages", "page-service": "pages"}


def televerser(wp, slug, chemin, alt, titre):
    """Reutilise le media existant : sinon WP empile des -1, -2 a chaque push."""
    d, _ = wp.get("media", {"slug": slug, "per_page": 1,
                            "_fields": "id,source_url"})
    if d:
        wp.post_json(f"media/{d[0]['id']}", {"alt_text": alt})
        return d[0], "reutilise"
    return wp.upload_media(chemin, title=titre, alt_text=alt), "cree"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifeste", required=True)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", help="ne traiter qu'un slug")
    a = ap.parse_args()

    wp = WP(load_env())
    items = json.load(open(a.manifeste, encoding="utf-8"))
    if a.only:
        items = [x for x in items if x["slug"] == a.only]

    print(f"{'contenu':32s} {'type':12s} {'action':14s} {'statut':8s} parution")
    print("-" * 84)
    for it in items:
        pt = POST_TYPE.get(it.get("type", "article"), "posts")
        d, _ = wp.get(pt, {"slug": it["slug"], "per_page": 1,
                           "status": "publish,draft,pending,future,private",
                           "_fields": "id,status,date"})
        existant = d[0] if d else None
        action = "MAJ" if existant else "CREATION"
        statut = existant["status"] if existant else "draft"
        date = existant["date"][:10] if existant else "—"
        print(f"{it['slug'][:32]:32s} {it.get('type','article'):12s} "
              f"{action:14s} {statut:8s} {date}")

        if a.dry_run:
            continue

        html = open(it["fichier"], encoding="utf-8").read()

        # images : la une d'abord, puis l'ecran dont l'URL entre dans le corps
        media_une = None
        if it.get("une"):
            media_une, _ = televerser(wp, f"article-{it['slug']}", it["une"],
                                      it.get("une_alt") or it["kw"], it["titre"])
        if it.get("ecran"):
            m, _ = televerser(wp, f"ecran-{it['slug']}", it["ecran"],
                              it.get("ecran_alt") or it["kw"], it["titre"])
            html = html.replace("{{ECRAN_URL}}", m["source_url"])

        charge = {"title": it["titre"], "slug": it["slug"], "content": html,
                  # ne JAMAIS forcer un statut : cela deprogramme les planifies
                  "status": statut}
        if media_une:
            charge["featured_media"] = media_une["id"]
        # Yoast : ecrivable sur les articles uniquement
        if pt == "posts":
            charge["meta"] = {"_yoast_wpseo_title": it.get("title", ""),
                              "_yoast_wpseo_metadesc": it.get("meta", ""),
                              "_yoast_wpseo_focuskw": it["kw"]}

        chemin = f"{pt}/{existant['id']}" if existant else pt
        r = wp.post_json(chemin, charge)
        note = ""
        if pt == "pages" and (it.get("title") or it.get("meta")):
            note = " · ⚠ Yoast a saisir a la main"
        print(f"   ✅ #{r['id']} /{r['slug']}/ ({r['status']}){note}")

    if a.dry_run:
        print("\n— simulation, rien n'a ete ecrit. Relancer sans --dry-run.")
    else:
        print("\nSi un contenu passe par Elementor (_elementor_edit_mode=builder) :")
        print("  vider le cache — Elementor → Outils → Effacer les fichiers et les donnees")


if __name__ == "__main__":
    main()
