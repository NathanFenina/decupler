# Décisions — ce qui a été tranché, et pourquoi

Une ligne par décision. On ne rouvre pas une décision sans fait nouveau.

## Règles permanentes (Nathan)

- Ne jamais inventer : adresse (seule : 10 avenue Lympia, 06300 Nice), chiffre
  client, note, avis, anecdote. Une image générée ne représente jamais un lieu
  réel ni une personne de l'équipe.
- Secrets dans `.env`, jamais dans le dépôt ni dans la conversation.
- Ne jamais charger l'export XML WordPress (23 Mo) dans la conversation.
- Accès Notion permanent : ne plus demander (22/09). Agir sans demander
  d'autorisation à chaque étape (29/09) ; les actions irréversibles restent
  réversibles quand c'est possible (rétrograder plutôt que supprimer, sauvegarder
  avant d'écrire).
- Pas d'identifiant de modèle d'IA dans les commits ni les contenus publiés.

## SEO et contenu

- Pages locales : « agence » pour le 06 et le Var, « consultant » pour les
  grandes villes ; une page seulement là où il y a des recherches (22/09).
- Doublons d'intention : redirection 301 seulement si la cible couvre déjà
  l'intention ; sinon on garde les deux et on relie (23/09).
- Spam du piratage : 410 + sitemap des URL supprimées, pas de demandes de
  suppression une par une ; les préfixes restants ne valent pas le temps
  (0 impression depuis juillet) (29/09).
- Lead magnets : pop-up obligatoire seulement pour `?acces=linkedin` ; Google
  lit librement (pénalité des interstitiels intrusifs sur mobile) (28/09).
- Chaque lead magnet a un mot-clé principal ET un prompt IA principal (29/09).
- /claude-code-design/ remplace le guide « site premium en 24h » (28/09),
  mot-clé « claude code design » (170/mois, difficulté 20).

## Technique

- Tout correctif serveur passe par un plugin versionné et testé dans un vrai
  WordPress (banc SQLite + Yoast), jamais par un réglage fait à la main dans
  l'admin sans trace.
- Trio sémantique : une seule Organisation (`#organization`) et une seule
  Personne (`#nathan-fenina`) ; les blocs JSON-LD référencent ces @id (29/09).
- Le thème final sera fait par un freelance : le contenu reste en HTML
  sémantique, sans dépendance à Elementor pour les nouvelles pages.
