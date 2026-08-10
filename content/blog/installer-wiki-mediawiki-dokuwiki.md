+++
title = "Installer son propre wiki avec MediaWiki ou DokuWiki"
slug = "installer-wiki-mediawiki-dokuwiki"
date = "2026-08-10T08:35:00+10:00"
draft = false
description = "Choisir entre MediaWiki et DokuWiki, préparer l’hébergement, installer le wiki et sécuriser les mises à jour et sauvegardes."
summary = "Deux solutions open source encore actives pour créer une documentation privée ou un wiki public."
tags = ["wiki", "mediawiki", "dokuwiki", "open source", "documentation"]
priority = true
priority_topics = ["tech"]
original_title = "Créez votre propre Wiki en moins de 10 minutes !"
source_01script = "https://01script.com/logiciel-php-wiki-doc/"
+++

Un wiki reste pratique pour documenter un produit, une association, une équipe ou un projet personnel. Deux solutions PHP ont traversé les années : MediaWiki et DokuWiki.

Le bon choix dépend surtout du volume, de l’hébergement et du niveau de personnalisation attendu.

## MediaWiki pour une base riche

[MediaWiki](https://www.mediawiki.org/) est le logiciel utilisé par Wikipédia. Il convient aux contenus liés entre eux, aux historiques détaillés, aux nombreux comptes et aux extensions.

Il demande un serveur web, PHP et une base de données. La [documentation d’installation](https://www.mediawiki.org/wiki/Manual:Installing_MediaWiki/en) recommande MariaDB ou MySQL, tout en prenant aussi en charge PostgreSQL et SQLite.

La procédure générale est simple :

1. Vérifie les versions de PHP et de la base demandées par la version choisie.
2. Télécharge une version stable ou LTS depuis le site officiel.
3. Décompresse les fichiers dans le répertoire du site.
4. Crée une base et un utilisateur dédiés.
5. Ouvre l’URL du wiki et suis l’installateur.
6. Place le fichier `LocalSettings.php` généré à la racine du wiki.

Ne reprends pas une ancienne archive trouvée sur un site tiers. Les versions dépassées peuvent contenir des failles corrigées depuis.

## DokuWiki pour une installation légère

[DokuWiki](https://www.dokuwiki.org/dokuwiki) stocke les pages dans des fichiers texte et ne demande pas de base de données. C’est pratique pour une petite documentation, un intranet ou un hébergement simple.

Son installation consiste à déposer les fichiers, ouvrir `install.php`, créer le compte administrateur puis supprimer ou protéger l’installateur selon les instructions du projet.

L’absence de base simplifie les sauvegardes. Il faut tout de même sauvegarder les pages, la configuration, les médias et les données des extensions.

## Mon choix rapide

Je choisis MediaWiki quand j’ai besoin d’une communauté, de nombreuses extensions ou d’un modèle proche de Wikipédia.

Je choisis DokuWiki pour une documentation plus petite, facile à déplacer et à sauvegarder.

Dans les deux cas, je vérifie ces points avant de publier :

1. HTTPS est actif.
2. Les inscriptions publiques sont désactivées si elles ne servent pas.
3. Les sauvegardes sont automatiques et testées.
4. Le logiciel et ses extensions sont mis à jour.
5. Les droits d’écriture du serveur sont limités au nécessaire.

Créer le wiki prend peu de temps. Le garder propre, sauvegardé et à jour est le vrai travail.

