"""O código abaixo é responsável por criar o nosso produto. """

"""Abaixo importamos da biblioteca sqlalchemy algumas de suas funções
para criar colunas e definir tipos de valores. """
from sqlalchemy import Column, Integer, String, Float

"""Importamos de database a classe Base"""
from app.core.database import Base

"""Aqui criamos a classe Product, que vai ser o nosso produto, que herda de Base
(classe base para a criar tabelas) e dentro da classe, definimos o nome da tabela,
coluna de id, nome, preço e quantidade do produto, juntamente com o tipo de valores
que vão ter (Integer, String, Float). 
A coluna id é a chave primaria, e o index=true cria um indice para a coluna "id" e "name"
para que seja possível encontrar rapidamente os valores na tabela."""
class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
