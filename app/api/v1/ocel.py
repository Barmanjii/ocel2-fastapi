# FastAPI Import
from fastapi import APIRouter, Depends

# Local Python Import
from app.api import deps
from app.db import session
from app.models.request_model import RequestModel, EventTypeModel

router = APIRouter(prefix="/ocel2", tags=["Ocel2"])


@router.post("/")
def test(request_model: EventTypeModel, db: session = Depends(deps.get_db)):
    return "Hello World"
