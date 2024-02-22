# FastAPI Imports
from fastapi import FastAPI


# Uvicorn Import
import uvicorn
from app.api import healthz
from app.api.v1 import ocel

from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


app.include_router(ocel.router)
app.include_router(healthz.router)

# Root View


@app.get("/")
def root():
    return "Welcome to ocel2"


def start():
    # Starts the uvicorn backend server

    # Setting it to the Default gateway so anyone can access it with in the network
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    start()
