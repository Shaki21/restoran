from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from controller.order import OrderController
from core.auth import is_admin
from core.database import get_db
from schemas.order import OrderDisplay, OrderUpdate, OrderDelete

router = APIRouter(
    prefix='/orders',
    tags=['orders']
)


@router.post("/", response_model=OrderDisplay)
async def create_order(
        dish_id: int,
        drink_id: int,
        db: Session = Depends(get_db),
        current_user: OrderDisplay = Depends(is_admin)):
    order_controller = OrderController(db)
    return order_controller.create_order(dish_id, drink_id)


@router.get("/", response_model=List[OrderDisplay])
async def get_all_orders(db: Session = Depends(get_db)):
    order_controller = OrderController(db)
    return order_controller.get_all_orders()


@router.put("/{order_id}", response_model=OrderDisplay)
async def update_order(
        order_id: int,
        order_update: OrderUpdate,
        db: Session = Depends(get_db),
        current_user: OrderDisplay = Depends(is_admin)
):
    order_controller = OrderController(db)
    return order_controller.update_order(order_id, order_update)


@router.delete("/{order_id}", response_model=OrderDelete)
async def delete_order(
        order_id: int,
        db: Session = Depends(get_db),
        current_user: OrderDisplay = Depends(is_admin)):
    order_controller = OrderController(db)
    return order_controller.delete_order(order_id)
