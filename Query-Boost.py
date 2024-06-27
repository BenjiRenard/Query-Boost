import os
import openai
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

mysql_config = {
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DATABASE'),
    'port': 3306,
    'use_pure': True
}

def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**mysql_config)
        if connection.is_connected():
            print("Connexion à la base de données MySQL réussie")
        return connection
    except Error as e:
        print(f"Erreur de connexion à MySQL: {e}")
        return None

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
        print(f"Erreur lors de la génération de la requête SQL: {e}")
        return None

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Requête exécutée avec succès")
    except Error as e:
        print(f"Erreur lors de l'exécution de la requête: {e}")

def main():
    connection = create_connection()
    if connection is None:
        return

    prompt = input("Veuillez décrire la requête SQL que vous souhaitez effectuer: ")
    sql_query = generate_sql_query(prompt)
    if sql_query:
        print(f"Requête SQL générée : {sql_query}")
        execute_query(connection, sql_query)
    connection.close()

if __name__ == "__main__":
    main()
