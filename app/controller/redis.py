from sqlalchemy.orm import Session

from app.model.dish import Dish
from app.model.drink import Drink


class OrderController:
    def __init__(self, db: Session):
        self.db = db

    def fetch_from_db(self, model_name):
        # Funkcija za dohvaćanje podataka iz baze podataka
        if model_name == 'Dishes':
            return self.db.query(Dish).all()
        elif model_name == 'Drinks':
            return self.db.query(Drink).all()
