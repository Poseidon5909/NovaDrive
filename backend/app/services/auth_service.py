from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.user_repository import user_repository
from app.schemas.auth import (
    RegisterRequest,
    TokenResponse,
)
from app.schemas.user import UserResponse
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)
from app.core.exceptions import (
    InvalidCredentialsException,
    UserAlreadyExistsException,
)
from app.models.user import User


class AuthService:

    async def register_user(
        self,
        db: AsyncSession,
        payload: RegisterRequest
    ) -> User:

        existing_user = await user_repository.get_by_email(
            db,
            payload.email
        )

        if existing_user:
            raise UserAlreadyExistsException()

        user = await user_repository.create(
            db,
            {
                "email": payload.email,
                "full_name": payload.full_name,
                "hashed_password": hash_password(
                    payload.password
                )
            }
        )

        return user

    async def login_user(
        self,
        db: AsyncSession,
        email: str,
        password: str
    ) -> TokenResponse:

        user = await user_repository.get_by_email(
            db,
            email
        )

        if not user:
            raise InvalidCredentialsException()

        valid_password = verify_password(
            password,
            user.hashed_password
        )

        if not valid_password:
            raise InvalidCredentialsException()

        token = create_access_token(
            str(user.id)
        )

        return TokenResponse(
            access_token=token,
            token_type="bearer",
            user=UserResponse.model_validate(user)
        )


auth_service = AuthService()