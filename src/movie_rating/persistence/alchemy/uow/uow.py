from sqlalchemy.orm import sessionmaker

from ...uow import UnitOfWork


class AlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory: sessionmaker) -> None:
        self.__session_factory = session_factory
        self.__ref = 0

    def __enter__(self) -> UnitOfWork:
        if self.__ref == 0:
            self.__session = self.__session_factory()

        self.__ref += 1

        return super().__enter__()

    def __exit__(self, *args) -> None:
        if self.__ref == 1:
            super().__exit__(*args)
            self.__session.close()

        self.__ref -= 1

    def commit(self) -> None:
        if self.__ref == 1:
            self.__session.commit()

    def rollback(self) -> None:
        self.__session.rollback()
