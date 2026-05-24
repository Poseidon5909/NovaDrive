from fastapi import APIRouter

from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.readiness import router as readiness_router

api_router = APIRouter()

api_router.include_router(
    health_router,
    prefix="/health",
    tags=["Health"]
)

api_router.include_router(
  readiness_router,
  prefix="/readiness",
  tags=["Readiness"],
)