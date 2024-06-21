from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controller.drink import DrinkController
from core.redis import redis_client
from schemas.drink import DrinkCreate, DrinkDisplay, DrinkDelete, DrinkUpdate, DrinkName
from core.database import get_db
from core.auth import is_admin
from utils.redis import serialize, deserialize

router = APIRouter(
    prefix='/drinks',
    tags=['drinks']
)


@router.post("/", response_model=DrinkDisplay)
async def create_drink(
        request: DrinkCreate,
        db: Session = Depends(get_db),
        current_user: DrinkDisplay = Depends(is_admin)):
    return DrinkController(db=db).create_drink(request=request)


@router.get("/", response_model=list[DrinkDisplay])
async def get_all_drinks(db: Session = Depends(get_db)):
    drinks = redis_client.get('drinks')
    if not drinks:
        drinks = DrinkController(db=db).get_all_drinks()
        drinks_display = [DrinkDisplay.from_orm(drink) for drink in drinks]
        redis_client.set('drinks', serialize(drinks_display))
    else:
        drinks = deserialize(drinks, DrinkDisplay)
    return drinks


@router.get("/{id}", response_model=DrinkDisplay)
async def get_drink_by_id(
        id: int,
        db: Session = Depends(get_db),
        current_user: DrinkDisplay = Depends(is_admin)):
    return DrinkController(db=db).get_drink_by_id(id=id)


@router.get("/name/{name}", response_model=DrinkName)
async def get_drink_by_name(
        name: str,
        db: Session = Depends(get_db),
        current_user: DrinkDisplay = Depends(is_admin)):
    return DrinkController(db=db).get_drink_by_name(name=name)


@router.put("/{id}", response_model=DrinkUpdate)
async def update_drink(
        id: int, request: DrinkCreate,
        db: Session = Depends(get_db),
        current_user: DrinkDisplay = Depends(is_admin)):
    return DrinkController(db=db).update_drink(id=id, request=request)


@router.delete("/{id}", response_model=DrinkDelete)
async def delete_drink(
        id: int,
        db: Session = Depends(get_db),
        current_user: DrinkDisplay = Depends(is_admin)):
    return DrinkController(db=db).delete_drink(id=id)
