+++
title = "Comment je configure PhpStorm pour un projet PHP"
slug = "configurer-phpstorm-projet-php"
date = "2026-08-10T09:05:00+10:00"
draft = false
description = "Configurer PhpStorm avec EditorConfig, Composer, les inspections, PHP_CodeSniffer et les vérifications Git utiles à une équipe PHP."
summary = "Une configuration PhpStorm courte, centrée sur les règles du projet plutôt que sur une longue liste de plugins."
tags = ["phpstorm", "php", "composer", "phpcs", "ide"]
priority = true
priority_topics = ["tech"]
original_title = "Mes configurations & Plugins PHPStorm (en image)"
source_01script = "https://01script.com/configurations-plugins-phpstorm/"
+++

Ma configuration PhpStorm a changé. Plusieurs fonctions qui demandaient autrefois un plugin sont maintenant intégrées à l’IDE. Je préfère aussi placer les règles dans le projet afin que toute l’équipe partage le même résultat.

## Commencer par EditorConfig

Ajoute un fichier `.editorconfig` à la racine :

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
indent_style = space
indent_size = 4
trim_trailing_whitespace = true

[*.{yml,yaml,json}]
indent_size = 2
```

PhpStorm lit ce fichier. Les autres éditeurs compatibles aussi. Cela évite de régler manuellement les fins de ligne et l’indentation sur chaque poste.

## Configurer PHP et Composer

Dans les paramètres du projet, vérifie l’interpréteur PHP et sa version. Ouvre ensuite `composer.json` et installe les dépendances depuis l’IDE ou le terminal.

Je garde les outils de qualité dans `require-dev` afin que le projet indique lui-même ce qu’il attend.

## Activer les inspections utiles

PhpStorm détecte les erreurs probables, le code mort, les problèmes de structure et certaines fautes. Les [inspections sont organisées en profils](https://www.jetbrains.com/help/phpstorm/code-inspection.html).

Je crée un profil de projet et je limite les règles trop bruyantes. Une alerte ignorée chaque jour ne sert plus à rien.

## Relier PHP_CodeSniffer

Installe PHP_CodeSniffer dans le projet :

```bash
composer require --dev squizlabs/php_codesniffer
```

Ajoute un fichier `phpcs.xml` avec la norme choisie, par exemple PSR-12. PhpStorm détecte généralement l’exécutable dans `vendor/bin`.

La [documentation JetBrains sur PHP_CodeSniffer](https://www.jetbrains.com/help/phpstorm/using-php-code-sniffer.html) explique l’activation dans **PHP > Quality Tools** et dans le profil d’inspection.

## Vérifier avant le commit

PhpStorm peut reformater le code, optimiser les imports et lancer une analyse avant un commit. Je n’active que les contrôles rapides. La suite complète reste dans la CI.

Je partage le profil d’inspection utile, `.editorconfig` et les fichiers de configuration des outils. Je n’ajoute pas `workspace.xml`, qui contient des préférences propres au poste.

Une bonne configuration d’IDE ne tient pas à dix plugins. Elle tient à quelques règles visibles, versionnées et exécutables aussi hors de l’éditeur.

