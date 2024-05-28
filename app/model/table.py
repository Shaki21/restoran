from sqlalchemy import Column, Integer, Boolean, relationship
from sqlalchemy import declarative_base
from app.model.order import Order


Base = declarative_base()


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, index=True)
    status = Column(Boolean, default=True)


Table.orders = relationship("Order", order_by=Order.id, back_populates="table")

