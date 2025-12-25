from dataclasses import dataclass, field
from typing import Optional

from .entity import Entity


@dataclass
class Genre(Entity):
    MAX_NAME_LEN = 255
    MAX_DESC_LEN = 255

    name: str
    description: Optional[str] = field(default=None)
