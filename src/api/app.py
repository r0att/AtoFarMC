from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
import bcrypt

from src.api.schemas import FarmCreate, FarmResponse
from src.database.db_connection import get_session
from src.database.farm_repository import FarmRepository
from src.models import Farm


app = FastAPI()


@app.get("/farms", response_model=list[FarmResponse])
def get_farms(session: Session = Depends(get_session)) -> list[FarmResponse]:
    repository = FarmRepository(session)
    farms = repository.get_all()

    return [
        FarmResponse(
            id=farm.id,
            name=farm.name,
            farm_type=farm.farm_type,
            version=farm.version
        )
        for farm in farms
    ]

@app.post("/farms", response_model=FarmResponse)
def create_farm(
    farm: FarmCreate,
    session: Session = Depends(get_session)
) -> FarmResponse:
    password_hash = bcrypt.hashpw(
        farm.access_password.encode(),
        bcrypt.gensalt()
    ).decode()

    farm_model = Farm(
        id=None,
        name=farm.name,
        farm_type=farm.farm_type,
        created_by=farm.created_by,
        world_id=farm.world_id,
        created_at=None,
        version=farm.version,
        coordinates=None,
        description=farm.description,
        productivity={},
        access_password_hash=password_hash,
        guide_link=farm.guide_link,
        favourites=0
    )

    repository = FarmRepository(session)
    created = repository.create(farm_model)

    return FarmResponse(
        id=created.id,
        name=created.name,
        farm_type=created.farm_type,
        version=created.version
    )