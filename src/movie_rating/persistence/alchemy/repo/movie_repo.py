from typing import Optional
from sqlalchemy import select

from .repo import AlchemyRepository
from ...model import Movie, Genre


class AlchemyMovieRepository(AlchemyRepository[Movie]):
    __model__ = Movie

    def list_movies(self,
                    page: int,
                    page_size: int,
                    title: Optional[str] = None,
                    release_year: Optional[int] = None,
                    genre_id: Optional[int] = None) -> tuple[list[Movie], int]:
        query = select(Movie)

        if title:
            query = query.where(Movie.title.ilike(f"%{title}%"))

        if release_year:
            query = query.where(Movie.release_year == release_year)

        if genre_id:
            query = query.join(Movie.genres).where(Genre.id == genre_id)

        total_items = self._session.execute(
                query.with_only_columns(Movie.id).order_by(None)
                ).all()
        total_count = len(total_items)

        offset = (page - 1) * page_size
        query = query.offset(offset).limit(page_size)

        movies = self._session.execute(query).scalars().all()
        return movies, total_count

