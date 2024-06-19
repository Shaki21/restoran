from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.model.order import Order


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, nullable=False)

    order_id = Column(Integer, ForeignKey('orders.id'))
    order = relationship('Order', back_populates='tables')


Order.tables = relationship('Table', back_populates='order')
