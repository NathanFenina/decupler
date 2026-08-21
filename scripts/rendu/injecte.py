#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Injecte un fragment dans le miroir d'une page réelle du site.

Permet de juger un brouillon avec le VRAI thème et les VRAIES polices, sans
avoir à le publier. La coquille locale de `captures.mjs` rend avec les polices
système, plus étroites : elle sous-estime les retours à la ligne.

    python3 scripts/rendu/injecte.py <miroir>/page.html <fragment.html> <sortie.html>
"""
import re, sys
from pathlib import Path

def injecte(miroir, fragment, sortie):
    h = Path(miroir).read_text(encoding='utf-8')
    frag = Path(fragment).read_text(encoding='utf-8')
    # Les images du fragment pointent vers decupler.com : on les fait passer par
    # le miroir quand il les a deja, sinon elles resteront simplement absentes.
    frag = re.sub(r'https://decupler\.com/wp-content/uploads/',
                  'assets/decupler.com/wp-content/uploads/', frag)
    m = re.search(r'(<div class="entry-content[^"]*"[^>]*>)(.*?)(</div><!-- \.entry-content)', h, re.S)
    if not m:
        m = re.search(r'(<div class="entry-content[^"]*"[^>]*>)(.*)(</div>\s*</article>)', h, re.S)
    assert m, "conteneur .entry-content introuvable dans le miroir"
    Path(sortie).write_text(h[:m.start(2)] + frag + h[m.end(2):], encoding='utf-8')
    print(f'{sortie} · fragment de {len(frag)} octets injecté')

if __name__ == '__main__':
    injecte(*sys.argv[1:4])
