from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import ExpiredSignatureError
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.exceptions import (
    ExpiredTokenException,
    InvalidTokenException,
    UnauthorizedException,
    UserNotFoundException,
)
from app.core.security import (
    ACCESS_TOKEN_TYPE,
    decode_token,
)
from app.db.session import get_db
from app.repositories.user_repository import user_repository


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: AsyncSession = Depends(get_db),
):

    try:
        payload = decode_token(token)

    except ExpiredSignatureError:
        raise ExpiredTokenException()

    except JWTError:
        raise InvalidTokenException()

    user_id = payload.get("sub")
    token_type = payload.get("type")

    if not user_id:
        raise InvalidTokenException()

    if token_type != ACCESS_TOKEN_TYPE:
        raise InvalidTokenException()

    user = await user_repository.get_by_id(
        db,
        user_id,
    )

    if not user:
        raise UserNotFoundException()

    return user


async def get_current_active_user(
    current_user=Depends(get_current_user),
):

    if not current_user.is_active:
        raise UnauthorizedException()

    return current_user