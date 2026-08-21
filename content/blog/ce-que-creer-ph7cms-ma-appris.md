+++
title = "Ce que la création de pH7CMS m’a appris"
slug = "ce-que-creer-ph7cms-ma-appris"
date = "2014-03-30T01:09:00+01:00"
draft = false
description = "Les leçons que je retiens de la création de pH7CMS, une plateforme open source de rencontre et de réseau social, entre architecture, sécurité et produit."
summary = "Créer pH7CMS m’a appris qu’une plateforme communautaire ne se résume pas à ses fonctionnalités. La confiance, l’exploitation et les choix d’architecture comptent autant que le code."
tags = ["pH7CMS", "open source", "PHP", "architecture logicielle", "site de rencontre", "retour d’expérience"]
priority = true
priority_topics = ["tech", "entrepreneurship"]
original_title = "pH7CMS : Le nouveau CMS révolutionnaire !"
source_01script = "https://01script.com/cms-rencontre-open-source-gratuit/"
+++

En 2014, je présentais pH7CMS avec une longue liste de modules : profils, messagerie, géolocalisation, forums, modération, internationalisation et bien d’autres fonctions.

Cette liste montrait ce que le logiciel savait faire. Avec le recul, elle ne disait pas ce que sa création m’avait appris.

pH7CMS, aujourd’hui nommé [pH7Builder](https://github.com/pH7Software/pH7-Social-Dating-CMS), est un projet open source en PHP destiné aux services de rencontre et aux communautés en ligne. Le construire m’a obligé à penser au-delà d’une page web ou d’une fonctionnalité isolée.

{{< figure src="/images/blog/ph7cms/ph7cms-2014-interface.webp" alt="Interface d’inscription de pH7CMS en 2014" title="Interface de pH7CMS en 2014" caption="Une interface de pH7CMS publiée avec mon article original en 2014. Le design a vieilli, mais il documente une étape réelle du projet." >}}

## Une plateforme est un ensemble de systèmes

Un profil ne fonctionne pas seul. Il dépend de l’inscription, des permissions, de la recherche, des messages, des notifications, du blocage et de la suppression des données.

Une modification locale peut donc avoir des conséquences ailleurs. Ajouter un champ au profil paraît simple. Il faut pourtant décider qui peut le voir, comment le rechercher, le traduire, l’exporter et le supprimer.

Cette dépendance entre les fonctions m’a appris à raisonner en parcours complets. Je ne demande plus seulement si une page fonctionne. Je vérifie ce qui se passe avant, après et lorsque l’utilisateur change d’avis.

## Un framework maison a un coût durable

J’avais construit pH7Framework pour répondre aux besoins du CMS. Cela m’a donné une compréhension concrète du routage, des contrôleurs, des modèles, des vues, du cache et de la sécurité.

Ce choix m’a aussi appris le coût d’un framework interne. Chaque composant ajouté devient une responsabilité : documentation, compatibilité, tests, mises à jour et correction des failles.

Aujourd’hui, je ne construirais pas un framework complet par défaut. Je commencerais par un framework maintenu et je n’ajouterais une abstraction interne que pour un besoin propre au produit. L’expérience reste précieuse, mais elle m’a rendu plus prudent avec le code que seule une petite équipe sait maintenir.

## La modularité doit réduire les dépendances

pH7CMS comportait de nombreux modules. Leur nombre n’était pas le principal intérêt. Le vrai enjeu était de pouvoir désactiver une fonction sans casser le reste de l’application.

Un module utile possède une responsabilité claire, des dépendances visibles et une interface stable. S’il lit directement les tables de plusieurs autres modules, modifie leurs fichiers ou suppose leur présence, il n’est indépendant que dans son nom.

Cette leçon reste valable dans un monolithe modulaire comme dans une architecture distribuée. Une frontière technique n’a de valeur que si elle aide à comprendre, tester et remplacer une partie du système.

## La confiance fait partie du produit

Une plateforme de rencontre reçoit des photos, des messages, des préférences et parfois une localisation. Le signalement, le blocage, les permissions et la modération ne sont donc pas des fonctions secondaires.

Il faut également prévoir les abus : faux profils, spam, harcèlement, comptes compromis et collecte de données par des tiers. Une règle écrite ne suffit pas. Il faut un parcours de traitement, des traces utiles pour les responsables et une manière de corriger une décision.

Je considère maintenant la sécurité et la modération dès la conception. L’[OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) donne une base vérifiable pour les contrôles techniques. Les besoins propres à la communauté doivent ensuite compléter cette base.

## L’open source change la manière de travailler

Publier le code expose les décisions, les incohérences et la qualité de la documentation. Une installation difficile ou une convention implicite devient vite un problème pour les contributeurs.

Le dépôt public m’a appris à écrire pour une personne qui n’a pas mon contexte. Une issue claire, une procédure de reproduction et une petite contribution bien limitée peuvent faire avancer le projet plus qu’une longue discussion générale.

Il faut aussi protéger le temps de maintenance. Accepter chaque demande produit un logiciel plus large, mais pas forcément plus utile. Refuser une fonction peut être une décision d’architecture autant qu’une décision produit.

## Le déploiement appartient aussi au produit

Un logiciel auto-hébergé ne s’arrête pas au code source. L’installation, les variables de configuration, les migrations, les sauvegardes et les mises à jour font partie de l’expérience.

Une fonction qui marche sur ma machine mais complique chaque mise à jour n’est pas terminée. Je préfère maintenant une procédure répétable, des dépendances explicites et un chemin de mise à niveau testé.

## Ce que je ferais aujourd’hui

Je commencerais par un noyau plus petit : comptes, profils, découverte, messagerie, signalement, blocage et administration. Je testerais ces parcours avec une communauté précise avant d’ajouter des dizaines de modules.

Je garderais un monolithe modulaire tant que l’équipe et la charge ne justifient pas une séparation plus coûteuse. Je choisirais des composants maintenus pour les besoins courants. Je documenterais les décisions qui concernent les données personnelles et la modération avant la première mise en production.

Construire pH7CMS m’a surtout appris qu’un produit communautaire est un système vivant. Le code lance le service. La maintenance, la confiance et les décisions prises sur plusieurs années déterminent s’il reste utile.
