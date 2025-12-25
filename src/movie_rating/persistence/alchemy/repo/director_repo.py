from .repo import AlchemyRepository
from ...model import Director


class AlchemyDirectorRepository(AlchemyRepository[Director]):
    __model__ = Director
