from typing import Optional
import base64
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt, JWTError

from pydantic import BaseModel

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm, OAuth2
from fastapi.security.base import SecurityBase
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.openapi.utils import get_openapi

from starlette.status import HTTP_403_FORBIDDEN
from starlette.responses import RedirectResponse, Response, JSONResponse
from starlette.requests import Request

from app.core.database import get_db
from app.controller.user import UserController, User
from app.schemas.user import TokenData
from sqlalchemy.orm import Session

SECRET_KEY = '0b6535c5a840f0f37516b60d514d241d5af2f851f23aba2ee8b6e6ac5e5e61dc'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 1000


class OAuth2PasswordBearerCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: str = None,
        scopes: dict = None,
        auto_error: bool = True,
    ):
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        cookie_authorization: str = request.cookies.get("access_token")

        cookie_scheme, cookie_param = get_authorization_scheme_param(
            cookie_authorization
        )

        if cookie_scheme.lower() == "bearer":
            authorization = True
            scheme = cookie_scheme
            param = cookie_param

        else:
            authorization = False

        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=HTTP_403_FORBIDDEN, detail="Not authenticated"
                )
            else:
                return None
        return param


oauth2_scheme = OAuth2PasswordBearerCookie(tokenUrl="/auth/token")


def create_access_token(*, data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials"
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = UserController(db=db).get_user_by_username(username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: User = Depends(get_current_user)):
    return current_user


def is_admin(current_user: User = Depends(get_current_active_user)):
    if not current_user.is_admin():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not admin")
    return current_user


def is_manager(current_user: User = Depends(get_current_active_user)):
    if not current_user.is_manager():
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not manager")
    return current_user

