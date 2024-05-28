from sqlalchemy import Column, Integer, String, DateTime, relationship
from sqlalchemy.ext.declarative import declarative_base
from app.model.order import Order


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    role = Column(String, index=True)
    created_at = Column(DateTime)


User.orders = relationship("Order", order_by=Order.id, back_populates="user")
