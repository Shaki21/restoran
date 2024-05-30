from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime)

    table = relationship("Table", back_populates="orders")
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")
