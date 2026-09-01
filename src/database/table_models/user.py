from datetime import datetime
from sqlalchemy import Boolean ,Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from .base import Base


class UserTable(Base):
    __tablename__ = "users"

    # Klucz głowny
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    # Pola wymagane
    login: Mapped[str] = mapped_column(String(25), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    # Pola opcjonalne
    description: Mapped[str | None] = mapped_column(String(999))

    # Pola z wartościami domyślnymi
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    