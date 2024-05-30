from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserDisplay
from app.controller.user import UserController
from app.core.database import get_db


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post("/", response_model=UserDisplay)
def create_user(request: UserCreate, db: Session = Depends(get_db)):
    return UserController(db=db).create_user(request=request)

