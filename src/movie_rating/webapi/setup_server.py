import uvicorn

from fastapi import FastAPI

from .router import (
    post_director_router,
    post_genre_router,
    post_movie_router,
    post_rating_router,
    get_movie_router,
    delete_movie_router,
    update_movie_router,
    get_movies_with_paging_router,
)

def setup_server(port: int):
    app = FastAPI()

    app.include_router(post_director_router)
    app.include_router(post_genre_router)
    app.include_router(post_movie_router)
    app.include_router(post_rating_router)
    app.include_router(get_movies_with_paging_router)
    app.include_router(get_movie_router)
    app.include_router(delete_movie_router)
    app.include_router(update_movie_router)

    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
