from typing import Protocol

from ..model import Rating
from .repo import Repository


class RatingRepository(Repository[Rating], Protocol):
    pass
