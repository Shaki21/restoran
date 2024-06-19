from fastapi import HTTPException
from sqlalchemy.orm import Session, joinedload

from app.model.dish import Dish
from app.model.drink import Drink
from app.model.order import Order
from app.schemas.order import OrderUpdate


class OrderController:
    def __init__(self, db: Session):
        self.db = db

    def create_order(self, dish_id: int, drink_id: int):
        try:
            db_dish = self.db.query(Dish).filter(Dish.id == dish_id).first()
            db_drink = self.db.query(Drink).filter(Drink.id == drink_id).first()
            if not db_dish or not db_drink:
                raise HTTPException(status_code=400, detail="Dish or drink not found")
            order_price = db_dish.price + db_drink.price
            db_order = Order(dish_id=dish_id, drink_id=drink_id, price=order_price)
            self.db.add(db_order)
            self.db.commit()
            self.db.refresh(db_order)
            return {
                "id": db_order.id,
                "dish_name": db_dish.name,
                "drink_name": db_drink.name,
                "price": db_order.price
            }
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_all_orders(self):
        orders = self.db.query(Order).options(joinedload(Order.dish), joinedload(Order.drink)).all()
        return [
            {
                "id": order.id,
                "dish_name": order.dish.name,
                "drink_name": order.drink.name,
                "price": order.price
            }
            for order in orders
        ]

    def update_order(self, order_id: int, order_update: OrderUpdate):
        db_order = self.db.query(Order).filter(Order.id == order_id).first()
        if not db_order:
            raise HTTPException(status_code=404, detail="Order not found")

        if order_update.dish_id:
            db_dish = self.db.query(Dish).filter(Dish.id == order_update.dish_id).first()
            if not db_dish:
                raise HTTPException(status_code=400, detail="Dish not found")
            db_order.dish_id = order_update.dish_id
            db_order.price = db_dish.price + db_order.drink.price

        if order_update.drink_id:
            db_drink = self.db.query(Drink).filter(Drink.id == order_update.drink_id).first()
            if not db_drink:
                raise HTTPException(status_code=400, detail="Drink not found")
            db_order.drink_id = order_update.drink_id
            db_order.price = db_order.dish.price + db_drink.price

        self.db.commit()
        self.db.refresh(db_order)

        return {
            "id": db_order.id,
            "dish_name": db_order.dish.name,
            "drink_name": db_order.drink.name,
            "price": db_order.price
        }

    def delete_order(self, order_id: int):
        db_order = self.db.query(Order).filter(Order.id == order_id).first()
        if not db_order:
            raise HTTPException(status_code=404, detail="Order not found")

        self.db.delete(db_order)
        self.db.commit()

        return {"detail": f"Order with ID {order_id} has been deleted"}
