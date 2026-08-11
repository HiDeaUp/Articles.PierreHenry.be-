+++
title = "Créer une API web en C++ avec Drogon"
slug = "creer-api-web-cpp-drogon"
date = "2012-01-28T13:14:00+01:00"
draft = false
description = "Créer une petite API HTTP en C++ avec Drogon, CMake et une route JSON, puis comprendre quand ce choix technique est pertinent."
summary = "Un premier serveur HTTP en C++ moderne avec Drogon, sans revenir aux anciens scripts CGI."
tags = ["c++", "api", "drogon", "backend", "développement web"]
priority = true
priority_topics = ["tech"]
original_title = "Développez votre site Web en C++, c'est possible !"
source_01script = "https://01script.com/developpement-web-en-c-plus-plus/"
+++

Oui, on peut créer un service web en C++. Je ne choisirais pas ce langage pour chaque site, mais il a du sens lorsqu’une équipe connaît déjà C++, vise une faible latence ou veut partager du code avec un autre composant natif.

Les anciens exemples CGI ne sont plus une bonne introduction. Un framework actuel gère le routage, HTTP, JSON, TLS, les WebSockets et l’accès aux bases de données.

## Pourquoi Drogon

[Drogon](https://github.com/drogonframework/drogon) est un framework HTTP en C++17 et C++20. Il fonctionne sur Linux, macOS et Windows. Il fournit des entrées-sorties non bloquantes, des routes, des filtres, des sessions, du JSON et un ORM.

Pour un petit service, on peut enregistrer une route directement dans `main`.

## Un premier endpoint JSON

Crée un fichier `main.cc` :

```cpp
#include <drogon/drogon.h>

int main()
{
    drogon::app().registerHandler(
        "/api/health",
        [](const drogon::HttpRequestPtr&,
           std::function<void(const drogon::HttpResponsePtr&)>&& callback) {
            Json::Value body;
            body["status"] = "ok";
            callback(drogon::HttpResponse::newHttpJsonResponse(body));
        },
        {drogon::Get}
    );

    drogon::app()
        .addListener("127.0.0.1", 8080)
        .run();
}
```

Ajoute `CMakeLists.txt` :

```cmake
cmake_minimum_required(VERSION 3.16)
project(hello_drogon LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Drogon CONFIG REQUIRED)

add_executable(hello_drogon main.cc)
target_link_libraries(hello_drogon PRIVATE Drogon::Drogon)
```

Compile et lance :

```bash
cmake -S . -B build
cmake --build build
./build/hello_drogon
```

Teste la route :

```bash
curl http://127.0.0.1:8080/api/health
```

La réponse doit contenir :

```json
{"status":"ok"}
```

## Préparer le passage en production

Le gestionnaire déclaré dans `main` convient à ce prototype. Quand l’API grandit, je déplace les routes dans des contrôleurs et je sépare le transport HTTP de la logique métier.

Je vérifie aussi cinq points avant une mise en production :

1. Les entrées JSON sont validées et les erreurs suivent un format constant.
2. La taille des requêtes et les délais d’attente sont limités.
3. Aucun appel bloquant ne ralentit les gestionnaires asynchrones.
4. Les journaux sont structurés et les métriques couvrent les erreurs et la latence.
5. Le service ne tourne pas avec les droits administrateur et son exposition TLS est maîtrisée.

## Quand je choisirais un autre langage

C++ demande une chaîne de compilation, une gestion attentive des dépendances et une bonne maîtrise des erreurs mémoire. Pour un produit classique avec beaucoup de formulaires et peu de calcul, PHP, Python, Go ou TypeScript permet souvent d’avancer plus vite.

Je garde C++ pour les services où ses contraintes apportent une valeur réelle. Le langage n’est pas un argument commercial. La fiabilité de l’API, ses tests, son suivi et sa facilité de maintenance comptent davantage.
