+++
title = "Réparer un système Linux qui ne démarre plus avec fsck"
slug = "reparer-systeme-linux-fsck"
date = "2026-08-10T08:05:00+10:00"
draft = false
description = "Diagnostiquer puis réparer un système de fichiers ext4 depuis une session live Linux, sans lancer fsck sur une partition montée."
summary = "Une procédure prudente pour utiliser fsck lorsqu’une partition Linux ext4 empêche le démarrage."
tags = ["linux", "fsck", "ext4", "dépannage", "système de fichiers"]
priority = true
priority_topics = ["tech"]
original_title = "Comment rendre son système d'exploitation à nouveau bootable"
source_01script = "https://01script.com/rendre-son-os-bottable/"
+++

Une mise à jour peut parfois révéler un problème de disque ou de système de fichiers. Linux s’arrête alors dans un mode de secours, affiche une erreur `initramfs` ou refuse de monter la partition principale.

J’avais publié une commande rapide il y a plusieurs années. Elle était trop générale. `fsck` peut corriger un système de fichiers, mais une mauvaise partition ou un disque défaillant peut aggraver la situation.

Cette procédure concerne surtout les partitions `ext4`. Elle ne remplace pas une sauvegarde.

## Lire l’erreur avant d’agir

Une erreur de démarrage ne vient pas toujours du système de fichiers. Elle peut aussi venir de GRUB, d’un noyau, d’un volume chiffré, de LVM ou du matériel.

Si le message cite un UUID, une partition ou une erreur `EXT4-fs`, note-le. Si le disque fait du bruit, disparaît du BIOS ou remonte des erreurs d’entrée-sortie, arrête les écritures et pense d’abord à récupérer les données.

## Démarrer depuis une session live

Crée une clé USB Linux Mint, démarre dessus et choisis la session live. Ouvre ensuite un terminal.

Liste les disques, leurs systèmes de fichiers et leurs points de montage :

```bash
lsblk -f
```

Tu peux compléter avec :

```bash
sudo blkid
```

Repère la partition Linux concernée. Sur un PC récent, son nom ressemble souvent à `/dev/nvme0n1p2`. Sur un autre disque, ce sera peut-être `/dev/sda2`.

Ne devine pas le nom de la partition. Vérifie son type, sa taille et son UUID.

## Vérifier que la partition est démontée

La page de manuel de [`fsck`](https://man7.org/linux/man-pages/man8/fsck.8.html) rappelle qu’il ne faut pas vérifier un système de fichiers monté en écriture.

Contrôle le point de montage avec `lsblk -f`. Si la partition est montée par la session live, démonte-la :

```bash
sudo umount /dev/nvme0n1p2
```

Remplace le nom par celui de ta partition.

## Lancer la vérification

Pour une partition `ext4`, lance :

```bash
sudo fsck -f /dev/nvme0n1p2
```

Lis chaque question avant de confirmer une correction. Je préfère cette approche interactive à l’option `-y`, qui accepte tout sans contrôle.

Une fois la vérification terminée, redémarre :

```bash
sudo reboot
```

Retire la clé USB lorsque l’ordinateur s’éteint.

## Les cas où il faut s’arrêter

N’utilise pas cette commande telle quelle sur XFS, Btrfs, ZFS ou une partition chiffrée. Chaque technologie possède ses propres outils. Ne lance pas non plus `fsck` sur le disque entier, comme `/dev/sda`, si le système de fichiers se trouve sur `/dev/sda2`.

Si les erreurs reviennent, consulte les données SMART du disque et sauvegarde ce qui reste accessible. `fsck` répare une structure logique. Il ne répare pas un SSD ou un disque dur en fin de vie.

