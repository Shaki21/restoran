from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.model.user import User
from app.core.hash import Hash


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
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_user_by_username(self, username: str):
        user = self.db.query(User).filter(User.username == username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'User {username} not found!')
        return user

    def get_user_by_id(self, id: int):
        user = self.db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'User with id {id} not found!')
        return user

    def get_all_users(self):
        users = self.db.query(User).all()
        return users

    def delete_user(self, id: int):
        user = self.db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'User with id {id} not found!')
        self.db.delete(user)
        self.db.commit()
        return {"detail": 'user deleted!'}
