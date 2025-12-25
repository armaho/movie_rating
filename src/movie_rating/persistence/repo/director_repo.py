from typing import Protocol

from ..model import Director
from .repo import Repository


class DirectorRepository(Repository[Director], Protocol):
    pass
