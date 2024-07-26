# Query-Boost

Query-Boost est un outil puissant qui permet de générer et d'exécuter des requêtes SQL à partir de descriptions en langage naturel. En utilisant l'API GPT d'OpenAI, Query-Boost simplifie l'interaction avec les bases de données MySQL, rendant SQL accessible à tous.

## Objectif du Projet

L'objectif principal de Query-Boost est de rendre SQL accessible à tous, même à ceux qui n'ont pas forcément de connaissances approfondies en requêtage.

## Fonctionnalités

- **Génération Automatique de Requêtes SQL** : Décrivez ce que vous souhaitez faire en langage naturel et Query-Boost se charge du reste.
- **Connexion Sécurisée à MySQL** : Connectez-vous facilement et en toute sécurité à votre base de données.
- **Exécution et Validation des Requêtes** : Query-Boost exécute les requêtes générées et vérifie leur succès.
- **Visualisation des Données Avant et Après** : Affichez les données de la table avant et après l'exécution de la requête pour une meilleure transparence.

## Prérequis

- Python 3.x
- [OpenAI Python Client Library](https://beta.openai.com/docs/libraries)
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- [pandas](https://pypi.org/project/pandas/)
- [tkinter](https://docs.python.org/3/library/tkinter.html)

## Installation

1. Clonez le dépôt GitHub :
    ```bash
    git clone https://github.com/BenjiRenard/Query-Boost.git
    cd Query-Boost
    ```

2. Installez les dépendances :
    ```bash
    pip install openai mysql-connector-python python-dotenv pandas
    ```

3. Configurez votre clé API OpenAI dans un fichier `.env` (optionnel mais recommandé) :
    ```bash
    echo "OPENAI_API_KEY=your_openai_api_key" > .env
    ```

## Utilisation

1. Exécutez le script Python :
    ```bash
    python main.py
    ```

2. Entrez les informations de connexion MySQL via l'interface utilisateur.

3. Décrivez la requête SQL en langage naturel et cliquez sur "Générer et Exécuter".

4. Visualisez les données de la table avant et après l'exécution de la requête dans l'interface.

## Exemple

```plaintext
Veuillez décrire la requête SQL que vous souhaitez effectuer :
Récupérez les 10 premières lignes de la table utilisateurs.

Requête SQL générée : SELECT * FROM users LIMIT 10;
Requête exécutée avec succès.
