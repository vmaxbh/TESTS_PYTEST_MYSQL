import os
import sys
import pytest
from dotenv import load_dotenv
from pathlib import Path

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Adiciona o diretório src ao PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from src.database_config import get_db_connection

@pytest.fixture(scope="session")
def db_connection():
    """
    Fixture que fornece uma conexão com o banco de dados para todos os testes
    """
    connection = get_db_connection()
    yield connection
    connection.close()

@pytest.fixture(scope="function")
def db_cursor(db_connection):
    """
    Fixture que fornece um cursor limpo para cada teste
    """
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()

@pytest.fixture(autouse=True)
def cleanup_test_data(db_connection):
    """
    Fixture para limpar dados de teste antes e depois de cada teste
    """
    cursor = db_connection.cursor()
    try:
        # Limpa dados antes do teste
        cursor.execute("DELETE FROM itens_pedido WHERE pedido_id IN (SELECT id FROM pedidos WHERE cliente_id IN (SELECT id FROM clientes WHERE email LIKE 'test%@test.com'))")
        cursor.execute("DELETE FROM pedidos WHERE cliente_id IN (SELECT id FROM clientes WHERE email LIKE 'test%@test.com')")
        cursor.execute("DELETE FROM clientes WHERE email LIKE 'test%@test.com'")
        db_connection.commit()

        yield

        # Limpa dados após o teste
        cursor.execute("DELETE FROM itens_pedido WHERE pedido_id IN (SELECT id FROM pedidos WHERE cliente_id IN (SELECT id FROM clientes WHERE email LIKE 'test%@test.com'))")
        cursor.execute("DELETE FROM pedidos WHERE cliente_id IN (SELECT id FROM clientes WHERE email LIKE 'test%@test.com')")
        cursor.execute("DELETE FROM clientes WHERE email LIKE 'test%@test.com'")
        db_connection.commit()
    finally:
        cursor.close()
