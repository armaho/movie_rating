from dataclasses import dataclass, field

from .entity import Entity
from .movie import Movie


@dataclass
class Rating(Entity):
    MIN_SCORE = 0
    MAX_SCORE = 10

    movie_id: int
    movie: Movie = field(init=False)
    score: int
