from sqlalchemy import inspect
from src.database.db_connection import create_tables
from src.database.table_models import Base
from src.database.farm_repository import FarmRepository


def test_create_tables(session):
    """Testuje czy tabele tworzą się poprawnie w bazie danych."""

    expected_tables = {
        "users",
        "worlds",
        "farms",
        "world_players",
        "user_friends",
        "user_favourite_farms",
        "user_favourite_worlds",
        "user_followers"
    }

    # Testowanie, czy modele są zarejestrowany
    assert set(Base.metadata.tables.keys()) == expected_tables

    # Testowanie, czy tabele zostały utworzone
    inspector = inspect(session.bind)
    created_tables = set(inspector.get_table_names())

    assert created_tables == expected_tables
