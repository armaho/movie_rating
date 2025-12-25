from typing import Protocol

from ..model import Movie
from .repo import Repository


class MovieRepository(Repository[Movie], Protocol):
    pass
