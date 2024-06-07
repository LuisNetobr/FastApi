from pydantic import BaseModel # Importa a classe BaseModel do Pydantic para a criação de esquemas de validação de dados

#Essa é a classe base para os dados de um produto
class ProductBase(BaseModel):
    name: str
    quantity: int
    price: float

#Classe para criação de um produto, herdando de ProductBase
class CreateProduct(ProductBase):
    pass # Não adiciona novos campos, apenas utiliza os campos de ProductBase

#Classe para representar um produto com ID
class Product(ProductBase):
    id: int

    #Configurações adicionais da classe
    class Config:
        orm_mode = True #Habilita o modo ORM para compatibilidade com modelos ORM do SQLAlchemy
