from fastapi import APIRouter

from . import ocel


v1_router = APIRouter()
v1_router.include_router(ocel.router)
