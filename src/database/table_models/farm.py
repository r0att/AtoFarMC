from datetime import datetime
from sqlalchemy import ForeignKey,Integer, String, JSON, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class FarmTable(Base):
    __tablename__ = "farms"

    # Klucz główny
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Pola wymagane
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    farm_type: Mapped[str] = mapped_column(String(50), nullable=False)
    version: Mapped[str] = mapped_column(String(25), nullable=False)
    created_by: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    access_password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    # Pola opcjonalne
    world_id: Mapped[int | None] = mapped_column(ForeignKey("worlds.id"))
    x: Mapped[int | None] = mapped_column(Integer)
    y: Mapped[int | None] = mapped_column(Integer)
    z: Mapped[int | None] = mapped_column(Integer)
    description: Mapped[str | None] = mapped_column(String(999))
    guide_link: Mapped[str | None] = mapped_column(String(500))

    # Pola z wartościami domyślnymi
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    productivity: Mapped[dict[str, float]] = mapped_column(JSON, default=dict, nullable=False)
