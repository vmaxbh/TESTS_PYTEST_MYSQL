import pytest
import uuid
from mysql.connector.errors import DataError, IntegrityError, DatabaseError

@pytest.mark.usefixtures("cleanup_test_data")
class TestClientes:
    def test_inserir_cliente(self, db_connection, db_cursor):
        """Testa a inserção de um novo cliente"""
        cpf = f"{uuid.uuid4().int % 10**11:011d}"  # Gera CPF único
        email = f"test_{uuid.uuid4()}@test.com"  # Gera email único
        db_cursor.execute("""
            INSERT INTO clientes (nome, email, cpf)
            VALUES ('Test User', %s, %s)
        """, (email, cpf))
        db_connection.commit()

        db_cursor.execute("SELECT * FROM clientes WHERE email = %s", (email,))
        result = db_cursor.fetchone()
        assert result is not None, "Cliente não foi inserido corretamente"

    def test_atualizar_cliente(self, db_connection, db_cursor):
        """Testa a atualização de um cliente"""
        # Primeiro insere o cliente
        cpf = f"{uuid.uuid4().int % 10**11:011d}"  # Gera CPF único
        email = f"test_{uuid.uuid4()}@test.com"  # Gera email único
        db_cursor.execute("""
            INSERT INTO clientes (nome, email, cpf)
            VALUES ('Test User', %s, %s)
        """, (email, cpf))
        db_connection.commit()

        # Atualiza o nome
        db_cursor.execute("""
            UPDATE clientes
            SET nome = 'Updated Test User'
            WHERE email = %s
        """, (email,))
        db_connection.commit()

        # Verifica a atualização
        db_cursor.execute("SELECT nome FROM clientes WHERE email = %s", (email,))
        result = db_cursor.fetchone()
        assert result[0] == 'Updated Test User', "Update não funcionou corretamente"

    def test_deletar_cliente(self, db_connection, db_cursor):
        """Testa a deleção de um cliente"""
        # Primeiro insere o cliente
        cpf = f"{uuid.uuid4().int % 10**11:011d}"  # Gera CPF único
        email = f"test_{uuid.uuid4()}@test.com"  # Gera email único
        db_cursor.execute("""
            INSERT INTO clientes (nome, email, cpf)
            VALUES ('Test User', %s, %s)
        """, (email, cpf))
        db_connection.commit()

        # Deleta o cliente
        db_cursor.execute("DELETE FROM clientes WHERE email = %s", (email,))
        db_connection.commit()

        # Verifica a deleção
        db_cursor.execute("SELECT * FROM clientes WHERE email = %s", (email,))
        result = db_cursor.fetchone()
        assert result is None, "Delete não funcionou corretamente"

    def test_cpf_duplicado(self, db_connection, db_cursor):
        """Testa a restrição de CPF único"""
        cpf = f"{uuid.uuid4().int % 10**11:011d}"  # Gera CPF único

        # Insere primeiro cliente com email único
        email1 = f"test1_{uuid.uuid4()}@test.com"
        db_cursor.execute("""
            INSERT INTO clientes (nome, email, cpf)
            VALUES ('Test User 1', %s, %s)
        """, (email1, cpf))
        db_connection.commit()

        # Tenta inserir segundo cliente com mesmo CPF mas email diferente
        email2 = f"test2_{uuid.uuid4()}@test.com"
        with pytest.raises(IntegrityError):
            db_cursor.execute("""
                INSERT INTO clientes (nome, email, cpf)
                VALUES ('Test User 2', %s, %s)
            """, (email2, cpf))
            db_connection.commit()

    def test_email_formato_invalido(self, db_connection, db_cursor):
        """Testa a validação do formato de email"""
        cpf = f"{uuid.uuid4().int % 10**11:011d}"  # Gera CPF único
        email_invalido = 'invalid_email'

        with pytest.raises((IntegrityError, DatabaseError)):
            db_cursor.execute("""
                INSERT INTO clientes (nome, email, cpf)
                VALUES ('Test User', %s, %s)
            """, (email_invalido, cpf))
            db_connection.commit()

    def test_email_vazio(self, db_connection, db_cursor):
        """Testa a validação de email vazio"""
        cpf = f"{uuid.uuid4().int % 10**11:011d}"  # Gera CPF único

        with pytest.raises((IntegrityError, DatabaseError)):
            db_cursor.execute("""
                INSERT INTO clientes (nome, email, cpf)
                VALUES ('Test User', '', %s)
            """, (cpf,))
            db_connection.commit()

