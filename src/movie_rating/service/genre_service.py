from ..persistence.uow import UnitOfWork
from ..persistence.model import Genre


def persist_genre(genre: Genre, uow: UnitOfWork):
    with uow:
        uow.genre_repo.insert(genre)
        uow.commit()

