#!/usr/bin/env python3
"""
yoast_seo.py — Serveur MCP autonome pour lire et écrire les métadonnées
**Yoast SEO** des articles et pages WordPress (via l'API REST).

Pensé pour l'atelier Décupler : quand on rédige/publie un contenu, on peut aussi
régler d'un coup le titre SEO, la méta description, la requête cible (focus
keyphrase), le canonical, l'indexation (noindex/nofollow) et l'Open Graph — sans
passer par l'admin WordPress.

CARACTÉRISTIQUES
- Zéro dépendance : uniquement la bibliothèque standard Python 3.9+.
- Transport MCP stdio (JSON-RPC 2.0 délimité par des retours à la ligne).
- Réutilise les identifiants WordPress du .env (comme scripts/wp_publish.py) :
  WP_SITE_URL, WP_USER, WP_APP_PASSWORD.

OUTILS EXPOSÉS
- find_content   Cherche un article/une page (par mot-clé ou slug), brouillons
                 compris, et renvoie leurs IDs.
- get_seo        Lit les métadonnées Yoast SEO actuelles d'un contenu.
- set_seo        Écrit les métadonnées Yoast SEO d'un contenu.

⚠️ ÉCRITURE (set_seo) : WordPress protège les métadonnées Yoast (préfixe « _ »).
Pour les écrire via l'API REST, ajoute le petit mu-plugin fourni dans
`wordpress/decupler-yoast-rest.php` (voir scripts/mcp/README.md). La LECTURE
fonctionne sans rien, via `yoast_head_json`.
"""
import base64
import json
import os
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request

SERVER_NAME = "yoast-seo"
SERVER_VERSION = "1.0.0"
DEFAULT_PROTOCOL = "2025-06-18"
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))

# Clés de métadonnées Yoast SEO (postmeta WordPress)
YOAST_KEYS = {
    "seo_title": "_yoast_wpseo_title",
    "meta_description": "_yoast_wpseo_metadesc",
    "focus_keyphrase": "_yoast_wpseo_focuskw",
    "canonical": "_yoast_wpseo_canonical",
    "og_title": "_yoast_wpseo_opengraph-title",
    "og_description": "_yoast_wpseo_opengraph-description",
    "og_image": "_yoast_wpseo_opengraph-image",
    "twitter_title": "_yoast_wpseo_twitter-title",
    "twitter_description": "_yoast_wpseo_twitter-description",
}
ROBOTS_NOINDEX_KEY = "_yoast_wpseo_meta-robots-noindex"   # '1' = noindex, '2' = index, '0' = défaut
ROBOTS_NOFOLLOW_KEY = "_yoast_wpseo_meta-robots-nofollow"  # '1' = nofollow, '0' = follow


def log(*args):
    print("[yoast-seo]", *args, file=sys.stderr, flush=True)


