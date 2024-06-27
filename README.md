# Query-Boost

Query-Boost utilise l'API GPT pour générer des requêtes SQL cohérentes et les exécuter sur une base de données MySQL.

## Fonctionnalités

- Connexion sécurisée à la base de données MySQL.
- Génération de requêtes SQL à partir de descriptions en langage naturel.
- Exécution et validation des requêtes SQL générées.

## Prérequis

- Python 3.x
- MySQL Server
- Clé API OpenAI

## Installation

1. Clonez ce dépôt :

    ```bash
    git clone https://github.com/BenjiRenard/Query-Boost.git
    cd Query-Boost
    ```

2. Créez un fichier `.env` dans le répertoire du projet et ajoutez vos configurations :

    ```env
    OPENAI_API_KEY=your_openai_api_key
    MYSQL_USER=your_mysql_username
    MYSQL_PASSWORD=your_mysql_password
    MYSQL_HOST=your_mysql_host
    MYSQL_DATABASE=your_mysql_database
    ```

3. Installez les dépendances :

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

1. Lancez le script principal :

    ```bash
    Query-Boost.py
    ```

2. Entrez la description de la requête SQL souhaitée lorsqu'elle est demandée.

## Exemple

```plaintext
Veuillez décrire la requête SQL que vous souhaitez effectuer :
Récupérer les 10 premières lignes de la table utilisateurs.

Requête SQL générée : SELECT * FROM users LIMIT 10;
Requête exécutée avec succès

---------------------------------------------------------------------------------------------------------
Vérification

Pour vérifier que tout fonctionne correctement, suivez ces étapes :

1. Installez les dépendances nécessaires avec `pip install mysql-connector-python openai python-dotenv`.
2. Assurez-vous que le fichier `.env` est correctement configuré.
3. Exécutez le script `main.py` et entrez une description de la requête SQL lorsque vous y êtes invité.
