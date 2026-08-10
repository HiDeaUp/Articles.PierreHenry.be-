+++
title = "Comment créer une clé USB bootable pour Linux Mint"
slug = "creer-une-cle-usb-bootable-linux-mint"
date = "2026-08-10T08:00:00+10:00"
draft = false
description = "Créer une clé USB bootable pour installer Linux Mint avec USB Image Writer ou balenaEtcher, puis démarrer le PC sur la clé."
summary = "La méthode actuelle pour écrire une image ISO de Linux Mint sur une clé USB sans copier le fichier comme un document ordinaire."
tags = ["linux", "linux mint", "clé usb", "image iso", "tutoriel"]
priority = true
priority_topics = ["tech"]
original_title = "Comment rendre bootable (exécutable) une image ISO sur une clé USB"
source_01script = "https://01script.com/rendre-bootable-executable-image-iso-sur-une-cle-usb/"
+++

Quand je veux installer Linux Mint ou réparer un ordinateur, je prépare une clé USB bootable. Copier le fichier ISO sur la clé ne suffit pas. Il faut écrire l’image disque avec un outil prévu pour cela.

Attention : l’opération efface le contenu de la clé USB. Vérifie deux fois le périphérique choisi avant de lancer l’écriture.

## Télécharger et vérifier l’image ISO

Télécharge Linux Mint depuis le [site officiel](https://linuxmint.com/download.php). Le site fournit aussi les sommes SHA256 et les instructions de vérification.

Cette étape évite d’installer une image incomplète ou modifiée. Sous Linux, tu peux calculer sa somme avec :

```bash
sha256sum linuxmint.iso
```

Compare le résultat avec la valeur publiée par Linux Mint.

## Créer la clé depuis Linux Mint

Linux Mint intègre déjà l’outil nécessaire :

1. Branche une clé USB d’au moins 4 Go.
2. Fais un clic droit sur le fichier ISO.
3. Choisis **Créer une clé USB bootable**.
4. Sélectionne la bonne clé.
5. Lance l’écriture et attends la fin complète de l’opération.

Tu peux aussi ouvrir **USB Image Writer** depuis le menu des applications. La [documentation d’installation de Linux Mint](https://linuxmint-installation-guide.readthedocs.io/en/latest/burn.html) décrit les deux méthodes.

## Depuis Windows ou macOS

La documentation de Linux Mint recommande [balenaEtcher](https://etcher.balena.io/) sur Windows, macOS et les autres distributions Linux :

1. Sélectionne l’image ISO.
2. Sélectionne la clé USB.
3. Clique sur **Flash**.

Etcher écrit l’image puis vérifie le résultat. Ne retire pas la clé avant la confirmation finale.

## Démarrer sur la clé USB

Redémarre l’ordinateur avec la clé branchée. Ouvre le menu de démarrage au début de l’allumage. La touche dépend du fabricant : `F12`, `F10`, `F2`, `Échap` ou `Suppr` sont fréquentes.

Choisis la clé USB dans la liste. Linux Mint démarre alors en session live. Tu peux tester le Wi-Fi, le son et l’affichage avant de lancer l’installation. Le [guide officiel explique aussi le démarrage en mode BIOS ou EFI](https://linuxmint-installation-guide.readthedocs.io/en/latest/boot.html).

Si la clé n’apparaît pas, essaie un autre port USB, recrée le support et vérifie les réglages UEFI. N’active ou ne désactive pas Secure Boot au hasard : commence par consulter la documentation du fabricant de ton ordinateur.

