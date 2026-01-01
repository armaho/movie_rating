from .invalid_entity_error import InvalidEntityError
from ..persistence.uow import get_uow
from ..persistence.errors import EntityNotFoundError
from ..persistence.model import Rating


def validate_rating(rating: Rating):
    if not (Rating.MIN_SCORE <= rating.score <= Rating.MAX_SCORE):
        raise InvalidEntityError(
            f"Rating score must be between {Rating.MIN_SCORE} and {Rating.MAX_SCORE}"
        )

    with get_uow() as uow:
        try:
            uow.movie_repo.get(rating.movie_id)
        except EntityNotFoundError:
            raise InvalidEntityError(f"Cannot find movie with id {rating.movie_id}")

