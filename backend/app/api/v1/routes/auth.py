from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.auth import Token
from app.schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse,
)
from app.services.auth_service import AuthService

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse,
)
async def register(
    user_data: UserCreate,
    db: AsyncSession = Depends(get_db),
):
    repository = UserRepository(db)

    service = AuthService(repository)

    return await service.register(user_data)


@router.post(
    "/login",
    response_model=Token,
)
async def login(
    user_data: UserLogin,
    db: AsyncSession = Depends(get_db),
):
    repository = UserRepository(db)

    service = AuthService(repository)

    return await service.login(user_data) 
