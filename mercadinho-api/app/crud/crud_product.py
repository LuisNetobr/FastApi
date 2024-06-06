"""Aqui importamos as classes para manipular os dados no banco de dados do produto."""

"""a classe "session" vai definir a interação com o banco de dados e as funções CRUD."""
from sqlalchemy.orm import Session

"""Importa a classe "product"."""
from app.models.product import Products

"""Importamos a classe "ProductCreate" que serve para validar os dados do produto."""
from app.schemas.schema import CreateProduct
"""-----------------------------------------------------------------------------------------------------------"""

"""A função abaixo possui dois parâmetros um que recebem uma sessão no db e um que recebe o id de um produto, 
ela busca esse produto na tabela e retorna o que está escrito. A função "query" vai iniciar a consulta
depois que a "Session" estabelece uma conexão com o db, a função "filter" vai filtrar o valor com base 
no id do produto, e o "first" vai dar o primeiro resultado que encontrar."""
def get_product(db: Session, product_id: int):
    return db.query(Products).filter(Products.id == product_id).first()

"""Nesta função vamos buscar/mostrar/consultar os produtos que se encontram no db, 
temos o parâmetro para mostrar todo o conteúdo."""
def get_products(db: Session):
    return db.query(Products).all()

"""Aqui vamos criar um produto, com o parâmetro para receber uma sessão, e outro,
um produto, esse produto vai ter nome, preço, e quantidade, e será adicionado no
db, comitado, atualizado e retornado para visualização."""
def create_product(db: Session, product: CreateProduct):
    db_product = Products(name=product.name, price=product.price, quantity=product.quantity)
    db.add(db_product)
    db.commit()
    return db_product

"""Esta função recebe como parâmetros a sessão no db, o id do produto, e o objeto "product"
para fazer alterações em determinado produto, ela cria uma variavel que se comunica com o db e
filtra o id do produto, após isso, atualiza/altera seus valores, faz commit e atualiza o banco
e retorna os novos valores."""
def update_product(db: Session, product_id: int, product: CreateProduct):
    db_product = db.query(Products).filter(Products.id == product_id).first()
    if db_product:
        db_product.name = product.name
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()

    return db_product

"""Essa função tem o objetivo de deletar/excluir um produto do banco de dados,
ela recebe novamente uma sessão e o id do produto que vai ser excluído, faz
 commit e retorna o produto que foi excluído. """
def delete_product(db: Session, product_id: int):
    db_product = db.query(Products).filter(Products.id == product_id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
    return db_product
