from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models
from .database import engine  # importa a configuração do banco de dados

from .routers.clients import router as routerClients
from .routers.medicines import router as routerMedicines

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Alterar para domínios confiáveis em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routerClients, tags=['clients'], prefix='/api')
app.include_router(routerMedicines, tags=['medicines'], prefix='/api')

@app.get("/")
def root():
    return {"message": "200, ok"}
