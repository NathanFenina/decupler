#!/usr/bin/env python3
"""
Parseur d'export WordPress (WXR) pour la migration Décupler -> Next.js.

Objectif : lire le gros XML (23 Mo) SUR LE DISQUE, sans jamais le charger
dans la conversation. Produit un inventaire léger + des fichiers de contenu
découpés, un par page/article.

Usage:
    python3 scripts/parse_wxr.py /chemin/vers/export.xml

Sorties (dans content/cleaned/) :
    - inventory.md        : tableau récapitulatif (type, statut, titre, slug, tailles)
    - pages/<slug>.html   : contenu brut des pages publiées
    - blog/<slug>.html    : contenu brut des articles publiés
    - elementor/<slug>.json : données Elementor brutes (si le texte est dedans)
"""
import sys
import os
import json
import re
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "content", "cleaned")

# Mapping des clés Yoast -> champs lisibles pour le seo-meta.json
YOAST_MAP = {
    "_yoast_wpseo_title": "seo_title",
    "_yoast_wpseo_metadesc": "description",
    "_yoast_wpseo_canonical": "canonical",
    "_yoast_wpseo_focuskw": "focus_keyword",
    "_yoast_wpseo_opengraph-title": "og_title",
    "_yoast_wpseo_opengraph-description": "og_description",
    "_yoast_wpseo_opengraph-image": "og_image",
    "_yoast_wpseo_meta-robots-noindex": "noindex",
    "_yoast_wpseo_meta-robots-nofollow": "nofollow",
}


def local(tag):
    """Retourne le nom de balise sans namespace : '{...}encoded' -> 'encoded'."""
    return tag.rsplit("}", 1)[-1]


