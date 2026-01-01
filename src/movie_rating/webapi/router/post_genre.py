from typing import Optional
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from ...persistence.model import Genre
from ...persistence.uow import get_uow
from ...service.genre_service import persist_genre
from ...validation import InvalidEntityError


router = APIRouter()


class CreateGenreRequest(BaseModel):
    name: str
    description: Optional[str] = Field(default=None)


class CreateGenreSuccessResponse(BaseModel):
    status: str = Field(default="success", init=None)
    id: int


class CreateGenreFailureResponse(BaseModel):
    status: str = Field(default="failure", init=False)
    message: str


@router.post("/api/v1/genres")
def create_genre(request: CreateGenreRequest):
    genre = Genre(name=request.name, description=request.description)
    
    try:
        with get_uow() as uow:
            persist_genre(genre, uow)
            uow.commit()
            return CreateGenreSuccessResponse(id=genre.id)
    except InvalidEntityError as iee:
        failure_response = CreateGenreFailureResponse(message=str(iee))
        return JSONResponse(
            status_code=422,
            content=failure_response.model_dump())
    except Exception as e:
        failure_response = CreateGenreFailureResponse(message=str(e))
        return JSONResponse(
            status_code=500,
            content=failure_response.model_dump())

        
