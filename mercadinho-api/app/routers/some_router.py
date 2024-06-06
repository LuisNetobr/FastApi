from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import crud_product
from app.schemas.schema import Product, CreateProduct
from app.core.database import get_db

router = APIRouter()

@router.post("/products/", response_model=Product)
def create_product(product: CreateProduct, db: Session = Depends(get_db)):
    return crud_product.create_product(db=db, product=product)


@router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud_product.get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.get("/products/")
def read_products(db: Session = Depends(get_db)):
    return crud_product.get_products(db)

@router.put("/products/{product_id}", response_model=Product)
def update_product(product_id: int, product: CreateProduct, db: Session = Depends(get_db)):
    db_product = crud_product.update_product(db=db, product_id=product_id, product=product)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product

@router.delete("/products/{product_id}", response_model=Product)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud_product.delete_product(db=db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return db_product


