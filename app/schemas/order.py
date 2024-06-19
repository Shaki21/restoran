from typing import Optional
from pydantic import BaseModel


class OrderBase(BaseModel):
    dish_id: int
    drink_id: int


class OrderCreate(OrderBase):
    pass


class OrderDisplay(BaseModel):
    id: int
    dish_name: str
    drink_name: str
    price: int

    class Config:
        from_attributes = True


class OrderUpdate(BaseModel):
    dish_id: Optional[int] = None
    drink_id: Optional[int] = None

    class Config:
        orm_mode = True


class OrderDelete(BaseModel):
    detail: str
