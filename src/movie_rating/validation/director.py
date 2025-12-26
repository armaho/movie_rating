from .invalid_entity_error import InvalidEntityError
from ..persistence.model.director import Director


def validate_director(director: Director):
    if len(director.name) > Director.MAX_NAME_LEN:
        raise InvalidEntityError(f"Director's name should be at most {Director.MAX_NAME_LEN} characters.")

    if director.description is not None and len(director.description) > Director.MAX_DESC_LEN:
        raise InvalidEntityError(f"Director's description should be at most {Director.MAX_DESC_LEN} characters.")

