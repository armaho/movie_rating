from dataclasses import field

from .entity import Entity
from .director import Director


class Movie(Entity):
    MAX_TITLE_LEN = 255

    title: str
    release_year: int
    director_id: int
    director: Director
    genres: list["Genre"] = field(default_factory=list)
