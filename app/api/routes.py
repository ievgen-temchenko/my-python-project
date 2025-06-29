from fastapi import APIRouter
from app.api.endpoints import items

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(items.router, prefix="/items", tags=["items"])
