from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper
from core.schemas.user import UserRead
from crud import users as users_crud
from core.config import settings

router = APIRouter(
    prefix=settings.api_prefix.v1.users,
    tags=["Users"],
)


@router.get("", response_model=list[UserRead])
async def get_users(session: AsyncSession = Depends(db_helper.session_getter)):
    users = await users_crud.get_all_users(session=session)
    return users
