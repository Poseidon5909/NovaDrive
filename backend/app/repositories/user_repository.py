from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_by_email(
        self,
        email: str,
    ):
        query = select(User).where(
            User.email == email
        )

        result = await self.db.execute(query)

        return result.scalar_one_or_none()

    async def create(
        self,
        user_data: dict,
    ):
        user = User(**user_data)

        self.db.add(user)

        await self.db.commit()

        await self.db.refresh(user)

        return user 
