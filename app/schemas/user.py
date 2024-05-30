from pydantic import BaseModel
from app.model.user import RoleEnum


class UserBase(BaseModel):
    username: str
    password: str
    role: RoleEnum


class UserCreate(UserBase):
    pass


class UserDisplay(UserBase):
    id: int
    username: str
    role: RoleEnum

    class Config:
        from_attributes = True
