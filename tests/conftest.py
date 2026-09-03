import os
import pytest
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from src.database.table_models import Base


load_dotenv()


@pytest.fixture
def session():
    test_database_url = os.getenv("TEST_DATABASE_URL")

    if test_database_url is None:
        raise RuntimeError("TEST_DATABASE_URL is not defined")

    engine = create_engine(test_database_url)

    Base.metadata.create_all(engine)

    with Session(engine) as session:
        yield session

    Base.metadata.drop_all(engine)
    engine.dispose()
    