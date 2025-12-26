from sqlalchemy import event

from ..persistence.model import Director
from .director import validate_director


def create_listener(callback):
    return lambda mapper, connection, target: callback(target)

def setup_validation_alchemy():
    validate_director_listener = create_listener(validate_director)

    event.listen(Director, "before_insert", validate_director_listener)
    event.listen(Director, "before_update", validate_director_listener)
