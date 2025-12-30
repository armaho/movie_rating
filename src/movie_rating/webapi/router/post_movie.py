import traceback

from typing import List
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

from ...persistence.model import Movie
from ...persistence.uow import get_uow
from ...persistence.errors import EntityNotFoundError
from ...service.movie_service import persist_movie
from ...validation import InvalidEntityError


router = APIRouter()


class CreateMovieRequest(BaseModel):
    title: str
    director_id: int
    release_year: int
    genres: List[int]


class CreateMovieSuccessResponse(BaseModel):
    status: str = Field(default="success", init=False)
    id: int


class CreateMovieFailureResponse(BaseModel):
    status: str = Field(default="failure", init=False)
    message: str


@router.post("/api/v1/movies")
def create_movie(request: CreateMovieRequest):
    movie = Movie(
        title=request.title,
        release_year=request.release_year,
        director_id=request.director_id
    )

    try:
        with get_uow() as uow:
            for genre_id in request.genres:
                movie.genres.append(uow.genre_repo.get(genre_id))
            persist_movie(movie, uow)
            uow.commit()
            return CreateMovieSuccessResponse(id=movie.id)

    except InvalidEntityError as iee:
        return JSONResponse(
            status_code=422,
            content=CreateMovieFailureResponse(
                message=str(iee)
            ).model_dump()
        )

    except EntityNotFoundError as enfe:
        return JSONResponse(
            status_code=422,
            content=CreateMovieFailureResponse(
                message=str(enfe)
            ).model_dump()
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content=CreateMovieFailureResponse(
                message=str(e)
            ).model_dump() | {
                "traceback": traceback.format_exc()
            },
        )

