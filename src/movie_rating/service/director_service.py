from ..persistence.uow import UnitOfWork
from ..persistence.model import Director


def persist_director(director: Director, uow: UnitOfWork):
    with uow:
        uow.director_repo.insert(director)
        uow.commit()

