from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm.session import Session

from app.core.auth import get_current_active_user, get_current_user
from app.core.database import get_db
from app.model.user import User
from app.schemas.user import UserDisplay
from app.controller.user import UserController
from app.core.hash import Hash
from fastapi.responses import JSONResponse
from app.core import auth

router = APIRouter(
    tags=['authentication']
)


@router.post('/auth/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")

    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Incorrect password")

    access_token = auth.create_access_token(data={'sub': user.username})
    response = JSONResponse(content="Successfully logged in!")
    response.set_cookie(
        key="access_token",
        value=f"Bearer {access_token}",
        httponly=True,
        samesite=None,
        max_age=1800,
        expires=1800
    )
    return response


@router.post('/auth/logout')
def logout():
    response = JSONResponse(content="Successfully logged out!")
    response.set_cookie(
        key="access_token",
        value="",
        httponly=True,
        samesite=None,
        max_age=0,
        expires=0
    )
    return response


@router.get('/auth/me', response_model=UserDisplay)
def get_me(current_user: UserDisplay = Depends(get_current_active_user)):
    return current_user

