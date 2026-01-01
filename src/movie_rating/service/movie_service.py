from typing import List, Optional

from ..persistence.model import Movie
from ..persistence.uow import UnitOfWork


def persist_movie(movie: Movie, uow: UnitOfWork):
    with uow:
        uow.movie_repo.insert(movie)
        uow.commit()


def get_movie(movie_id: int, uow: UnitOfWork) -> Movie:
    with uow:
        return uow.movie_repo.get(movie_id)


def delete_movie(movie_id: int, uow: UnitOfWork):
    with uow:
        movie = uow.movie_repo.get(movie_id)
        uow.movie_repo.delete(movie)
        uow.commit()


def update_movie(
    movie_id: int,
    title: str,
    director_id: int,
    release_year: int,
    genres: List[int],
    uow: UnitOfWork
) -> Movie:
    with uow:
        movie = uow.movie_repo.get(movie_id)

        movie.title = title
        movie.director_id = director_id
        movie.release_year = release_year

        movie.genres.clear()
        for genre_id in genres:
            movie.genres.append(uow.genre_repo.get(genre_id))

        uow.commit()
        return movie

def list_movies(
    page: int,
    page_size: int,
    title: Optional[str],
    release_year: Optional[int],
    genre: Optional[int],
    uow: UnitOfWork
) -> tuple[list[Movie], int]:
    movies, total_count = uow.movie_repo.list_movies(
        page=page,
        page_size=page_size,
        title=title,
        release_year=release_year,
        genre_id=genre
    )
    return movies, total_count
