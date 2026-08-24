# -*- coding: utf-8 -*-
"""Rend une feuille de style inline sûre pour WordPress.

wpautop transforme toute ligne vide en `</p><p>` — y compris À L'INTÉRIEUR
d'un bloc <style>. Le parseur CSS abandonne alors toutes les règles qui
suivent la première balise injectée. Un skin lisible, écrit avec des
commentaires de section et des lignes vides, perd donc la moitié de ses
règles une fois publié.

On garde le fichier source lisible et on le minifie à la génération.
"""
import re


def minify_css(css: str) -> str:
    """Retire commentaires et sauts de ligne, sans toucher aux valeurs."""
    # Les chaînes (content:'→') sont mises de côté avant tout traitement.
    strings = []

    def stash(m):
        strings.append(m.group(0))
        return f'\x00{len(strings) - 1}\x00'

    css = re.sub(r"'[^'\n]*'|\"[^\"\n]*\"", stash, css)
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.S)      # commentaires
    css = re.sub(r'\s+', ' ', css)                        # tout blanc -> 1 espace
    css = re.sub(r'\s*([{};,])\s*', r'\1', css)           # autour des séparateurs
    css = re.sub(r';\}', '}', css)                        # point-virgule final
    css = css.strip()
    return re.sub(r'\x00(\d+)\x00', lambda m: strings[int(m.group(1))], css)


def sans_lignes_vides(bloc: str) -> str:
    """Supprime les lignes vides d'un bloc, en gardant le reste lisible.

    wpautop coupe sur `\n\n` PARTOUT, y compris dans un <script>. Une ligne
    vide au milieu du JS y fait apparaitre `</p><p>` : le script ne parse plus,
    et tout ce qu'il devait faire ne se fait pas. Vu en production le 21 aout
    2026 sur /site-internet-offert/ — la page entiere restait a opacity:0.
    """
    return re.sub(r'\n\s*\n+', '\n', bloc)


def harden(html: str) -> str:
    """Rend inline styles ET scripts insensibles a wpautop."""
    def css(m):
        return '<style>' + minify_css(m.group(1)) + '</style>'
    html = re.sub(r'<style>(.*?)</style>', css, html, flags=re.S)

    def js(m):
        return m.group(1) + sans_lignes_vides(m.group(2)) + '</script>'
    html = re.sub(r'(<script[^>]*>)(.*?)</script>', js, html, flags=re.S)

    # Un <noscript> multiligne subit le meme sort : wpautop le coupe en deux et
    # sa feuille de secours s'applique alors TOUT LE TEMPS.
    def nos(m):
        return '<noscript>' + re.sub(r'\s*\n\s*', '', m.group(1)) + '</noscript>'
    return re.sub(r'<noscript>(.*?)</noscript>', nos, html, flags=re.S)


def audit(html: str):
    """Contrôle qu'aucun bloc <style>, <script> ou <noscript> ne peut plus
    déclencher wpautop."""
    problemes = []
    for i, bloc in enumerate(re.findall(r'<script[^>]*>(.*?)</script>', html, flags=re.S)):
        if re.search(r'\n\s*\n', bloc):
            problemes.append(f'script {i}: ligne vide (wpautop y insérera </p><p> '
                             f'et le script ne parsera plus)')
        if '&' in bloc:
            # WordPress convertit tout `&` isolé (donc aussi `&&`) en `&#038;`
            # a l'enregistrement, meme a l'interieur d'un <script> — le JS ne
            # parse plus. Vu en production sur /site-gratuit-local/ le 24 aout
            # 2026 : `&&` devenait `&#038;&#038;`. Jamais de `&` litteral dans
            # un script ; utiliser un ternaire (A?B:false) au lieu de `A&&B`.
            n = bloc.count('&')
            problemes.append(f"script {i}: {n} caractere(s) '&' — WordPress les "
                              f"transforme en '&#038;' et casse le JS (pas de && ; "
                              f"remplacer A&&B par A?B:false)")
    for i, bloc in enumerate(re.findall(r'<noscript>(.*?)</noscript>', html, flags=re.S)):
        if '\n' in bloc:
            problemes.append(f'noscript {i}: saut de ligne (wpautop le coupera en deux)')
    for i, bloc in enumerate(re.findall(r'<style>(.*?)</style>', html, flags=re.S)):
        if '\n\n' in bloc:
            problemes.append(f'bloc {i}: ligne vide (wpautop y insérera </p><p>)')
        if '\n' in bloc:
            problemes.append(f'bloc {i}: saut de ligne résiduel ({bloc.count(chr(10))})')
        if re.search(r'/\*', bloc):
            problemes.append(f'bloc {i}: commentaire non retiré')
    return problemes


