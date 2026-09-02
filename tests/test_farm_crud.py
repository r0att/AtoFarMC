from src.database.farm_repository import FarmRepository
from src.models import Farm
from datetime import datetime


def test_crud_farm(session):
    repository = FarmRepository(session)

    farm = Farm(
        id=None,
        name="Iron Farm",
        farm_type="Iron",
        created_by=1,
        world_id=None,
        created_at=None,
        version="1.21.8",
        coordinates=None,
        description="Testowa farma",
        productivity={},
        access_password_hash="hash",
        guide_link=None,
        favourites=0
    )

    # Test tworzenia farmy
    created = repository.create(farm)

    assert created.id is not None
    assert created.name == "Iron Farm"

    # Test znajdowania farmy po id
    found = repository.get_by_id(created.id)

    assert found is not None
    assert found.id == created.id
    assert found.name == "Iron Farm"

    # Test znajdowania nieistniejącej farmy po id
    result = repository.get_by_id(99999)

    assert result is None

    # Test znajdowania wszystkich farm
    farm2 = repository.create(farm)

    farms = repository.get_all()

    assert len(farms) == 2
    assert farms[0].id == created.id
    assert farms[1].id == farm2.id

    # Test aktualizowania farmy
    created.name = "Updated Farm"
    created.version = "1.21.9"

    updated = repository.update(created)

    assert updated is not None
    assert updated.name == "Updated Farm"
    assert updated.version == "1.21.9"

    # Test usuwania farmy
    result = repository.delete(created.id)

    assert result is True
    assert repository.get_by_id(created.id) is None

    # Test usuwania nieistniejącej farmy
    result = repository.delete(999999)

    assert result is False
