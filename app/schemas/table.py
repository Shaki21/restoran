from pydantic import BaseModel


class TableBase(BaseModel):
    number: int
    status: bool


class TableCreate(TableBase):
    pass


class Table(TableBase):
    id: int

    class Config:
        from_attributes = True
        