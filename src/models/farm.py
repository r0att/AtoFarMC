"""
Model farmy
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Farm:
    """Reprezentacja farmy."""

    id: int | None
    name: str
    farm_type: str
    created_by: int
    world_id: int | None
    created_at: datetime | None
    favourites: int | None = field(repr=False)
    version: str = field(repr=False)
    coordinates: tuple[int, int, int] | None = field(repr=False)
    description: str | None = field(repr=False)
    productivity: dict[str, float] = field(repr=False)
    access_password_hash: str = field(repr=False)
    guide_link: str | None = field(repr=False)
    