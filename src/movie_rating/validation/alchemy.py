from sqlalchemy import event

from ..persistence.model import Director, Genre, Movie
from .director import validate_director
from .genre import validate_genre
from .movie import validate_movie


def create_listener(callback):
    return lambda mapper, connection, target: callback(target)


def setup_validation_alchemy():
    validate_director_listener = create_listener(validate_director)

    event.listen(Director, "before_insert", validate_director_listener)
    event.listen(Director, "before_update", validate_director_listener)

    validate_genre_listener = create_listener(validate_genre)

    event.listen(Genre, "before_insert", validate_genre_listener)
    event.listen(Genre, "before_update", validate_genre_listener)

    validate_movie_listener = create_listener(validate_movie)

    event.listen(Movie, "before_insert", validate_movie_listener)
    event.listen(Movie, "before_update", validate_movie_listener)
