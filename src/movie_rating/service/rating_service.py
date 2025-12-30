from ..persistence.model import Rating
from ..persistence.uow import UnitOfWork


def persist_rating(rating: Rating, uow: UnitOfWork):
    with uow:
        uow.rating_repo.insert(rating)
        uow.commit()
