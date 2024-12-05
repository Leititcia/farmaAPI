# Gerenciamento Farmacêutico - API

Este projeto se trata de uma API construída utilizando o FastAPI para gerenciar um sistema simples de clientes e medicamentos. A aplicação permite a criação, leitura, atualização e exclusão de clientes e medicamentos por meio de rotas RESTful.

### Principais Funcionalidades

- **Gerenciamento de Clientes:** Permite adicionar, listar, atualizar e excluir clientes.
- **Gerenciamento de Medicamentos:** Permite adicionar, listar, atualizar e excluir medicamentos.
- **Validação de Dados:** Utiliza o Pydantic para validação e estruturação dos dados de entrada e saída.

---

## Rotas da API

### Clientes
- `GET /clientes`: Lista todos os clientes.
- `GET /clientes/{cliente_id}`: Obtém um cliente pelo ID.
- `POST /clientes`: Adiciona um novo cliente.
- `PUT /clientes/{cliente_id}`: Atualiza as informações de um cliente existente.
- `DELETE /clientes/{cliente_id}`: Deleta um cliente.

### Medicamentos
- `GET /medicamentos`: Lista todos os medicamentos.
- `GET /medicamentos/{medicamento_id}`: Obtém um medicamento pelo ID.
- `POST /medicamentos`: Adiciona um novo medicamento.
- `PUT /medicamentos/{medicamento_id`}: Atualiza as informações de um medicamento existente.
- `DELETE /medicamentos/{medicamento_id}`: Deleta um medicamento.

---

## Retorno da API

### POST /cliente
``` bash
{
  "id": 1,
  "nome": "Manuela Viana",
  "email": "e@email.com",
  "telefone": "123456789"
}

```

### POST /medicamento
``` bash
{
  "id": 0,
  "nome": "string",
  "quantidade": 0,
  "preco": 0
}

```

---

## Tecnologias Utilizadas

- **FastAPI**: Framework para construção de APIs em Python.
- **Pydantic**: Biblioteca de validação de dados e criação de modelos.
- **Python10**: Linguagem utilizada para o desenvolvimento da aplicação.

---

## Como Clonar

1. **Clone o repositório**:
   ```
   git clone https://github.com/Leititcia/farmaAPI.git
   ```

2. **Crie e ative um ambiente virtual**:
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

3. **Instale as dependências**:
    ```bash
    pip install -r requirements.txt
    ```
     
4. **Execute a API**:
     ```bash
     uvicorn main:app --reload
     ```

5. **Acesse a documentação da API**:
   - Após rodar o servidor, você pode acessar a documentação interativa da API no endereço: [http://localhost:8000/docs](http://localhost:8000/docs).

---

## Autora
Letícia Vale