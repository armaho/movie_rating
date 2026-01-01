from ..persistence.model import Rating
from ..persistence.uow import UnitOfWork


def persist_rating(rating: Rating, uow: UnitOfWork):
    with uow:
        uow.rating_repo.insert(rating)
        uow.commit()


def get_rating_count_for_movie(movie_id: int, uow: UnitOfWork) -> int:
    with uow:
        return uow.rating_repo.get_rating_count_for_movie(movie_id)


def get_rating_average_for_movie(movie_id: int, uow: UnitOfWork) -> float:
    with uow:
        return uow.rating_repo.get_rating_average_for_movie(movie_id)

