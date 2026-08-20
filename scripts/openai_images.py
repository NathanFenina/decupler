#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère une image avec l'API OpenAI et l'enregistre sur disque.

La clé est lue dans l'environnement : OPEN_AI_KEY, ou OPENAI_API_KEY si elle
est nommée selon la convention. Elle n'est jamais écrite dans un fichier.

    python3 scripts/openai_images.py --prompt "..." --out img.png --size 1536x1024
"""
import argparse, base64, json, os, sys, urllib.request, urllib.error

ENDPOINT = 'https://api.openai.com/v1/images/generations'
MODELE = 'gpt-image-1'


def cle():
    for nom in ('OPEN_AI_KEY', 'OPENAI_API_KEY'):
        if os.environ.get(nom):
            return os.environ[nom]
    sys.exit("❌ Aucune clé trouvée. Définis OPEN_AI_KEY dans l'environnement "
             "(jamais dans un fichier, jamais dans une conversation).")


def genere(prompt, taille='1536x1024', qualite='high', fond='opaque'):
    charge = {'model': MODELE, 'prompt': prompt, 'size': taille,
              'quality': qualite, 'n': 1, 'output_format': 'png'}
    if fond == 'transparent':
        charge['background'] = 'transparent'
    req = urllib.request.Request(
        ENDPOINT, data=json.dumps(charge).encode('utf-8'), method='POST',
        headers={'Authorization': f'Bearer {cle()}', 'Content-Type': 'application/json',
                 'User-Agent': 'DecuplerClaude/1.0'})
    try:
        with urllib.request.urlopen(req, timeout=300) as r:
            rep = json.load(r)
    except urllib.error.HTTPError as e:
        corps = e.read().decode('utf-8', 'replace')
        sys.exit(f'❌ Erreur {e.code} : {corps[:600]}')
    d = rep['data'][0]
    if d.get('b64_json'):
        return base64.b64decode(d['b64_json'])
    with urllib.request.urlopen(d['url'], timeout=180) as r:   # certains modèles renvoient une URL
        return r.read()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--prompt', required=True)
    ap.add_argument('--out', required=True)
    ap.add_argument('--size', default='1536x1024',
                    choices=['1024x1024', '1536x1024', '1024x1536', 'auto'])
    ap.add_argument('--quality', default='high', choices=['low', 'medium', 'high', 'auto'])
    ap.add_argument('--background', default='opaque', choices=['opaque', 'transparent'])
    a = ap.parse_args()

    donnees = genere(a.prompt, a.size, a.quality, a.background)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)) or '.', exist_ok=True)
    open(a.out, 'wb').write(donnees)
    print(f'✅ {a.out} · {len(donnees)//1024} Ko · {a.size} · {MODELE}')


if __name__ == '__main__':
    main()
