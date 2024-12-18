from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter()

# rotas clients
@router.get("/clients", response_model=List[schemas.Client])
def list_clients(db: Session = Depends(get_db)):
    clients = db.query(models.Client).all()
    return clients

@router.get("/clients/{client_id}", response_model=schemas.Client)
def get_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    return client

@router.post("/clients/{client_id}", response_model=schemas.Client, status_code=status.HTTP_201_CREATED)
def add_client(client_id: int, client: schemas.ClientCreate, db: Session = Depends(get_db)):
    saved_client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if saved_client:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Já existe um cliente com o ID {client_id}."
        )

    new_client = models.Client(id=client_id, **client.dict())
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

@router.put("/clients/{client_id}", response_model=schemas.Client)
def update_client(client_id: int, updated_client: schemas.ClientCreate, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    
    for key, value in updated_client.dict(exclude_unset=True).items():
        setattr(client, key, value)
    db.commit()
    db.refresh(client)
    return client

@router.delete("/clients/{client_id}", response_model=dict, status_code=status.HTTP_200_OK)
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    db.delete(client)
    db.commit()
    return {"message": f"Cliente com ID {client_id} deletado com sucesso."}
