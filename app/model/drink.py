from sqlalchemy import Column, Integer, String
from core.database import Base


class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
