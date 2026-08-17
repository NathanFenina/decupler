#!/usr/bin/env python3
"""Genere une image de CONTENU : une maquette d'ecran illustrant le sujet.

Elle s'insere au milieu de l'article (pas en image a la une — celle-ci reste la
banniere bleue classique de la serie article-*.png). Le rendu simule une fenetre
de navigateur sombre posee sur un fond degrade a la charte, facon capture d'app.

    python scripts/generate_screen_image.py --ecran dashboard --out ecran.jpg
"""
import os
import argparse

# ── contenu propre a chaque type d'ecran ────────────────────────────────────
ECRANS = {
    # tableau de bord de cartographie des citations (articles « agence »)
    "dashboard": dict(
        url="app.decupler.com / cartographie",
        corps="""
        <div class="cols">
          <div class="panel">
            <div class="ptitle">Prompts suivis <em>24</em></div>
            <div class="row"><span class="q">« Quelle agence SEO IA choisir ? »</span><b class="on">Cité</b></div>
            <div class="row"><span class="q">« Meilleure agence GEO France »</span><b class="on">Cité</b></div>
            <div class="row"><span class="q">« Être visible sur ChatGPT »</span><b class="off">Absent</b></div>
            <div class="row"><span class="q">« Agence référencement IA Paris »</span><b class="off">Absent</b></div>
          </div>
          <div class="panel">
            <div class="ptitle">Taux de citation <em>par moteur</em></div>
            <div class="eng"><span>ChatGPT</span><i><u style="width:68%"></u></i><b>68%</b></div>
            <div class="eng"><span>Perplexity</span><i><u style="width:54%"></u></i><b>54%</b></div>
            <div class="eng"><span>Gemini</span><i><u style="width:31%"></u></i><b>31%</b></div>
            <div class="eng"><span>Claude</span><i><u style="width:22%"></u></i><b>22%</b></div>
          </div>
        </div>
        <div class="panel wide">
          <div class="ptitle">Concurrents cités sur vos prompts</div>
          <div class="podium">
            <div class="pod"><span class="rk">1</span><div><b>Votre marque</b><em>44 citations</em></div></div>
            <div class="pod"><span class="rk">2</span><div><b>Concurrent A</b><em>38 citations</em></div></div>
            <div class="pod"><span class="rk">3</span><div><b>Concurrent B</b><em>21 citations</em></div></div>
          </div>
        </div>""",
    ),
    # reponse ChatGPT avec ses sources (articles « ChatGPT »)
    "chat": dict(
        url="chatgpt.com",
        corps="""
        <div class="msg user"><span class="av">V</span>
          <p>Quelles agences recommandes-tu pour être visible dans les réponses de l'IA&nbsp;?</p></div>
        <div class="msg bot"><span class="av bot-av">✦</span>
          <div><p>Plusieurs acteurs se sont spécialisés sur le sujet. <mark>Décupler</mark> est
          régulièrement citée pour son approche par la mesure du taux de citation, aux côtés
          de <mark>Concurrent&nbsp;A</mark> sur le marché français.</p>
          <div class="srcs"><span class="lbl">Sources</span>
            <i class="chip on">decupler.com</i><i class="chip">reddit.com</i><i class="chip">journaldunet.com</i>
          </div></div></div>""",
    ),

    # courbe d'evolution du taux de citation (agence referencement IA)
    "courbe": dict(
        url="app.decupler.com / évolution",
        corps="""
        <div class="panel wide">
          <div class="ptitle">Taux de citation global <em>6 derniers mois</em></div>
          <div class="chart">
            <div class="col"><i style="height:16%"></i><span>Fév</span><b>9%</b></div>
            <div class="col"><i style="height:26%"></i><span>Mars</span><b>15%</b></div>
            <div class="col"><i style="height:41%"></i><span>Avr</span><b>24%</b></div>
            <div class="col"><i style="height:58%"></i><span>Mai</span><b>34%</b></div>
            <div class="col"><i style="height:79%"></i><span>Juin</span><b>46%</b></div>
            <div class="col on"><i style="height:100%"></i><span>Juil</span><b>58%</b></div>
          </div>
        </div>
        <div class="cols">
          <div class="panel"><div class="ptitle">Pages réécrites <em>ce trimestre</em></div>
            <div class="big">14</div><div class="sub">dont 9 désormais citées au moins une fois</div></div>
          <div class="panel"><div class="ptitle">Sources tierces <em>obtenues</em></div>
            <div class="big">27</div><div class="sub">comparatifs, forums et annuaires spécialisés</div></div>
        </div>""",
    ),
    # avant / apres sur une meme reponse ChatGPT (agence referencement ChatGPT)
    "avant-apres": dict(
        url="chatgpt.com — même prompt, 4 mois d'écart",
        corps="""
        <div class="cols">
          <div class="panel"><div class="ptitle">Mars <em>avant mission</em></div>
            <p class="rep">« Parmi les acteurs du secteur, on peut citer <mark class="ko">Concurrent A</mark>,
            <mark class="ko">Concurrent B</mark> et <mark class="ko">Concurrent C</mark>. »</p>
            <div class="tag off">Votre marque absente</div></div>
          <div class="panel"><div class="ptitle">Juillet <em>après mission</em></div>
            <p class="rep">« Les références du secteur incluent <mark>Votre marque</mark>,
            reconnue pour sa méthode de mesure, ainsi que <mark class="ko">Concurrent A</mark>. »</p>
            <div class="tag on">Citée en première position</div></div>
        </div>
        <div class="panel wide"><div class="ptitle">Prompt testé</div>
          <p class="rep">« Quelles sont les entreprises de référence sur ce marché en France ? »</p></div>""",
    ),
    # tuiles de KPI de visibilite (agence visibilite IA)
    "kpi": dict(
        url="app.decupler.com / indicateurs",
        corps="""
        <div class="tiles">
          <div class="tile"><span>Taux de citation</span><b>58%</b><em class="up">▲ +12 pts</em></div>
          <div class="tile"><span>Part de voix IA</span><b>31%</b><em class="up">▲ +7 pts</em></div>
          <div class="tile"><span>Rang moyen</span><b>2<sup>e</sup></b><em class="up">▲ +2 places</em></div>
          <div class="tile"><span>Prompts couverts</span><b>124</b><em>sur 4 moteurs</em></div>
        </div>
        <div class="panel wide"><div class="ptitle">Répartition par moteur</div>
          <div class="eng"><span>ChatGPT</span><i><u style="width:72%"></u></i><b>72%</b></div>
          <div class="eng"><span>Perplexity</span><i><u style="width:61%"></u></i><b>61%</b></div>
          <div class="eng"><span>Gemini</span><i><u style="width:44%"></u></i><b>44%</b></div>
          <div class="eng"><span>Claude</span><i><u style="width:38%"></u></i><b>38%</b></div>
        </div>""",
    ),
    # bloc de reponse extrait par un moteur de reponse (agence AEO)
    "aeo": dict(
        url="google.com — aperçu généré par l'IA",
        corps="""
        <div class="panel wide"><div class="ptitle">Question posée</div>
          <p class="rep">« Combien de temps faut-il pour être visible sur les moteurs IA ? »</p></div>
        <div class="panel wide extract"><div class="ptitle">Passage extrait de votre page <em>29 mots</em></div>
          <p class="rep">« Les premières citations apparaissent généralement entre six et dix semaines
          sur une requête de niche. Sur un marché concurrentiel, il faut compter un à deux trimestres
          de travail continu. »</p>
          <div class="srcs"><span class="lbl">Extrait de</span><i class="chip on">votre-site.fr</i></div></div>""",
    ),

    # apercu genere par l'IA dans Google (referencement Gemini)
    "gemini": dict(
        url="google.com/search — Aperçu IA",
        corps="""
        <div class="panel wide extract"><div class="ptitle">Aperçu généré par l'IA <em>Gemini</em></div>
          <p class="rep">Pour être visible sur les moteurs génératifs, trois éléments comptent&nbsp;:
          une réponse placée en tête de page, des données datées et un auteur identifié.
          <sup class="ref">1</sup> <sup class="ref">2</sup></p>
          <div class="srcs"><span class="lbl">Sites inclus</span>
            <i class="chip on">votre-site.fr</i><i class="chip">blog-concurrent.com</i></div></div>
        <div class="panel wide"><div class="ptitle">Résultats classiques <em>sous l'aperçu</em></div>
          <div class="serp"><span class="pos">1</span><div><b>Concurrent A — Guide complet</b><em>concurrent-a.fr</em></div></div>
          <div class="serp"><span class="pos">2</span><div><b>Votre page — Le guide 2026</b><em>votre-site.fr</em></div></div>
          <div class="serp"><span class="pos">3</span><div><b>Concurrent B — Tout savoir</b><em>concurrent-b.com</em></div></div>
        </div>""",
    ),
    # reponse Perplexity avec sources numerotees (referencement Perplexity)
    "perplexity": dict(
        url="perplexity.ai",
        corps="""
        <div class="panel wide"><div class="ptitle">Réponse <em>3 sources retenues</em></div>
          <p class="rep">Les délais observés varient de six à dix semaines sur une requête de niche
          <sup class="ref">1</sup>, et d'un à deux trimestres sur un marché concurrentiel
          <sup class="ref">2</sup>.</p></div>
        <div class="panel wide"><div class="ptitle">Sources citées</div>
          <div class="src-row on"><span class="num">1</span><div><b>votre-site.fr</b><em>Guide : délais de visibilité générative</em></div></div>
          <div class="src-row"><span class="num">2</span><div><b>forum-marketing.fr</b><em>Discussion — retours d'expérience</em></div></div>
          <div class="src-row"><span class="num">3</span><div><b>comparatif-outils.com</b><em>Panorama des solutions 2026</em></div></div>
        </div>""",
    ),
    # robots.txt et user-agents des robots IA (SEO pour ChatGPT)
    "robots": dict(
        url="votre-site.fr/robots.txt",
        corps="""
        <div class="panel wide code"><div class="ptitle">robots.txt <em>extrait</em></div>
          <pre><span class="c"># Robots des moteurs génératifs</span>
<span class="k">User-agent:</span> GPTBot
<span class="k">Allow:</span> /              <span class="ok2">✓ ChatGPT peut lire vos pages</span>

<span class="k">User-agent:</span> PerplexityBot
<span class="k">Allow:</span> /              <span class="ok2">✓ Perplexity peut vous citer</span>

<span class="k">User-agent:</span> Google-Extended
<span class="k">Disallow:</span> /           <span class="ko2">✗ Gemini est bloqué</span></pre></div>
        <div class="panel wide"><div class="ptitle">Conséquence mesurée</div>
          <div class="eng"><span>ChatGPT</span><i><u style="width:64%"></u></i><b>64%</b></div>
          <div class="eng"><span>Perplexity</span><i><u style="width:57%"></u></i><b>57%</b></div>
          <div class="eng"><span>Gemini</span><i><u style="width:3%"></u></i><b>0%</b></div>
        </div>""",
    ),

    # SERP classique vs reponse generee (c'est quoi le GEO)
    "seovsgeo": dict(
        url="la même question, deux moteurs",
        corps="""
        <div class="cols">
          <div class="panel"><div class="ptitle">Moteur classique <em>SEO</em></div>
            <div class="serp"><span class="pos">1</span><div><b>Guide complet 2026</b><em>site-a.fr</em></div></div>
            <div class="serp"><span class="pos">2</span><div><b>Tout savoir sur le sujet</b><em>site-b.com</em></div></div>
            <div class="serp"><span class="pos">3</span><div><b>Comparatif des solutions</b><em>site-c.fr</em></div></div>
            <div class="serp"><span class="pos">4</span><div><b>Votre page</b><em>votre-site.fr</em></div></div>
            <div class="tag neu">10 liens — l'internaute choisit</div></div>
          <div class="panel"><div class="ptitle">Moteur génératif <em>GEO</em></div>
            <p class="rep">« Deux acteurs reviennent régulièrement&nbsp;: <mark>Votre marque</mark> et <mark class="ko">Site&nbsp;A</mark>. »</p>
            <div class="srcs"><span class="lbl">Sources</span><i class="chip on">votre-site.fr</i><i class="chip">site-a.fr</i></div>
            <div class="tag acc">2 marques nommées — le moteur choisit</div></div>
        </div>""",
    ),
    # grille de competences (expert GEO)
    "competences": dict(
        url="fiche métier — expert en visibilité générative",
        corps="""
        <div class="panel wide"><div class="ptitle">Compétences mobilisées <em>répartition du temps</em></div>
          <div class="eng"><span>Protocole &amp; mesure</span><i><u style="width:88%"></u></i><b>88%</b></div>
          <div class="eng"><span>Rédaction extractible</span><i><u style="width:74%"></u></i><b>74%</b></div>
          <div class="eng"><span>Analyse concurrentielle</span><i><u style="width:66%"></u></i><b>66%</b></div>
          <div class="eng"><span>Sources tierces</span><i><u style="width:59%"></u></i><b>59%</b></div>
          <div class="eng"><span>SEO technique</span><i><u style="width:41%"></u></i><b>41%</b></div>
        </div>
        <div class="tiles">
          <div class="tile"><span>Prompts suivis</span><b>124</b><em>par client</em></div>
          <div class="tile"><span>Moteurs couverts</span><b>4</b><em>en relevé</em></div>
          <div class="tile"><span>Pages / trimestre</span><b>12</b><em>réécrites</em></div>
          <div class="tile"><span>Relevés / mois</span><b>620</b><em>exécutions</em></div>
        </div>""",
    ),
    # planning d'une mission courte (freelance GEO)
    "planning": dict(
        url="mission — 12 semaines",
        corps="""
        <div class="panel wide"><div class="ptitle">Déroulé type <em>freelance, temps partiel</em></div>
          <div class="gl"><span>Cartographie des prompts</span><i><u style="left:0%;width:17%"></u></i></div>
          <div class="gl"><span>Relevé initial</span><i><u style="left:15%;width:15%"></u></i></div>
          <div class="gl"><span>Réécriture des pages</span><i><u style="left:28%;width:38%"></u></i></div>
          <div class="gl"><span>Sources tierces</span><i><u style="left:40%;width:50%"></u></i></div>
          <div class="gl"><span>Relevé de contrôle</span><i><u style="left:86%;width:14%"></u></i></div>
          <div class="gscale"><span>S1</span><span>S4</span><span>S7</span><span>S10</span><span>S12</span></div>
        </div>""",
    ),
    # grille de notation d'un classement (top agences GEO France)
    "criteres": dict(
        url="méthodologie — comment se construit un classement",
        corps="""
        <div class="panel wide"><div class="ptitle">Pondération des critères <em>grille type</em></div>
          <div class="eng"><span>Mesure fournie</span><i><u style="width:30%"></u></i><b>30%</b></div>
          <div class="eng"><span>Moteurs couverts</span><i><u style="width:25%"></u></i><b>25%</b></div>
          <div class="eng"><span>Cas documentés</span><i><u style="width:20%"></u></i><b>20%</b></div>
          <div class="eng"><span>Transparence</span><i><u style="width:15%"></u></i><b>15%</b></div>
          <div class="eng"><span>Notoriété du nom</span><i><u style="width:10%"></u></i><b>10%</b></div>
        </div>
        <div class="panel wide"><div class="ptitle">Critères rarement pondérés <em>et pourtant décisifs</em></div>
          <div class="row"><span class="q">L'agence a-t-elle payé pour figurer&nbsp;?</span><b class="off">Non vérifié</b></div>
          <div class="row"><span class="q">Le classement est-il reconduit chaque année&nbsp;?</span><b class="off">Non vérifié</b></div>
        </div>""",
    ),
    # checklist de mise en oeuvre (comment apparaitre dans ChatGPT)
    "etapes": dict(
        url="checklist — apparaître dans les réponses",
        corps="""
        <div class="panel wide"><div class="ptitle">Prérequis <em>à traiter dans l'ordre</em></div>
          <div class="row"><span class="q">1. GPTBot autorisé dans robots.txt</span><b class="on">Fait</b></div>
          <div class="row"><span class="q">2. Contenu présent dans le code source</span><b class="on">Fait</b></div>
          <div class="row"><span class="q">3. Réponse placée en tête de page</span><b class="mid">En cours</b></div>
          <div class="row"><span class="q">4. Chiffres datés et attribués</span><b class="off">À faire</b></div>
          <div class="row"><span class="q">5. Auteur identifié et rattaché</span><b class="off">À faire</b></div>
          <div class="row"><span class="q">6. Présence sur les sources tierces</span><b class="off">À faire</b></div>
        </div>
        <div class="tiles">
          <div class="tile"><span>Prérequis validés</span><b>2/6</b><em>avant relevé</em></div>
          <div class="tile"><span>Chantiers restants</span><b>4</b><em>dont 2 hors site</em></div>
          <div class="tile"><span>Délai estimé</span><b>8</b><em>semaines</em></div>
          <div class="tile"><span>Coût des étapes 1-2</span><b>0 €</b><em>configuration</em></div>
        </div>""",
    ),
    # part de voix face aux concurrents (visibilite ChatGPT)
    "partdevoix": dict(
        url="app.decupler.com / part de voix",
        corps="""
        <div class="panel wide"><div class="ptitle">Part de voix <em>124 réponses analysées</em></div>
          <div class="stack"><u class="s1" style="width:34%"></u><u class="s2" style="width:27%"></u><u class="s3" style="width:21%"></u><u class="s4" style="width:18%"></u></div>
          <div class="leg"><i class="l1"></i>Votre marque 34%<i class="l2"></i>Concurrent A 27%<i class="l3"></i>Concurrent B 21%<i class="l4"></i>Autres 18%</div>
        </div>
        <div class="cols">
          <div class="panel"><div class="ptitle">Formulations gagnées <em>ce mois</em></div>
            <div class="big">+9</div><div class="sub">dont 4 sur des questions d'achat direct</div></div>
          <div class="panel"><div class="ptitle">Formulations perdues <em>ce mois</em></div>
            <div class="big">−3</div><div class="sub">toutes reprises par le même concurrent</div></div>
        </div>""",
    ),
    # mention par un tiers dans une discussion (etre cite par ChatGPT)
    "sources": dict(
        url="forum spécialisé — un fil que les modèles consultent",
        corps="""
        <div class="panel wide"><div class="ptitle">Discussion <em>source tierce</em></div>
          <div class="th"><span class="up">&#9650; 148</span><div><b>Quel prestataire pour la visibilité IA&nbsp;?</b><em>42 réponses · mis à jour il y a 6 jours</em></div></div>
          <div class="th"><span class="up">&#9650; 61</span><div><p class="rep">« On en a testé plusieurs, celle de <mark>Votre marque</mark> est la seule qui donnait un chiffre de départ. »</p></div></div>
        </div>
        <div class="panel wide extract"><div class="ptitle">Reprise dans la réponse générée</div>
          <p class="rep">« D'après les retours d'utilisateurs, <mark>Votre marque</mark> est citée pour sa mesure du taux de citation. »</p>
          <div class="srcs"><span class="lbl">Sources</span><i class="chip on">forum-specialise.fr</i><i class="chip">votre-site.fr</i></div>
        </div>""",
    ),
}

