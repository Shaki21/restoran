from pydantic import BaseModel


class DishBase(BaseModel):
    name: str
    price: int


class DishCreate(DishBase):
    pass


class Dish(DishBase):
    id: int

    class Config:
        from_attributes = True
