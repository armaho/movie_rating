from ..persistence.uow import UnitOfWork
from ..persistence.model import Movie

def update_movie(movie_id: int, data: dict, uow: UnitOfWork) -> Movie | None:
    with uow:
        movie = uow.movie_repo.get(movie_id)
        if not movie:
            return None
        for key, value in data.items():
            if value is not None:
                setattr(movie, key, value)
        uow.movie_repo.update(movie)
        uow.commit()
        return movie
