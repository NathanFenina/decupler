#!/usr/bin/env python3
"""
gemini_images.py — Serveur MCP autonome pour générer des images avec Google
Gemini (« Nano Banana », modèle gemini-2.5-flash-image) via l'API REST.

Pensé pour l'atelier de contenu Décupler : créer des images (illustrations,
schémas, visuels d'articles) pour nos pages et celles des sites clients, puis
les téléverser dans WordPress (voir scripts/wp_upload_media.py).

CARACTÉRISTIQUES
- Zéro dépendance : uniquement la bibliothèque standard Python 3.9+.
  → tourne partout, sans pip, sans venv, sans installation réseau.
- Transport MCP stdio (JSON-RPC 2.0 délimité par des retours à la ligne).
- Respecte HTTPS_PROXY / SSL_CERT_FILE (utile en environnement mandaté).

CONFIGURATION (variables d'environnement)
- GEMINI_API_KEY      Clé API Google AI Studio (obligatoire). Alias acceptés :
                      GOOGLE_API_KEY, GOOGLE_GENAI_API_KEY, IMAGE_API_KEY.
- GEMINI_IMAGE_MODEL  Modèle (défaut : gemini-2.5-flash-image).
- GEMINI_IMAGE_DIR    Dossier de sortie par défaut (défaut : ./generated-images).

La clé est aussi lue depuis un fichier .env situé à la racine du dépôt (ou dans
le dossier de travail / les dossiers parents), pour coller au workflow existant.

OUTILS EXPOSÉS
- generate_image      Génère une image depuis un prompt texte (+ images de
                      référence optionnelles pour l'édition/le style). Enregistre
                      un PNG sur disque et renvoie son chemin.
- list_models         Rappelle les modèles image Gemini utilisables.
"""
import base64
import json
import mimetypes
import os
import ssl
import sys
import time
import urllib.error
import urllib.request

SERVER_NAME = "gemini-images"
SERVER_VERSION = "1.0.0"
DEFAULT_MODEL = os.environ.get("GEMINI_IMAGE_MODEL", "gemini-2.5-flash-image")
API_BASE = "https://generativelanguage.googleapis.com/v1beta"
# Version du protocole MCP par défaut si le client n'en propose pas.
DEFAULT_PROTOCOL = "2025-06-18"


def log(*args):
    """Journalise sur stderr uniquement — stdout est réservé au protocole MCP."""
    print("[gemini-images]", *args, file=sys.stderr, flush=True)


