# Journal des arbitrages

Pourquoi chaque règle existe. À lire quand une contrainte paraît absurde —
elle vient presque toujours d'un incident réel.

---

**Le bloc « À découvrir aussi sur Décupler » est supprimé.**
Demande explicite de Nathan, août 2026. Un bloc de liens en pied est ignoré des
lecteurs et dilué pour les moteurs. Remplacé par ≥ 8 ancres contextuelles posées
dans le fil du texte. → `maillage.md`

**On n'ajoute pas de phrase pour caser un lien.**
Corollaire du point précédent. Quand aucune ancre naturelle ne se présente, deux
cas : soit le lien n'est pas pertinent, soit il manque une idée au texte. Sur
deux articles du cluster, c'était le second cas — une phrase utile a été ajoutée,
et le lien s'est ancré tout seul.

**Un article ne lie que ses prédécesseurs de publication.**
Le cluster de 16 articles est programmé sur cinq semaines. Lier un article qui
paraît trois semaines plus tard publie un lien mort. Le tri par date de parution
règle le problème sans arbitrage humain.

**Les ancres sont relues en contexte.**
Trois ancres tombaient sur des tournures critiques : « méthode propriétaire
opaque », « accepter un seul moteur ». Le lien pointait vers une page Décupler
depuis une phrase décrivant une mauvaise pratique. Contrôle automatisable pour
le comptage, pas pour le sens.

---

**La longueur se calcule, elle ne s'estime pas.**
Demande de 20 occurrences du mot-clé + plafond de densité à 3,5 % = une contrainte
de longueur, pas un choix éditorial. Sur « agence SEO IA », 20 occurrences dans
1500 mots donnaient 4,0 % et déclenchaient le malus −5. D'où la formule et les
2286 mots des mots-clés de 4 mots.

**Face à une densité trop haute, on ajoute du texte.**
Réflexe inverse de l'intuition. Retirer des occurrences ferait passer sous le
plancher de 20. Un paragraphe utile de 120 mots fait gagner ~0,15 point.

---

**La sidebar est exclue du contrôle de duplication.**
Elle est identique sur tous les articles. Sans exclusion, le contrôle signalait
5 phrases communes entre deux articles dont 3 venaient du CTA — faux positif sur
tout le lot.

**Le seuil de duplication est à 4 phrases, pas 0.**
Deux articles du même cluster partagent légitimement une ou deux formulations
courtes. Le premier jet des pages villes montait à 29 phrases communes, soit
41 % — « c'est une cata » selon Nathan. Une rédaction correcte descend à 1.

---

**L'image à la une reste la bannière bleue.**
Un essai de bannière sombre à la charte violette a été rejeté : la série
`article-*.png` existe depuis longtemps, l'harmonie du blog prime.

**La maquette d'écran est obligatoire.**
Le gabarit d'article masque l'en-tête du thème : l'image à la une ne s'affiche
nulle part sur la page. Sans image de corps, l'article n'a aucun visuel. Constaté
après avoir cru le problème résolu.

**Chaque sujet a sa propre maquette.**
16 articles, 16 écrans distincts. Réutiliser le même visuel sur deux articles du
même cluster les fait se ressembler dans les listes et les partages.

---

**Le push ne force jamais un statut.**
Un `POST` avec `status: draft` déprogramme un article planifié, sans
avertissement. Découvert alors que 15 articles venaient d'être programmés — le
script les aurait tous remis en brouillon.

**Le push cherche par slug avant d'écrire.**
Sinon WordPress crée un doublon suffixé `-2`. Arrivé une fois sur deux articles,
avec le média associé également dupliqué.

**Les médias se réutilisent par slug.**
Quatre fichiers pour une image après quelques allers-retours, et le slug de
l'original décalé en `-2`. Purge puis push unique pour rattraper.

---

**`position: sticky` natif suffit.**
La version JavaScript relâchait le CTA à la fin de `.dcp-layout`, avant la FAQ.
Le `overflow-x: hidden` du body ne l'empêche pas — vérifié sur 23 articles.

**Les champs Yoast sont perdus silencieusement sur les pages.**
L'API renvoie 200 et jette les valeurs. Vérifié via le schéma `OPTIONS`. Il faut
prévenir, pas supposer.

**Le cache Elementor bloque tout.**
Prouvé en changeant un identifiant de widget en base : la page publique servait
toujours l'ancien. Aucun contournement par API trouvé.

---

**Trois hypothèses du skill de scoring sont périmées.**
`llms.txt`, `/search-everywhere/` et `/tarifs/` renvoient 410. D'où
`check_urls.py` et le fichier `etat-du-site.md`, à régénérer plutôt qu'à croire.

**Un audit se fait séquentiellement.**
Douze requêtes concurrentes donnaient des comptages incohérents (1533 puis 1068
sur le même périmètre). En séquentiel : 0 faux négatif sur 25 échantillons.

---

**« Top agences GEO France » n'est pas un second classement.**
L'article existant `/agences-geo-france/` occupe déjà ce terrain. Le nouvel
article traite de la lecture des classements et pointe vers lui, pour ne pas se
cannibaliser. Choix signalé à Nathan, validé implicitement.
