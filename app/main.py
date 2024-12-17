from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import models
from .database import engine  # importa a configuração do banco de dados

from .routers.clients import router as routerClients
from .routers.medicines import router as routerMedicines

# Criar as tabelas no banco de dados
models.Base.metadata.create_all(bind=engine)

# Inicializa a aplicação FastAPI
app = FastAPI()

# Definição de origens permitidas para CORS (Cross-Origin Resource Sharing)
origins = [
    "http://localhost:8000",  # por exemplo, se você estiver usando um frontend em React no localhost:3000
]

# Adiciona o middleware CORS para permitir requisições de origens específicas
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui o roteador das notas, com prefixo "/api/notes" e tag "Notes"
app.include_router(routerClients, tags=['clients'], prefix='/api')
app.include_router(routerMedicines, tags=['medicines'], prefix='/api')

# Rota simples para verificar o estado da API
@app.get("/")
def root():
    return {"message": "200, ok"}
