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
        except:
            raise HTTPException(status_code=400, detail="Something went wrong!")

    def get_user_by_id(self, id: int):
        user = self.db.query(User).filter(User.id == id).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'User with id {id} not found!')
        return user
