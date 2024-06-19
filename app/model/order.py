from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    dish_id = Column(Integer, ForeignKey("dishes.id"), nullable=False)
    drink_id = Column(Integer, ForeignKey("drinks.id"), nullable=False)
    price = Column(Integer, nullable=False)

    dish = relationship("Dish")
    drink = relationship("Drink")
