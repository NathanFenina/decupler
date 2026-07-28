# 🎨 Générer des images avec Gemini — Guide stagiaire

Ce guide t'explique, **sans aucune notion technique**, comment créer des images
(illustrations, visuels de couverture, schémas) pour les sites clients et pour
Décupler, puis les envoyer dans WordPress.

Tu n'as **rien à coder**. Tu écris à Claude en français, il fait le reste.

---

## Étape 1 — Récupérer une clé Gemini (une seule fois)

1. Va sur 👉 https://aistudio.google.com/apikey
2. Connecte-toi avec un compte Google.
3. Clique sur **« Create API key »** (Créer une clé API).
4. Copie la clé (une longue suite de lettres et chiffres). Garde-la au chaud.

> ⚠️ Cette clé est un **secret**, comme un mot de passe. On ne la partage pas,
> on ne la met JAMAIS dans un message public, un article ou GitHub.

---

## Étape 2 — Coller ta clé dans le fichier `.env`

À la racine du projet, il y a un fichier qui s'appelle **`.env`**.
Ouvre-le et trouve la ligne :

```
GEMINI_API_KEY=
```

Colle ta clé juste après le `=`, sans espace :

```
GEMINI_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

Enregistre. C'est tout.

> 💡 Si tu ne vois pas de fichier `.env`, demande à Claude :
> **« Crée le fichier .env à partir de .env.example »**, puis colle ta clé.

> 🔒 Le fichier `.env` reste **sur ta machine uniquement**. Il n'est jamais
> envoyé sur GitHub (il est volontairement ignoré). Chaque personne met sa
> propre clé.

---

## Étape 3 — Demander une image à Claude

Écris simplement ta demande, en décrivant l'image voulue. Exemples :

> « Génère un visuel de couverture **16:9** pour l'article “Agence GEO”,
> style **dark violet/vert Décupler**, épuré, et enregistre-le dans
> `content/articles/images/hero.png`. »

> « Fais-moi une illustration **1:1** pour le client [NOM], sur le thème
> [SUJET], couleurs [préciser], et mets-la dans
> `content/clients/[nom]/images/visuel.png`. »

Astuces pour une bonne image :
- **Précise le format** : `16:9` (bannière), `1:1` (carré), `3:2` (photo).
- **Décris le style** : couleurs, ambiance, « épuré », « moderne », etc.
- **Dis où l'enregistrer** : un chemin de fichier clair.

Claude génère l'image et te donne le **chemin du fichier** créé.

---

## Étape 4 — Envoyer l'image dans WordPress

Une fois l'image générée, demande à Claude :

> « Téléverse cette image dans WordPress avec un titre et un texte alternatif
> (alt) optimisés SEO. »

Claude s'occupe de l'envoi (via `scripts/wp_upload_media.py`). Tu récupères
l'image dans la médiathèque WordPress, prête à être insérée dans l'article.

---

## En cas de problème

| Message / souci | Ce que ça veut dire | Solution |
|---|---|---|
| « Clé API détectée : NON » | La clé n'est pas lue | Vérifie l'étape 2 (clé bien collée dans `.env`, sans espace). Redémarre Claude. |
| « Erreur 400 / 403 » à la génération | Clé invalide ou quota épuisé | Recrée une clé sur AI Studio (étape 1). |
| Rien ne se passe | Le serveur MCP n'est pas lancé | Demande à Claude : « Vérifie que le MCP gemini-images est connecté. » |

---

## À retenir

- 🔑 **Une clé par personne**, collée dans `.env`, jamais partagée.
- 🗣️ Tu **écris en français** à Claude, tu ne codes pas.
- 🖼️ Toujours **préciser le format, le style et le chemin** de l'image.
- 📤 L'envoi WordPress se fait en **brouillon** : quelqu'un relit avant publication.

Détails techniques (pour info) : `scripts/mcp/README.md`.
