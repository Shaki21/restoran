from typing import Optional
from pydantic import BaseModel


class TableBase(BaseModel):
    number: int


class TableCreate(TableBase):
    pass


class TableDisplay(TableBase):
    id: int
    order_id: Optional[int] = None

    class Config:
        from_attributes = True


class TableDelete(BaseModel):
    detail: str
