# -*- coding: utf-8 -*-
"""Mesure la longueur des phrases sur du HTML, en respectant les blocs.

`analyze_content.py` du skill de scoring retire les balises puis découpe sur
la ponctuation. Un titre et le paragraphe qui le suit n'ont pas de point entre
eux : ils sont comptés comme UNE phrase. Sur une page en cartes — un titre et
un paragraphe par carte — ça gonfle mécaniquement le taux de phrases longues :
37 % mesuré contre 16 % réels sur supprimer-un-avis-google.

On insère donc un point à chaque frontière de bloc avant de découper.
"""
import re

BLOCS = 'h1|h2|h3|h4|h5|h6|p|li|td|th|div|summary|section|figcaption|blockquote'


def phrases(html: str):
    html = re.sub(r'<style>.*?</style>|<script.*?</script>', '', html, flags=re.S)
    html = re.sub(rf'</({BLOCS})>', '. ', html)
    txt = re.sub(r'<[^>]+>', ' ', html).replace('&nbsp;', ' ')
    txt = re.sub(r'\s+', ' ', txt)
    return [p.strip() for p in re.split(r'(?<=[.!?])\s+', txt) if len(p.split()) > 2]


def taux_phrases_longues(html: str, seuil: int = 20):
    """Part des phrases de plus de `seuil` mots. Vert sous 25 %."""
    ph = phrases(html)
    if not ph:
        return 0.0
    return 100 * sum(1 for p in ph if len(p.split()) > seuil) / len(ph)


if __name__ == '__main__':
    import sys
    for f in sys.argv[1:]:
        h = open(f, encoding='utf-8').read()
        ph = phrases(h)
        longues = [p for p in ph if len(p.split()) > 20]
        print(f'{f.split("/")[-1]:32} {len(ph):>4} phrases · {len(longues):>3} longues · '
              f'{taux_phrases_longues(h):>4.0f}%')
