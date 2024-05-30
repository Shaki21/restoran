import enum
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base


class RoleEnum(str, enum.Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, index=True)
    password: str = Column(String, nullable=False)
    role: str = Column(String, Enum(RoleEnum), nullable=False)

    orders = relationship("Order", back_populates="user")

    def is_admin(self):
        return self.role == RoleEnum.ADMIN

    def is_manager(self):
        return self.role == RoleEnum.MANAGER
