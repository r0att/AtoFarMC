from datetime import datetime
from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class WorldTable(Base):
    __tablename__ = "worlds"

    # Klucz głowny
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Pola wymagane
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    access_password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    # Pola opcjonalne
    description: Mapped[str | None] = mapped_column(String(999))

    # Pola z wartościami domyślnymi
    favourites: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    