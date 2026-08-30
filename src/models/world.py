"""
Model świata
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class World:
    """Reprezentacja świata."""

    id: int
    name: str
    address: str
    created_by: int
    created_at: datetime
    description: str = field(repr=False)
    access_password_hash: str = field(repr=False)
