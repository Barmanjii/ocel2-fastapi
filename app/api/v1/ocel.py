# FastAPI Import
from fastapi import APIRouter


router = APIRouter(prefix="/ocel2", tags=["Ocel2"])


@router.get("/")
def test():
    return "Hello World"
