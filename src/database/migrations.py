from datetime import datetime
from sqlalchemy import ForeignKey, Boolean ,Integer, String, JSON, DateTime, create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from pathlib import Path


class Base(DeclarativeBase):
    pass


class FarmModel(Base):
    __tablename__ = "farms"

    # Pola wymagane
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
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


class WorldModel(Base):
    __tablename__ = "worlds"

    # Pola wymagane
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    address: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    access_password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    # Pola opcjonalne
    description: Mapped[str | None] = mapped_column(String(999))

    # Pola z wartościami domyślnymi
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)


class UserModel(Base):
    __tablename__ = "users"

    # Pola wymagane
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    login: Mapped[str] = mapped_column(String(25), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    # Pola opcjonalne
    description: Mapped[str | None] = mapped_column(String(999))

    # Pola z wartościami domyślnymi
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, nullable=False)


DATABASE_PATH = Path(__file__).resolve().parent.parent / "data.db"

def create_tables(db_url=f"sqlite:///{DATABASE_PATH}"):
    """Tworzy wszystkie tabele"""
    
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
