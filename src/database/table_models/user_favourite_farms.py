from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class UserFavouriteFarms(Base):
    __tablename__ = "user_favourite_farms"

    # Klucz głowny
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    farm_id: Mapped[int] = mapped_column(Integer, ForeignKey("farms.id"), primary_key=True)
    