"""
Model farmy
"""
from dataclasses import dataclass, field

@dataclass
class Farm:
    """Reprezentacja farmy"""
    farm_id: int
    name: str
    farm_type: str
    coordinated: str
    version: str
    world: str
    created_by: int = field(repr=False)
    created_at: str = field(repr=False)
    description: str = field(repr=False)
    productivity: dict = field(repr=False)
