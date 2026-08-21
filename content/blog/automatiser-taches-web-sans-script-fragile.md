+++
title = "Automatiser des tâches web sans créer un script fragile"
slug = "automatiser-taches-web-sans-script-fragile"
date = "2015-12-22T09:20:00+01:00"
draft = false
description = "Choisir entre une API, Playwright, Selenium et une tâche planifiée pour automatiser un travail web répétitif sans produire un script fragile."
summary = "Une méthode actuelle pour automatiser les tâches web utiles, avec des contrôles, des journaux et des sélecteurs qui résistent aux changements."
tags = ["automatisation", "playwright", "selenium", "tests", "github actions", "développement web"]
priority = true
priority_topics = ["tech", "productivity"]
original_title = "Comment automatiser ses tâches Web"
source_01script = "https://01script.com/automatiser-taches-web/"
+++

Quand j’ai écrit la première version de cet article, je présentais une extension Firefox basée sur Selenium IDE. L’idée reste valable : une tâche répétée dans un navigateur mérite parfois d’être automatisée. L’outil et la méthode ont changé.

Je commence maintenant par une question simple : cette action doit-elle vraiment passer par un navigateur ?

## Chercher une API avant de piloter une page

Une API est généralement plus stable qu’une suite de clics. Si le service permet d’exporter un rapport, créer une ressource ou mettre à jour un enregistrement par API, je choisis cette voie.

J’utilise le navigateur lorsque je teste le parcours réel d’un utilisateur ou quand aucune interface programmée n’existe. Je vérifie aussi les conditions d’utilisation du service. Automatiser la création de faux comptes, l’envoi de messages non sollicités ou le contournement d’une limite reste une mauvaise utilisation, même si le script fonctionne.

## Choisir Playwright ou Selenium

Pour un nouveau projet JavaScript ou TypeScript, [Playwright](https://playwright.dev/docs/intro) constitue souvent un bon point de départ. Ses locators peuvent cibler un rôle, un libellé ou un texte visible. Ses actions attendent aussi que l’élément soit prêt avant de cliquer.

[Selenium WebDriver](https://www.selenium.dev/documentation/webdriver/) reste pertinent pour une base existante, plusieurs langages ou une infrastructure Selenium Grid déjà en place. Selenium IDE existe encore pour enregistrer un premier scénario, mais je transforme ensuite ce scénario en code lisible et versionné.

## Écrire un scénario qui résiste mieux

Voici un test Playwright volontairement court pour un environnement de test :

```ts
import { test, expect } from "@playwright/test";

test("exporte un rapport", async ({ page }) => {
  await page.goto(process.env.APP_URL!);

  await page.getByLabel("Adresse e-mail").fill(process.env.TEST_EMAIL!);
  await page.getByLabel("Mot de passe").fill(process.env.TEST_PASSWORD!);
  await page.getByRole("button", { name: "Se connecter" }).click();

  await expect(page.getByRole("heading", { name: "Rapports" })).toBeVisible();

  const download = page.waitForEvent("download");
  await page.getByRole("button", { name: "Exporter" }).click();
  await download;
});
```

Je n’utilise pas de position comme « le troisième bouton ». Je cible ce que l’utilisateur voit. La [documentation des locators Playwright](https://playwright.dev/docs/locators) recommande aussi de privilégier les rôles et les libellés.

Les identifiants restent dans des secrets, jamais dans le dépôt. Le compte de test possède uniquement les droits nécessaires.

## Planifier sans perdre le contrôle

Un test peut être lancé à chaque changement dans la CI. Une tâche métier peut suivre un calendrier, à condition qu’elle soit idempotente et qu’un nouvel essai ne crée pas de doublon.

[GitHub Actions](https://docs.github.com/en/actions/concepts/workflows-and-actions/workflows) peut exécuter un workflow sur événement, manuellement ou selon un horaire. Pour une tâche importante, je garde un déclenchement manuel et j’enregistre le résultat : date, entrée traitée, sortie produite et erreur éventuelle.

## Les contrôles qui comptent

Avant de laisser une automatisation tourner seule, je vérifie :

1. qu’elle peut être relancée sans conséquence indésirable ;
2. qu’elle échoue clairement si la page ou les données ont changé ;
3. qu’elle limite ses droits et protège ses secrets ;
4. qu’elle produit des journaux utiles ;
5. qu’une personne sait comment l’arrêter et la reprendre.

Le temps gagné vient rarement du premier enregistrement de clics. Il vient d’un petit script compréhensible, surveillé et assez fiable pour ne pas réclamer une réparation chaque semaine.
