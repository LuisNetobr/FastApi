from fastapi import FastAPI #Importamos O fastAPI
from app.models.product import Base #Importamos do diretório "models" a classe "product."
from app.core.database import engine #Importamos de "core" o "database"
from app.routers import some_router #Importamos "some_router" do módulo "routers"

Base.metadata.create_all(bind=engine) # Cria as tabelas no banco de dados.

app = FastAPI()  #Cria a instância da classe fastapi chamada de "app".

app.include_router(some_router.router) #Coloca as rotas definidas para o "app".
