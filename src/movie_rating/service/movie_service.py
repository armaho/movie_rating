from ..persistence.model import Movie
from ..persistence.uow import UnitOfWork


# We're getting genre_ids seprately cause we had bugs defining the field genre_ids.
# We should fix this.
def persist_movie(movie: Movie, genre_ids: list[int], uow: UnitOfWork):
    with uow:
        for genre_id in genre_ids:
            genre = uow.genre_repo.get(genre_id)
            movie.genres.append(genre)
        uow.movie_repo.insert(movie)
        uow.commit()

