from sqlalchemy.orm import Session
from src.models import World
from src.database.table_models import WorldTable


class WorldRepository:
    def __init__(self, session: Session):
        self.session = session
    

    def create(self, world: World) -> World:
        """Dodaje świat do bazy."""

        world_table = self._to_table(world)

        self.session.add(world_table)
        self.session.flush()

        return self._to_domain(world_table)


    def delete(self, world_id: int) -> bool:
        """Usuwa świat z bazy."""

        world_table = self.session.get(WorldTable, world_id)

        if world_table is None:
            return False

        self.session.delete(world_table)
        self.session.flush()

        return True


    @staticmethod
    def _to_table(world: World) -> WorldTable:
        """Konwertuje World na WorldTable."""

        return WorldTable(
            id = world.id,
            name = world.name,
            address = world.address,
            created_by = world.created_by,
            created_at = world.created_at,
            favourites = world.favourites,
            description = world.description,
            access_password_hash = world.access_password_hash
        ) 


    @staticmethod
    def _to_domain(world_table: WorldTable) -> World:
        """Konwertuje WorldTable na World."""

        return World(
            id = world_table.id,
            name = world_table.name,
            address = world_table.address,
            created_by = world_table.created_by,
            created_at = world_table.created_at,
            favourites = world_table.favourites,
            description = world_table.description,
            access_password_hash = world_table.access_password_hash
        )
        
        