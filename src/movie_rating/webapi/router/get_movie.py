from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from ...persistence.uow import get_uow
from ...persistence.errors import EntityNotFoundError
from ...service.get_movie_service import get_movie

router = APIRouter()

@router.get("/api/v1/movies/{movie_id}")
def get_movie_api(movie_id: int = Path(...)):
    try:
        with get_uow() as uow:
            movie = get_movie(movie_id, uow)
            if not movie:
                raise EntityNotFoundError(f"Movie {movie_id} not found")
            return movie.model_dump()  
    except EntityNotFoundError as e:
        return JSONResponse(status_code=404, content={"status": "failure", "message": str(e)})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "failure", "message": str(e)})
