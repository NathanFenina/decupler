#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rapatrie une page en ligne et tous ses assets, pour la rendre localement.

Le navigateur de cette machine ne joint pas decupler.com (le proxy sortant
ne laisse passer que les clients qui lisent les variables d'environnement).
On telecharge donc la page et ses ressources avec urllib, on reecrit les URL
en chemins relatifs, et on sert le tout depuis 127.0.0.1 — que Chromium
atteint sans proxy. Ce qu'on regarde ensuite est la vraie page : vrai theme,
vrai header, vrais scripts inline.

    python3 scripts/rendu/miroir.py https://decupler.com/site-internet-offert/ /tmp/miroir
"""
import os, re, sys, urllib.parse, urllib.request
from pathlib import Path

UA = ('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36')


def telecharge(url, timeout=60):
    req = urllib.request.Request(url, headers={'User-Agent': UA,
                                               'Accept': '*/*',
                                               'Accept-Language': 'fr-FR,fr;q=0.9'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read(), r.headers.get('Content-Type', '')


def chemin_local(url):
    """Un chemin de fichier stable et sans surprise pour une URL."""
    u = urllib.parse.urlsplit(url)
    p = u.path.lstrip('/') or 'index'
    if u.query:
        p += '_' + re.sub(r'[^A-Za-z0-9]+', '', u.query)[:24]
    if not re.search(r'\.[A-Za-z0-9]{2,5}$', p):
        p += '.bin'
    return f'assets/{u.netloc}/{p}'


def miroir(url_page, dossier):
    base = Path(dossier)
    base.mkdir(parents=True, exist_ok=True)
    html = telecharge(url_page)[0].decode('utf-8', 'replace')
    origine = urllib.parse.urlsplit(url_page)

    # Toutes les URL citees dans un attribut, plus celles des url() de CSS inline.
    urls = set(re.findall(r'(?:href|src)="([^"]+)"', html))
    urls |= set(re.findall(r'url\((?:\'|")?([^)\'"]+)', html))

    vus, file = {}, []
    for u in urls:
        if u.startswith(('data:', 'mailto:', 'tel:', '#', 'javascript:')):
            continue
        abs_u = urllib.parse.urljoin(url_page, u)
        s = urllib.parse.urlsplit(abs_u)
        if s.scheme not in ('http', 'https'):
            continue
        file.append((u, abs_u))

    for brut, abs_u in file:
        if abs_u in vus:
            continue
        # On ne rapatrie pas les liens de navigation : seulement les ressources.
        if not re.search(r'\.(css|js|png|jpe?g|gif|svg|webp|woff2?|ttf|ico|avif)(\?|$)', abs_u) \
           and 'fonts.googleapis' not in abs_u:
            continue
        rel = chemin_local(abs_u)
        dest = base / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        try:
            corps, ctype = telecharge(abs_u)
        except Exception as e:
            print(f'  ⚠ {abs_u[:80]} → {str(e)[:50]}')
            continue
        # Une CSS peut appeler des polices : on rapatrie aussi ce second niveau.
        if 'css' in ctype or abs_u.endswith('.css') or 'fonts.googleapis' in abs_u:
            txt = corps.decode('utf-8', 'replace')
            for sous in set(re.findall(r'url\((?:\'|")?([^)\'"]+)', txt)):
                if sous.startswith('data:'):
                    continue
                sa = urllib.parse.urljoin(abs_u, sous)
                if not urllib.parse.urlsplit(sa).scheme.startswith('http'):
                    continue
                srel = chemin_local(sa)
                sdest = base / srel
                sdest.parent.mkdir(parents=True, exist_ok=True)
                if not sdest.exists():
                    try:
                        sdest.write_bytes(telecharge(sa)[0])
                    except Exception:
                        continue
                # Chemin relatif depuis l'emplacement de la CSS.
                txt = txt.replace(sous, os.path.relpath(sdest, dest.parent))
            dest.write_text(txt, encoding='utf-8')
        else:
            dest.write_bytes(corps)
        vus[abs_u] = rel

    # Une seule passe : remplacer d'abord la forme complete puis la forme sans
    # schema reecrivait les chemins deja traites (assets/assets/...).
    variantes = {}
    for abs_u, rel in vus.items():
        variantes[abs_u] = rel
        variantes['//' + abs_u.split('//', 1)[1]] = rel
    motif = re.compile('|'.join(re.escape(k) for k in
                                sorted(variantes, key=len, reverse=True)))
    html = motif.sub(lambda m: variantes[m.group(0)], html)

    (base / 'page.html').write_text(html, encoding='utf-8')
    print(f'{len(vus)} ressources · {base}/page.html')
    return base / 'page.html'


if __name__ == '__main__':
    miroir(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else '/tmp/miroir')
