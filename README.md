
# Query-Boost


**Query-Boost** est une solution innovante permettant de rendre l'utilisation de SQL plus accessible grâce à l'intelligence artificielle. L'outil génère des requêtes SQL à partir de descriptions en langage naturel et les exécute sur des bases de données MySQL. Il s'adresse aussi bien aux développeurs novices qu'aux professionnels cherchant à automatiser leurs requêtes.

## Fonctionnalités

- **Génération Automatique de Requêtes SQL** : Décrivez simplement ce que vous voulez faire, et Query-Boost génère automatiquement la requête SQL correspondante.
- **Connexion MySQL Distante** : Pas besoin d'avoir MySQL installé localement. Query-Boost se connecte directement à des bases de données MySQL distantes.
- **Visualisation des Données** : Affichage des données avant et après l'exécution des requêtes pour une meilleure transparence.
- **Graphiques Dynamiques** : Génération de graphiques pour visualiser les données en un clic.

---

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les éléments suivants :

- **Python 3.x**
- Bibliothèques Python :
  - `openai`
  - `mysql-connector-python`
  - `pandas`
  - `matplotlib`
  - `tkinter`
- **Clé API OpenAI**

---

## Installation

1. **Clonez ce dépôt** :
   ```bash
   git clone https://github.com/BenjiRenard/Query-Boost.git
   ```

2. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurez votre clé API OpenAI** :
   - Créez un fichier `.env` à la racine du projet.
   - Ajoutez votre clé API OpenAI dans ce fichier :
     ```
     OPENAI_API_KEY=votre_cle_api_openai
     ```

---

## Utilisation

1. **Lancez l'application** :
   ```bash
   python main.py
   ```

2. **Connectez-vous à votre base de données MySQL** :
   - Entrez les informations de connexion dans l'interface (Utilisateur, Mot de passe, Hôte, Base de données).

3. **Générez et exécutez des requêtes SQL** :
   - Décrivez la requête SQL en langage naturel (ex : *"Sélectionner les 10 premières lignes de la table `users`"*).
   - Cliquez sur **Générer et Exécuter** pour obtenir la requête SQL correspondante et l'exécuter sur votre base de données.

4. **Visualisation des Données** :
   - Les résultats avant et après l'exécution de la requête sont affichés dans des tableaux.
   - Utilisez l'option **Visualiser Graphique** pour générer des graphiques basés sur vos données.

---

## Exemple d'Utilisation

### Exemple 1 : Génération Automatique de Requête

#### Description
```plaintext
Sélectionne les 10 premières lignes de la table `users`.
```

#### Requête SQL Générée
```sql
SELECT * FROM users LIMIT 10;
```

---

## Graphiques

Query-Boost vous permet de générer des graphiques à partir des données obtenues par vos requêtes SQL. Cela est particulièrement utile pour visualiser des tendances ou pour analyser des données en profondeur.

---

## Développement Futur

- **Optimisation des Performances** : Réduire les temps de latence lors de l'exécution des requêtes.
- **Sécurité Renforcée** : Intégrer des mesures de sécurité supplémentaires pour une utilisation en entreprise.
- **Interface Utilisateur Améliorée** : Créer une interface encore plus intuitive et conviviale.
