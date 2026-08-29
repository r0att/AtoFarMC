"""
Model współrzędnych
"""
from dataclasses import dataclass


@dataclass
class Coordinates:
    """Reprezentacja współrzędnych."""
    
    x: float
    y: float
    z: float
