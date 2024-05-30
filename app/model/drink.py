from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)

    orders = relationship("OrderItem", back_populates="drink")
