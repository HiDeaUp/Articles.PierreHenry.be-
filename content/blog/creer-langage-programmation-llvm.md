+++
title = "Créer son propre langage de programmation : par où commencer"
slug = "creer-langage-programmation-llvm"
date = "2026-08-10T09:00:00+10:00"
draft = false
description = "Comprendre les étapes d’un petit langage de programmation : syntaxe, lexer, parser, arbre syntaxique, interprétation et génération de code LLVM."
summary = "Créer un langage devient plus concret lorsque l’on commence par quelques expressions et un interpréteur minimal."
tags = ["programmation", "compilateur", "llvm", "parser", "langage"]
priority = true
priority_topics = ["tech"]
original_title = "Créez votre propre langage de programmation !"
source_01script = "https://01script.com/comment-creer-son-langage-de-programmation/"
+++

Créer un langage de programmation paraît immense. Le projet devient plus clair lorsque l’on oublie un moment les classes, les modules et les bibliothèques pour commencer par une expression simple.

Un premier langage peut accepter ceci :

```text
let total = 4 + 5 * 2
print total
```

Il suffit alors de transformer ce texte en étapes compréhensibles par le programme.

## Définir une petite syntaxe

Décide d’abord ce que ton langage sait faire :

1. des nombres ;
2. quatre opérateurs ;
3. des variables ;
4. une commande d’affichage.

Écris quelques exemples valides et invalides. Ils deviendront les premiers tests du parser.

## Découper le texte avec un lexer

Le lexer transforme les caractères en jetons. L’expression `4 + 5` devient par exemple :

```text
NUMBER(4), PLUS, NUMBER(5)
```

Cette étape gère les espaces, les nombres, les mots réservés et les symboles inconnus.

## Construire un arbre syntaxique

Le parser vérifie l’ordre des jetons et produit un arbre syntaxique abstrait, souvent nommé AST.

Pour `4 + 5 * 2`, l’arbre doit respecter la priorité de la multiplication :

```text
Add
├── Number(4)
└── Multiply
    ├── Number(5)
    └── Number(2)
```

Un bon parser retourne aussi une erreur lisible avec la ligne et la colonne concernées.

## Interpréter ou compiler

La voie la plus courte consiste à parcourir l’AST et calculer le résultat. Tu obtiens alors un interpréteur.

Pour aller vers du code natif, LLVM fournit une représentation intermédiaire, un optimiseur et plusieurs cibles. Son tutoriel officiel [My First Language Frontend with LLVM](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/) construit le langage Kaleidoscope en C++. Il couvre le lexer, le parser, l’AST, la génération LLVM IR, le JIT et les informations de débogage.

LLVM précise que ce tutoriel enseigne les techniques de compilation, pas toutes les pratiques d’architecture logicielle. C’est une distinction utile.

## Le projet qui apprend vraiment

Je commencerais avec un interpréteur de quelques centaines de lignes, des tests et un REPL. J’ajouterais ensuite les variables, les fonctions, les conditions et des messages d’erreur plus précis.

Le but du premier langage n’est pas de remplacer Python ou C++. Il sert à comprendre comment un texte devient une action exécutée par une machine.
