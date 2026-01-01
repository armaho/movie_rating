from sqlalchemy import func, select

from ...model import Rating
from .repo import AlchemyRepository


class AlchemyRatingRepository(AlchemyRepository[Rating]):
    __model__ = Rating

    def get_rating_count_for_movie(self, movie_id: int) -> int: 
        return self._session \
                .query(func.count(Rating.id)) \
                .filter(Rating.movie_id == movie_id) \
                .scalar()

    def get_rating_average_for_movie(self, movie_id: int) -> float: 
        stmt = select(func.avg(Rating.score)).where(Rating.movie_id == movie_id)
        avg = self._session.scalar(stmt)

        return float(avg) if avg is not None else 0.0

