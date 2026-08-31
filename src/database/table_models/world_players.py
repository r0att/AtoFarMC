from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class WorldPlayersModel(Base):
    __tablename__ = "world_players"

    # Klucz głowny
    world_id: Mapped[int] = mapped_column(Integer, ForeignKey("worlds.id"), primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"), primary_key=True)
    