def slugify(text, fallback):
    text = (text or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or fallback


def main(xml_path):
    os.makedirs(os.path.join(OUT, "pages"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "blog"), exist_ok=True)
    os.makedirs(os.path.join(OUT, "elementor"), exist_ok=True)

    rows = []
    counters = {}
    seo_meta = {}  # slug -> dict des balises Yoast

    # iterparse = lecture en flux, faible mémoire, ne charge pas tout en RAM d'un coup
    context = ET.iterparse(xml_path, events=("end",))
    idx = 0
    for event, elem in context:
        if local(elem.tag) != "item":
            continue

        data = {
            "title": "",
            "link": "",
            "post_type": "",
            "status": "",
            "post_name": "",
            "post_date": "",
            "content": "",
        }
        elementor_data = None
        yoast = {}

        for child in elem:
            name = local(child.tag)
            if name == "title":
                data["title"] = child.text or ""
            elif name == "link":
                data["link"] = child.text or ""
            elif name == "encoded" and child.text and "</" in (child.text or "") or name == "encoded":
                # content:encoded ET excerpt:encoded portent tous deux 'encoded'
                # on ne garde que le plus long (le contenu réel)
                if child.text and len(child.text) > len(data["content"]):
                    data["content"] = child.text
            elif name == "post_type":
                data["post_type"] = child.text or ""
            elif name == "status":
                data["status"] = child.text or ""
            elif name == "post_name":
                data["post_name"] = child.text or ""
            elif name == "post_date":
                data["post_date"] = child.text or ""
            elif name == "postmeta":
                meta_key = ""
                meta_val = ""
                for m in child:
                    if local(m.tag) == "meta_key":
                        meta_key = m.text or ""
                    elif local(m.tag) == "meta_value":
                        meta_val = m.text or ""
                if meta_key == "_elementor_data":
                    elementor_data = meta_val
                elif meta_key in YOAST_MAP and meta_val:
                    yoast[YOAST_MAP[meta_key]] = meta_val

        idx += 1
        ptype = data["post_type"] or "?"
        counters[ptype] = counters.get(ptype, 0) + 1

        # On ne traite vraiment que pages + articles publiés
        keep = ptype in ("page", "post") and data["status"] == "publish"

        slug = slugify(data["post_name"] or data["title"], f"item-{idx}")
        content_len = len(data["content"] or "")
        elem_len = len(elementor_data or "")

        if keep:
            folder = "pages" if ptype == "page" else "blog"
            with open(os.path.join(OUT, folder, slug + ".html"), "w", encoding="utf-8") as f:
                f.write(f"<!-- titre: {data['title']} -->\n")
                f.write(f"<!-- url: {data['link']} -->\n")
                f.write(f"<!-- date: {data['post_date']} -->\n\n")
                f.write(data["content"] or "")
            # Si le texte est dans Elementor (contenu HTML quasi vide), on sauve le JSON
            if elementor_data and content_len < 200:
                with open(os.path.join(OUT, "elementor", slug + ".json"), "w", encoding="utf-8") as f:
                    f.write(elementor_data)

        if keep:
            # Résout les variables Yoast (%%title%%, %%sep%%, %%sitename%%, %%page%%)
            def resolve(val):
                if not val:
                    return val
                val = val.replace("%%title%%", data["title"])
                val = val.replace("%%sep%%", "·")
                val = val.replace("%%sitename%%", "Décupler")
                val = re.sub(r"%%[^%]+%%", "", val)  # autres variables -> vide
                return re.sub(r"\s+", " ", val).strip(" ·")
            meta_entry = {"title": data["title"], "url": data["link"], "type": ptype}
            for k, v in yoast.items():
                meta_entry[k] = resolve(v) if k in ("seo_title", "og_title") else v
            # Titre SEO par défaut = titre de la page si Yoast vide
            meta_entry.setdefault("seo_title", data["title"])
            seo_meta[slug] = meta_entry

            rows.append({
                "type": ptype,
                "title": (data["title"] or "")[:60],
                "slug": slug,
                "url": data["link"],
                "content_len": content_len,
                "elementor_len": elem_len,
                "source": "elementor" if (elem_len and content_len < 200) else "html",
            })

        elem.clear()  # libère la mémoire

    # Fichier SEO consommable par Next.js (generateMetadata)
    with open(os.path.join(OUT, "seo-meta.json"), "w", encoding="utf-8") as f:
        json.dump(seo_meta, f, ensure_ascii=False, indent=2)

    # Inventaire markdown
    rows.sort(key=lambda r: (r["type"], r["slug"]))
    with open(os.path.join(OUT, "inventory.md"), "w", encoding="utf-8") as f:
        f.write("# Inventaire du contenu (pages + articles publiés)\n\n")
        f.write("| Type | Titre | Slug | Taille texte | Source du texte |\n")
        f.write("|------|-------|------|-------------:|-----------------|\n")
        for r in rows:
            f.write(f"| {r['type']} | {r['title']} | {r['slug']} | {r['content_len']} | {r['source']} |\n")

    # Résumé sur stdout (léger)
    print("=== Comptage par type ===")
    for k, v in sorted(counters.items(), key=lambda x: -x[1]):
        print(f"  {v:>5}  {k}")
    print(f"\n=== Pages/articles publiés extraits : {len(rows)} ===")
    html_src = sum(1 for r in rows if r["source"] == "html")
    elem_src = sum(1 for r in rows if r["source"] == "elementor")
    print(f"  texte dans HTML standard : {html_src}")
    print(f"  texte dans Elementor JSON: {elem_src}")
    with_desc = sum(1 for s in seo_meta.values() if s.get("description"))
    print(f"\nMéta SEO Yoast récupérées : {len(seo_meta)} entrées, dont {with_desc} avec meta description")
    print(f"Inventaire écrit : content/cleaned/inventory.md")
    print(f"Méta SEO écrites : content/cleaned/seo-meta.json")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/parse_wxr.py /chemin/vers/export.xml")
        sys.exit(1)
    main(sys.argv[1])
