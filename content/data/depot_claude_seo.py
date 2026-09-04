# -*- coding: utf-8 -*-
"""Inventaire du dépôt claude-seo, extrait de sa documentation.

Régénéré depuis docs/SKILLS.md, agents/ et commands/ du dépôt plutôt que
recopié : une page qui annonce 40 skills alors que le dépôt en a 43 est
une page qui ment, et personne ne s'en aperçoit avant un lecteur attentif.
"""

# Données extraites du dépôt NathanFenina/claude-seo (v2.0.0), pas saisies
# à la main : la page et le dépôt doivent dire la même chose.

BLOCS = [
    ('Diagnostic et technique', [
        ('seo-onboarding', 'Accueille, diagnostique, configure, lance la première action'),
        ('seo-audit-360', 'Audit complet, 8 agents en parallèle, score /100, plan priorisé'),
        ('seo-technique-autofix', 'Détecte et corrige : robots, canonicals, redirections, balises'),
        ('seo-crawl-architecture', 'Crawl, arborescence, orphelines, profondeur, autorité interne'),
        ('seo-core-web-vitals', 'LCP, INP, CLS mesurés, causes, correctifs front'),
        ('seo-indexation', 'Pourquoi Google ignore vos pages, sitemaps, budget de crawl'),
        ('seo-migration', 'Refonte sans perte : inventaire, redirections, surveillance J+90'),
        ('seo-veille', 'Surveillance continue, alertes diagnostiquées'),
    ]),
    ('Recherche et stratégie', [
        ('seo-quick-wins', 'Les pages en position 4-20 à rattraper, chiffrées, avec les corrections écrites'),
        ('seo-keyword-research', 'Volumes, intention, risque zero-click IA, arbitrage'),
        ('seo-competitor-gap', '4 types de gaps, benchmark GEO, plan 90 jours'),
        ('seo-cocon-semantique', 'Silos, piliers, satellites, plan de maillage, calendrier'),
        ('seo-serp-analysis', 'Intention réelle, features, format attendu, difficulté vraie'),
        ('seo-traffic-drop', 'Dater, isoler, expliquer, récupérer'),
    ]),
    ('Contenu', [
        ('seo-brief', 'Brief complet, réponse directe et FAQ déjà rédigées'),
        ('seo-redaction', 'Rédaction SEO + GEO, style humain, sources vérifiées'),
        ('seo-optimisation-onpage', 'Note /100 par critère puis réécrit'),
        ('seo-meta-serp', '3 titles, 2 metas, aperçu SERP, comptage pixel'),
        ('seo-faq-paa', 'FAQ ciblant PAA, snippets et LLM, + schema'),
        ('seo-eeat', 'Score /40, verdict, correctifs localisés'),
        ('seo-comparatifs', 'Pages « X vs Y » et « alternative à », cadre juridique inclus'),
    ]),
    ('Structure et échelle', [
        ('seo-page-builder-html', 'Pages HTML autonomes, prêtes à coller'),
        ('seo-programmatique', "Pages à l'échelle, garde-fous anti-contenu mince"),
        ('seo-maillage-interne', "Orphelines, flux d'autorité, plan de liens exécutable"),
        ('seo-schema-jsonld', 'Détection, validation, génération, dépréciations'),
        ('seo-hreflang-i18n', 'Validation et génération hreflang, architecture i18n'),
        ('seo-images', 'Poids, formats, alt, lazy loading, impact LCP et CLS'),
    ]),
    ('GEO — moteurs IA', [
        ('geo-visibilite-ia', 'Score GEO /100, analyse par moteur, roadmap 90 jours'),
        ('geo-citation-tracker', "Pourquoi cette page n'est pas citée, réponse directe réécrite"),
        ('geo-llms-txt', 'llms.txt, crawlers IA, entité, Wikidata, cohérence de marque'),
        ('geo-share-of-model', 'Part de voix mesurée, suivi mensuel, benchmark'),
    ]),
    ('Autorité et acquisition', [
        ('seo-netlinking', 'Profil, prospection, qualification /20, emails rédigés'),
        ('seo-reddit-communautes', 'Threads à valeur LLM, réponses rédigées, vocabulaire audience'),
        ('seo-local', 'Google Business Profile, NAP, avis, pages zones sans doorway'),
        ('seo-digital-pr', 'Études, baromètres, outils : ce qui se cite tout seul'),
    ]),
    ('Production et pilotage', [
        ('seo-publication-cms', 'WordPress, Webflow, générique. Sauvegarde et vérification'),
        ('seo-pilotage-notion', '5 bases : leads, objectifs, roadmap, contenus, backlinks'),
        ('seo-reporting', 'Rapport avec les causes, pas seulement les courbes'),
        ('seo-dashboard', 'Tableau de bord HTML autonome, partageable'),
        ('seo-ecommerce', 'Facettes, catégories, fiches, produits morts, pagination'),
    ]),
]

