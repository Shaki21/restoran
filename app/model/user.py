import enum
from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base


class RoleEnum(str, enum.Enum):
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username: str = Column(String, unique=True, nullable=False)
    password: str = Column(String, nullable=False)
    role: str = Column(String, Enum(RoleEnum), nullable=False)

    def is_admin(self):
        return self.role == RoleEnum.ADMIN

    def is_manager(self):
        return self.role == RoleEnum.MANAGER
