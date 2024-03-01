# FastAPI Import
from fastapi import APIRouter, Depends

# Local Python Import
from app.api import deps
from app.db import session
from app.custom_logger import logger
from app.crud.crud_event_type import eventType
from app.models.request_model import RequestModel, EventTypeModel

router = APIRouter(prefix="/ocel2", tags=["Ocel2"])


@router.post("/")
def test(request_model: EventTypeModel, db: session = Depends(deps.get_db)):
    try:
        req = eventType.create(obj_in=request_model, db=db)
        logger.info("Worked!!")
        return req
    except Exception as e:
        logger.error(f"Exception While testing : {str(e)}")
