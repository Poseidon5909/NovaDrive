from app.repositories.user_repository import UserRepository
from app.schemas.auth import TokenResponse
from app.schemas.user import UserCreate, UserLogin, UserResponse
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
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def register(
        self,
        payload: UserCreate,
    ) -> User:

        existing_user = await self.repository.get_by_email(
            payload.email
        )

        if existing_user:
            raise UserAlreadyExistsException()

        user = await self.repository.create(
            {
                "username": payload.username,
                "email": payload.email,
                "hashed_password": hash_password(
                    payload.password
                )
            }
        )

        return user

    async def login(
        self,
        payload: UserLogin,
    ) -> TokenResponse:

        user = await self.repository.get_by_email(
            payload.email
        )

        if not user:
            raise InvalidCredentialsException()

        valid_password = verify_password(
            payload.password,
            user.hashed_password,
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
