# -*- coding: utf-8 -*-
"""Meta descriptions des pages deja publiees.

Yoast est regle sur `%%excerpt%%` pour le type « Pages » : la meta description
servie dans le <head> est donc l'extrait WordPress, qui lui est ecrivable via
l'API REST (contrairement au champ Yoast, absent du schema REST).

Cible : 120-156 caracteres. Applique par scripts/wp_meta_desc.py.
"""

# Pages volontairement laissees sans meta description :
#   9308 panier, 9310 mon-compte, 9309 commander, 6136 confirmation-de-rdv,
#   5332 decupler-2 (ancienne HP), 19852 homepage (doublon), 9307 boutique
#   (archive WooCommerce sans contenu propre). Ces pages n'ont pas vocation a
#   etre indexees.

METAS = {
    # --- Agence / offre ---
    6090: "Agence SEO et GEO en France : stratégie sur-mesure, SEO technique, contenu, netlinking et visibilité dans les IA. Résultats mesurables dès 3 mois.",
    5915: "Accompagnement SEO complet : technique, contenu, netlinking et pilotage pris en charge par nos experts. Premiers résultats dès 3 mois, consultation offerte.",
    20098: "Agence SEO à Nice : référencement naturel local, fiche Google et visibilité IA pour capter les recherches des Azuréens. Audit gratuit, résultats en 90 jours.",
    7257: "Agence SEO e-commerce spécialiste PrestaShop, WooCommerce et Shopify : des agents IA pour optimiser des milliers de fiches produits. Audit e-commerce gratuit.",
    7295: "Agence SEO SaaS : requêtes à haute intention d'achat, SEO technique JS et agents IA pour transformer votre blog en machine à démos. Audit SaaS gratuit.",
    5233: "SEO local : optimisation de votre site, de votre fiche GMB et de vos pages villes pour dominer Google Maps et les moteurs IA. 30+ entreprises accompagnées.",
    6421: "Optimisation de fiche GMB : la méthode pour passer d'une visibilité locale nulle au haut de Google Maps, sans budget publicitaire. Audit GMB offert.",
    8976: "100 citations locales NAP créées à la main sur les meilleurs annuaires français pour renforcer votre pack local et Google Maps. 200 € HT, paiement unique.",
    20177: "Visibilité en ligne : la méthode Search Everywhere de Décupler pour être présent sur Google, ChatGPT, LinkedIn et Reddit en 60 jours. Audit gratuit.",
    20070: "Visibilité LLM : soyez cité par ChatGPT, Perplexity et Gemini quand vos clients les interrogent. Premiers résultats en 6 à 8 semaines. Audit gratuit.",

    # --- Cluster GEO (reecritures : hors format) ---
    7214: "Agence GEO : rendez votre marque visible et citée par ChatGPT, Perplexity, Claude et Google AI. Audit GEO gratuit, plus de 70 entreprises accompagnées.",
    19947: "Consultant GEO : la mécanique des citations dans l'IA, la méthode pour y entrer et les chiffres qui comptent pour votre marque sur ChatGPT et Perplexity.",
    19942: "Meilleure agence GEO : 7 critères pour bien choisir, la mécanique des citations IA, les fourchettes de prix et les questions à poser avant de signer.",
    19948: "Agence SEO ChatGPT : la mécanique des citations dans l'IA et la méthode Décupler pour faire apparaître votre marque dans ses réponses. Audit gratuit.",
    20006: "Quand un décideur demande à l'IA qui est le meilleur, elle doit répondre : vous. On identifie où vous perdez ces clients sur Google et dans l'IA.",
    19793: "Le playbook GEO en 8 sections actionnables pour être cité par ChatGPT, Perplexity et Google AI. Le système qui a placé un client dans le top 1 % en 90 jours.",
    19958: "Monter sa machine de guerre SEO/GEO dans Claude Code : rulebook, skills, agents, automatisations et connecteurs MCP (GSC, DataForSEO, WordPress, Notion).",
    20451: "Brancher Google Search Console sur Claude : connecteur sans code ou service account, et les skills qui transforment ces données en décisions et en contenu.",

    # --- Pages villes GEO ---
    19949: "Agence GEO à Paris : faites citer votre entreprise par ChatGPT, Claude et Perplexity quand vos prospects franciliens leur demandent un prestataire.",
    20255: "Agence GEO à Bordeaux : faites citer votre entreprise girondine par ChatGPT et Claude quand vos acheteurs leur demandent un prestataire. Audit gratuit.",
    20257: "Agence GEO à Lille : apparaissez dans les réponses de ChatGPT et Claude quand un acheteur du Nord cherche un fournisseur. Diagnostic gratuit en une minute.",
    20256: "Agence GEO à Lyon : les directions achats interrogent l'IA avant de consulter. On travaille votre présence dans ChatGPT et Claude. Audit GEO gratuit.",
    20259: "Agence GEO à Marseille : soyez la marque que ChatGPT et Claude recommandent aux acheteurs des Bouches-du-Rhône, en français comme à l'international.",
    20258: "Agence GEO à Nantes : très peu d'entreprises ligériennes sortent dans les réponses des IA. On y installe la vôtre. Diagnostic GEO gratuit en une minute.",
    20012: "Agence GEO à Nice : rendez votre entreprise azuréenne visible dans ChatGPT, Claude et Perplexity, de Sophia Antipolis au reste du 06. Audit gratuit.",
    20254: "Agence GEO à Toulouse : quand un décideur haut-garonnais interroge ChatGPT, il ne retient que deux ou trois noms. On y met le vôtre. Audit GEO gratuit.",

    # --- Outils et diagnostics ---
    20218: "Audit GEO gratuit : on interroge ChatGPT, Claude, Gemini et Perplexity avec 5 prompts tirés de votre site pour voir si votre marque sort — ou un concurrent.",
    20219: "Cartographie IA : vos mots-clés, vos positions Search Console, les volumes, l'écart concurrentiel et vos citations dans les IA réunis sur une seule carte.",
    20220: "EEAT Google : les 4 piliers — expérience, expertise, autorité, fiabilité — que les Quality Raters et les IA appliquent à vos pages. Analysez la vôtre.",
    20080: "Mesurer sa visibilité sur les IA : ce qu'est le Share of Model, comment le calculer sur 4 moteurs et comment le faire progresser en 6 à 8 semaines.",
    8931: "L'app Décupler automatise 80 % de votre SEO avec des agents IA : audit E-E-A-T, briefs, rédaction, maillage interne. 7 jours gratuits à l'inscription.",
    6808: "SEO AI Systems : les agents IA qui automatisent 80 % de votre SEO et vous font citer par ChatGPT, Perplexity et Gemini. Démo live, 7 jours gratuits.",
    20075: "Générer un article SEO avec l'IA sans sacrifier la qualité : le Contenu Studio de l'app Décupler produit du contenu calibré pour Google et les IA.",
    20088: "Automatisation SEO en 5 étapes : audit, stratégie sémantique, production de contenu, technique et citations IA. Avec l'agence, ou seul avec notre app.",

    # --- Guides et ressources ---
    8639: "Générer un audit GEO complet avec Claude Code en 10 minutes : la méthode Décupler pour mesurer sa visibilité dans ChatGPT, Perplexity et AI Overviews.",
    8623: "Claude Code SEO OS : le système complet — skills, fichiers mémoire, 5 slash commands et MCP Search Console/DataForSEO — pour piloter son SEO au terminal.",
    7805: "12 Skills SEO pour Claude Code, open source sous licence MIT : audit technique, schema JSON-LD, optimisation GEO. 5 heures d'audit ramenées à 3 minutes.",
    7679: "10 Skills Claude prêts à l'emploi pour dominer Google et les moteurs IA. Installation en moins de 5 minutes, zéro prompt engineering. Guide gratuit.",
    7854: "12 agents IA sous forme de Skills Claude pour automatiser votre SEO et votre visibilité dans les moteurs IA. Installation en 5 minutes, 100 % gratuit.",
    5738: "Connecter DataForSEO et Google Search Console à Claude en 7 étapes : recherche de mots-clés, analyse SERP et audits GSC en langage naturel, sans export CSV.",
    8466: "WP MCP Ultimate : le plugin open source qui pilote WordPress depuis Claude Code — 58 capacités, rédaction, publication, images, maillage interne, en 5 minutes.",
    6446: "Automatiser son maillage interne WordPress en 5 minutes : la méthode complète, les scripts Python et l'automatisation Make pour gagner 20 h par mois.",
    8027: "La matrice de Gap GEO : 8 sections et un Google Sheet prêt à l'emploi pour repérer où vos concurrents vous battent sur ChatGPT, Perplexity et Claude.",
    8032: "Workflow de recherche de prompts GEO : 9 étapes et un Google Sheet pour bâtir 40 à 60 prompts cibles et repérer vos gaps face aux concurrents sur les LLMs.",
    5709: "Le guide complet du GEO : framework, 15 outils, 7 méthodes et 50 actions pour dominer ChatGPT, Perplexity et les autres moteurs de recherche IA.",
    7820: "Reddit pour les LLMs : la méthode en 6 étapes pour faire citer sa marque par ChatGPT, Perplexity et Claude, qui s'entraînent sur ses conversations.",
    20059: "Reddit est la 3e source citée par ChatGPT. Sans présence dans les bonnes conversations, votre marque n'existe pas pour les IA. Décupler la construit pas-à-pas.",
    7722: "OpenClaw pour le SEO : un agent IA autonome qui surveille vos positions, analyse vos concurrents et vous envoie un rapport chaque matin. Open source, gratuit.",
    6263: "Créer un site premium en 24 h avec l'IA (Gemini et Claude) : la méthode Vibe Coding, du brief stratégique au site qui convertit, sans coder ni designer.",
    7668: "Comment créer une app IA qui optimise plus de 100 fiches produits en 5 minutes : le case study complet, du problème client au workflow reproductible.",
    6440: "Transformer une vidéo en texte gratuitement : collez l'URL YouTube et récupérez en 5 minutes un article SEO structuré avec H2, FAQ et méta description.",

    # --- Etudes de cas ---
    19963: "9 études de cas SEO, GEO et SEA : e-commerce, média, assurance, SaaS, énergie, BTP, urgence — méthodologie, leviers activés et résultats chiffrés.",
    19962: "Étude de cas SEA serrurerie d'urgence : 9 720 appels générés et 7 184 décrochés en 3 mois, 453 000 impressions et 24 200 clics avec une approche call-first.",
    19968: "Étude de cas Google Ads Allianz : ROI multiplié par 3, +135 % de trafic qualifié et −42 % de coût par lead en 4 mois, à budget constant.",
    19969: "Étude de cas SEO Atoo Énergie : +15 % de clics organiques en 3 mois pour un installateur de panneaux solaires, via audit technique et enrichissement sémantique.",
    19964: "Étude de cas SEO Decathlon Travel : +140 % de trafic organique en 6 mois, 300 mots-clés en top 10 Google et temps de chargement divisé par deux.",
    19966: "Étude de cas SEO Double Trade : +105 % de trafic organique en 3 mois pour une plateforme de trading, via quick wins techniques et contenu IA supervisé.",
    19967: "Étude de cas SEO Le Point : trafic d'un article multiplié par 3,2 en 21 jours, position n°1 Google et 3 featured snippets, sans nouveau contenu.",
    19970: "Étude de cas SEO Reux Travaux : +450 % de clics sur une page de service en 3 mois pour une entreprise de rénovation, via SEO local et maillage interne.",
    19971: "Étude de cas SEO Speed Inter : +46 % de clics organiques en 3 mois pour un service de dépannage d'urgence, après correction de 80 erreurs techniques.",
    19965: "Étude de cas SEO Spigao : trafic organique d'un SaaS B2B triplé en 6 mois et 420 mots-clés en top 10, face à Asana, Monday et Notion.",

    # --- Formations, evenements, divers ---
    7626: "Bootcamp GEO Accelerator : 1 mois en cohorte, 16 h de live avec Nathan Fenina, 12 places maximum. Éligible Qualiopi et financement OPCO, sur dossier.",
    7841: "Masterclass GEO en LinkedIn Live : analyse concurrentielle sur les LLMs en direct, signaux qui déclenchent une citation et roadmap GEO concrète en 1 heure.",
    8039: "Masterclass GEO en LinkedIn Live : pourquoi vos concurrents sortent dans les LLMs avant vous, et comment passer de zéro citation au top 3 en 90 jours.",
    8224: "AI Search for E-commerce, Nathan Fenina at E-Commerce Warsaw Expo 2026: how to get your products cited, recommended and bought through ChatGPT and Perplexity.",
    9189: "La newsletter SEO, GEO et IA de Nathan Fenina : chaque semaine, les tactiques testées en vrai, envoyées à plus de 2 000 abonnés. Gratuit, sans spam.",
    2769: "Le blog SEO, GEO et IA de Décupler : Claude Skills, MCP, prompts ChatGPT, SEO technique et local — les stratégies testées sur plus de 70 clients.",
    4355: "Politique de conditionnalité Décupler : conditions de vente, modalités de remboursement et garanties applicables aux prestations SEO, web, IA et formation.",
}
