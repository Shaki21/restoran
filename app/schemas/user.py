from pydantic import BaseModel
from app.model.user import RoleEnum


class UserBase(BaseModel):
    username: str
    role: RoleEnum


class UserCreate(UserBase):
    password: str


class UserDisplay(UserBase):
    id: int

    class Config:
        from_attributes = True
