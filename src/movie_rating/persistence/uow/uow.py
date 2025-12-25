from abc import ABC, abstractmethod

from ..repo import DirectorRepository, GenreRepository, MovieRepository, RatingRepository

class UnitOfWork(ABC):
    director_repo: DirectorRepository
    genre_repo: GenreRepository
    movie_repo: MovieRepository
    rating_repo: RatingRepository

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
    

