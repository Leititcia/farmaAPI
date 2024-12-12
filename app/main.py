from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List

app = FastAPI()

# basemodels
class Cliente(BaseModel):
    id: int
    nome: str
    email: str
    telefone: str

class Medicamento(BaseModel):
    id: int
    nome: str
    quantidade: int
    preco: float

clientes = []
medicamentos = []

@app.get("/")
async def root():
    return {"message": "200 ok"}


# Rotas Clientes
@app.get("/clientes", response_model=List[Cliente])
def listar_clientes():
    return clientes

@app.get("/clientes/{cliente_id}", response_model=Cliente)
def obter_cliente(cliente_id: int):
    for cliente in clientes:
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente não encontrado.")

@app.post("/clientes", response_model=Cliente)
async def adicionar_cliente(cliente: Cliente):
    for c in clientes:
        if c.id == cliente.id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Já existe um cliente com o ID {cliente.id}."
            )
    clientes.append(cliente)
    return cliente

@app.put("/clientes/{cliente_id}", response_model=Cliente)
def atualizar_cliente(cliente_id: int, cliente_atualizado: Cliente):
    for index, cliente in enumerate(clientes):
        if cliente.id == cliente_id:
            clientes[index] = cliente_atualizado
            return cliente_atualizado
    raise HTTPException(status_code=404, detail="Cliente não encontrado.")

@app.delete("/clientes/{cliente_id}")
def deletar_cliente(cliente_id: int):
    for index, cliente in enumerate(clientes):
        if cliente.id == cliente_id:
            del clientes[index]
            return {"message": "Cliente deletado com sucesso."}
    raise HTTPException(status_code=404, detail="Cliente não encontrado.")


# Rotas Medicamentos
@app.get("/medicamentos", response_model=List[Medicamento])
def listar_medicamentos():
    return medicamentos

@app.get("/medicamentos/{medicamento_id}", response_model=Medicamento)
def obter_medicamento(medicamento_id: int):
    for medicamento in medicamentos:
        if medicamento.id == medicamento_id:
            return medicamento
    raise HTTPException(status_code=404, detail="Medicamento não encontrado.")

@app.post("/medicamentos", response_model=Medicamento)
async def adicionar_medicamento(medicamento: Medicamento):
    for m in medicamentos:
        if m.id == medicamento.id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail=f"Já existe um medicamento com o ID {medicamento.id}."
            )
    medicamentos.append(medicamento)
    return medicamento

@app.put("/medicamentos/{medicamento_id}", response_model=Medicamento)
def atualizar_medicamento(medicamento_id: int, medicamento_atualizado: Medicamento):
    for index, medicamento in enumerate(medicamentos):
        if medicamento.id == medicamento_id:
            medicamentos[index] = medicamento_atualizado
            return medicamento_atualizado
    raise HTTPException(status_code=404, detail="Medicamento não encontrado.")

@app.delete("/medicamentos/{medicamento_id}")
def remover_medicamento(medicamento_id: int):
    for index, medicamento in enumerate(medicamentos):
        if medicamento.id == medicamento_id:
            del medicamentos[index]
            return {"message": "Medicamento removido com sucesso."}
    raise HTTPException(status_code=404, detail="Medicamento não encontrado.")