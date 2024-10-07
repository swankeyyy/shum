from fastapi import APIRouter
from core.config import settings
from .api_v1 import router as api_v1
router = APIRouter()
router.include_router(api_v1)
