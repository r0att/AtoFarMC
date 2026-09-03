from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class UserFavouriteWorlds(Base):
    __tablename__ = "user_favourite_worlds"

    # Klucz głowny
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    world_id: Mapped[int] = mapped_column(Integer, ForeignKey("worlds.id"), primary_key=True)
    