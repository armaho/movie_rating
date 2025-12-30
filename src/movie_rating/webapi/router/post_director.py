from typing import Optional
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from urllib.parse import urlparse
from pydantic import BaseModel, Field

from ...persistence.model.director import Director
from ...persistence.uow import get_uow
from ...service.director_service import persist_director
from ...validation import InvalidEntityError


router = APIRouter()


class CreateDirectorRequest(BaseModel):
    name: str
    birth_year: int
    description: Optional[str] = Field(default=None)


class CreateDirectorSuccessResponse(BaseModel):
    status: str = Field(default="success", init=None)
    id: int


class CreateDirectorFailureResponse(BaseModel):
    status: str = Field(default="failure", init=False)
    message: str


@router.post("/api/v1/directors")
def create_director(request: CreateDirectorRequest):
    director = Director(request.name, request.birth_year, request.description)
    
    try:
        with get_uow() as uow:
            persist_director(director, uow)
            uow.commit()
            return CreateDirectorSuccessResponse(id=director.id)
    except InvalidEntityError as iee:
        failure_response = CreateDirectorFailureResponse(message=str(iee))
        return JSONResponse(
            status_code=422,
            content=failure_response.model_dump())
    except Exception as e:
        failure_response = CreateDirectorFailureResponse(message=str(e))
        return JSONResponse(
            status_code=500,
            content=failure_response.model_dump())

        
