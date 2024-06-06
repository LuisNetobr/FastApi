from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    quantity: int
    price: float


class CreateProduct(ProductBase):
    pass

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True