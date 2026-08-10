+++
title = "Comment changer le système lancé par défaut dans GRUB"
slug = "changer-systeme-par-defaut-grub"
date = "2026-08-10T08:30:00+10:00"
draft = false
description = "Changer l’entrée de démarrage par défaut dans GRUB depuis /etc/default/grub, sans modifier directement le fichier grub.cfg généré."
summary = "La méthode actuelle pour choisir Linux ou Windows par défaut dans le menu GRUB."
tags = ["linux", "grub", "dual boot", "démarrage", "tutoriel"]
priority = true
priority_topics = ["tech"]
original_title = "Comment changer l'ordre du boot avec GRUB"
source_01script = "https://01script.com/modifier-lordre-du-boot-avec-grub/"
+++

Dans une configuration Linux et Windows, GRUB choisit une entrée après quelques secondes. Tu peux changer ce choix sans réorganiser tout le menu.

Mon ancien tutoriel proposait de modifier `/boot/grub/grub.cfg`. Ce fichier est généré automatiquement et peut être remplacé lors d’une mise à jour. La bonne configuration se trouve dans `/etc/default/grub`.

## Voir les entrées disponibles

Sur Ubuntu et Linux Mint, tu peux afficher les entrées principales avec :

```bash
grep "^menuentry" /boot/grub/grub.cfg
```

Les entrées commencent à zéro. La première vaut `0`, la suivante `1`.

La [documentation GNU GRUB](https://www.gnu.org/software/grub/manual/grub/html_node/Simple-configuration) autorise un numéro, un titre ou un identifiant. Un identifiant est plus stable qu’un titre traduit, mais un numéro reste pratique pour une configuration simple.

## Modifier la valeur par défaut

Ouvre le fichier :

```bash
sudo nano /etc/default/grub
```

Repère cette ligne :

```text
GRUB_DEFAULT=0
```

Pour choisir la deuxième entrée, utilise :

```text
GRUB_DEFAULT=1
```

Enregistre, puis régénère la configuration :

```bash
sudo update-grub
```

Redémarre pour vérifier.

## Choisir une entrée enregistrée

Si tu veux définir une entrée par son identifiant, utilise le mode enregistré :

```text
GRUB_DEFAULT=saved
```

Mets ensuite GRUB à jour et choisis l’entrée :

```bash
sudo update-grub
sudo grub-set-default 'identifiant-de-l-entree'
```

La commande `grub-set-default` est prévue par GRUB pour renseigner `saved_entry`. Tu peux consulter la [documentation de cette variable](https://www.gnu.org/software/grub/manual/grub/html_node/saved_005fentry.html).

## Une entrée dans un sous-menu

Les noyaux plus anciens se trouvent souvent dans **Advanced options**. GRUB accepte alors une notation avec `>` entre le sous-menu et l’entrée :

```text
GRUB_DEFAULT="Advanced options for Linux Mint>Linux Mint, with Linux 6.x"
```

Les titres peuvent changer après une mise à jour. Pour un besoin ponctuel, sélectionne simplement l’entrée dans le menu au démarrage. Pour une configuration durable, préfère un identifiant stable.

Avant toute modification, garde une copie de `/etc/default/grub`. Et surtout, ne modifie plus directement `grub.cfg` : la prochaine génération effacerait ton changement.

