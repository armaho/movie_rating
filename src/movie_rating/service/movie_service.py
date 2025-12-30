from ..persistence.model import Movie
from ..persistence.uow import UnitOfWork


def persist_movie(movie: Movie, uow: UnitOfWork):
    with uow:
        uow.movie_repo.insert(movie)
        uow.commit()

