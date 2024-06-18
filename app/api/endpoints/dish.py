from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controller.dish import DishController
from app.schemas.dish import DishCreate, DishDisplay, DishDelete, DishUpdate, DishName
from app.core.database import get_db
from app.core.auth import is_admin, is_manager, get_current_user


router = APIRouter(
    prefix='/dishes',
    tags=['dishes']
)


@router.post("/", response_model=DishDisplay)
async def create_dish(request: DishCreate, db: Session = Depends(get_db), current_user: DishDisplay = Depends(is_admin)):
    return DishController(db=db).create_dish(request=request)


@router.get("/{id}", response_model=DishDisplay)
async def get_dish_by_id(id: int, db: Session = Depends(get_db), current_user: DishDisplay = Depends(is_admin)):
    return DishController(db=db).get_dish_by_id(id=id)


@router.get("/name/{name}", response_model=DishName)
async def get_dish_by_name(name: str, db: Session = Depends(get_db), current_user: DishDisplay = Depends(is_admin)):
    return DishController(db=db).get_dish_by_name(name=name)


@router.get("/", response_model=list[DishDisplay])
async def get_all_dishes(db: Session = Depends(get_db)):
    return DishController(db=db).get_all_dishes()


@router.put("/{id}", response_model=DishUpdate)
async def update_dish(id: int, request: DishCreate, db: Session = Depends(get_db), current_user: DishDisplay = Depends(is_admin)):
    return DishController(db=db).update_dish(id=id, request=request)


@router.delete("/{id}", response_model=DishDelete)
async def delete_dish(id: int, db: Session = Depends(get_db), current_user: DishDisplay = Depends(is_admin)):
    return DishController(db=db).delete_dish(id=id)
