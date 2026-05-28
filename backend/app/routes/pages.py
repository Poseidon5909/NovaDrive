from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(tags=["Pages"])

templates = Jinja2Templates(
    directory=str(Path(__file__).resolve().parents[1] / "templates")
)


@router.get("/", response_class=HTMLResponse)
async def dashboard(request: Request):
    return templates.TemplateResponse(
        "dashboard/index.html",
        {
            "request": request,
            "page_title": "Dashboard",
        },
    )


@router.get("/auth/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse(
        "auth/login.html",
        {
            "request": request,
            "page_title": "Sign in",
        },
    )


@router.get("/auth/register", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse(
        "auth/register.html",
        {
            "request": request,
            "page_title": "Create account",
        },
    )
