from sqlalchemy import Column, Integer, Boolean
from app.core.database import Base


class Table(Base):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True, index=True)
    number = Column(Integer, unique=True, nullable=False)
    status = Column(Boolean, nullable=False)

