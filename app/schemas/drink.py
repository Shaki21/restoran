from pydantic import BaseModel


class DrinkBase(BaseModel):
    name: str
    price: int


class DrinkCreate(DrinkBase):
    pass


class Drink(DrinkBase):
    id: int

    class Config:
        from_attributes = True
