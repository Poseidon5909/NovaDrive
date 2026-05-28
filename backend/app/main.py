from contextlib import asynccontextmanager
from pathlib import Path

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi import Request
from fastapi.staticfiles import StaticFiles

from app.api.v1.router import api_router
from app.core.config import settings
from app.core.exceptions import AppException
from app.middleware.logging_middleware import LoggingMiddleware
from app.middleware.timing_middleware import TimingMiddleware
from app.routes.pages import router as pages_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting application...")
    
    # Future Initializations:
    # Redis
    # MinIO
    # Kafka
    # Background workers

    yield

    print("Shutting down application...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan,
)

static_dir = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")


# Middleware Registration

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(LoggingMiddleware)
app.add_middleware(TimingMiddleware)

# Exception Handlers

@app.exception_handler(AppException)
async def app_exception_handler(
    request: Request,
    exc: AppException,
):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.message,
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,
):
    return JSONResponse(
        status_code=422,
        content={
            "success": False,
            "message": "Validation Error",
            "errors": exc.errors(),
        },
    )


@app.exception_handler(Exception)
async def global_exception_handler(
    request: Request,
    exc: Exception,
):
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "message": "Internal Server Error",
        },
    )

# API Router Registration

app.include_router(pages_router)

app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX,
)