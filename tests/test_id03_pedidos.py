import pytest
import uuid

class TestPedidos:
    def test_integridade_referencial(self, db_connection, db_cursor):
        """Testa a integridade referencial entre pedidos e clientes"""
        with pytest.raises(Exception):
            db_cursor.execute("""
                INSERT INTO pedidos (cliente_id, valor_total)
                VALUES (999999, 100.00)
            """)
            db_connection.commit()

    def test_calculo_valor_total(self, db_connection, db_cursor):
        """Testa o cálculo do valor total do pedido"""
        # Insere cliente de teste com email e CPF únicos
        email_unico = f"test_{uuid.uuid4()}@test.com"
        cpf = f"{uuid.uuid4().int % 10**11:011d}"  # Gera CPF único
        db_cursor.execute("""
            INSERT INTO clientes (nome, email, cpf)
            VALUES ('Test User', %s, %s)
        """, (email_unico, cpf))
        db_connection.commit()

        # Pega o ID do cliente inserido
        db_cursor.execute("SELECT id FROM clientes WHERE email = %s", (email_unico,))
        cliente_id = db_cursor.fetchone()[0]

        # Cria pedido
        db_cursor.execute("""
            INSERT INTO pedidos (cliente_id, valor_total)
            VALUES (%s, 150.00)
        """, (cliente_id,))
        db_connection.commit()

        # Verifica o valor total
        db_cursor.execute("""
            SELECT valor_total
            FROM pedidos
            WHERE cliente_id = %s
        """, (cliente_id,))
        result = db_cursor.fetchone()
        assert result[0] == 150.00, "Valor total incorreto"

    @pytest.mark.parametrize("status", ['pendente', 'aprovado', 'cancelado'])
    def test_status_pedido(self, db_connection, db_cursor, status):
        """Testa os diferentes status de pedido"""
        # Insere cliente de teste com email e CPF únicos
        email_unico = f"test_{uuid.uuid4()}@test.com"
        cpf = f"{uuid.uuid4().int % 10**11:011d}"  # Gera CPF único
        db_cursor.execute("""
            INSERT INTO clientes (nome, email, cpf)
            VALUES ('Test User', %s, %s)
        """, (email_unico, cpf))
        db_connection.commit()

        # Pega o ID do cliente inserido
        db_cursor.execute("SELECT id FROM clientes WHERE email = %s", (email_unico,))
        cliente_id = db_cursor.fetchone()[0]

        # Cria pedido com status específico
        db_cursor.execute("""
            INSERT INTO pedidos (cliente_id, status, valor_total)
            VALUES (%s, %s, 100.00)
        """, (cliente_id, status))
        db_connection.commit()

        # Verifica o status
        db_cursor.execute("""
            SELECT status
            FROM pedidos
            WHERE cliente_id = %s
        """, (cliente_id,))
        result = db_cursor.fetchone()
        assert result[0] == status, f"Status do pedido deveria ser {status}"
