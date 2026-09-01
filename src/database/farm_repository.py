from sqlalchemy.orm import Session
from sqlalchemy import select
from src.models import Farm
from src.database.table_models import FarmTable


class FarmRepository:
    def __init__(self, session: Session):
        self.session = session


    def create(self, farm: Farm) -> Farm:
        """Dodaje farmę do bazy."""

        farm_model = self._to_model(farm)

        self.session.add(farm_model)
        self.session.flush()

        # Zwraca Farm z wartościami przypisanymi przez BD
        return self._to_domain(farm_model)


    def delete(self, farm_id: int) -> bool:
        """Usuwa farmę z bazy."""

        farm_table = self.session.get(FarmTable, farm_id)

        if farm_table is None:
            return False

        self.session.delete(farm_table)
        self.session.flush()

        return True


    def update(self, farm: Farm) -> Farm | None:
        """Aktualizuje tabelę."""

        farm_table = self.session.get(FarmTable, farm.id)

        if farm_table is None:
            return None

        x, y, z = farm.coordinates if farm.coordinates else (None, None, None)

        farm_table.name = farm.name
        farm_table.farm_type = farm.farm_type
        farm_table.version = farm.version
        farm_table.created_by = farm.created_by
        farm_table.world_id = farm.world_id
        farm_table.x = x
        farm_table.y = y
        farm_table.z = z
        farm_table.description = farm.description
        farm_table.guide_link = farm.guide_link
        farm_table.productivity = farm.productivity
        farm_table.access_password_hash = farm.access_password_hash

        self.session.flush()

        return self._to_domain(farm_table)


    def get_by_id(self, farm_id: int) -> Farm | None:
        """Wyszukuje farmę po id."""

        farm_table = self.session.get(FarmTable, farm_id)

        if farm_table is None:
            return None

        return self._to_domain(farm_table)


    def get_all(self) -> list[Farm]:
        """Zwraca wszystkie farmy."""

        farm_tables = self.session.scalars(select(FarmTable)).all()

        return [self._to_domain(farm) for farm in farm_tables]


    @staticmethod
    def _to_domain(farm_model: FarmTable) -> Farm:
        """Konwertuje FarmTable na Farm."""

        return Farm(
            id = farm_model.id,
            name = farm_model.name,
            farm_type = farm_model.farm_type,
            created_by = farm_model.created_by,
            world_id = farm_model.world_id,
            created_at = farm_model.created_at,
            version = farm_model.version,
            coordinates = (farm_model.x, farm_model.y, farm_model.z) if farm_model.x else None,
            description = farm_model.description,
            productivity = farm_model.productivity,
            access_password_hash = farm_model.access_password_hash,
            guide_link = farm_model.guide_link,
        )


    @staticmethod
    def _to_model(farm: Farm) -> FarmTable:
        """Konwertuje Farm na FarmTable."""

        x, y, z = farm.coordinates if farm.coordinates else (None, None, None)

        return FarmTable(
            id = farm.id,
            name = farm.name,
            farm_type = farm.farm_type,
            created_by = farm.created_by,
            world_id = farm.world_id,
            created_at = farm.created_at,
            version = farm.version,
            x = x,
            y = y,
            z = z,
            description = farm.description,
            productivity = farm.productivity,
            access_password_hash = farm.access_password_hash,
            guide_link = farm.guide_link
        )
    