from ...model import Rating
from .repo import AlchemyRepository


class AlchemyRatingRepository(AlchemyRepository[Rating]):
    __model__ = Rating
