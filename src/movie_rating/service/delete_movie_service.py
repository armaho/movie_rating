from ..persistence.uow import UnitOfWork
from ..persistence.model import Movie

def delete_movie(movie_id: int, uow: UnitOfWork) -> bool:
    with uow:
        success = uow.movie_repo.delete(movie_id)
        if success:
            uow.commit()
        return success
