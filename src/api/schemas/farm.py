from pydantic import BaseModel


class FarmResponse(BaseModel):
    id: int
    name: str
    farm_type: str
    version: str