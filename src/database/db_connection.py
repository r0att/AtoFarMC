from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from pathlib import Path
from .table_models.base import Base


DATABASE_PATH = Path(__file__).resolve().parent / "data.db"

def create_tables(db_url: str | None = None):
    """Tworzy wszystkie tabele"""

    if db_url is None:
        db_url = f"sqlite:///{DATABASE_PATH}"

    engine = create_engine(db_url)
    Base.metadata.create_all(engine)

    return engine


def get_session(engine) -> Session:
    """Zwraca nową sesję bazy danych"""

    return Session(engine)
