from fastapi import FastAPI, Request, Depends  # Certifique-se de importar Depends aqui
from app import models
from .database import engine, get_db
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

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

@app.get("/clientes")
async def clientes(request: Request, db: Session = Depends(get_db)):
    clients = db.query(models.Client).all()
    return templates.TemplateResponse("clientes.html", {"request": request, "clients": clients})

