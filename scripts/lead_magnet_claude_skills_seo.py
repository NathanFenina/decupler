"""Assemble content/articles/claude-skills-seo.body.html (page /claude-skills-seo/)
depuis le gabarit .body.tpl.html, les SKILL.md du pack
(content/lead-magnets/skills-seo-claude/) et la FAQ.

    python3 scripts/lead_magnet_claude_skills_seo.py   puis build_article.py (voir le skill lead-magnet)
"""
import html, json
from pathlib import Path

R = Path(__file__).resolve().parents[1]
PACK = R / 'content/lead-magnets/skills-seo-claude'

SKILLS = [
    ('seo-site-auditor', 'Audit SEO', "Audit technique et on-page d'une page ou d'un site : un tableau priorisé et les 3 quick wins.", "Audite cette page et donne-moi les 3 quick wins."),
    ('aeo-content-optimizer', 'Optimisation pour les IA', "Réécrit un contenu pour qu'il soit repris par les AI Overviews, ChatGPT et Perplexity, sans perdre Google.", "Réécris cet article pour qu'il soit cité sur « prix d'une toiture »."),
    ('schema-markup-generator', 'Données structurées', "JSON-LD valide (Article, FAQ, LocalBusiness…), une entité = un @id, et rien d'inventé.", "Génère le JSON-LD de cette page service."),
    ('eeat-content-scorer', 'Contrôle E-E-A-T', "Note un contenu avant publication sur l'expérience, l'expertise, l'autorité et la fiabilité.", "Note cet article avant que je le publie."),
    ('keyword-intent-classifier', 'Intention de recherche', "Classe des requêtes par intention, étape d'achat et risque de zéro clic, et dit quel format de page.", "Classe ces 40 requêtes Search Console par intention."),
    ('competitor-gap-finder', 'Écart concurrentiel', "Trouve ce que les pages mieux classées traitent et pas la tienne : sous-sujets, questions, preuves.", "Pourquoi ces deux pages sont devant la mienne ?"),
    ('gbp-post-generator', 'Posts Google Business', "Trois posts pour la fiche Google : actualité, offre, saison. La ville citée, pas de hashtag.", "Trois posts pour la fiche d'un plombier à Antibes."),
    ('internal-linking-strategist', 'Maillage interne', "Cocons pilier et satellites, liens à ajouter avec l'ancre et la phrase, pages orphelines.", "Voici mon sitemap : propose le maillage."),
    ('seo-content-brief', 'Brief de contenu', "Intention, plan H2/H3, questions, entités, maillage, title et meta : prêt pour un rédacteur.", "Fais le brief pour « création site internet dentiste »."),
    ('ai-search-visibility', 'Visibilité IA', "Note sur 10 les chances d'être cité par les moteurs IA, avec les 3 corrections prioritaires.", "Cette page a-t-elle une chance d'être citée par Perplexity ?"),
]

e = html.escape
lignes, cartes = [], []
for i, (slug, titre, quoi, dire) in enumerate(SKILLS, 1):
    code = (PACK / slug / 'SKILL.md').read_text(encoding='utf-8').rstrip()
    # pas de ligne vide dans <pre> (wpautop) : on garde une espace
    code = '\n'.join(l if l.strip() else ' ' for l in code.split('\n'))
    lignes.append(f'        <tr><td>{e(titre)}</td><td>{e(quoi)}</td><td>« {e(dire)} »</td></tr>')
    cartes.append(
        f'      <div class="skc"><div class="skc-h"><span class="skc-n">{i}</span><h3>{e(titre)}<small>{slug}</small></h3></div>'
        f'<p>{e(quoi)}</p><p class="say"><b>Dis à Claude :</b> « {e(dire)} »</p>'
        f'<details class="cmd"><summary>Voir le SKILL.md</summary><div class="codeblock"><div class="codeblock-h"><i class="r"></i><i class="y"></i><i class="g"></i><span>{slug}/SKILL.md</span></div><pre>{e(code, quote=False)}</pre></div></details></div>')

faq = json.loads((R / 'content/articles/claude-skills-seo.faq.json').read_text(encoding='utf-8'))
faq_html = '\n'.join(f'      <details><summary>{e(q["question"])}</summary><p>{e(q["answer"])}</p></details>' for q in faq)

tpl = (R / 'content/articles/claude-skills-seo.body.tpl.html').read_text(encoding='utf-8')
out = tpl.replace('__TABLEAU__', '\n'.join(lignes)).replace('__CARTES__', '\n'.join(cartes)).replace('__FAQ__', faq_html)
assert '__' not in out.replace('__IMG', '')
(R / 'content/articles/claude-skills-seo.body.html').write_text(out, encoding='utf-8')
print('ok', len(out))
