# Calculer les 4 blocs du tableau de bord GEO

Règle d'or : **Jev juge, le code calcule.** Jev répond aux questions de
`questions-jev-geo.json` ; les chiffres du tableau de bord se calculent
ensuite, dans un tableur ou un script, avec les formules ci-dessous.

## Les données à réunir

1. **Un lot de prompts** : 30 à 50 questions que vos clients posent vraiment
   à une IA. Sources : vos requêtes Search Console, les questions reçues par
   le commercial, « Autres questions posées » de Google.
2. **Les réponses des IA** à ces prompts, moteur par moteur (ChatGPT,
   Claude, Perplexity). À la main, ou avec DataForSEO (API « LLM
   responses » / mode `--full` de jev-seo).
3. **Le texte de vos pages** (jev-seo le récupère en explorant le site).

Seuil de décision : une réponse Noul au-dessus de **0,5** compte comme un
oui. Une réponse Choice ou Score dont la `confidence` est sous **0,6** est
marquée « à vérifier » et relue par un humain avant d'entrer dans les
chiffres.

## Bloc 1 — Visibilité moteur par moteur

Pour chaque moteur :

    taux de citation = nb de réponses où marque_citee > 0,5
                       ÷ nb de prompts testés

À côté, afficher le même taux pour `concurrent_cite` : c'est l'écart qui
compte. Lister les 3 pages les plus souvent en source (`site_en_source`).

## Bloc 2 — Score GEO global (sur 100)

Pour chaque page, avec les réponses de `requete-page.json` :

    score_page = 100 × ( 0,30 × citabilite/4
                       + 0,25 × va_droit_au_but
                       + 0,20 × precision/4
                       + 0,15 × confiance/4
                       + 0,10 × repond_au_prompt )

(les Score vont de 0 à 4, les Noul de 0 à 1). Le score global est la
moyenne des pages, pondérée par leur importance (trafic Search Console, ou
1 par défaut).

    gains restants = part des pages dont score_page < 60

Les poids sont un choix éditorial, pas une vérité : gardez les mêmes d'un
mois sur l'autre pour comparer.

## Bloc 3 — Couverture des intentions

Pour chaque intention (info, prix, comparatif, avis, local, achat) :

    couverture = nb de réponses où marque_citee > 0,5 pour cette intention
                 ÷ nb de prompts de cette intention

Une intention sous 10 % = une page à créer ou à refaire pour ce type de
question.

## Bloc 4 — Citabilité par type de page

Grouper les pages par `type_page`, puis :

    citabilité du type = 100 × moyenne(citabilite/4) des pages du type

Le type le plus bas est le premier chantier de réécriture.

## Ce que ces chiffres ne sont pas

Des prédictions. Ils classent le travail et se comparent d'un mois sur
l'autre avec le même lot de prompts. Ils ne disent rien du trafic futur.
