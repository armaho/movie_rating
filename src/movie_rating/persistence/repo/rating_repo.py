from typing import Protocol

from ..model import Rating
from .repo import Repository


class RatingRepository(Repository[Rating], Protocol):
    def get_rating_count_for_movie(self, movie_id: int) -> int: ...
    def get_rating_average_for_movie(self, movie_id: int) -> float: ...
