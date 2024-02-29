# FastAPI Imports
from fastapi import FastAPI

# Uvicorn Import
import uvicorn
from app.api import healthz
from app.api.v1.v1_router import v1_router

# Local Imports
from app.core.config import settings
from app.custom_logger import logger
from app.db.session import SessionLocal

# Starting the database session
session = SessionLocal()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
)


app.include_router(healthz.router)
app.include_router(v1_router, prefix=settings.API_V1_STR)


# Root View
@app.get("/")
def root():
    return "Welcome to ocel2-fastapi"


# Help you debug if you want to run it without VS code debugger
def start():
    try:
        # Setting it to the Default gateway so anyone can access it with in the network
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
        logger.info("Server is UP!!!! ")
    except Exception as e:
        logger.error(f"The Server couldn't load because of {str(e)}")


if __name__ == "__main__":
    start()
