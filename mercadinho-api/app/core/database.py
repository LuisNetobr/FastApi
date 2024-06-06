"""Importa da biblioteca "sqlalchemy" a função create_engine que tem a função de
conectar com o banco de dados. """
from sqlalchemy import create_engine

"""Importa de "sqlalchemy" a função "declarative_base" que serve 
para criar uma classe para definir as tabelas no banco de dados. """
from sqlalchemy.ext.declarative import declarative_base

""" "sessionmaker" é a função responsável por criar uma classe 
que vai permitir interagir com o banco de dados. """
from sqlalchemy.orm import sessionmaker


"""O "os" é uma biblioteca que tem funcionalidades que permite
 o app interagir com o sistema operacional. """
import os

"""Variável que vai armazenar a URL do banco de dados. """
DATABASE_URL = os.getenv("DATABASE_URL")

""" A variável "engine" vai criar conexão com o banco dados. """
engine = create_engine(DATABASE_URL)

"""A variável "SessionLocal" que recebe a função "sessionmaker" cria 
uma classe de sessão, com os parâmetros controlando suas interações,
e o "bind=engine", associa essa sessão ao banco de dados. """
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""A função declarative_base() cria uma classe base que serve como 
inicio para criar tabelas """
Base = declarative_base()

"""A função abaixo vai criar e fechar uma sessão do banco de dados,
 o "yield" serve como uma especie de gerador, que vai retornar o db. """
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

