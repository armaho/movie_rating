from .entity import Entity
from .movie import Movie


class Rating(Entity):
    MIN_SCORE = 0
    MAX_SCORE = 10

    movie_id: int
    movie: Movie
    score: int
