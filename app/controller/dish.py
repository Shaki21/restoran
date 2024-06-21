from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from model.dish import Dish


class DishController:
    def __init__(
            self,
            db: Session
    ):
        self.db = db

    def create_dish(self, request):
        try:
            new_dish = Dish(
                name=request.name,
                price=request.price
            )
            self.db.add(new_dish)
            self.db.commit()
            self.db.refresh(new_dish)
            return new_dish
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_dish_by_id(self, id: int):
        dish = self.db.query(Dish).filter(Dish.id == id).first()
        if not dish:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Dish with id {id} not found!')
        return dish

    def get_dish_by_name(self, name: str):
        dish = self.db.query(Dish).filter(Dish.name == name).first()
        if not dish:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Dish with name {name} not found!')
        return dish

    def get_all_dishes(self):
        dishes = self.db.query(Dish).all()
        return dishes

    def update_dish(self, id: int, request):
        dish = self.db.query(Dish).filter(Dish.id == id).first()
        if not dish:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Dish with id {id} not found!')
        dish.name = request.name
        dish.price = request.price
        self.db.commit()
        return dish

    def delete_dish(self, id: int):
        dish = self.db.query(Dish).filter(Dish.id == id).first()
        if not dish:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Dish with id {id} not found!')
        self.db.delete(dish)
        self.db.commit()
        return {"detail": 'dish deleted!'}
