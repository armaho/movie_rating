from abc import ABC, abstractmethod

class UnitOfWork(ABC):
    @abstractmethod
    def rollback(self) -> None:
        pass

    @abstractmethod
    def commit(self) -> None:
        pass

    def __enter__(self) -> UnitOfWork:
        return self

    def __exit__(self, *args) -> None:
        self.rollback()
    

