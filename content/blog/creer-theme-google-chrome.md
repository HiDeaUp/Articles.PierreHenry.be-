+++
title = "Comment créer son propre thème Google Chrome"
slug = "creer-theme-google-chrome"
date = "2011-09-04T15:13:00+02:00"
draft = false
description = "Créer un thème Google Chrome avec un fichier manifest.json, des couleurs et une image, puis le charger localement dans le navigateur."
summary = "Un thème Chrome est une extension sans JavaScript ni page HTML. Voici sa structure minimale."
tags = ["google chrome", "thème", "manifest json", "extension chrome", "navigateur"]
priority = true
priority_topics = ["tech"]
original_title = "Créez en 2 minutes votre propre thème pour Google Chrome !"
source_01script = "https://01script.com/creer-son-theme-navigateur-web-google-chrome/"
+++

Un thème Chrome change les couleurs du navigateur et peut ajouter une image à la page du nouvel onglet. Il se présente comme une extension, mais ne contient ni JavaScript ni page HTML.

Les anciens générateurs en ligne de mon premier article ne sont plus une base fiable. Un petit fichier JSON suffit et reste facile à comprendre.

## Préparer le dossier

Crée cette structure :

```text
mon-theme/
├── manifest.json
└── images/
    └── fond.png
```

Choisis une image PNG assez grande pour ton écran. La documentation Chrome précise que les autres formats peuvent ne pas s’afficher correctement. Évite aussi un fichier lourd, car Chrome doit le charger à chaque nouvel onglet.

## Écrire le manifeste

Dans `manifest.json`, ajoute :

```json
{
  "manifest_version": 3,
  "name": "Mon thème sobre",
  "version": "1.0.0",
  "theme": {
    "images": {
      "theme_ntp_background": "images/fond.png"
    },
    "colors": {
      "frame": [32, 33, 36],
      "toolbar": [255, 255, 255],
      "tab_text": [245, 245, 245],
      "bookmark_text": [32, 33, 36],
      "ntp_background": [245, 245, 245],
      "ntp_text": [32, 33, 36]
    },
    "properties": {
      "ntp_background_alignment": "center",
      "ntp_background_repeat": "no-repeat"
    }
  }
}
```

Les couleurs utilisent des tableaux RGB. Par exemple, `[255, 255, 255]` correspond au blanc.

La [documentation Chrome sur les thèmes](https://developer.chrome.com/docs/extensions/develop/ui/themes) contient les propriétés disponibles et un exemple de manifeste.

## Charger le thème localement

1. Ouvre `chrome://extensions`.
2. Active le **Mode développeur**.
3. Clique sur **Charger l’extension non empaquetée**.
4. Sélectionne le dossier `mon-theme`.

Le thème s’applique immédiatement. Si Chrome affiche une erreur, vérifie d’abord la syntaxe JSON, les virgules et le chemin de l’image.

## Garder le thème local ou le publier

Le mode développeur suffit pour ton usage personnel. Pour distribuer le thème, prépare une archive avec le manifeste et les images, puis passe par la procédure du Chrome Web Store. Vérifie que tu possèdes les droits sur chaque image avant de publier.

Un thème ne contient ni JavaScript ni HTML. S’il demande du code exécutable ou des permissions, ce n’est plus un simple thème et il faut revoir son périmètre comme une extension.

## Ajuster les couleurs

Je commence avec peu de couleurs : une pour le cadre, une pour la barre d’outils et une pour le texte. Je vérifie ensuite le contraste des onglets actifs et inactifs.

Une belle image ne compense pas un texte illisible. Teste le thème sur une fenêtre normale, une fenêtre privée et plusieurs tailles d’écran.

Pour revenir au thème par défaut, ouvre les paramètres d’apparence de Chrome et réinitialise le thème.
