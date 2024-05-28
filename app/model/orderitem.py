from sqlalchemy import Column, Integer, relationship, ForeignKey
from sqlalchemy import declarative_base


Base = declarative_base()


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