from dataclasses import dataclass, field
from typing import Optional, List

from .entity import Entity


@dataclass
class Genre(Entity):
    MAX_NAME_LEN = 255
    MAX_DESC_LEN = 255

    name: str
    description: Optional[str] = field(default=None)
    movies: List["Movie"] = field(default_factory=list)
