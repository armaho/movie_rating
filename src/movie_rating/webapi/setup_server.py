import uvicorn

from fastapi import FastAPI

from .router import post_director_router

def setup_server(port: int):
    app = FastAPI()

    app.include_router(post_director_router)

    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")

