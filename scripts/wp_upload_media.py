#!/usr/bin/env python3
"""
wp_upload_media.py — Téléverse une image dans la médiathèque WordPress (API REST).

Utilise le mot de passe d'application WordPress (.env, jamais commité). Renvoie
l'ID du média et son URL publique (source_url), à injecter dans le HTML d'un
article/page avant publication.

Usage :
    python3 scripts/wp_upload_media.py --file content/articles/images/hero.png \
        --title "Hero meilleure agence GEO" \
        --alt "Schéma d'une agence GEO : une IA cite une marque"

Sortie (dernière ligne) : SOURCE_URL=<url>  pour récupération facile en shell.
"""
import argparse
import base64
import json
import mimetypes
import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def optimize_image(path, max_dim=1600, quality=80):
    """Compresse/redimensionne l'image avant l'upload (évite les PNG lourds qui
    plombent le LCP). Utilise sips (macOS) : tient dans un cadre max_dim sans
    agrandir, convertit en JPEG. Garde le nom d'origine. Retourne le chemin à
    uploader (l'optimisé seulement s'il est plus léger), sinon l'original."""
    if not shutil.which("sips") or path.lower().endswith((".svg", ".gif", ".webp")):
        return path
    stem = os.path.splitext(os.path.basename(path))[0]
    out = os.path.join(tempfile.gettempdir(), stem + ".jpg")
    try:
        subprocess.run(
            ["sips", "-Z", str(max_dim), "-s", "format", "jpeg",
             "-s", "formatOptions", str(quality), path, "--out", out],
            check=True, capture_output=True)
        if os.path.exists(out) and os.path.getsize(out) < os.path.getsize(path):
            return out
    except Exception:  # noqa: BLE001
        pass
    return path


def load_env():
    env = {}
    path = os.path.join(ROOT, ".env")
    if not os.path.exists(path):
        sys.exit("❌ .env introuvable.")
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            env[k.strip()] = v.strip()
    return env


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", required=True, help="Chemin de l'image locale")
    ap.add_argument("--title", default=None)
    ap.add_argument("--alt", default=None, help="Texte alternatif (SEO/accessibilité)")
    ap.add_argument("--caption", default=None)
    ap.add_argument("--no-optimize", action="store_true",
                    help="Ne pas compresser/redimensionner avant l'upload")
    args = ap.parse_args()

    env = load_env()
    site = env.get("WP_SITE_URL", "").rstrip("/")
    user = env.get("WP_USER", "")
    app_pw = env.get("WP_APP_PASSWORD", "").replace(" ", "")
    if not (site and user and app_pw):
        sys.exit("❌ Renseigne WP_SITE_URL, WP_USER, WP_APP_PASSWORD dans .env")

    upload_path = args.file if args.no_optimize else optimize_image(args.file)
    if upload_path != args.file:
        print(f"   (optimisé : {os.path.getsize(args.file)//1024} Ko → "
              f"{os.path.getsize(upload_path)//1024} Ko)", file=sys.stderr)
    data = open(upload_path, "rb").read()
    filename = os.path.basename(upload_path)
    mime = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    token = base64.b64encode(f"{user}:{app_pw}".encode()).decode()

    req = urllib.request.Request(
        f"{site}/wp-json/wp/v2/media",
        data=data,
        method="POST",
        headers={
            "Authorization": f"Basic {token}",
            "Content-Type": mime,
            "Content-Disposition": f'attachment; filename="{filename}"',
            "User-Agent": "DecuplerClaude/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            media = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"❌ Erreur {e.code} : {e.read().decode('utf-8', 'replace')[:500]}")
    except Exception as e:
        sys.exit(f"❌ Échec : {e}")

    media_id = media.get("id")
    source_url = media.get("source_url")

    # Mise à jour des métadonnées (titre/alt/légende) si fournies
    meta = {}
    if args.title:
        meta["title"] = args.title
    if args.alt:
        meta["alt_text"] = args.alt
    if args.caption:
        meta["caption"] = args.caption
    if meta:
        up = urllib.request.Request(
            f"{site}/wp-json/wp/v2/media/{media_id}",
            data=json.dumps(meta).encode("utf-8"),
            method="POST",
            headers={
                "Authorization": f"Basic {token}",
                "Content-Type": "application/json",
                "User-Agent": "DecuplerClaude/1.0",
            },
        )
        try:
            urllib.request.urlopen(up, timeout=30)
        except Exception as e:  # noqa: BLE001
            print(f"⚠️ Média uploadé mais métadonnées non mises à jour : {e}", file=sys.stderr)

    print(f"✅ Média uploadé · ID {media_id}")
    print(f"   {source_url}")
    print(f"SOURCE_URL={source_url}")


if __name__ == "__main__":
    main()
