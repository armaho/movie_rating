from .repo import AlchemyRepository
from ...model import Movie


class AlchemyMovieRepository(AlchemyRepository[Movie]):
    __model__ = Movie
