from pydantic import BaseModel


class DrinkBase(BaseModel):
    name: str
    price: int


class DrinkCreate(DrinkBase):
    pass


class DrinkDisplay(DrinkBase):
    id: int

    class Config:
        from_attributes = True


class DrinkDelete(BaseModel):
    detail: str


class DrinkUpdate(DrinkBase):
    pass


class DrinkName(BaseModel):
    id: int
    name: str