# --------------------------------------------------------------------------- #
# Config : .env, SSL
# --------------------------------------------------------------------------- #
def load_env():
    env = dict(os.environ)
    for path in (os.path.join(ROOT, ".env"), os.path.join(os.getcwd(), ".env")):
        if not os.path.isfile(path):
            continue
        try:
            with open(path, encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    k, v = line.split("=", 1)
                    env.setdefault(k.strip(), v.strip().strip('"').strip("'"))
        except OSError:
            pass
    return env


def build_ssl_context():
    ctx = ssl.create_default_context()
    for env_var in ("SSL_CERT_FILE", "REQUESTS_CA_BUNDLE"):
        p = os.environ.get(env_var)
        if p and os.path.isfile(p):
            try:
                ctx.load_verify_locations(cafile=p)
            except ssl.SSLError:
                pass
    if os.path.isfile("/root/.ccr/ca-bundle.crt"):
        try:
            ctx.load_verify_locations(cafile="/root/.ccr/ca-bundle.crt")
        except ssl.SSLError:
            pass
    return ctx


SSL_CONTEXT = build_ssl_context()


def wp_creds():
    env = load_env()
    site = (env.get("WP_SITE_URL") or "").rstrip("/")
    user = env.get("WP_USER") or ""
    app_pw = (env.get("WP_APP_PASSWORD") or "").replace(" ", "")
    if not (site and user and app_pw) or "ton-utilisateur" in user or "xxxx" in app_pw:
        raise RuntimeError(
            "Identifiants WordPress manquants. Renseigne WP_SITE_URL, WP_USER et "
            "WP_APP_PASSWORD dans le .env du dépôt."
        )
    return site, user, app_pw


def wp_request(method, path, params=None, body=None, timeout=30):
    """Appelle l'API REST WordPress. path ex : '/wp/v2/posts'."""
    site, user, app_pw = wp_creds()
    url = f"{site}/wp-json{path}"
    if params:
        url += "?" + urllib.parse.urlencode(params, doseq=True)
    token = base64.b64encode(f"{user}:{app_pw}".encode()).decode()
    headers = {
        "Authorization": f"Basic {token}",
        "Content-Type": "application/json",
        "User-Agent": "DecuplerClaude/1.0",
    }
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CONTEXT) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = ""
        try:
            detail = e.read().decode("utf-8")
        except Exception:
            pass
        raise RuntimeError(f"Erreur WordPress {e.code} sur {method} {path} : {detail[:600]}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Erreur réseau vers WordPress : {e.reason}")


def _endpoint(ptype):
    return "pages" if ptype == "page" else "posts"


def _resolve_id(ptype, args):
    """Retourne l'ID à partir de 'id' ou 'slug'."""
    if args.get("id"):
        return int(args["id"])
    slug = args.get("slug")
    if not slug:
        raise RuntimeError("Fournis 'id' ou 'slug'.")
    res = wp_request("GET", f"/wp/v2/{_endpoint(ptype)}", params={
        "slug": slug, "status": "publish,future,draft,pending,private",
        "_fields": "id,slug", "per_page": 5,
    })
    if not res:
        raise RuntimeError(f"Aucun contenu de type '{ptype}' avec le slug '{slug}'.")
    return int(res[0]["id"])


# --------------------------------------------------------------------------- #
# Outils
# --------------------------------------------------------------------------- #
def tool_find_content(args):
    ptype = args.get("type", "post")
    search = args.get("search", "")
    slug = args.get("slug")
    params = {
        "status": "publish,future,draft,pending,private",
        "_fields": "id,title,slug,status,link,type",
        "per_page": int(args.get("per_page", 10)),
        "orderby": "modified",
    }
    if search:
        params["search"] = search
    if slug:
        params["slug"] = slug
    res = wp_request("GET", f"/wp/v2/{_endpoint(ptype)}", params=params)
    rows = []
    for p in res:
        rows.append({
            "id": p.get("id"),
            "title": (p.get("title") or {}).get("rendered", ""),
            "slug": p.get("slug"),
            "status": p.get("status"),
            "link": p.get("link"),
        })
    text = f"{len(rows)} résultat(s) ({ptype}) :\n" + json.dumps(rows, ensure_ascii=False, indent=2)
    return [{"type": "text", "text": text}]


def tool_get_seo(args):
    ptype = args.get("type", "post")
    pid = _resolve_id(ptype, args)
    p = wp_request("GET", f"/wp/v2/{_endpoint(ptype)}/{pid}", params={
        "context": "edit",
        "_fields": "id,title,slug,link,status,meta,yoast_head_json",
    })
    meta = p.get("meta") or {}
    stored = {name: meta.get(key) for name, key in YOAST_KEYS.items() if meta.get(key)}
    if meta.get(ROBOTS_NOINDEX_KEY):
        stored["robots_noindex_raw"] = meta.get(ROBOTS_NOINDEX_KEY)
    if meta.get(ROBOTS_NOFOLLOW_KEY):
        stored["robots_nofollow_raw"] = meta.get(ROBOTS_NOFOLLOW_KEY)

    head = p.get("yoast_head_json") or {}
    rendered = {
        "title": head.get("title"),
        "description": head.get("description"),
        "robots": head.get("robots"),
        "canonical": head.get("canonical"),
        "og_title": head.get("og_title"),
        "og_description": head.get("og_description"),
        "og_image": head.get("og_image"),
    }
    out = {
        "id": p.get("id"),
        "slug": p.get("slug"),
        "status": p.get("status"),
        "link": p.get("link"),
        "yoast_stored": stored or "(aucune méta Yoast brute exposée via REST — voir mu-plugin)",
        "rendu_actuel": rendered,
    }
    return [{"type": "text", "text": json.dumps(out, ensure_ascii=False, indent=2)}]


