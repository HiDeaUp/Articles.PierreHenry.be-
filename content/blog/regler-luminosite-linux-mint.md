+++
title = "Comment régler la luminosité sous Linux Mint"
slug = "regler-luminosite-linux-mint"
date = "2026-08-10T08:10:00+10:00"
draft = false
description = "Régler la luminosité sous Linux Mint avec les commandes brightnessctl, puis diagnostiquer un pilote de rétroéclairage mal détecté."
summary = "Des touches du clavier aux paramètres du noyau, voici l’ordre de diagnostic lorsque la luminosité ne répond plus sous Linux Mint."
tags = ["linux mint", "linux", "luminosité", "brightnessctl", "dépannage"]
priority = true
priority_topics = ["tech"]
original_title = "Comment ajuster la luminosité de l'écran avec Linux Mint"
source_01script = "https://01script.com/ajuster-luminosite-ecran-linux-mint/"
+++

Sur une installation récente de Linux Mint, les touches de luminosité et le curseur des paramètres fonctionnent normalement sans configuration. Si rien ne bouge, je commence par vérifier ce que le noyau détecte avant de modifier GRUB.

## Tester avec brightnessctl

Installe l’outil :

```bash
sudo apt update
sudo apt install brightnessctl
```

Liste les périphériques disponibles :

```bash
brightnessctl --list
```

Affiche les informations du premier périphérique de rétroéclairage :

```bash
brightnessctl info
```

Règle ensuite l’écran à 50 % :

```bash
brightnessctl set 50%
```

Pour augmenter ou réduire la valeur de 10 % :

```bash
brightnessctl set +10%
brightnessctl set 10%-
```

Le [projet brightnessctl](https://github.com/Hummer12007/brightnessctl) documente ces commandes et la gestion des permissions. L’outil est disponible dans Debian, Ubuntu et leurs dérivés.

## Vérifier l’interface du noyau

Linux expose les contrôles de rétroéclairage dans `/sys/class/backlight`. Liste-les :

```bash
ls -1 /sys/class/backlight
```

Si le dossier est vide, le noyau n’a probablement pas chargé le bon pilote. S’il contient plusieurs périphériques, `brightnessctl --list` t’aide à choisir le bon avec l’option `--device`.

La [documentation du noyau Linux](https://docs.kernel.org/gpu/backlight.html) décrit les valeurs `brightness`, `actual_brightness` et `max_brightness` fournies par chaque pilote.

## Tester un paramètre de démarrage

Cette étape vient en dernier, car le bon paramètre dépend du matériel.

Ouvre le fichier de configuration :

```bash
sudo nano /etc/default/grub
```

Dans `GRUB_CMDLINE_LINUX_DEFAULT`, ajoute un seul paramètre à tester. Les valeurs reconnues par le noyau sont notamment :

```text
acpi_backlight=native
acpi_backlight=vendor
acpi_backlight=video
```

Commence généralement par `native`, redémarre et teste. Si cela ne change rien, retire cette valeur avant d’en essayer une autre. La [liste officielle des paramètres du noyau](https://www.kernel.org/doc/html/latest/admin-guide/kernel-parameters.html?highlight=acpi_backlight) explique leur rôle.

Après chaque modification :

```bash
sudo update-grub
sudo reboot
```

Ne cumule pas plusieurs valeurs `acpi_backlight`. Garde aussi une copie de la ligne d’origine pour revenir en arrière.

## Et pour un écran externe ?

Le rétroéclairage d’un écran externe n’est souvent pas exposé comme celui d’un ordinateur portable. Les boutons de l’écran restent la méthode la plus fiable. Certains écrans prennent en charge DDC/CI, mais cela dépend du modèle, du câble et du pilote graphique.

Je préfère avancer dans cet ordre : interface graphique, `brightnessctl`, détection du noyau, puis GRUB. Cela évite de garder une ancienne astuce de démarrage alors qu’un outil simple suffisait.