# --------------------------------------------------------------------------- #
# Configuration : clé API, .env, contexte SSL
# --------------------------------------------------------------------------- #
def _load_dotenv_key():
    """Cherche une clé API dans un fichier .env (cwd puis dossiers parents, et le
    dossier du script). Ne remplace pas une variable déjà présente dans l'env."""
    names = ("GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_GENAI_API_KEY", "IMAGE_API_KEY")
    candidates = []
    here = os.path.dirname(os.path.abspath(__file__))
    # Racine probable du dépôt (scripts/mcp/.. -> scripts/.. -> repo)
    candidates.append(os.path.join(here, "..", "..", ".env"))
    d = os.getcwd()
    for _ in range(6):
        candidates.append(os.path.join(d, ".env"))
        parent = os.path.dirname(d)
        if parent == d:
            break
        d = parent
    seen = set()
    for path in candidates:
        path = os.path.abspath(path)
        if path in seen or not os.path.isfile(path):
            continue
        seen.add(path)
        try:
            with open(path, "r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.strip()
                    if not line or line.startswith("#") or "=" not in line:
                        continue
                    key, _, val = line.partition("=")
                    key = key.strip()
                    if key in names:
                        val = val.strip().strip('"').strip("'")
                        if val and key not in os.environ:
                            os.environ[key] = val
        except OSError:
            continue


def get_api_key():
    for name in ("GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_GENAI_API_KEY", "IMAGE_API_KEY"):
        val = os.environ.get(name)
        if val:
            return val
    return None


def build_ssl_context():
    """Contexte SSL par défaut, augmenté des bundles CA connus (proxy mandaté)."""
    ctx = ssl.create_default_context()
    for env_var in ("GEMINI_CA_BUNDLE", "SSL_CERT_FILE", "REQUESTS_CA_BUNDLE"):
        p = os.environ.get(env_var)
        if p and os.path.isfile(p):
            try:
                ctx.load_verify_locations(cafile=p)
            except ssl.SSLError:
                pass
    for p in ("/root/.ccr/ca-bundle.crt",):
        if os.path.isfile(p):
            try:
                ctx.load_verify_locations(cafile=p)
            except ssl.SSLError:
                pass
    return ctx


SSL_CONTEXT = build_ssl_context()


# --------------------------------------------------------------------------- #
# Appel à l'API Gemini
# --------------------------------------------------------------------------- #
def _read_image_as_part(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    mime = mimetypes.guess_type(path)[0] or "image/png"
    return {"inline_data": {"mime_type": mime, "data": base64.b64encode(raw).decode("ascii")}}


def gemini_generate(prompt, model, input_images=None, timeout=180):
    """Appelle {model}:generateContent et renvoie (bytes_image, mime, texte).
    Lève une RuntimeError avec un message clair en cas d'échec."""
    api_key = get_api_key()
    if not api_key:
        raise RuntimeError(
            "Aucune clé API. Définis GEMINI_API_KEY (ou GOOGLE_API_KEY / IMAGE_API_KEY) "
            "dans l'environnement ou dans le fichier .env du dépôt."
        )

    parts = [{"text": prompt}]
    for img in input_images or []:
        if not os.path.isfile(img):
            raise RuntimeError(f"Image de référence introuvable : {img}")
        parts.append(_read_image_as_part(img))

    body = {"contents": [{"role": "user", "parts": parts}]}
    # Les modèles « preview » 2.0 exigent responseModalities ; 2.5-flash-image non.
    if "2.0" in model:
        body["generationConfig"] = {"responseModalities": ["TEXT", "IMAGE"]}

    url = f"{API_BASE}/models/{model}:generateContent"
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json", "x-goog-api-key": api_key},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=SSL_CONTEXT) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        detail = ""
        try:
            detail = e.read().decode("utf-8")
        except Exception:
            pass
        raise RuntimeError(f"Erreur API Gemini {e.code} : {detail[:800]}")
    except urllib.error.URLError as e:
        raise RuntimeError(f"Erreur réseau vers l'API Gemini : {e.reason}")

    candidates = payload.get("candidates") or []
    if not candidates:
        fb = payload.get("promptFeedback") or {}
        raise RuntimeError(f"Aucune image renvoyée. promptFeedback={json.dumps(fb)[:500]}")

    img_bytes, mime, text_out = None, None, []
    for part in (candidates[0].get("content") or {}).get("parts") or []:
        inline = part.get("inlineData") or part.get("inline_data")
        if inline and inline.get("data"):
            img_bytes = base64.b64decode(inline["data"])
            mime = inline.get("mimeType") or inline.get("mime_type") or "image/png"
        elif part.get("text"):
            text_out.append(part["text"])

    if img_bytes is None:
        joined = " ".join(text_out).strip()
        raise RuntimeError(
            "Le modèle n'a pas renvoyé d'image."
            + (f" Réponse texte : {joined[:500]}" if joined else "")
        )
    return img_bytes, mime, " ".join(text_out).strip()


def _ext_for_mime(mime):
    return {"image/png": ".png", "image/jpeg": ".jpg", "image/webp": ".webp"}.get(mime, ".png")


def save_image(img_bytes, mime, output_path=None):
    if output_path:
        out = os.path.abspath(os.path.expanduser(output_path))
        os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    else:
        out_dir = os.path.abspath(os.environ.get("GEMINI_IMAGE_DIR", "generated-images"))
        os.makedirs(out_dir, exist_ok=True)
        stamp = time.strftime("%Y%m%d-%H%M%S")
        out = os.path.join(out_dir, f"gemini-{stamp}{_ext_for_mime(mime)}")
    with open(out, "wb") as fh:
        fh.write(img_bytes)
    return out


# --------------------------------------------------------------------------- #
# Définition des outils MCP
# --------------------------------------------------------------------------- #
TOOLS = [
    {
        "name": "generate_image",
        "description": (
            "Génère une image avec Google Gemini (Nano Banana, gemini-2.5-flash-image) "
            "à partir d'un prompt en texte. Idéal pour illustrer un article ou une page "
            "(illustration, schéma, visuel de couverture) pour Décupler ou un site client. "
            "Enregistre un fichier image sur le disque et renvoie son chemin, prêt à être "
            "téléversé dans WordPress. Des images de référence (input_images) peuvent être "
            "fournies pour de l'édition ou du transfert de style."
        ),
        "inputSchema": {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "Description détaillée de l'image souhaitée (sujet, style, ambiance, texte à afficher, couleurs). Plus c'est précis, mieux c'est.",
                },
                "output_path": {
                    "type": "string",
                    "description": "Chemin de sortie du fichier (ex : content/articles/images/hero.png). Optionnel : par défaut un fichier horodaté dans ./generated-images.",
                },
                "input_images": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Chemins d'images de référence à éditer ou dont s'inspirer (optionnel).",
                },
                "aspect_ratio": {
                    "type": "string",
                    "description": "Format souhaité, ajouté au prompt (ex : '16:9', '1:1', '3:2'). Optionnel.",
                },
                "model": {
                    "type": "string",
                    "description": f"Modèle Gemini à utiliser (défaut : {DEFAULT_MODEL}).",
                },
            },
            "required": ["prompt"],
        },
    },
    {
        "name": "list_models",
        "description": "Liste les modèles Gemini de génération d'images utilisables et le modèle par défaut configuré.",
        "inputSchema": {"type": "object", "properties": {}},
    },
]