def tool_set_seo(args):
    ptype = args.get("type", "post")
    pid = _resolve_id(ptype, args)

    meta = {}
    for name, key in YOAST_KEYS.items():
        if name in args and args[name] is not None:
            meta[key] = str(args[name])
    if "noindex" in args and args["noindex"] is not None:
        meta[ROBOTS_NOINDEX_KEY] = "1" if args["noindex"] else "2"
    if "nofollow" in args and args["nofollow"] is not None:
        meta[ROBOTS_NOFOLLOW_KEY] = "1" if args["nofollow"] else "0"

    if not meta:
        raise RuntimeError(
            "Rien à écrire. Fournis au moins un champ : seo_title, meta_description, "
            "focus_keyphrase, canonical, noindex, nofollow, og_title, og_description, og_image…"
        )

    wp_request("POST", f"/wp/v2/{_endpoint(ptype)}/{pid}", body={"meta": meta})

    # Relecture pour vérifier ce qui a bien été appliqué.
    check = wp_request("GET", f"/wp/v2/{_endpoint(ptype)}/{pid}", params={
        "context": "edit", "_fields": "id,meta,link",
    })
    got = check.get("meta") or {}
    applied, ignored = {}, {}
    for key, val in meta.items():
        if str(got.get(key, "")) == str(val):
            applied[key] = val
        else:
            ignored[key] = val

    lines = [f"Mise à jour SEO de {ptype} #{pid} ({check.get('link')})"]
    if applied:
        lines.append("✅ Appliqué : " + ", ".join(sorted(applied)))
    if ignored:
        lines.append(
            "⚠️ Non appliqué (WordPress a ignoré ces métas protégées) : "
            + ", ".join(sorted(ignored))
            + "\n→ Ajoute le mu-plugin `wordpress/decupler-yoast-rest.php` sur le site "
            "pour autoriser l'écriture Yoast via REST (voir scripts/mcp/README.md)."
        )
    return [{"type": "text", "text": "\n".join(lines)}]


