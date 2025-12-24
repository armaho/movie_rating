from dataclasses import dataclass, field

@dataclass
class Entity:
    id: int = field(default=0, init=False)

