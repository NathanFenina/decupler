#!/usr/bin/env python3
"""
Publie un ARTICLE ou une PAGE dans WordPress via l'API REST.

Sécurité : utilise un « mot de passe d'application » WordPress (révocable),
lu depuis le fichier .env (jamais commité). Par défaut on publie en BROUILLON
(draft) pour que tu relises dans l'admin avant de mettre en ligne.

Usage typique (Claude génère le contenu HTML puis appelle) :
    python3 scripts/wp_publish.py --type post \
        --title "Mon titre" --slug mon-titre \
        --content-file /tmp/article.html --status draft

Options :
    --type      post | page         (défaut: post)
    --title     titre               (obligatoire)
    --slug      slug d'URL           (optionnel ; WP le génère sinon)
    --content-file  fichier HTML     (obligatoire)
    --excerpt   extrait/méta-desc    (optionnel)
    --status    draft | publish      (défaut: draft)
"""
import os
import sys
import json
import base64
import argparse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env():
    env = {}
    path = os.path.join(ROOT, ".env")
    if not os.path.exists(path):
        sys.exit("❌ Fichier .env introuvable. Copie .env.example en .env et remplis-le.")
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--type", choices=["post", "page"], default="post")
    ap.add_argument("--id", default=None, help="ID d'un contenu existant à mettre à jour")
    ap.add_argument("--title", required=True)
    ap.add_argument("--slug", default=None)
    ap.add_argument("--content-file", required=True)
    ap.add_argument("--excerpt", default=None)
    ap.add_argument("--status", choices=["draft", "publish"], default="draft")
    args = ap.parse_args()

    env = load_env()
    site = env.get("WP_SITE_URL", "").rstrip("/")
    user = env.get("WP_USER", "")
    app_pw = env.get("WP_APP_PASSWORD", "").replace(" ", "")  # WP accepte sans espaces
    if not (site and user and app_pw) or "ton-utilisateur" in user or "xxxx" in app_pw:
        sys.exit("❌ Renseigne WP_SITE_URL, WP_USER et WP_APP_PASSWORD dans .env")

    html = open(args.content_file, encoding="utf-8").read()
    payload = {
        "title": args.title,
        "content": html,
        "status": args.status,
    }
    if args.slug:
        payload["slug"] = args.slug
    if args.excerpt:
        payload["excerpt"] = args.excerpt

    base = f"{site}/wp-json/wp/v2/{'pages' if args.type == 'page' else 'posts'}"
    endpoint = f"{base}/{args.id}" if args.id else base  # avec --id = mise à jour
    token = base64.b64encode(f"{user}:{app_pw}".encode()).decode()
    req = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        method="POST",
        headers={
            "Authorization": f"Basic {token}",
            "Content-Type": "application/json",
            "User-Agent": "DecuplerClaude/1.0",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.load(r)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        sys.exit(f"❌ Erreur {e.code} : {body[:500]}")
    except Exception as e:
        sys.exit(f"❌ Échec de connexion : {e}")

    print("✅ Publié !")
    print(f"   Type   : {args.type}")
    print(f"   Statut : {data.get('status')}")
    print(f"   ID     : {data.get('id')}")
    print(f"   Lien   : {data.get('link')}")
    edit = f"{site}/wp-admin/post.php?post={data.get('id')}&action=edit"
    print(f"   Éditer : {edit}")


if __name__ == "__main__":
    main()