TOOLS = [
    {
        "name": "find_content",
        "description": "Cherche un article ou une page WordPress (par mot-clé et/ou slug), brouillons inclus, et renvoie leurs IDs, titres, slugs, statuts et liens. Sert à récupérer l'ID avant get_seo / set_seo.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "type": {"type": "string", "enum": ["post", "page"], "description": "Type de contenu (défaut : post)."},
                "search": {"type": "string", "description": "Mot-clé à chercher dans le titre/contenu."},
                "slug": {"type": "string", "description": "Slug exact (optionnel)."},
                "per_page": {"type": "integer", "description": "Nombre de résultats (défaut 10)."},
            },
        },
    },
    {
        "name": "get_seo",
        "description": "Lit les métadonnées Yoast SEO actuelles d'un article/page (titre SEO, méta description, requête cible, canonical, robots, Open Graph) — valeurs stockées et rendu réel. Identifie le contenu par 'id' ou 'slug'.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "type": {"type": "string", "enum": ["post", "page"], "description": "Type de contenu (défaut : post)."},
                "id": {"type": "integer", "description": "ID du contenu."},
                "slug": {"type": "string", "description": "Slug du contenu (alternative à id)."},
            },
        },
    },
    {
        "name": "set_seo",
        "description": "Écrit les métadonnées Yoast SEO d'un article/page : seo_title, meta_description, focus_keyphrase, canonical, noindex, nofollow, og_title, og_description, og_image, twitter_title, twitter_description. Identifie le contenu par 'id' ou 'slug'. (Nécessite le mu-plugin decupler-yoast-rest.php côté WordPress pour l'écriture.)",
        "inputSchema": {
            "type": "object",
            "properties": {
                "type": {"type": "string", "enum": ["post", "page"], "description": "Type de contenu (défaut : post)."},
                "id": {"type": "integer", "description": "ID du contenu."},
                "slug": {"type": "string", "description": "Slug du contenu (alternative à id)."},
                "seo_title": {"type": "string", "description": "Titre SEO (balise <title>). Variables Yoast acceptées, ex : '%%title%% %%sep%% %%sitename%%'."},
                "meta_description": {"type": "string", "description": "Méta description (~155 caractères)."},
                "focus_keyphrase": {"type": "string", "description": "Requête cible principale."},
                "canonical": {"type": "string", "description": "URL canonique."},
                "noindex": {"type": "boolean", "description": "true = noindex, false = index."},
                "nofollow": {"type": "boolean", "description": "true = nofollow, false = follow."},
                "og_title": {"type": "string", "description": "Titre Open Graph (partage social)."},
                "og_description": {"type": "string", "description": "Description Open Graph."},
                "og_image": {"type": "string", "description": "URL de l'image Open Graph."},
                "twitter_title": {"type": "string", "description": "Titre Twitter/X."},
                "twitter_description": {"type": "string", "description": "Description Twitter/X."},
            },
        },
    },
]

TOOL_IMPL = {
    "find_content": tool_find_content,
    "get_seo": tool_get_seo,
    "set_seo": tool_set_seo,
}


# --------------------------------------------------------------------------- #
# Boucle MCP (JSON-RPC 2.0 sur stdio)
# --------------------------------------------------------------------------- #
def send(msg):
    sys.stdout.write(json.dumps(msg) + "\n")
    sys.stdout.flush()


def reply(msg_id, result):
    send({"jsonrpc": "2.0", "id": msg_id, "result": result})


def reply_error(msg_id, code, message):
    send({"jsonrpc": "2.0", "id": msg_id, "error": {"code": code, "message": message}})


def handle(msg):
    method = msg.get("method")
    msg_id = msg.get("id")
    is_request = msg_id is not None

    if method == "initialize":
        params = msg.get("params") or {}
        proto = params.get("protocolVersion") or DEFAULT_PROTOCOL
        reply(msg_id, {
            "protocolVersion": proto,
            "capabilities": {"tools": {"listChanged": False}},
            "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
        })
        return
    if method and method.startswith("notifications/"):
        return
    if method == "initialized":
        return
    if method == "ping":
        if is_request:
            reply(msg_id, {})
        return
    if method == "tools/list":
        reply(msg_id, {"tools": TOOLS})
        return
    if method == "tools/call":
        params = msg.get("params") or {}
        name = params.get("name")
        args = params.get("arguments") or {}
        impl = TOOL_IMPL.get(name)
        if impl is None:
            reply(msg_id, {"content": [{"type": "text", "text": f"Outil inconnu : {name}"}], "isError": True})
            return
        try:
            reply(msg_id, {"content": impl(args), "isError": False})
        except Exception as e:  # noqa: BLE001
            log(f"Erreur outil {name} : {e}")
            reply(msg_id, {"content": [{"type": "text", "text": f"Erreur : {e}"}], "isError": True})
        return
    if is_request:
        reply_error(msg_id, -32601, f"Méthode non gérée : {method}")


def main():
    log("démarrage")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            log(f"ligne JSON invalide ignorée : {line[:120]}")
            continue
        try:
            handle(msg)
        except Exception as e:  # noqa: BLE001
            log(f"erreur de traitement : {e}")
            if isinstance(msg, dict) and msg.get("id") is not None:
                reply_error(msg["id"], -32603, str(e))


if __name__ == "__main__":
    main()
