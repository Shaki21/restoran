from pydantic import BaseModel


class DishBase(BaseModel):
    name: str
    price: int


class DishCreate(DishBase):
    pass


class DishDisplay(DishBase):
    id: int

    class Config:
        from_attributes = True


class DishDelete(BaseModel):
    detail: str


class DishUpdate(DishBase):
    pass


class DishName(BaseModel):
    id: int
    name: str
