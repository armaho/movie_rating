import uvicorn

from fastapi import FastAPI

def setup_server(port: int):
    app = FastAPI()

    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")

