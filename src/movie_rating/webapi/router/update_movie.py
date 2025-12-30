from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional
from ...persistence.uow import get_uow
from ...persistence.errors import EntityNotFoundError
from ...service.update_movie_service import update_movie

router = APIRouter()

class UpdateMovieRequest(BaseModel):
    title: Optional[str] = None
    release_year: Optional[int] = None
    director_id: Optional[int] = None

@router.post("/api/v1/movies/{movie_id}")
def update_movie_api(request: UpdateMovieRequest, movie_id: int = Path(...)):
    try:
        with get_uow() as uow:
            movie = update_movie(movie_id, request.model_dump(), uow)
            if not movie:
                raise EntityNotFoundError(f"Movie {movie_id} not found")
            return {"status": "success", "id": movie.id}
    except EntityNotFoundError as e:
        return JSONResponse(status_code=404, content={"status": "failure", "message": str(e)})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "failure", "message": str(e)})
