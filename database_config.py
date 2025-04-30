import os
from dotenv import load_dotenv
import mysql.connector

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

def get_db_connection():
    """
    Cria e retorna uma conexão com o banco de dados MySQL
    """
    try:
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME'),
            port=os.getenv('DB_PORT')
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        raise
