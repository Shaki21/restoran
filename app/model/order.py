from sqlalchemy import Column, Integer, relationship, ForeignKey, DateTime
from sqlalchemy import declarative_base


Base = declarative_base()


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer, ForeignKey("tables.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime)

    table = relationship("Table", back_populates="orders")
    user = relationship("User", back_populates="orders")
