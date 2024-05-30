from pydantic import BaseModel
from typing import Optional


class OrderItemBase(BaseModel):
    order_id: int
    dish_id: Optional[int]
    drink_id: Optional[int]
    amount: int
    price: int


class OrderItemCreate(OrderItemBase):
    pass


class OrderItem(OrderItemBase):
    id: int

    class Config:
        from_attributes = True
