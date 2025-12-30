from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from ...persistence.model import Rating
from ...persistence.uow import get_uow
from ...service.rating_service import persist_rating
from ...validation import InvalidEntityError

router = APIRouter()


class CreateRatingRequest(BaseModel):
    score: int


class CreateRatingSuccessResponse(BaseModel):
    status: str = Field(default="success", init=False)
    id: int


class CreateRatingFailureResponse(BaseModel):
    status: str = Field(default="failure", init=False)
    message: str


@router.post("/api/v1/movies/{movie_id}/ratings")
def create_rating(request: CreateRatingRequest, movie_id: int = Path(...)):
    rating = Rating(
        movie_id=movie_id,
        score=request.score,
    )

    try:
        with get_uow() as uow:
            persist_rating(rating, uow)
            uow.commit()
            return CreateRatingSuccessResponse(id=rating.id)

    except InvalidEntityError as iee:
        failure_response = CreateRatingFailureResponse(message=str(iee))
        return JSONResponse(
            status_code=422,
            content=failure_response.model_dump()
        )

    except Exception as e:
        failure_response = CreateRatingFailureResponse(message=str(e))
        return JSONResponse(
            status_code=500,
            content=failure_response.model_dump()
        )


