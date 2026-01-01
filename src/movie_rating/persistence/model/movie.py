from dataclasses import field, dataclass

from .entity import Entity
from .director import Director


@dataclass
class Movie(Entity):
    MAX_TITLE_LEN = 255

    title: str
    release_year: int
    director_id: int
    director: Director = field(init=False)
    genres: list["Genre"] = field(default_factory=list)
