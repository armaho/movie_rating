from fastapi import APIRouter, Path
from fastapi.responses import Response, JSONResponse
from ...persistence.uow import get_uow
from ...persistence.errors import EntityNotFoundError
from ...service.movie_service import delete_movie  

router = APIRouter()

@router.delete("/api/v1/movies/{movie_id}")
def remove_movie(movie_id: int = Path(...)):
    try:
        with get_uow() as uow:
            delete_movie(movie_id, uow)
            
            return Response(status_code=204)

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
