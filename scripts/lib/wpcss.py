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


def harden(html: str) -> str:
    """Minifie chaque bloc <style> d'un document HTML destiné à WordPress."""
    def one(m):
        return '<style>' + minify_css(m.group(1)) + '</style>'
    return re.sub(r'<style>(.*?)</style>', one, html, flags=re.S)


def audit(html: str):
    """Contrôle qu'aucun bloc <style> ne peut plus déclencher wpautop."""
    problemes = []
    for i, bloc in enumerate(re.findall(r'<style>(.*?)</style>', html, flags=re.S)):
        if '\n\n' in bloc:
            problemes.append(f'bloc {i}: ligne vide (wpautop y insérera </p><p>)')
        if '\n' in bloc:
            problemes.append(f'bloc {i}: saut de ligne résiduel ({bloc.count(chr(10))})')
        if re.search(r'/\*', bloc):
            problemes.append(f'bloc {i}: commentaire non retiré')
    return problemes
