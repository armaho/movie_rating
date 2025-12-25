from ...model import Genre
from .repo import AlchemyRepository


class AlchemyGenreRepository(AlchemyRepository[Genre]):
    __model__ = Genre
