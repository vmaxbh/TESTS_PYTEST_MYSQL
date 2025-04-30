from database_config import get_db_connection

def test_mysql_connection():
    try:
        # Tenta estabelecer a conexão
        connection = get_db_connection()

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado ao MySQL versão {db_info}")

            # Testa uma query simples
            cursor = connection.cursor()
            cursor.execute("SELECT COUNT(*) FROM clientes")
            result = cursor.fetchone()
            if result is not None:
                print(f"Total de clientes no banco: {result[0]}")
            else:
                print("Nenhum resultado encontrado")

            cursor.close()
            connection.close()
            print("Conexão fechada com sucesso!")

    except Exception as e:
        print(f"Erro ao conectar ao MySQL: {e}")

if __name__ == "__main__":
    test_mysql_connection()
