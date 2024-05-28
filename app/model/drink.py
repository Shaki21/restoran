from sqlalchemy import Column, Integer, String, relationship
from sqlalchemy import declarative_base


Base = declarative_base()


class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Integer)


Drink.orders = relationship("OrderItem", back_populates="drink")
