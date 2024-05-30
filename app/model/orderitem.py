from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class OrderItem(Base):
    __tablename__ = "order_items"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    dish_id = Column(Integer, ForeignKey("dishes.id"))
    drink_id = Column(Integer, ForeignKey("drinks.id"))
    amount = Column(Integer)
    price = Column(Integer)

    order = relationship("Order", back_populates="items")
    dish = relationship("Dish", back_populates="orders")
    drink = relationship("Drink", back_populates="orders")
