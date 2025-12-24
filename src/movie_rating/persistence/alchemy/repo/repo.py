from typing import Generic, TypeVar

from sqlalchemy.orm import Session

from ...model import Entity
from ...errors import EntityNotFoundError


TEntity = TypeVar("TEntity", bound=Entity)


class AlchemyRepository(Generic[TEntity]):
    __model__: type[TEntity]

    def __init__(self, session: Session):
        self._session = session

    def get(self, id: int) -> TEntity:
        entity = self._session.get(self.__model__, id)
        if entity is None:
            raise EntityNotFoundError(
                    f"cannot find entity \"{self.__model__.__name__}\" "
                    f"with id={id}")

        return entity

    def get_all(self) -> list[TEntity]:
        return self._session.query(self.__model__).all()

    def insert(self, entity: TEntity) -> None:
        self._session.add(entity)

    def delete(self, entity: TEntity) -> None:
        self._session.delete(entity)

    def delete_by_id(self, id: int) -> None: 
        self.delete(self.get(id))

    def count(self) -> int:
        return self._session.query(self.__model__).count()

