from typing import List
from pydantic import BaseModel
from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse

from ...persistence.uow import get_uow
from ...persistence.errors import EntityNotFoundError
from ...service.movie_service import update_movie

router = APIRouter()

class UpdateMovieRequest(BaseModel):
    title: str
    director_id: int
    release_year: int
    genre_ids: List[int]  # changed from "genres" to "genre_ids" to match spec

@router.post("/api/v1/movies/{movie_id}")
def update_movie_api(request: UpdateMovieRequest, movie_id: int = Path(...)):
    try:
        with get_uow() as uow:
            movie = update_movie(
                movie_id=movie_id,
                title=request.title,
                director_id=request.director_id,
                release_year=request.release_year,
                genres=request.genre_ids, 
                uow=uow
            )
            return {
                "id": movie.id,
                "title": movie.title,
                "director": {"id": movie.director.id, "name": movie.director.name},
                "genres": [{"id": g.id, "name": g.name} for g in movie.genres],
                "release_year": movie.release_year
            }
    except EntityNotFoundError as e:
        return JSONResponse(
            status_code=404,
            content={"status": "failure", "message": str(e)}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"status": "failure", "message": str(e)}
        )
