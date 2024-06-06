from fastapi import FastAPI, HTTPException #Importamos O fastAPI e o HTTPEception afim de criar uma api capaz de lidar com exceções HTTP
from app.models.product import Base #Importamos do diretório "models" a classe "product."
from app.core.database import engine #Importamos de "core" o "database"
from app.routers import some_router #Importamos "some_router" do módulo "routers"
from fastapi.responses import JSONResponse# Importamos JSONResponse que é util para retornar respostas com um formato JSON.


Base.metadata.create_all(bind=engine) # Cria as tabelas no banco de dados.

app = FastAPI()  #Cria a instância da classe fastapi chamada de "app".

#Usado para definir uma função para tratar erros HTTP globalmente
def error_check(app: FastAPI):
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc: HTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": "Ocorreu um erro ao processar sua solicitação.","details": exc.detail},
        )

error_check(app) #Cria um tratamento de erros global


app.include_router(some_router.router) #Coloca as rotas definidas para o "app".

