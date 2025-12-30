from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse

from ...persistence.uow import get_uow
from ...persistence.errors import EntityNotFoundError
from ...service.movie_service import get_movie

router = APIRouter()

@router.get("/api/v1/movies/{movie_id}")
def get_movie_details(movie_id: int = Path(...)):
    try:
        with get_uow() as uow:
            movie = get_movie(movie_id, uow)
            if not movie:
                raise EntityNotFoundError(f"Movie with id {movie_id} not found")

          
            return {
                "id": movie.id,
                "title": movie.title,
                "director": {
                    "id": movie.director.id,
                    "name": movie.director.name
                },
                "genres": [{"id": g.id, "name": g.name} for g in movie.genres],
                "release_year": movie.release_year,
                "ratings": [r.score for r in getattr(movie, "ratings", [])]  # optional
            }

    except EntityNotFoundError as enfe:
        return JSONResponse(
            status_code=404,
            content={"status": "failure", "message": str(enfe)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "failure", "message": str(e)}
        )
