from sqlalchemy import inspect
from src.database.db_connection import create_tables
from src.database.table_models import Base


def test_create_tables():
    """Testuje czy tabele tworzą się poprawnie w bazie danych."""

    engine = create_tables("sqlite:///:memory:")

    expected_tables = {
        "users",
        "worlds",
        "farms",
        "world_players"
    }

    # Testowanie, czy modele są zarejestrowany
    assert set(Base.metadata.tables.keys()) == expected_tables

    # Testowanie, czy tabele zostały utworzone
    inspector = inspect(engine)
    created_tables = set(inspector.get_table_names())

    assert created_tables == expected_tables
