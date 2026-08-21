+++
title = "Héberger une classe virtuelle avec BigBlueButton"
slug = "heberger-classe-virtuelle-bigbluebutton"
date = "2012-01-12T12:40:00+01:00"
draft = false
description = "Quand auto-héberger BigBlueButton, quelles contraintes prévoir et comment évaluer serveur, réseau, enregistrements, intégration et exploitation."
summary = "BigBlueButton répond à un besoin précis de classe virtuelle. Son code est open source, mais son exploitation en production demande une vraie préparation."
tags = ["BigBlueButton", "visioconférence", "open source", "auto-hébergement", "WebRTC", "infrastructure"]
priority = true
priority_topics = ["tech"]
original_title = "Outil de Vidéo Conférence Web open source - BigBlueButton"
source_01script = "https://01script.com/outil-video-conference-web-bigbluebutton/"
+++

J’ai découvert BigBlueButton en 2012 comme un outil open source de visioconférence. Je le présentais alors par ses fonctions : voix, vidéo, diapositives, partage d’écran et chat.

Ces fonctions existent désormais dans beaucoup de services. La raison de choisir BigBlueButton est plus précise : le projet est conçu pour la classe virtuelle, avec des présentations, un tableau blanc, des sondages, des salles de travail et des enregistrements.

L’auto-hébergement donne du contrôle. Il ajoute aussi une responsabilité technique qu’il faut mesurer avant l’installation.

## Commencer par le besoin pédagogique

Je ne choisirais pas BigBlueButton pour remplacer automatiquement chaque réunion vidéo.

Je le considérerais si le service doit gérer plusieurs de ces usages :

- un enseignant ou un animateur avec des droits distincts ;
- des diapositives annotées pendant la séance ;
- des sondages et un tableau blanc partagé ;
- des salles de travail séparées ;
- une intégration avec une plateforme de formation ;
- des enregistrements structurés autour du cours.

Si le besoin se limite à quelques appels internes, un service géré sera souvent plus simple. L’exploitation de la vidéo en temps réel n’est pas un détail d’hébergement.

## Lire les prérequis avant de choisir le serveur

La [documentation d’installation de BigBlueButton 3.0](https://docs.bigbluebutton.org/administration/install/) recommande actuellement un serveur Ubuntu 22.04 dédié, 8 cœurs, 16 Go de mémoire, une connexion symétrique de 250 Mbit/s et beaucoup d’espace disque lorsque les sessions sont enregistrées.

Ces valeurs ne sont pas une promesse de capacité. Le nombre de webcams, la qualité vidéo, les partages d’écran, les enregistrements et la localisation des participants modifient la charge.

Je réalise donc un test avec un scénario proche de la réalité. Dix personnes qui écoutent une présentation ne consomment pas les mêmes ressources que plusieurs groupes avec leurs caméras, micros et tableaux blancs actifs.

## Le réseau compte autant que le processeur

Une classe virtuelle dépend du chemin entre chaque navigateur et le serveur. Un processeur disponible ne corrige pas une perte de paquets ou un pare-feu qui bloque les flux WebRTC.

Je vérifie au minimum :

- un nom de domaine et un certificat TLS valide ;
- les ports TCP et UDP demandés par la documentation ;
- un serveur TURN pour les réseaux restrictifs ;
- la bande passante entrante et sortante ;
- la latence depuis les régions où se trouvent les utilisateurs ;
- le comportement sur un réseau mobile ou partagé.

Le test doit inclure les navigateurs et appareils réellement utilisés par les participants.

## Les enregistrements changent l’exploitation

Un enregistrement ne correspond pas seulement à un fichier vidéo. BigBlueButton capture les événements et médias de la séance, puis les traite pour produire une lecture. La [documentation sur les enregistrements](https://docs.bigbluebutton.org/development/recording/) décrit ce processus.

Il faut décider :

- quelles séances peuvent être enregistrées ;
- qui peut démarrer l’enregistrement ;
- combien de temps conserver les données ;
- qui peut consulter, exporter ou supprimer le résultat ;
- comment sauvegarder les fichiers utiles ;
- comment informer les participants.

L’espace disque, le temps de traitement et la politique de conservation doivent être prévus avant la première séance enregistrée.

## Intégrer sans exposer les secrets

BigBlueButton fournit une API pour créer une réunion, générer les liens d’accès et consulter son état. Une application ou une plateforme de formation peut donc gérer les comptes et appeler BigBlueButton pour la session vidéo.

Je garde le secret de l’API côté serveur. Le navigateur ne doit pas pouvoir fabriquer seul un lien de modérateur ou modifier les paramètres sensibles.

Je teste aussi les erreurs : serveur indisponible, séance terminée, enregistrement en cours de traitement et utilisateur sans autorisation. L’intégration est complète lorsque ces états sont compréhensibles, pas seulement lorsque le premier appel fonctionne.

## Exploiter le service dans la durée

Une installation de production a besoin de surveillance, de journaux, de sauvegardes, de mises à jour et d’un plan de capacité. Je vérifie l’état du serveur avant une séance importante et je garde une procédure de repli si la plateforme ne répond plus.

Je préfère également tester les mises à jour sur une autre machine. Les dépendances vidéo, le navigateur client et le système d’exploitation changent. Une mise à jour directe avant un cours important ajoute un risque inutile.

## Auto-héberger ou utiliser un service géré

J’auto-hébergerais BigBlueButton lorsque le contrôle des données, l’intégration, la personnalisation ou le volume justifient une compétence d’exploitation dédiée.

Je choisirais un hébergement géré lorsque l’équipe veut surtout organiser des cours et ne possède pas le temps nécessaire pour surveiller une infrastructure temps réel.

Le logiciel est open source. Le service, lui, a toujours un coût : serveur, stockage, réseau, mises à jour et temps humain. La bonne décision consiste à comparer ce coût au contrôle réellement nécessaire.
