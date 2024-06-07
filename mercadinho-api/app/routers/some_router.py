from fastapi import APIRouter, Depends, HTTPException  # Importa classes e funções do FastAPI para criação de rotas e tratamento de dependências e exceções
from sqlalchemy.orm import Session  # Importa a classe Session do SQLAlchemy para manipulação de sessões de banco de dados
from app.crud import crud_product  # Importa as funções CRUD para produtos
from app.schemas.schema import Product, CreateProduct  # Importa os esquemas de produto para validação de dados
from app.core.database import get_db  # Importa a função para obter a sessão do banco de dados

# Cria um roteador para definir as rotas da API
router = APIRouter()

# Define a rota para criar um novo produto
@router.post("/products/", response_model=Product)
def create_product(product: CreateProduct, db: Session = Depends(get_db)):
    
    #cria um novo preoduto
    
    return crud_product.create_product(db=db, product=product)

# Define a rota para obter um produto específico pelo ID
@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    
    #Obtém um produto pelo ID.
    
    db_product = crud_product.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product
    
# Define a rota para obter a lista de produtos
@router.get("/products/")
def read_products(db: Session = Depends(get_db)):

    #Obtém a lista de produtos.
    
    return crud_product.get_products(db)

# Define a rota para atualizar um produto existente
@router.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: CreateProduct, db: Session = Depends(get_db)):

    #Atualiza um produto existente.
    
    db_product = crud_product.update_product(db=db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

# Define a rota para deletar um produto existente
@router.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):

    #Deleta um produto existente.
    
    db_product = crud_product.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


