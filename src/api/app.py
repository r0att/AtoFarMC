from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from src.api.schemas import FarmResponse
from src.database.db_connection import get_session
from src.database.farm_repository import FarmRepository


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