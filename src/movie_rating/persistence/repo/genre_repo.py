from typing import Protocol

from ..model import Genre
from .repo import Repository


class GenreRepository(Repository[Genre], Protocol):
    pass
