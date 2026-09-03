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
    rank: str | None
    is_superuser: bool
    created_at: datetime
    friends: list["User"] = field(repr=False)
    followers: int | None = field(repr=False)
    password_hash: str = field(repr=False)
    description: str | None = field(repr=False)
