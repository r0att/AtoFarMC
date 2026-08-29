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
    access_password_hash: str = field(repr=False)
