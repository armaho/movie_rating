from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from ...persistence.uow import get_uow
from ...persistence.errors import EntityNotFoundError
from ...service.delete_movie_service import delete_movie

router = APIRouter()

@router.delete("/api/v1/movies/{movie_id}")
def delete_movie_api(movie_id: int = Path(...)):
    try:
        with get_uow() as uow:
            success = delete_movie(movie_id, uow)
            if not success:
                raise EntityNotFoundError(f"Movie {movie_id} not found")
            return {"status": "success", "message": "Movie deleted successfully"}
    except EntityNotFoundError as e:
        return JSONResponse(status_code=404, content={"status": "failure", "message": str(e)})
    except Exception as e:
        return JSONResponse(status_code=500, content={"status": "failure", "message": str(e)})
