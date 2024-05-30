from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, index=True)
    status = Column(Boolean, default=True)

    orders = relationship("Order", back_populates="table")
