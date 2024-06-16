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


class UserDelete(BaseModel):
    detail: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str
