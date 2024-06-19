from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.core.database import get_db
from app.model.dish import Dish
from app.model.drink import Drink
from app.model.order import Order
from app.schemas.order import OrderCreate, OrderDisplay, OrderUpdate, OrderDelete

router = APIRouter(
    prefix='/orders',
    tags=['orders']
)


@router.post("/", response_model=OrderDisplay)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_dish = db.query(Dish).filter(Dish.id == order.dish_id).first()
    db_drink = db.query(Drink).filter(Drink.id == order.drink_id).first()
    if not db_dish or not db_drink:
        raise HTTPException(status_code=400, detail="Dish or drink not found")

    order_price = db_dish.price + db_drink.price
    db_order = Order(dish_id=order.dish_id, drink_id=order.drink_id, price=order_price)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return {
        "id": db_order.id,
        "dish_name": db_dish.name,
        "drink_name": db_drink.name,
        "price": db_order.price
    }


@router.get("/", response_model=List[OrderDisplay])
def get_all_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).options(joinedload(Order.dish), joinedload(Order.drink)).all()
    return [
        {
            "id": order.id,
            "dish_name": order.dish.name,
            "drink_name": order.drink.name,
            "price": order.price
        }
        for order in orders
    ]


@router.put("/{order_id}", response_model=OrderDisplay)
def update_order(
        order_id: int,
        order_update: OrderUpdate,
        db: Session = Depends(get_db)
):
    # Fetch the existing order from the database
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Update dish and drink if provided in order_update
    if order_update.dish_id:
        db_dish = db.query(Dish).filter(Dish.id == order_update.dish_id).first()
        if not db_dish:
            raise HTTPException(status_code=400, detail="Dish not found")
        db_order.dish_id = order_update.dish_id
        db_order.price = db_dish.price + db_order.drink.price  # Recalculate price if necessary

    if order_update.drink_id:
        db_drink = db.query(Drink).filter(Drink.id == order_update.drink_id).first()
        if not db_drink:
            raise HTTPException(status_code=400, detail="Drink not found")
        db_order.drink_id = order_update.drink_id
        db_order.price = db_order.dish.price + db_drink.price  # Recalculate price if necessary

    db.commit()
    db.refresh(db_order)

    # Return updated order details
    return {
        "id": db_order.id,
        "dish_name": db_order.dish.name,
        "drink_name": db_order.drink.name,
        "price": db_order.price
    }


@router.delete("/{order_id}", response_model=OrderDelete)
def delete_order(
        order_id: int,
        db: Session = Depends(get_db)
):
    # Fetch the existing order from the database
    db_order = db.query(Order).filter(Order.id == order_id).first()
    if not db_order:
        raise HTTPException(status_code=404, detail="Order not found")

    # Delete the order from the database
    db.delete(db_order)
    db.commit()

    return {"detail": f"Order with ID {order_id} has been deleted"}