def tool_generate_image(args):
    prompt = (args.get("prompt") or "").strip()
    if not prompt:
        raise RuntimeError("Le paramètre 'prompt' est obligatoire.")
    model = (args.get("model") or DEFAULT_MODEL).strip()
    aspect = (args.get("aspect_ratio") or "").strip()
    if aspect:
        prompt = f"{prompt}\n\nFormat / ratio de l'image : {aspect}."
    input_images = args.get("input_images") or []

    img_bytes, mime, text_out = gemini_generate(prompt, model, input_images=input_images)
    out = save_image(img_bytes, mime, args.get("output_path"))
    log(f"Image générée : {out} ({len(img_bytes)} octets, {mime})")

    summary = f"Image générée et enregistrée : {out}\nModèle : {model} · Type : {mime} · Taille : {len(img_bytes)} octets"
    if text_out:
        summary += f"\nNote du modèle : {text_out[:400]}"
    summary += (
        "\n\nÉtape suivante possible : téléverser dans WordPress via "
        f"`python3 scripts/wp_upload_media.py --file {out} --title \"...\" --alt \"...\"`."
    )
    content = [
        {"type": "text", "text": summary},
        {"type": "image", "data": base64.b64encode(img_bytes).decode("ascii"), "mimeType": mime},
    ]
    return content


def tool_list_models(_args):
    text = (
        "Modèles Gemini pour la génération d'images :\n"
        "- gemini-2.5-flash-image  (« Nano Banana », recommandé — défaut)\n"
        "- gemini-2.0-flash-preview-image-generation  (génération + texte)\n"
        f"\nModèle par défaut configuré : {DEFAULT_MODEL}\n"
        f"Clé API détectée : {'oui' if get_api_key() else 'NON — configure GEMINI_API_KEY'}"
    )
    return [{"type": "text", "text": text}]


TOOL_IMPL = {
    "generate_image": tool_generate_image,
    "list_models": tool_list_models,
}


# --------------------------------------------------------------------------- #
# Boucle MCP (JSON-RPC 2.0 sur stdio, messages délimités par des \n)
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

    if method in ("notifications/initialized", "initialized"):
        return  # notification, aucune réponse
    if method and method.startswith("notifications/"):
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
            reply(msg_id, {
                "content": [{"type": "text", "text": f"Outil inconnu : {name}"}],
                "isError": True,
            })
            return
        try:
            content = impl(args)
            reply(msg_id, {"content": content, "isError": False})
        except Exception as e:  # noqa: BLE001 — on renvoie l'erreur au client MCP
            log(f"Erreur outil {name} : {e}")
            reply(msg_id, {"content": [{"type": "text", "text": f"Erreur : {e}"}], "isError": True})
        return

    # Méthode inconnue
    if is_request:
        reply_error(msg_id, -32601, f"Méthode non gérée : {method}")


def main():
    _load_dotenv_key()
    log(f"démarrage · modèle par défaut={DEFAULT_MODEL} · clé API={'oui' if get_api_key() else 'non'}")
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
