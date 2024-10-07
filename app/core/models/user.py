from .base import Base
from sqlalchemy.orm import Mapped, mapped_column



class User(Base):
    __tablename__ = 'user'
    username: Mapped[str]
