from datetime import datetime
from sqlalchemy import Boolean, Integer, String, DateTime, Table, Column, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .base import Base


user_friends = Table(
    "user_friends",
    Base.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("friend_id", ForeignKey("users.id"), primary_key=True)
)


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
    followers: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    friends: Mapped[list["UserTable"]] = relationship(
        secondary=user_friends,
        primaryjoin=id == user_friends.c.user_id,
        secondaryjoin=id == user_friends.c.friend_id
        )
    favourite_farms: Mapped[list[int]] = mapped_column(Integer, default=list, nullable=False)
    favourite_worlds: Mapped[list[int]] = mapped_column(Integer, default=list, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)
    