from .post_director import router as post_director_router
from .post_genre import router as post_genre_router
from .post_movie import router as post_movie_router
from .post_rating import router as post_rating_router
from .get_movie import router as get_movie_router
from .delete_movie import router as delete_movie_router
from .update_movie import router as update_movie_router
from .get_movies_with_paging import router as get_movies_with_paging_router

__all__ = [
    "post_director_router",
    "post_genre_router",
    "post_movie_router",
    "post_rating_router",
    "get_movie_router",
    "delete_movie_router",
    "update_movie_router",
    "get_movies_with_paging_router",
]
