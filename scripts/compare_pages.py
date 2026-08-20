#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Compare le rendu WordPress d'une page à celui d'une page de référence.

Les pages Décupler s'injectent dans le thème Astra, qui impose son titre, ses
largeurs et ses fonds. Une page peut être parfaite en local et cassée en ligne.
Cet outil mesure les deux dans le MÊME gabarit et signale les écarts.

    python3 scripts/compare_pages.py --ref machine-de-guerre-seo --id 20478
"""
import argparse, base64, json, os, re, subprocess, sys, glob, urllib.request

SCR = '/tmp/claude-0/-home-user-decupler/7f36cd75-dfbd-53bb-ba68-088661fcc950/scratchpad'


def wp_rendered(page_id):
    site = os.environ['WP_SITE_URL'].rstrip('/')
    tok = base64.b64encode(
        f"{os.environ['WP_USER']}:{os.environ['WP_APP_PASSWORD'].replace(' ','')}".encode()).decode()
    r = urllib.request.Request(f'{site}/wp-json/wp/v2/pages/{page_id}?context=edit&_fields=content',
                               headers={'Authorization': f'Basic {tok}', 'User-Agent': 'DecuplerClaude/1.0'})
    return json.load(urllib.request.urlopen(r, timeout=45))['content']['rendered']


def localise(html, urls):
    for n, u in enumerate(urls, 1):
        html = html.replace(u, f'css/{n}.css')
    return re.sub(r'<link[^>]+rel=["\']stylesheet["\'][^>]*href=["\']https?://(?!fonts\.googleapis)[^"\']+["\'][^>]*>',
                  '', html)


def injecte(shell, contenu):
    m = (re.search(r'(<div class="entry-content[^"]*"[^>]*>)(.*?)(</div>\s*</div>\s*</article>)', shell, re.S)
         or re.search(r'(<div class="entry-content[^"]*"[^>]*>)(.*)(</div>)', shell, re.S))
    return shell[:m.start(2)] + contenu + shell[m.end(2):]


MESURES = """()=>{
  const g=s=>document.querySelector(s);
  const box=e=>e?{x:Math.round(e.getBoundingClientRect().x),w:Math.round(e.getBoundingClientRect().width)}:null;
  const vis=e=>{if(!e)return 'absent';const c=getComputedStyle(e);
    return (c.display==='none'||c.visibility==='hidden'||e.getBoundingClientRect().height<2)?'masqué':'VISIBLE'};
  // largeur de la colonne de texte : le plus large paragraphe de contenu
  const ps=[...document.querySelectorAll('.entry-content p')].filter(p=>p.textContent.trim().length>60);
  const larg=ps.length?Math.max(...ps.map(p=>Math.round(p.getBoundingClientRect().width))):0;
  const xs=[...new Set(ps.map(p=>Math.round(p.getBoundingClientRect().x)))];
  return {
    titre_du_theme: vis(g('.entry-title')||g('.entry-header')||g('.page-header')),
    entry_content: box(g('.entry-content')),
    ast_container: box(g('.ast-container')),
    site_content: box(g('.site-content')),
    fond_body: getComputedStyle(document.body).backgroundColor,
    colonne_texte_max: larg,
    alignements_gauche: xs.length,
    debordement_horizontal: document.documentElement.scrollWidth>document.documentElement.clientWidth+2,
    hauteur_doc: document.documentElement.scrollHeight};}"""


def mesure(pw_page, fichier):
    pw_page.goto('file://' + fichier, wait_until='domcontentloaded', timeout=60000)
    pw_page.wait_for_timeout(3400)
    return pw_page.evaluate(MESURES)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ref', required=True, help='slug d’une page publiée qui sert de référence')
    ap.add_argument('--id', required=True, help='ID de la page à contrôler')
    ap.add_argument('--largeur', type=int, default=1280)
    a = ap.parse_args()

    urls = open(f'{SCR}/urls.txt').read().split('\n')
    shell = urllib.request.urlopen(
        urllib.request.Request(f'https://decupler.com/{a.ref}/',
                               headers={'User-Agent': 'Mozilla/5.0'}), timeout=45).read().decode('utf-8', 'replace')
    open(f'{SCR}/cmp_ref.html', 'w', encoding='utf-8').write(localise(shell, urls))
    open(f'{SCR}/cmp_new.html', 'w', encoding='utf-8').write(
        localise(injecte(shell, wp_rendered(a.id)), urls))

    from playwright.sync_api import sync_playwright
    exe = sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux/chrome'))[0]
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path=exe, args=['--no-sandbox'])
        pg = b.new_page(viewport={'width': a.largeur, 'height': 1000})
        pg.route('**/*', lambda r: r.continue_() if (r.request.url.startswith('file:')
                 or 'fonts.g' in r.request.url) else r.abort())
        ref = mesure(pg, f'{SCR}/cmp_ref.html')
        new = mesure(pg, f'{SCR}/cmp_new.html')
        b.close()

    print(f'{"critère":26} {"référence ("+a.ref[:16]+")":30} {"page "+str(a.id):22} écart')
    print('─' * 92)
    ecarts = 0
    for k in ref:
        r, n = ref[k], new[k]
        egal = (json.dumps(r, sort_keys=True) == json.dumps(n, sort_keys=True)) if isinstance(r, (dict, list)) \
            else (abs(r - n) <= max(2, abs(r) * .06) if isinstance(r, (int, float)) and not isinstance(r, bool) else r == n)
        if k == 'hauteur_doc':
            egal = True  # les pages n'ont pas la même longueur
        if not egal:
            ecarts += 1
        print(f'{k:26} {str(r)[:30]:30} {str(n)[:22]:22} {"" if egal else "◄ ÉCART"}')
    print('─' * 92)
    print(f'{ecarts} écart(s)')
    return 1 if ecarts else 0


if __name__ == '__main__':
    sys.exit(main())
