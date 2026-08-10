+++
title = "Choisir un CMS Django : Wagtail ou django CMS"
slug = "choisir-cms-django-wagtail-django-cms"
date = "2026-08-10T09:10:00+10:00"
draft = false
description = "Comparer Wagtail et django CMS pour choisir un CMS Python actif, extensible et adapté à un projet construit avec Django."
summary = "Deux CMS Django encore maintenus, avec des approches différentes pour les modèles de contenu et l’édition des pages."
tags = ["django", "python", "wagtail", "django cms", "cms"]
priority = true
priority_topics = ["tech"]
original_title = "Liste des meilleurs CMS basé du framework Django"
source_01script = "https://01script.com/cms-base-framework-django-python/"
+++

Une liste de CMS vieillit vite. Plusieurs projets présents dans mon ancien article ont disparu ou ne correspondent pas vraiment à un CMS Django.

Je préfère retenir deux solutions actives avec une documentation claire : Wagtail et django CMS.

## Wagtail pour des modèles de contenu précis

[Wagtail](https://docs.wagtail.org/en/stable/getting_started/index.html) est un CMS open source construit sur Django. Il fournit la gestion des pages, des images, des documents, des workflows, des versions et de la publication planifiée.

Son intérêt vient de son intégration avec les modèles Django. Le développeur décrit la structure du contenu en Python, puis l’équipe éditoriale travaille dans une interface dédiée.

Je le choisirais pour un site éditorial, une documentation riche ou un projet où le contenu doit rester bien structuré.

Installation rapide :

```bash
python -m venv .venv
source .venv/bin/activate
pip install wagtail
wagtail start monsite
cd monsite
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Vérifie toujours la version de Python prise en charge par la version de Wagtail choisie.

## django CMS pour composer des pages

[django CMS](https://docs.django-cms.org/en/stable/) adopte une approche plus orientée vers la composition visuelle des pages et les plugins de contenu. Il peut créer un nouveau projet ou s’ajouter à une application Django existante.

La documentation actuelle propose :

```bash
python -m venv .venv
source .venv/bin/activate
pip install django-cms
djangocms monsite
```

Je le regarderais pour un site multilingue ou un projet où les responsables de contenu doivent composer les pages avec des blocs réutilisables.

## Comment décider

Je prépare une petite page réelle dans les deux outils, puis je compare :

1. la facilité d’édition pour la personne qui publie ;
2. la structure des modèles ;
3. les besoins multilingues ;
4. les permissions et le workflow ;
5. la maintenance des extensions nécessaires ;
6. le coût du déploiement et des mises à jour.

Le nombre de fonctionnalités sur une page d’accueil ne suffit pas. Le meilleur CMS est celui que l’équipe peut mettre à jour, tester et utiliser sans contourner son propre modèle de contenu.

