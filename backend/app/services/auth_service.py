from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.repositories.user_repository import UserRepository


class AuthService:
    def __init__(
        self,
        user_repository: UserRepository,
    ):
        self.user_repository = user_repository

    async def register(
        self,
        user_data,
    ):
        existing_user = await self.user_repository.get_by_email(
            user_data.email
        )

        if existing_user:
            raise Exception("User already exists")

        hashed_password = hash_password(
            user_data.password
        )

        user = await self.user_repository.create(
            {
                "username": user_data.username,
                "email": user_data.email,
                "hashed_password": hashed_password,
            }
        )

        return user

    async def login(
        self,
        user_data,
    ):
        user = await self.user_repository.get_by_email(
            user_data.email
        )

        if not user:
            raise Exception("Invalid credentials")

        valid_password = verify_password(
            user_data.password,
            user.hashed_password,
        )

        if not valid_password:
            raise Exception("Invalid credentials")

        token = create_access_token(
            {"sub": str(user.id)}
        )

        return {
            "access_token": token,
            "token_type": "bearer",
        } 