AGENTS = [
    ('seo-analyste-concurrence', 'Analyste concurrentiel SEO et GEO'),
    ('seo-contenu', 'Spécialiste qualité de contenu'),
    ('seo-crawler', 'Spécialiste crawl et architecture'),
    ('seo-data', 'Analyste données SEO'),
    ('seo-frontend', 'Développeur front spécialisé SEO'),
    ('seo-geo', 'Spécialiste visibilité dans les moteurs IA'),
    ('seo-netlinking', 'Spécialiste acquisition de liens'),
    ('seo-performance', 'Spécialiste performance web et Core Web Vitals'),
    ('seo-publisher', 'Spécialiste publication CMS'),
    ('seo-redacteur', 'Rédacteur SEO et GEO'),
    ('seo-schema', 'Spécialiste données structurées'),
    ('seo-serp', "Analyste de SERP. Relève ce que Google montre sur une requête, en déduit l'intention réelle, le format attendu, les features à viser et la difficulté véritable"),
    ('seo-strategiste', "Stratège SEO. Arbitre entre les opportunités, construit la roadmap priorisée par impact business, et décide ce qu'on ne fait pas"),
    ('seo-technique', 'Spécialiste SEO technique'),
]

COMMANDES = [
    ('seo-article', "Rédige un article ou une page à partir d'un brief"),
    ('seo-audit', "Audit SEO complet d'un site — technique, contenu, E-E-A-T, schema, performance, maillage, GEO"),
    ('seo-backlink', 'Campagne de netlinking — audit du profil, prospection qualifiée, emails rédigés'),
    ('seo-brief', "Produit un brief rédactionnel complet à partir d'un mot-clé"),
    ('seo-doctor', "Diagnostic d'installation — quels outils sont branchés, quoi connecter ensuite et pourquoi"),
    ('seo-fix', 'Détecte et corrige automatiquement les problèmes techniques SEO'),
    ('seo-geo', 'Audit de visibilité dans les moteurs IA — score GEO, analyse par moteur, roadmap 90 jours'),
    ('seo-notion', 'Crée et alimente les bases de pilotage Notion — leads, objectifs, roadmap, contenus, backlinks'),
    ('seo-onpage', 'Note un contenu sur 100 face à un mot-clé cible, puis le réécrit optimisé'),
    ('seo-page', 'Génère une page HTML autonome, esthétique et responsive, prête à coller'),
    ('seo-publish', 'Publie ou met à jour du contenu sur WordPress, Webflow ou un CMS générique'),
    ('seo-quickwins', 'Identifie les pages en position 4-20 à rattraper et produit les corrections exactes'),
    ('seo-rapport', 'Rapport SEO périodique — évolutions, causes, actions menées, priorités du mois'),
    ('seo-veille', 'Surveillance du site — positions, indexation, erreurs, liens perdus, avec alertes diagnostiquées'),
    ('seo', 'Routeur principal Claude Code SEO Décupler — dirige vers le bon skill selon ce que vous demandez'),
]
