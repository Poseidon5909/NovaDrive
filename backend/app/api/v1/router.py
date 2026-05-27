from fastapi import APIRouter

from app.api.v1.routes.auth import router as auth_router
from app.api.v1.routes.health import router as health_router
from app.api.v1.routes.readiness import router as readiness_router

api_router = APIRouter()

# Health Routes
api_router.include_router(
    health_router,
    prefix="/health",
    tags=["Health"],
)

# Readiness Routes
api_router.include_router(
    readiness_router,
    prefix="/readiness",
    tags=["Readiness"],
)

# Authentication Routes
api_router.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"],
)