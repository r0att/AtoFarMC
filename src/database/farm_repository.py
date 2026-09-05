from sqlalchemy.orm import Session
from sqlalchemy import select, asc, desc
from src.models import Farm
from src.database.table_models import FarmTable


class FarmRepository:
    def __init__(self, session: Session):
        self.session = session


    def create(self, farm: Farm) -> Farm:
        """Dodaje farmę do bazy."""

        farm_table = self._to_table(farm)

        self.session.add(farm_table)
        self.session.flush()

        # Zwraca Farm z wartościami przypisanymi przez BD
        return self._to_domain(farm_table)


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

        stmt = select(FarmTable)

        farm_tables = self.session.scalars(stmt).all()

        return [self._to_domain(farm_table) for farm_table in farm_tables]


    def search(
            self,
            name: str | None = None,
            farm_type: str | None = None,
            version: str | None = None,
            world_id: int | None = None,
            created_by: int | None = None,
            has_guide: bool | None = None,
            sort_by: str | None = None,
            descending: bool = True
    ) -> list[Farm]:
        """Wyszukuje farmy po argumentach."""

        stmt = select(FarmTable)

        if name is not None:
            stmt = stmt.where(FarmTable.name.ilike(f"{name}%"))
        if farm_type is not None:
            stmt = stmt.where(FarmTable.farm_type.ilike(f"{farm_type}%"))
        if version is not None:
            stmt = stmt.where(FarmTable.version.ilike(f"{version}%"))
        if world_id is not None:
            stmt = stmt.where(FarmTable.world_id == world_id)
        if created_by is not None:
            stmt = stmt.where(FarmTable.created_by == created_by)
        if has_guide is not None:
            stmt = stmt.where(FarmTable.guide_link.is_not(None)) if has_guide else stmt.where(FarmTable.guide_link.is_(None))

        sort_columns = {
            "created_at": FarmTable.created_at,
            "name": FarmTable.name,
            "favourites": FarmTable.favourites
        }
        column = sort_columns.get(sort_by, FarmTable.favourites)
        stmt = stmt.order_by(desc(column) if descending else asc(column))

        farm_tables = self.session.scalars(stmt).all()

        return [self._to_domain(farm_table) for farm_table in farm_tables]


    @staticmethod
    def _to_domain(farm_table: FarmTable) -> Farm:
        """Konwertuje FarmTable na Farm."""

        return Farm(
            id = farm_table.id,
            name = farm_table.name,
            farm_type = farm_table.farm_type,
            created_by = farm_table.created_by,
            world_id = farm_table.world_id,
            created_at = farm_table.created_at,
            version = farm_table.version,
            coordinates = (
                (farm_table.x, farm_table.y, farm_table.z)
                if farm_table.x is not None
                else None
            ),
            description = farm_table.description,
            productivity = farm_table.productivity,
            access_password_hash = farm_table.access_password_hash,
            guide_link = farm_table.guide_link,
            favourites = farm_table.favourites
        )


    @staticmethod
    def _to_table(farm: Farm) -> FarmTable:
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
            guide_link = farm.guide_link,
            favourites = farm.favourites
        )
    