from pydantic import BaseModel


class FarmResponse(BaseModel):
    id: int
    name: str
    farm_type: str
    version: str


class FarmCreate(BaseModel):
    name: str
    farm_type: str
    version: str
    created_by: int
    world_id: int | None = None
    description: str | None = None
    guide_link: str | None = None
    access_password: str