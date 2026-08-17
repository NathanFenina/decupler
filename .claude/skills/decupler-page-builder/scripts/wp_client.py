#!/usr/bin/env python3
"""Client REST WordPress minimal, partage par tous les scripts du skill.

Lit WP_SITE_URL / WP_USER / WP_APP_PASSWORD depuis le .env du projet.
NE JAMAIS ECRIRE dans ce .env : lecture seule.
"""
import os
import sys
import json
import base64
import mimetypes
import urllib.parse
import urllib.request


def trouver_env():
    """Le skill vit hors du projet : on remonte depuis le repertoire courant."""
    d = os.path.abspath(os.getcwd())
    while True:
        p = os.path.join(d, ".env")
        if os.path.exists(p):
            return p
        parent = os.path.dirname(d)
        if parent == d:
            return None
        d = parent


def load_env():
    env = {}
    path = os.environ.get("DECUPLER_ENV") or trouver_env()
    if not path or not os.path.exists(path):
        sys.exit("❌ .env introuvable — lancer depuis le projet, "
                 "ou definir DECUPLER_ENV=/chemin/.env")
    # LECTURE SEULE : ne jamais ecrire de variable dans ce fichier
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        env[k.strip()] = v.strip()
    return env


class WP:
    def __init__(self, env):
        self.site = env.get("WP_SITE_URL", "").rstrip("/")
        user = env.get("WP_USER", "")
        pw = env.get("WP_APP_PASSWORD", "").replace(" ", "")
        if not (self.site and user and pw):
            sys.exit("❌ Renseigne WP_SITE_URL, WP_USER et WP_APP_PASSWORD dans .env")
        self.token = base64.b64encode(f"{user}:{pw}".encode()).decode()

    def _req(self, url, data=None, method="GET", headers=None):
        h = {"Authorization": f"Basic {self.token}",
             "User-Agent": "DecuplerClaude/1.0"}
        h.update(headers or {})
        return urllib.request.Request(url, data=data, method=method, headers=h)

    def get(self, path, params=None):
        url = f"{self.site}/wp-json/wp/v2/{path}"
        if params:
            url += "?" + urllib.parse.urlencode(params)
        with urllib.request.urlopen(self._req(url), timeout=30) as r:
            return json.load(r), dict(r.headers)

    def post_json(self, path, payload):
        url = f"{self.site}/wp-json/wp/v2/{path}"
        req = self._req(url, data=json.dumps(payload).encode("utf-8"),
                        method="POST", headers={"Content-Type": "application/json"})
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)

    def upload_media(self, filepath, title, alt_text):
        url = f"{self.site}/wp-json/wp/v2/media"
        name = os.path.basename(filepath)
        ctype = mimetypes.guess_type(name)[0] or "image/png"
        with open(filepath, "rb") as f:
            body = f.read()
        req = self._req(url, data=body, method="POST", headers={
            "Content-Type": ctype,
            "Content-Disposition": f'attachment; filename="{name}"',
        })
        with urllib.request.urlopen(req, timeout=120) as r:
            media = json.load(r)
        # titre + texte alternatif (SEO) en second appel
        self.post_json(f"media/{media['id']}", {
            "title": title, "alt_text": alt_text,
        })
        return media

    def url_ok(self, url):
        try:
            req = urllib.request.Request(
                url, method="HEAD", headers={"User-Agent": "DecuplerClaude/1.0"})
            with urllib.request.urlopen(req, timeout=20) as r:
                return r.status == 200
        except Exception:
            return False


# ── Texte ────────────────────────────────────────────────────────────────────
