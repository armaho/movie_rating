from dataclasses import field, dataclass
from typing import Optional
from .entity import Entity


@dataclass
class Director(Entity):
    MAX_NAME_LEN = 255
    MAX_DESC_LEN = 255

    name: str
    birth_year: int
    description: Optional[str] = field(default=None)
