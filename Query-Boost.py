import tkinter as tk
from tkinter import messagebox, ttk
import openai
import mysql.connector
from dotenv import load_dotenv
import os
import pandas as pd

# Charge les variables d'environnement depuis un fichier .env (si disponible)
load_dotenv()

# Configure OpenAI avec possibilité de définir directement la clé API
openai.api_key = os.getenv('OPENAI_API_KEY', 'votre_cle_api_openai_ici')

# Connexion MySQL
def create_connection(user, password, host, database):
    try:
        connection = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            database=database,
            port=3306,
            use_pure=True
        )
        if connection.is_connected():
            messagebox.showinfo("Connexion", "Connexion à la base de données MySQL réussie")
        return connection
    except mysql.connector.Error as e:
        messagebox.showerror("Erreur", f"Erreur de connexion à MySQL: {e}")
        return None

# Génère la requête SQL à partir du prompt
def generate_sql_query(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            max_tokens=150
        )
        query = response.choices[0].text.strip()
        return query
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la génération de la requête SQL: {e}")
        return None

# Exécute la requête
def execute_query():
    user = user_entry.get()
    password = password_entry.get()
    host = host_entry.get()
    database = database_entry.get()

    prompt = Boutade.get()
    sql_query = generate_sql_query(prompt)
    if sql_query:
        query_text.set(sql_query)
        connection = create_connection(user, password, host, database)
        if connection:
            cursor = connection.cursor()
            try:
                # Visualise la table avant l'exécution de la requête
                cursor.execute("SELECT * FROM table_name LIMIT 10")
                before_results = cursor.fetchall()
                display_table(before_tree, before_results)

                cursor.execute(sql_query)
                connection.commit()

                # Visualise la table après l'exécution de la requête
                cursor.execute("SELECT * FROM table_name LIMIT 10")
                after_results = cursor.fetchall()
                display_table(after_tree, after_results)

                messagebox.showinfo("Succès", "Requête exécutée avec succès")
            except mysql.connector.Error as e:
                messagebox.showerror("Erreur", f"Erreur lors de l'exécution de la requête: {e}")
            connection.close()

# Affiche les résultats dans un Treeview
def display_table(tree, data):
    # Supprimer les anciennes données
    for i in tree.get_children():
        tree.delete(i)
    # Ajouter les nouvelles données
    for row in data:
        tree.insert("", "end", values=row)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Query-Boost")

# Widgets de l'interface pour les détails de connexion MySQL
tk.Label(root, text="Utilisateur MySQL:").pack(pady=5)
user_entry = tk.Entry(root, width=50)
user_entry.pack(pady=5)

tk.Label(root, text="Mot de passe MySQL:").pack(pady=5)
password_entry = tk.Entry(root, show='*', width=50)
password_entry.pack(pady=5)

tk.Label(root, text="Hôte MySQL:").pack(pady=5)
host_entry = tk.Entry(root, width=50)
host_entry.pack(pady=5)

tk.Label(root, text="Base de données MySQL:").pack(pady=5)
database_entry = tk.Entry(root, width=50)
database_entry.pack(pady=5)

# Widgets de l'interface pour la génération de requêtes SQL
tk.Label(root, text="Description de la requête SQL:").pack(pady=5)
Boutade = tk.Entry(root, width=50)
Boutade.pack(pady=5)

tk.Button(root, text="Générer et Exécuter", command=execute_query).pack(pady=10)

tk.Label(root, text="Requête SQL générée:").pack(pady=5)
query_text = tk.StringVar()
tk.Entry(root, textvariable=query_text, width=50, state='readonly').pack(pady=5)

# Treeview pour afficher les résultats avant l'exécution de la requête
tk.Label(root, text="Table avant l'exécution de la requête:").pack(pady=5)
before_tree = ttk.Treeview(root, columns=("Col1", "Col2", "Col3"), show='headings')
before_tree.heading("Col1", text="Colonne 1")
before_tree.heading("Col2", text="Colonne 2")
before_tree.heading("Col3", text="Colonne 3")
before_tree.pack(pady=5)

# Treeview pour afficher les résultats après l'exécution de la requête
tk.Label(root, text="Table après l'exécution de la requête:").pack(pady=5)
after_tree = ttk.Treeview(root, columns=("Col1", "Col2", "Col3"), show='headings')
after_tree.heading("Col1", text="Colonne 1")
after_tree.heading("Col2", text="Colonne 2")
after_tree.heading("Col3", text="Colonne 3")
after_tree.pack(pady=5)

# Lancement de l'application
root.mainloop()
