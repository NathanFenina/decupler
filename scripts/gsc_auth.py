#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Obtient un jeton de rafraichissement Google, une seule fois, sur TA machine.

Pourquoi un compte OAuth et pas un compte de service : un compte de service
doit etre invite proprietee par proprietee dans Search Console. Toi, tu en as
23. Avec OAuth sur ton compte Google, tout ce que tu vois dans l'interface est
accessible d'un coup, sans invitation.

À FAIRE UNE FOIS, EN LOCAL (pas dans une session Claude) :

 1. console.cloud.google.com → nouveau projet, par exemple « decupler-gsc ».
 2. « API et services » → Bibliotheque → activer **Google Search Console API**.
 3. « API et services » → Identifiants → Creer → **ID client OAuth** →
    type **Application de bureau**. Telecharge le JSON.
 4. Ecran de consentement : externe, ajoute-toi en utilisateur de test.
 5. Puis ici :

        python3 scripts/gsc_auth.py --client-secret ~/Downloads/client_secret_xxx.json

    Le navigateur s'ouvre, tu autorises, le script affiche trois valeurs.

 6. Colle ces trois valeurs dans les **secrets d'environnement** de Claude
    Code (Reglages → Environnement), PAS dans le chat, PAS dans le depot :

        GSC_CLIENT_ID
        GSC_CLIENT_SECRET
        GSC_REFRESH_TOKEN

Le jeton de rafraichissement ne perime pas tant que tu ne le revoques pas.
"""
import os
import re
import sys
import json
import base64
import hashlib
import secrets
import argparse
import threading
import webbrowser
import urllib.parse
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer

AUTH = "https://accounts.google.com/o/oauth2/v2/auth"
TOKEN = "https://oauth2.googleapis.com/token"
SCOPE = "https://www.googleapis.com/auth/webmasters.readonly"

recu = {}


class Retour(BaseHTTPRequestHandler):
    def do_GET(self):
        q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        recu.update({k: v[0] for k, v in q.items()})
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        ok = "code" in recu
        self.wfile.write((
            "<meta charset='utf-8'><body style='font-family:system-ui;padding:60px;"
            "background:#fbfbfe;color:#14152b'><h2>"
            + ("Autorisation reçue." if ok else "Autorisation refusée.")
            + "</h2><p>Reviens dans ton terminal.</p></body>").encode())

    def log_message(self, *a):
        pass


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--client-secret", required=True,
                    help="le JSON telecharge depuis Google Cloud")
    ap.add_argument("--port", type=int, default=8765)
    args = ap.parse_args()

    conf = json.load(open(os.path.expanduser(args.client_secret), encoding="utf-8"))
    conf = conf.get("installed") or conf.get("web") or conf
    cid, csecret = conf["client_id"], conf["client_secret"]
    redirect = f"http://localhost:{args.port}"

    # PKCE : le secret d'une application de bureau n'est pas un secret, le
    # verificateur, si.
    verif = base64.urlsafe_b64encode(secrets.token_bytes(64)).decode().rstrip("=")
    defi = base64.urlsafe_b64encode(
        hashlib.sha256(verif.encode()).digest()).decode().rstrip("=")
    etat = secrets.token_urlsafe(16)

    url = AUTH + "?" + urllib.parse.urlencode({
        "client_id": cid, "redirect_uri": redirect, "response_type": "code",
        "scope": SCOPE, "access_type": "offline", "prompt": "consent",
        "code_challenge": defi, "code_challenge_method": "S256", "state": etat})

    srv = HTTPServer(("localhost", args.port), Retour)
    threading.Thread(target=srv.handle_request, daemon=True).start()
    print(f"→ Ouvre cette adresse si le navigateur ne le fait pas :\n{url}\n")
    webbrowser.open(url)
    srv_thread_done = threading.Event()
    while not recu:
        srv_thread_done.wait(0.3)

    if recu.get("state") != etat:
        sys.exit("❌ state invalide — recommence.")
    if "code" not in recu:
        sys.exit(f"❌ refus : {recu.get('error')}")

    data = urllib.parse.urlencode({
        "code": recu["code"], "client_id": cid, "client_secret": csecret,
        "redirect_uri": redirect, "grant_type": "authorization_code",
        "code_verifier": verif}).encode()
    with urllib.request.urlopen(urllib.request.Request(TOKEN, data=data)) as r:
        jetons = json.load(r)

    if "refresh_token" not in jetons:
        sys.exit("❌ Pas de refresh_token. Revoque l'acces sur "
                 "myaccount.google.com/permissions et recommence.")

    print("\n✅ À copier dans les secrets d'environnement de Claude Code :\n")
    print(f"GSC_CLIENT_ID={cid}")
    print(f"GSC_CLIENT_SECRET={csecret}")
    print(f"GSC_REFRESH_TOKEN={jetons['refresh_token']}")
    print("\n⚠️  Ne les colle pas dans une conversation : tout ce qui passe par "
          "le chat reste dans l'historique.")


if __name__ == "__main__":
    main()
