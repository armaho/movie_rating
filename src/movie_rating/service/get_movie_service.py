from ..persistence.uow import UnitOfWork
from ..persistence.model import Movie

def get_movie(movie_id: int, uow: UnitOfWork) -> Movie | None:
    with uow:
        movie = uow.movie_repo.get(movie_id)
        return movie
