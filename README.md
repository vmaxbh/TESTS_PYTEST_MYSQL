# Sistema de Testes MySQL

Este projeto implementa um conjunto de testes automatizados para um banco de dados MySQL, focando em validações de integridade de dados, conexão e operações básicas.

## 🏗️ Arquitetura do Projeto

### Estrutura de Diretórios
```
.
├── src/                    # Código fonte do projeto
│   ├── __init__.py        # Torna o diretório um pacote Python
│   └── database_config.py # Configuração da conexão com o banco de dados
│
├── tests/                 # Testes automatizados
│   ├── __init__.py       # Torna o diretório um pacote Python
│   ├── test_id01_connection.py  # Testes de conexão
│   ├── test_id02_clientes.py    # Testes de clientes
│   └── test_id03_pedidos.py     # Testes de pedidos
│
├── conftest.py           # Configuração do pytest e fixtures
├── requirements.txt      # Dependências do projeto
├── setup.py             # Configuração do pacote
└── .env                 # Variáveis de ambiente
```

### Componentes Principais

1. **Configuração do Banco de Dados** (`src/database_config.py`)
   - Gerencia a conexão com o banco de dados MySQL
   - Utiliza variáveis de ambiente para configuração segura
   - Implementa conexão com tratamento de erros

2. **Testes** (`tests/`)
   - Testes de conexão: Valida a conexão com o banco de dados
   - Testes de clientes: Verifica operações CRUD e integridade dos dados
   - Testes de pedidos: Valida operações relacionadas a pedidos e itens

3. **Fixtures** (`conftest.py`)
   - `db_connection`: Conexão persistente para toda a sessão de testes
   - `db_cursor`: Cursor limpo para cada teste
   - `cleanup_test_data`: Limpeza automática de dados de teste

## 🚀 Requisitos

- Python 3.8+
- MySQL Server
- pip (gerenciador de pacotes Python)

## 📦 Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITÓRIO]
cd [NOME_DO_PROJETO]
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
.\venv\Scripts\activate  # Windows
source venv/bin/activate # Linux/Mac
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o arquivo `.env`:
```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=seu_banco
```

## 🧪 Executando os Testes

Execute todos os testes:
```bash
pytest tests/ -v
```

Execute testes específicos:
```bash
pytest tests/test_id01_connection.py -v
pytest tests/test_id02_clientes.py -v
pytest tests/test_id03_pedidos.py -v
```

## 📊 Estrutura do Banco de Dados

O projeto assume a existência das seguintes tabelas:

1. **clientes**
   - id (PK)
   - nome
   - email (UNIQUE)
   - data_cadastro

2. **produtos**
   - id (PK)
   - nome
   - preco
   - estoque

3. **pedidos**
   - id (PK)
   - cliente_id (FK)
   - data_pedido
   - status

4. **itens_pedido**
   - id (PK)
   - pedido_id (FK)
   - produto_id (FK)
   - quantidade
   - preco_unitario

## 🔍 Cobertura de Testes

Os testes cobrem:

- Conexão com o banco de dados
- Integridade dos dados
- Restrições de chave estrangeira
- Validação de campos obrigatórios
- Operações CRUD básicas
- Limpeza de dados de teste

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
