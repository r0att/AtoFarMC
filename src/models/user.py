"""
Model użytkownika
"""
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class User:
    """Reprezentacja użytkownika."""

    id: int | None
    login: str
    email: str
    is_superuser: bool
    created_at: datetime
    password_hash: str = field(repr=False)
    description: str | None = field(repr=False)
