from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from model.drink import Drink


class DrinkController:
    def __init__(
            self,
            db: Session
    ):
        self.db = db

    def create_drink(self, request):
        try:
            new_drink = Drink(
                name=request.name,
                price=request.price
            )
            self.db.add(new_drink)
            self.db.commit()
            self.db.refresh(new_drink)
            return new_drink
        except Exception as e:
            raise HTTPException(status_code=400, detail=str(e))

    def get_drink_by_id(self, id: int):
        drink = self.db.query(Drink).filter(Drink.id == id).first()
        if not drink:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Drink with id {id} not found!')
        return drink

    def get_drink_by_name(self, name: str):
        drink = self.db.query(Drink).filter(Drink.name == name).first()
        if not drink:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Drink with name {name} not found!')
        return drink

    def get_all_drinks(self):
        drinks = self.db.query(Drink).all()
        return drinks

    def update_drink(self, id: int, request):
        drink = self.db.query(Drink).filter(Drink.id == id).first()
        if not drink:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Drink with id {id} not found!')
        drink.name = request.name
        drink.price = request.price
        self.db.commit()
        return drink

    def delete_drink(self, id: int):
        drink = self.db.query(Drink).filter(Drink.id == id).first()
        if not drink:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f'Drink with id {id} not found!')
        self.db.delete(drink)
        self.db.commit()
        return {"detail": 'drink deleted!'}
