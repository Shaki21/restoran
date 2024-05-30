from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.core.hash import Hash
from app.model.user import User
from app.schemas.user import UserCreate


class UserController:
    def __init__(
            self,
            db: Session
    ):
        self.db = db

    def create_user(self, request):
        try:
            new_user = User(
                username=request.username,
                password=Hash.bcrypt(request.password),
                role=request.role
            )
            self.db.add(new_user)
            self.db.commit()
            self.db.refresh(new_user)
            return new_user
        except:
            raise HTTPException(status_code=400, detail="Something went wrong!")


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user: UserCreate):
    db_user = db.query(User).filter(User.id == user_id).first()
    for key, value in user.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    db.delete(db_user)
    db.commit()
