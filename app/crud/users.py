from sqlalchemy.ext.asyncio import AsyncSession
from typing import Sequence
from core.models import User
from sqlalchemy import select


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User).order_by(User.id)
    result = await session.scalars(stmt)
    return result.all()