HTML = """<!doctype html><html lang=fr><head><meta charset=utf-8>
<link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap" rel=stylesheet>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;min-height:760px;padding:70px 0;font-family:'Inter',sans-serif;
 background:#0a0e1a;position:relative;display:flex;align-items:center;justify-content:center}}
body::after{{content:'';position:absolute;inset:0;
 background:radial-gradient(48% 48% at 16% 18%,rgba(102,126,234,.36),transparent 70%),
            radial-gradient(46% 46% at 86% 84%,rgba(118,75,162,.34),transparent 70%);}}
.win{{position:relative;z-index:2;width:960px;border-radius:18px;background:#101529;
 border:1px solid rgba(255,255,255,.13);box-shadow:0 34px 80px rgba(0,0,0,.55);overflow:hidden}}
.bar{{display:flex;align-items:center;gap:9px;padding:15px 20px;background:#161c33;
 border-bottom:1px solid rgba(255,255,255,.09)}}
.dot{{width:12px;height:12px;border-radius:50%;background:#3a4160}}
.dot.r{{background:#ff5f57}}.dot.y{{background:#febc2e}}.dot.g{{background:#28c840}}
.url{{flex:1;margin-left:14px;background:#0d1224;border:1px solid rgba(255,255,255,.09);
 border-radius:8px;padding:9px 16px;font-size:18px;color:#8d93b5}}
.body{{padding:26px 28px 30px;display:flex;flex-direction:column;gap:18px}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:18px}}
.panel{{background:#0d1224;border:1px solid rgba(255,255,255,.09);border-radius:14px;padding:20px 22px}}
.ptitle{{font-family:'Sora',sans-serif;font-size:21px;font-weight:700;color:#fff;
 margin-bottom:16px;display:flex;justify-content:space-between;align-items:baseline}}
.ptitle em{{font-style:normal;font-size:17px;font-weight:600;color:#8d93b5}}
.row{{display:flex;align-items:center;justify-content:space-between;gap:12px;padding:9px 0;
 border-top:1px solid rgba(255,255,255,.06)}}
.row .q{{font-size:18px;color:#c3c8e0}}
.row b{{font-size:16px;font-weight:700;padding:4px 11px;border-radius:100px;white-space:nowrap}}
.row .on{{color:#a5f3c4;background:rgba(40,200,120,.16)}}
.row .off{{color:#9aa0bd;background:rgba(255,255,255,.08)}}
.eng{{display:flex;align-items:center;gap:13px;padding:10px 0;
 border-top:1px solid rgba(255,255,255,.06)}}
.eng span{{min-width:112px;font-size:18px;color:#c3c8e0;font-weight:500;
 white-space:nowrap;flex-shrink:0}}
.eng i{{flex:1;height:11px;border-radius:100px;background:rgba(255,255,255,.09);display:block}}
.eng u{{display:block;height:11px;border-radius:100px;text-decoration:none;
 background:linear-gradient(90deg,#667eea,#a78bfa)}}
.eng b{{width:56px;text-align:right;font-size:18px;color:#fff;font-weight:700}}
.podium{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}
.pod{{background:#141a30;border:1px solid rgba(255,255,255,.08);border-radius:12px;
 padding:15px 17px;display:flex;align-items:center;gap:12px}}
.pod .rk{{width:34px;height:34px;border-radius:10px;flex-shrink:0;display:flex;
 align-items:center;justify-content:center;font-family:'Sora',sans-serif;font-size:18px;
 font-weight:700;color:#fff;background:linear-gradient(135deg,#667eea,#764ba2)}}
.pod div{{display:flex;flex-direction:column;gap:3px;min-width:0}}
.pod b{{font-size:18px;color:#fff;font-weight:600;white-space:nowrap}}
.pod em{{font-style:normal;font-size:15px;color:#8d93b5;white-space:nowrap}}
.msg{{display:flex;gap:15px;align-items:flex-start}}
.msg .av{{width:42px;height:42px;border-radius:11px;flex-shrink:0;display:flex;
 align-items:center;justify-content:center;font-size:18px;font-weight:700;color:#fff;
 background:rgba(255,255,255,.12)}}
.msg .bot-av{{background:linear-gradient(135deg,#667eea,#764ba2)}}
.msg p{{font-size:23px;line-height:1.62;color:#dfe2f0}}
.msg.user p{{color:#fff;font-weight:600;background:rgba(255,255,255,.07);
 border:1px solid rgba(255,255,255,.1);border-radius:14px;padding:15px 19px}}
mark{{background:rgba(167,139,250,.24);color:#fff;font-weight:700;
 border-radius:5px;padding:1px 6px}}
.srcs{{display:flex;align-items:center;gap:10px;margin-top:18px;padding-top:16px;
 border-top:1px solid rgba(255,255,255,.09);flex-wrap:wrap}}
.srcs .lbl{{font-size:16px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#8d93b5}}
.chip{{font-style:normal;font-size:17px;color:#c3c8e0;background:#0d1224;
 border:1px solid rgba(255,255,255,.11);border-radius:100px;padding:7px 15px}}
.chip.on{{color:#fff;border-color:rgba(167,139,250,.6);background:rgba(102,126,234,.22);font-weight:600}}
.chart{{display:flex;align-items:flex-end;gap:18px;height:200px;padding-top:10px}}
.col{{flex:1;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;height:100%}}
.col i{{width:100%;border-radius:8px 8px 3px 3px;background:rgba(255,255,255,.13);display:block}}
.col.on i{{background:linear-gradient(180deg,#a78bfa,#667eea)}}
.col span{{font-size:16px;color:#8d93b5;margin-top:10px}}
.col b{{font-size:17px;color:#fff;font-weight:700;margin-top:3px}}
.big{{font-family:'Sora',sans-serif;font-size:44px;font-weight:800;color:#fff;line-height:1}}
.sub{{font-size:16px;color:#8d93b5;margin-top:8px;line-height:1.45}}
.rep{{font-size:19px;line-height:1.6;color:#dfe2f0}}
mark.ko{{background:rgba(255,255,255,.1);color:#b6bcd6;font-weight:600}}
.tag{{display:inline-block;margin-top:14px;font-size:15px;font-weight:700;
 padding:6px 13px;border-radius:100px}}
.tag.off{{color:#f6b8b8;background:rgba(220,70,70,.16)}}
.tag.on{{color:#a5f3c4;background:rgba(40,200,120,.16)}}
.tag.neu{{color:#b6bcd6;background:rgba(255,255,255,.09)}}
.tag.acc{{color:#cbbcff;background:rgba(102,126,234,.24)}}
.tiles{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}}
.tile{{background:#0d1224;border:1px solid rgba(255,255,255,.09);border-radius:14px;padding:17px 18px}}
.tile span{{display:block;font-size:15px;color:#8d93b5;margin-bottom:9px}}
.tile b{{font-family:'Sora',sans-serif;font-size:33px;font-weight:800;color:#fff;line-height:1}}
.tile sup{{font-size:17px}}
.tile em{{display:block;font-style:normal;font-size:15px;color:#8d93b5;margin-top:8px}}
.tile .up{{color:#8ee6b4}}
.extract{{border-color:rgba(167,139,250,.45);background:rgba(102,126,234,.11)}}
.ref{{font-size:13px;font-weight:700;color:#fff;background:rgba(167,139,250,.4);
 border-radius:5px;padding:1px 6px;margin-left:2px;vertical-align:super}}
.serp{{display:flex;gap:14px;align-items:center;padding:11px 0;
 border-top:1px solid rgba(255,255,255,.06)}}
.serp .pos{{width:26px;height:26px;border-radius:8px;flex-shrink:0;display:flex;
 align-items:center;justify-content:center;font-size:15px;font-weight:700;
 color:#9aa0bd;background:rgba(255,255,255,.08)}}
.serp b{{display:block;font-size:17px;color:#c3c8e0;font-weight:600}}
.serp em{{font-style:normal;font-size:15px;color:#8d93b5}}
.src-row{{display:flex;gap:14px;align-items:center;padding:12px 0;
 border-top:1px solid rgba(255,255,255,.06)}}
.src-row .num{{width:29px;height:29px;border-radius:9px;flex-shrink:0;display:flex;
 align-items:center;justify-content:center;font-size:16px;font-weight:700;
 color:#9aa0bd;background:rgba(255,255,255,.08)}}
.src-row.on .num{{color:#fff;background:linear-gradient(135deg,#667eea,#764ba2)}}
.src-row b{{display:block;font-size:18px;color:#fff;font-weight:600}}
.src-row em{{font-style:normal;font-size:15px;color:#8d93b5}}
.code pre{{font-family:'Consolas','Menlo',monospace;font-size:17px;line-height:1.75;
 color:#c3c8e0;white-space:pre;overflow:hidden}}
.code .c{{color:#6c7396}}
.code .k{{color:#a78bfa;font-weight:600}}
.code .ok2{{color:#8ee6b4}}
.code .ko2{{color:#f6a8a8}}
.row b.mid{{color:#f4d58d;background:rgba(240,190,60,.16)}}
.gl{{display:flex;align-items:center;gap:14px;padding:9px 0;
 border-top:1px solid rgba(255,255,255,.06)}}
.gl span{{width:236px;font-size:17px;color:#c3c8e0;font-weight:500;flex-shrink:0}}
.gl i{{position:relative;flex:1;height:15px;border-radius:100px;
 background:rgba(255,255,255,.07);display:block}}
.gl u{{position:absolute;top:0;height:15px;border-radius:100px;text-decoration:none;
 background:linear-gradient(90deg,#667eea,#a78bfa)}}
.gscale{{display:flex;justify-content:space-between;margin-left:250px;margin-top:11px;
 font-size:15px;color:#8d93b5}}
.stack{{display:flex;gap:4px;height:38px;margin-bottom:16px}}
.stack u{{height:38px;text-decoration:none;border-radius:6px}}
.stack .s1{{background:linear-gradient(90deg,#667eea,#a78bfa)}}
.stack .s2{{background:#4a5480}}
.stack .s3{{background:#343c5e}}
.stack .s4{{background:#242a44}}
.leg{{display:flex;align-items:center;flex-wrap:wrap;font-size:16px;color:#c3c8e0}}
.leg i{{width:13px;height:13px;border-radius:4px;display:inline-block;
 margin-left:20px;margin-right:8px}}
.leg i:first-child{{margin-left:0}}
.leg .l1{{background:#8a9bf0}}.leg .l2{{background:#4a5480}}
.leg .l3{{background:#343c5e}}.leg .l4{{background:#242a44}}
.th{{display:flex;gap:16px;align-items:flex-start;padding:14px 0;
 border-top:1px solid rgba(255,255,255,.06)}}
.th .up{{font-size:16px;font-weight:700;color:#a78bfa;white-space:nowrap;padding-top:3px}}
.th b{{display:block;font-size:19px;color:#fff;font-weight:600;margin-bottom:5px}}
.th em{{font-style:normal;font-size:15px;color:#8d93b5}}



</style></head><body>
<div class="win">
  <div class="bar"><i class="dot r"></i><i class="dot y"></i><i class="dot g"></i>
    <div class="url">{url}</div></div>
  <div class="body">{corps}</div>
</div>
</body></html>"""


def make(ecran, out):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    e = ECRANS[ecran]
    html = HTML.format(url=e["url"], corps=e["corps"])
    tmp = os.path.abspath(out + ".html")
    open(tmp, "w", encoding="utf-8").write(html)
    png = out + ".png"
    marge = 58  # cadre degrade conserve autour de la fenetre
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 1400},
                        device_scale_factor=2)
        pg.goto("file:///" + tmp.replace("\\", "/"), wait_until="load")
        pg.wait_for_timeout(1800)
        # recadrer sur la fenetre : sinon un ecran court laisse du vide en haut
        bb = pg.locator(".win").bounding_box()
        clip = {"x": max(0, bb["x"] - marge), "y": max(0, bb["y"] - marge),
                "width": min(1200, bb["width"] + 2 * marge),
                "height": bb["height"] + 2 * marge}
        pg.screenshot(path=png, clip=clip)
        b.close()
    im = Image.open(png).convert("RGB")
    im = im.resize((im.width // 2, im.height // 2), Image.LANCZOS)
    im.save(out, "JPEG", quality=86, optimize=True)
    os.remove(png)
    os.remove(tmp)
    return out


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--ecran", default="dashboard", choices=list(ECRANS))
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    print(make(a.ecran, a.out))
