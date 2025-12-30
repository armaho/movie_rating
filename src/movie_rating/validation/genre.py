from .invalid_entity_error import InvalidEntityError
from ..persistence.model.genre import Genre


def validate_genre(genre: Genre):
    if len(genre.name) > Genre.MAX_NAME_LEN:
        raise InvalidEntityError(f"genre's name should be at most {Genre.MAX_NAME_LEN} characters")

    if genre.description is not None and len(genre.description) > Genre.MAX_DESC_LEN:
        raise InvalidEntityError(f"genre's description should be at most {Genre.MAX_DESC_LEN} characters")

