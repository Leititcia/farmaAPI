# API de Gerenciamento Farmacêutico Integrado com BD

Uma API RESTful baseada no FastAPI para gerencia farmacêutica. A API fornece endpoints para listar, recuperar, adicionar, atualizar e excluir clientes e medicamentos, além de garantir a integração com um banco de dados relacional.

---

## Tecnologias Utilizadas

- **Python**: Linguagem utilizada para o desenvolvimento da aplicação.
- **FastAPI**: Framework para construção de APIs em Python.
- **Pydantic**: Biblioteca de validação de dados e criação de modelos.
- **Uvicorn**: Servidor ASGI utilizado para rodar a aplicação FastAPI.
- **SQLAlchemy**: Biblioteca de ORM para manipulação e interação com o banco de dados.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenamento de informações.
- **Postman**: Ferramenta utilizada para testar as rotas da API e validar as funcionalidades.

---

## Estrutura de Pastas
```sh
├── app/
│     ├── routers/
│           ├── __init__.py
│           ├── clients.py
│           └── medicine.py
│     ├── __init__.py
│     ├── config.py
│     ├── database.py
│     ├── main.py
│     ├── models.py
│     └── schemas.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt
```

### Detalhamento dos Arquivos

- **app/**: Diretório principal da aplicação contendo todos os módulos e arquivos essenciais.
  - **app/routers/**: Diretório que organiza as rotas da aplicação.
    - **__init__.py**: Arquivo que torna o diretório um pacote Python, permitindo a importação dos módulos.
    - **clients.py**: Contém as rotas relacionadas à gestão de clientes.
    - **medicines.py**: Contém as rotas para gerenciamento de medicamentos.
  - **__init__.py**: Arquivo que torna o diretório um pacote Python, permitindo organizar os módulos.
  - **config.py**: Contém as variáveis de ambiente e parâmetros de conexão com o banco de dados.
  - **database.py**: Configura a conexão com o banco de dados PostgreSQL.
  - **main.py**: Inicializa a aplicação FastAPI, configura as rotas, e cria as tabelas no banco de dados.
  - **models.py**: Define os modelos de dados para as tabelas do banco de dados.
  - **schemas.py**: Define os esquemas Pydantic para validação e serialização dos dados.
- **.env**: Armazena variáveis de ambiente para configuração do banco de dados, como credenciais e host.
- **.gitignore**: Ignora arquivos e pastas gerados automaticamente.
- **README.md**: Documento de documentação do projeto.
- **requirements.txt**: Lista as dependências do projeto.
---

## Rotas da API

### Clients
- `GET /api/clients`: Lista todos os clientes.
- `GET /api/clients/{client_id}`: Obtém um cliente pelo ID.
- `POST /api/clients{client_id}`: Adiciona um novo cliente.
- `PUT /clients/{client_id}`: Atualiza as informações de um cliente existente.
- `DELETE /clients/{client_id}`: Deleta um cliente.

### Medicines
- `GET /api/medicines`: Lista todos os medicamentos.
- `GET /api/medicines{medicine_id}`: Obtém um medicamento pelo ID.
- `POST /api/medicines{medicine_id}`: Adiciona um novo medicamento.
- `PUT /api/medicines{medicine_id}`}: Atualiza as informações de um medicamento existente.
- `DELETE /api/medicines{medicine_id}`: Deleta um medicamento.

---

## Retorno da API

### POST /api/client/{client_id}
``` bash
{
    "id": 1,
    "name": "samara",
    "email": "sam@gmail.com",
    "phone": "40028922"
}

```

### DELETE /api/client/{client_id}
``` bash
{
    "message": "Cliente com ID {client_id} deletado com sucesso."
}
```

---

## Esquema do Banco de Dados

### Tabela de Clientes

| Coluna  | Tipo    | Descrição         |
|---------|---------|-------------------|
| id      | Integer | Chave primária    |
| name    | String  | Nome do cliente   |
| email   | String  | E-mail do cliente |
| phone   | String  | Telefone do cliente |

### Tabela de Medicamentos

| Coluna      | Tipo    | Descrição               |
|-------------|---------|-------------------------|
| id          | Integer | Chave primária          |
| name        | String  | Nome do medicamento     |
| quantity    | Integer | Quantidade em estoque   |
| price       | Float   | Preço por unidade       |

---

## Como Clonar

1. **Clone o Repositório**:
   - No terminal, execute o comando abaixo para clonar a branch específica do projeto:   
   ```
   git clone --branch v2.0 https://github.com/Leititcia/farmaAPI.git
   ```

2. **Crie e Ative um Ambiente Virtual**:
   - Com o diretório do projeto aberto crie o ambiente virtual com o comando abaixo:
    ```bash
      python -m venv venv
     ```
      - Para ativar
          - No windows:
            ```bash
              venv\Scripts\activate
             ```
          - No Linux/macOS:
            ```bash
              source venv/bin/activate
             ```

4. **Instale as Dependências**:
    ```bash
    pip install -r requirements.txt
    ```
     
5. **Execute a API**:
     ```bash
     uvicorn app.main:app --reload
     ```

6. **Acesse a documentação da API**:
   - Após iniciar o servidor, você pode acessar a documentação interativa da API no endereço: [http://localhost:8000/docs](http://localhost:8000/docs).

---

## Arquivo JSON para Postman  

Para facilitar os testes desta API, disponibilizo um arquivo JSON com todas as rotas configuradas para importação no **Postman**.

### 📥 **Download do Arquivo**
Clique no link abaixo para fazer o download do arquivo JSON:  
[🔗 Link para o arquivo JSON no Google Drive](https://drive.google.com/file/d/10ROfxS__4zUrNbQkDYxCB0wTbYFfQoJQ/view?usp=sharing) 

---

## Autora
Letícia Vale.