# ── Détection du motif que wpautop casse ────────────────────────────────────
BLOCS = {'div', 'p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'ul', 'ol', 'li', 'table',
         'section', 'article', 'figure', 'blockquote', 'pre', 'form', 'details', 'header'}
INLINES = {'span', 'a', 'b', 'i', 'em', 'strong', 'small', 'code', 'sup', 'sub'}


def audit_markup(html: str):
    """Signale les conteneurs qui mélangent enfants inline et enfants block.

    wpautop insère un `</p>` orphelin juste après l'enfant inline. Le navigateur
    en fait un paragraphe vide, qui devient un enfant supplémentaire du conteneur
    — et décale toute grille ou tout flex.
    """
    from html.parser import HTMLParser

    class P(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.pile = []           # (tag, classe, [tags des enfants])
            self.pb = []

        def handle_starttag(self, tag, attrs):
            cls = dict(attrs).get('class', '')
            if self.pile:
                self.pile[-1][2].append(tag)
            if tag not in ('br', 'img', 'hr', 'input', 'meta', 'link', 'source'):
                self.pile.append((tag, cls, []))

        def handle_endtag(self, tag):
            if not self.pile or self.pile[-1][0] != tag:
                return
            t, cls, enfants = self.pile.pop()
            b = [e for e in enfants if e in BLOCS]
            i = [e for e in enfants if e in INLINES]
            if b and i:
                self.pb.append(f'<{t} class="{cls[:34]}"> mélange {sorted(set(i))} et {sorted(set(b))}')

    p = P()
    p.feed(html)
    return p.pb


def audit_structure(html: str):
    """Vérifie que chaque balise est fermée par la bonne.

    Un `<div>` fermé par `</span>` ne fait pas planter le navigateur : il laisse
    le div OUVERT, qui avale la suite du document et lui impose ses styles.
    C'est silencieux et ça ne se voit qu'au rendu.
    """
    from html.parser import HTMLParser
    VOID = {'br', 'img', 'hr', 'input', 'meta', 'link', 'source'}

    class P(HTMLParser):
        def __init__(self):
            super().__init__(convert_charrefs=True)
            self.pile, self.pb = [], []

        def handle_starttag(self, tag, attrs):
            if tag not in VOID:
                self.pile.append((tag, dict(attrs).get('class', '')[:30], self.getpos()[0]))

        def handle_endtag(self, tag):
            if tag in VOID:
                return
            if not self.pile:
                self.pb.append(f'</{tag}> orphelin ligne {self.getpos()[0]}')
                return
            if self.pile[-1][0] != tag:
                t, c, l = self.pile[-1]
                self.pb.append(f'</{tag}> ligne {self.getpos()[0]} ferme mal <{t} class="{c}"> ouvert ligne {l}')
                for k in range(len(self.pile) - 1, -1, -1):
                    if self.pile[k][0] == tag:
                        del self.pile[k:]
                        return
                return
            self.pile.pop()

    p = P()
    p.feed(html)
    p.pb += [f'<{t} class="{c}"> jamais fermé (ligne {l})' for t, c, l in p.pile]
    return p.pb
