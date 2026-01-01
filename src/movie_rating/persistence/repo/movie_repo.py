from typing import Protocol, Optional

from ..model import Movie
from .repo import Repository


class MovieRepository(Repository[Movie], Protocol):
    def list_movies(
            self,
            page: int,
            page_size: int,
            title: Optional[str] = None,
            release_year: Optional[int] = None,
            genre_id: Optional[int] = None) -> tuple[list[Movie], int]: ...
