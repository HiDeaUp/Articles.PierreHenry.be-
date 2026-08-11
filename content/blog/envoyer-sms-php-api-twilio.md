+++
title = "Comment envoyer un SMS avec PHP via une API"
slug = "envoyer-sms-php-api-twilio"
date = "2015-02-04T10:12:00+01:00"
draft = false
description = "Envoyer un SMS avec PHP et l’API Twilio, stocker les identifiants dans l’environnement et respecter le consentement du destinataire."
summary = "Un exemple PHP actuel pour envoyer un SMS avec une API, sans promettre un service gratuit ni exposer les identifiants."
tags = ["php", "sms", "api", "twilio", "sécurité"]
priority = true
priority_topics = ["tech"]
original_title = "Envoyer des SMS avec PHP : La solution 100% gratuite"
source_01script = "https://01script.com/envoyer-des-sms-avec-php/"
+++

Envoyer un SMS depuis PHP est simple. Le faire proprement demande un fournisseur, un numéro autorisé, une gestion des erreurs et le consentement du destinataire.

Mon ancien article parlait d’une méthode gratuite. Ce n’est plus une promesse sérieuse. Les passerelles changent, les opérateurs filtrent les abus et les envois réels ont un coût.

Voici un exemple avec Twilio. Le principe reste proche chez d’autres fournisseurs.

## Installer le SDK PHP

Dans ton projet, installe la bibliothèque officielle avec Composer :

```bash
composer require twilio/sdk
```

Crée un compte, choisis un numéro compatible avec le pays visé et termine les éventuelles vérifications demandées. Les obligations varient selon le pays et le type de numéro.

## Garder les secrets hors du code

Définis les identifiants dans l’environnement :

```bash
export TWILIO_ACCOUNT_SID='ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
export TWILIO_AUTH_TOKEN='ton_secret'
export TWILIO_FROM_NUMBER='+15017122661'
export TWILIO_TO_NUMBER='+32470000000'
```

N’ajoute jamais ces valeurs dans Git. En production, utilise de préférence une clé API avec des droits limités. La [documentation Twilio](https://www.twilio.com/docs/messaging/tutorials/how-to-send-sms-messages) recommande aussi de protéger les identifiants et de terminer les enregistrements requis.

## Envoyer le message

```php
<?php

declare(strict_types=1);

require __DIR__ . '/vendor/autoload.php';

use Twilio\Rest\Client;

$sid = getenv('TWILIO_ACCOUNT_SID');
$token = getenv('TWILIO_AUTH_TOKEN');
$from = getenv('TWILIO_FROM_NUMBER');
$to = getenv('TWILIO_TO_NUMBER');

if (!$sid || !$token || !$from || !$to) {
    throw new RuntimeException('La configuration Twilio est incomplète.');
}

$client = new Client($sid, $token);

$message = $client->messages->create(
    $to,
    [
        'from' => $from,
        'body' => 'Votre rendez-vous est confirmé pour demain à 10 h.',
    ]
);

printf("Message créé : %s\n", $message->sid);
```

Les numéros doivent utiliser le format international E.164, avec le signe `+` et l’indicatif du pays.

## Prévoir les échecs

La création d’un message ne garantit pas sa livraison. Enregistre son identifiant et suis son statut avec les callbacks prévus par le fournisseur. [Vérifie la signature de chaque callback](https://www.twilio.com/docs/usage/webhooks/webhooks-security) avant de lui faire confiance. Prévois aussi les numéros invalides, les refus de l’opérateur et les limites de débit.

Pour une application réelle, place l’envoi dans une file de tâches. Une requête web ne doit pas rester bloquée pendant un appel externe. Associe aussi chaque demande à un identifiant interne afin qu’une nouvelle tentative ne crée pas un second message sans contrôle.

## Respecter le destinataire

N’envoie pas de publicité à une personne qui n’a rien demandé. Conserve la preuve du consentement, annonce clairement l’expéditeur et propose une méthode de désinscription. Pour un message transactionnel, limite le contenu à l’information attendue.

Le code est la partie facile. La qualité d’un système SMS repose surtout sur le consentement, la sécurité des secrets et le suivi de livraison.
