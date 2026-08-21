+++
title = "Internationaliser un site sans widget de traduction"
slug = "internationaliser-site-sans-widget-traduction"
date = "2010-12-13T23:02:00+01:00"
draft = false
description = "Une méthode actuelle pour internationaliser un site avec des URLs stables, des fichiers de traduction, Intl, lang, hreflang et une validation humaine."
summary = "Une traduction automatique affichée dans un widget ne remplace pas une architecture multilingue. Les URLs, le contenu, les formats et le référencement doivent être conçus ensemble."
tags = ["internationalisation", "i18n", "traduction", "SEO", "accessibilité", "développement web"]
priority = true
priority_topics = ["tech"]
original_title = "Internationalisez votre site grâce aux outils de Google"
source_01script = "https://01script.com/script-internationalisation-pour-webmasters/"
+++

Mon article de 2010 proposait plusieurs outils Google et un widget capable de traduire une page dans le navigateur. Ces services ne constituent plus une base adaptée pour un site multilingue.

Une traduction visible ne suffit pas. Un produit internationalisé doit conserver des URLs stables, afficher les bons formats, rester accessible et permettre aux moteurs de recherche de trouver chaque version.

## Séparer le contenu de l’interface

Je commence par sortir les textes de l’interface du code. Un bouton ne devrait pas contenir sa phrase française directement dans le composant.

Je lui donne une clé stable, par exemple `account.delete.confirm`, puis je conserve une valeur pour chaque langue prise en charge. Les clés décrivent l’intention, pas la position à l’écran. `header.button.2` devient incompréhensible dès que l’interface change.

Le contenu éditorial demande une décision distincte. Un article, une fiche produit ou une page juridique possède son propre cycle de traduction et de révision. Je ne mélange pas ces textes avec les messages courts de l’application.

## Donner une URL à chaque langue

Chaque version doit pouvoir être ouverte, liée et partagée sans dépendre d’un cookie. J’utilise par exemple :

```text
https://example.com/fr/produits
https://example.com/en/products
```

Google recommande des [URLs différentes pour chaque langue](https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites) et déconseille de dépendre uniquement d’une redirection selon la langue du navigateur.

Je peux proposer la version probable au premier passage, mais je garde un sélecteur visible et je respecte ensuite le choix de la personne. Une redirection forcée devient pénible pour un voyageur, un traducteur ou une personne qui préfère une autre langue.

## Déclarer la langue dans le document

La page française doit commencer avec une déclaration correcte :

```html
<html lang="fr">
```

Le [W3C recommande l’attribut `lang`](https://www.w3.org/International/questions/qa-html-language-declarations.html) sur l’élément `html`. Les lecteurs d’écran, correcteurs et autres outils peuvent alors traiter le texte avec les bonnes règles.

Si un passage utilise une autre langue, je la déclare sur l’élément concerné. Je pense aussi à `dir="rtl"` pour les écritures de droite à gauche et je teste la mise en page avec des textes plus longs que le français.

## Formater les données selon la locale

Je ne traduis pas seulement des mots. Les dates, nombres, devises, listes et pluriels changent selon la locale.

En JavaScript, l’API [`Intl`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Intl) fournit les règles du navigateur :

```js
const amount = new Intl.NumberFormat("fr-FR", {
  style: "currency",
  currency: "EUR",
}).format(1250.5);
```

Je conserve les données dans un format neutre, puis je les présente selon la locale. Je n’enregistre pas `1 250,50 €` comme une valeur destinée aux calculs.

La devise, le pays et la langue sont trois informations différentes. Une personne peut lire le français en Australie et payer en dollars australiens. Je ne déduis pas automatiquement toute son expérience à partir d’un seul code.

## Relier les versions pour le référencement

Lorsque plusieurs pages sont des variantes traduites, j’ajoute des liens `hreflang` réciproques dans le HTML ou le sitemap. La [documentation de Google](https://developers.google.com/search/docs/specialty/international/localized-versions) précise que chaque version doit se référencer elle-même et référencer les autres versions correspondantes.

Je vérifie également que :

- chaque page possède un titre et une description dans sa langue ;
- les liens internes restent dans la langue choisie ;
- la version canonique désigne l’URL correcte de cette langue ;
- le sitemap ne contient pas de pages inexistantes ;
- une langue incomplète ne produit pas des pages presque vides.

`hreflang` ne corrige pas une mauvaise traduction. Il aide seulement à relier des pages qui existent déjà.

## Utiliser la traduction automatique comme outil

La traduction automatique peut produire un premier brouillon, repérer des chaînes oubliées ou aider l’équipe à comprendre un retour. Je ne la publie pas sans contrôle pour les textes importants.

Je demande une révision humaine pour les pages de vente, les conditions, les messages de sécurité et les parcours sensibles. Je donne au traducteur le contexte de la chaîne, une capture de l’interface et les limites de longueur utiles.

Je conserve aussi un glossaire. Un même concept doit garder le même terme dans la navigation, l’aide et les messages d’erreur.

## Tester une langue comme un produit complet

Avant de publier, je parcours l’inscription, la connexion, les courriels, les erreurs, le paiement et la suppression du compte dans chaque langue prise en charge.

Je cherche les chaînes non traduites, les textes coupés, les dates ambiguës et les liens qui reviennent vers la langue par défaut. J’ajoute ces vérifications aux tests lorsque c’est possible.

Internationaliser un site ne consiste pas à poser un bouton de traduction sur une page. Il faut concevoir le contenu, les URLs, les formats et la maintenance comme une partie du produit.
