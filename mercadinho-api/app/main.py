from fastapi import FastAPI
from app.models.product import Base
from app.core.database import engine
from app.routers import some_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(some_router.router)