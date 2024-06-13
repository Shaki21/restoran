from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controller.user import UserController
from app.schemas.user import UserCreate, UserDisplay, UserDelete
from app.core.database import get_db

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post("/", response_model=UserDisplay)
async def create_user(request: UserCreate, db: Session = Depends(get_db)):
    return UserController(db=db).create_user(request=request)


@router.get("/{id}", response_model=UserDisplay)
async def get_user(id: int, db: Session = Depends(get_db)):
    return UserController(db=db).get_user_by_id(id=id)


@router.get("/", response_model=list[UserDisplay])
async def get_users(db: Session = Depends(get_db)):
    return UserController(db=db).get_all_users()


@router.delete("/{id}", response_model=UserDelete)
async def delete_user(id: int, db: Session = Depends(get_db)):
    return UserController(db=db).delete_user(id=id)
