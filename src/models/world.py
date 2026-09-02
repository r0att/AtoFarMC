"""
Model świata
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class World:
    """Reprezentacja świata."""

    id: int | None
    name: str
    address: str
    created_by: int
    created_at: datetime
    favourites: int | None = field(repr=False)
    description: str | None = field(repr=False)
    access_password_hash: str = field(repr=False)
