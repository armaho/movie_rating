from fastapi import APIRouter, Query
from fastapi.responses import JSONResponse

from ...persistence.uow import get_uow
from ...service.movie_service import list_movies
from ...service.rating_service import get_rating_average_for_movie

router = APIRouter()

@router.get("/api/v1/movies")
def get_movies(
    page: int = Query(..., ge=1),
    page_size: int = Query(..., ge=1),
    title: str | None = Query(None),
    release_year: int | None = Query(None),
    genre: int | None = Query(None),
):
    try:
        with get_uow() as uow:
            movies, total_items = list_movies(
                page=page,
                page_size=page_size,
                title=title,
                release_year=release_year,
                genre=genre,
                uow=uow
            )

            items = []
            for movie in movies:
                items.append({
                    "id": movie.id,
                    "title": movie.title,
                    "release_year": movie.release_year,
                    "director": {
                        "id": movie.director.id,
                        "name": movie.director.name
                    },
                    "genres": [g.name for g in movie.genres],
                    "average_rating": get_rating_average_for_movie(movie.id, uow)
                })

            return {
                "page": page,
                "page_size": page_size,
                "total_items": total_items,
                "items": items
            }
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "failure", "message": str(e)}
        )
