from .invalid_entity_error import InvalidEntityError
from ..persistence.uow import get_uow
from ..persistence.errors import EntityNotFoundError
from ..persistence.model.movie import Movie


def validate_movie(movie: Movie):
    if len(movie.title) > Movie.MAX_TITLE_LEN:
        raise InvalidEntityError(f"movie's title should be at most {Movie.MAX_TITLE_LEN} characters")

    with get_uow() as uow:
        try:
            uow.director_repo.get(movie.director_id)
        except EntityNotFoundError:
            raise InvalidEntityError(f"cannot find director with id {movie.director_id}")

