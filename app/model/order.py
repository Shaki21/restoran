from sqlalchemy import Column, Integer, ForeignKey
from app.core.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    table_id = Column(Integer, ForeignKey("tables.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
