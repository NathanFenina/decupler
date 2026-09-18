# Email 06 — Blog technique WordPress / SEO : l'outil comme prétexte

**Cible :** `seomix.fr` (Daniel Roch), autres blogs WordPress techniques
**Offre :** un outil open source, gratuit, utile, publié sur GitHub
**Pourquoi ça marche :** un consultant technique ne relaie pas une agence. Il
relaie un outil que ses lecteurs vont installer. Le lien suit l'outil.
**⚠️ Prérequis : le dépôt doit être public, documenté et fonctionner.**

**Objet :** Un outil gratuit pour publier depuis Claude vers WordPress — votre avis avant que je le sorte

---

Bonjour Daniel,

Je suis SeoMix depuis longtemps ; c'est la référence quand il s'agit de faire du
SEO propre sur WordPress plutôt que d'empiler des plugins.

On a développé un outil en interne qu'on s'apprête à publier en open source :
un pont entre Claude et l'API REST de WordPress. On rédige, on publie en
brouillon, on gère les métadonnées Yoast, sans passer par l'admin. On l'utilise
tous les jours sur nos sites.

Avant de le sortir, j'aimerais l'avis de quelqu'un qui connaît WordPress mieux
que nous. Deux points sur lesquels je bloque et qui vous parleront :

— `wpautop` casse les blocs `<style>` et `<script>` en injectant des `</p><p>`
  sur les lignes vides. On neutralise en supprimant les lignes vides à
  l'intérieur des balises. Vous faites comment, vous ?
— Yoast n'expose aucun champ SEO dans son schéma REST. On passe par le template
  `%%excerpt%%` pour router l'extrait natif vers la meta description — mais une
  valeur Yoast au niveau de la page écrase toujours le template. Il y a mieux ?

Je vous donne l'accès au dépôt, vous cassez ce que vous voulez. Si l'outil vous
paraît bon, il est à vous d'en parler ou pas — je ne demande rien en échange de
la relecture.

Nathan Fenina
Décupler — https://decupler.com
