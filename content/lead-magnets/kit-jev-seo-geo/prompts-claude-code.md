# Les prompts du playbook Jev SEO, à coller dans Claude Code

Un prompt par étape. Remplacez ce qui est entre crochets.

## 1. Installer

    Installe pour tous mes projets le skill jev-seo depuis
    https://github.com/AgriciDaniel/jev-seo (environnement virtuel Python,
    dépendances, lien dans ~/.claude/skills/jev-seo), puis le skill officiel
    TypeSafe. Lance `bin/jevseo doctor` et dis-moi quelles clés manquent.
    Ne me demande jamais de coller une clé dans la conversation : dis-moi
    dans quel fichier la mettre.

## 2. Lancer l'audit

    /jev-seo https://[monsite.fr]

## 3. Lire le rapport

    Lis digest.md de l'audit. Donne-moi en 10 lignes : le score, les 3
    actions qui comptent le plus et pourquoi, et les réponses de Jev
    marquées « à vérifier ». Pas de jargon.

## 4. Corriger dans l'ordre

    Prends les actions P1 puis les quick wins (effort « heures »).
    Pour chacune : vérifie d'abord l'alerte sur le site réel (curl), montre-
    moi la preuve, propose la correction, et attends mon feu vert avant de
    modifier quoi que ce soit. Sauvegarde chaque page avant de la modifier.

## 5. Rendre les pages citables

    Dans le rapport, prends les 5 pages les plus importantes marquées
    « ne va pas droit au but » ou avec une citabilité faible. Pour chacune,
    réécris les deux premières phrases pour répondre directement à la
    question visée. N'ajoute aucun chiffre qui n'est pas déjà dans la page :
    marque [à compléter] là où il faut une preuve. Montre avant / après.

## 6. Mesurer les citations dans les IA

    Voici mes 30 prompts clients : [liste]. Pour chacun, récupère les
    réponses de ChatGPT, Claude et Perplexity, puis envoie chaque réponse à
    Jev avec requete-reponse-ia.json. Calcule le bloc 1 et le bloc 3 selon
    calcul-tableau-de-bord.md et sors un tableau.

## 7. Remesurer

    Relance l'audit jev-seo sur [monsite.fr] et le même lot de prompts.
    Compare avec le mois dernier : score, actions, taux de citation par
    moteur, couverture par intention. Qu'est-ce qui a bougé, et pourquoi ?
