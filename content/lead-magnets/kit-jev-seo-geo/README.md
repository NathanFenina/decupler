# Kit Jev SEO & GEO — Décupler

Le kit du playbook https://decupler.com/jev-seo/ (30/09/2026).

| Fichier | Pour quoi faire |
|---|---|
| `prompts-claude-code.md` | Les 7 prompts du playbook, à coller dans Claude Code |
| `ordre-des-corrections.md` | Dans quel ordre corriger, de la page invisible à la page citée |
| `questions-jev-geo.json` | Toutes les questions Jev des 4 blocs du tableau de bord, commentées |
| `requete-page.json` | Requête prête : juger une page (blocs 2 et 4) |
| `requete-reponse-ia.json` | Requête prête : juger une réponse de ChatGPT, Claude ou Perplexity (blocs 1 et 3) |
| `exemple-requete.sh` | Envoyer une requête à l'API TypeSafe en une commande |
| `calcul-tableau-de-bord.md` | Les formules des 4 blocs : Jev juge, votre tableur calcule |

## Démarrer

1. Créez une clé sur https://console.typesafe.ai/keys (ou testez d'abord
   les questions à la main dans le Playground :
   https://console.typesafe.ai/playground).
2. Dans votre terminal : `export TYPESAFE_API_KEY=...`
3. Remplissez `state` dans `requete-page.json` avec une de vos pages, puis :
   `bash exemple-requete.sh requete-page.json`

Le format des requêtes suit la documentation officielle
(https://docs.typesafe.ai/api), relevée le 30/09/2026. Vérifiez le modèle
disponible (`jev-latest`) et les prix sur la documentation avant un gros
volume.

## Pour l'audit technique complet

Le skill open source jev-seo (MIT) de Daniel Agrici :
https://github.com/AgriciDaniel/jev-seo

---
Décupler — https://decupler.com · Nathan Fenina
