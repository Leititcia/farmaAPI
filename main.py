from fastapi import FastAPI, Request, Depends, HTTPException, status, Form # Certifique-se de importar Depends aqui
from app import models
from .database import engine, get_db
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from . import schemas  # Importar schemas corretamente


from .routers.clients import router as routerClients
from .routers.medicines import router as routerMedicines

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.include_router(routerClients, tags=['clients'], prefix='/api')
app.include_router(routerMedicines, tags=['medicines'], prefix='/api')

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# clientes
@app.get("/clientes")
async def clientes(request: Request, db: Session = Depends(get_db)):
    clients = db.query(models.Client).all()
    return templates.TemplateResponse("clientes.html", {"request": request, "clients": clients})

@app.get("/clientes/adicionar")
def add_client_form(request: Request):
    return templates.TemplateResponse("adicionar_cliente.html", {"request": request})

@app.post("/clientes/adicionar")
def add_client(
    name: str = Form(...),
    email: str = Form(...),
    phone: str = Form(None),
    db: Session = Depends(get_db)
):
    new_client = models.Client(name=name, email=email, phone=phone)
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return RedirectResponse(url="/clientes", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/clientes/editar/{client_id}")
def edit_client_form(client_id: int, request: Request, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    return templates.TemplateResponse("editar_cliente.html", {"request": request, "client": client})

@app.post("/clientes/editar/{client_id}")
def edit_client(client_id: int, name: str = Form(...), email: str = Form(...), phone: str = Form(None), db: Session = Depends(get_db)):
    existing_client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if existing_client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    
    existing_client.name = name
    existing_client.email = email
    if phone:
        existing_client.phone = phone
    
    db.commit()
    db.refresh(existing_client)
    return RedirectResponse(url="/clientes", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/clientes/deletar/{client_id}")
def delete_client_form(client_id: int, request: Request, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    return templates.TemplateResponse("deletar_cliente.html", {"request": request, "client": client})

@app.post("/clientes/deletar/{client_id}")
def delete_client(client_id: int, db: Session = Depends(get_db)):
    client = db.query(models.Client).filter(models.Client.id == client_id).first()
    if client is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado.")
    
    db.delete(client)
    db.commit()
    return RedirectResponse(url="/clientes", status_code=status.HTTP_303_SEE_OTHER)


# medicamentos
@app.get("/medicamentos")
async def listar_medicamentos(request: Request, db: Session = Depends(get_db)):
    medicines = db.query(models.Medicine).all()
    return templates.TemplateResponse("medicamentos.html", {"request": request, "medicines": medicines})

@app.get("/medicamentos/adicionar")
def add_medicine_form(request: Request):
    return templates.TemplateResponse("adicionar_medicamento.html", {"request": request})

@app.post("/medicamentos/adicionar")
def add_medicine(
    name: str = Form(...), 
    quantity: int = Form(...), 
    price: float = Form(...), 
    db: Session = Depends(get_db)
):

    existing_medicine = db.query(models.Medicine).filter(models.Medicine.name == name).first()
    if existing_medicine:
        raise HTTPException(status_code=409, detail="Medicamento já cadastrado.")

    new_medicine = models.Medicine(name=name, quantity=quantity, price=price)
    db.add(new_medicine)
    db.commit()
    db.refresh(new_medicine)

    return RedirectResponse(url="/medicamentos", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/medicamentos/editar/{medicine_id}")
def edit_medicine_form(medicine_id: int, request: Request, db: Session = Depends(get_db)):
    medicine = db.query(models.Medicine).filter(models.Medicine.id == medicine_id).first()
    if medicine is None:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    return templates.TemplateResponse("editar_medicamento.html", {"request": request, "medicine": medicine})

@app.post("/medicamentos/editar/{medicine_id}")
def edit_medicine(
    medicine_id: int,
    name: str = Form(...),
    quantity: int = Form(...),
    price: float = Form(...),
    db: Session = Depends(get_db)
):

    existing_medicine = db.query(models.Medicine).filter(models.Medicine.id == medicine_id).first()
    if existing_medicine is None:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    
    existing_medicine.name = name
    existing_medicine.quantity = quantity
    existing_medicine.price = price
    db.commit()
    db.refresh(existing_medicine)
    
    return RedirectResponse(url="/medicamentos", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/medicamentos/deletar/{medicine_id}")
def delete_medicine_form(medicine_id: int, request: Request, db: Session = Depends(get_db)):
    medicine = db.query(models.Medicine).filter(models.Medicine.id == medicine_id).first()
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    return templates.TemplateResponse("deletar_medicamento.html", {"request": request, "medicine": medicine})

# Rota para realizar a deleção
@app.post("/medicamentos/deletar/{medicine_id}")
def delete_medicine(medicine_id: int, db: Session = Depends(get_db)):
    medicine = db.query(models.Medicine).filter(models.Medicine.id == medicine_id).first()
    if not medicine:
        raise HTTPException(status_code=404, detail="Medicamento não encontrado.")
    db.delete(medicine)
    db.commit()
    return RedirectResponse("/medicamentos", status_code=303)
