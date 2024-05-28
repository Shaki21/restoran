from sqlalchemy import Column, Integer, String, relationship
from sqlalchemy import declarative_base


Base = declarative_base()


class Dish(Base):
    __tablename__ = "dishes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)


Dish.orders = relationship("OrderItem", back_populates="dish")
