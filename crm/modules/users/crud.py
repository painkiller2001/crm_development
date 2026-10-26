from sqlalchemy.ext.asyncio import AsyncSession

from .models import UserModel
from .schemas import UserCreate


async def create_user(db: AsyncSession, new_user_data: UserCreate) -> UserModel:
    db_new_user = UserModel(**new_user_data.model_dump())
    db.add(db_new_user)
    await db.commit()
    await db.refresh(db_new_user)
    return db_new_user


async def get_user(db: AsyncSession, ...):
    ...


async def get_users(db: AsyncSession, ...):
    ...


async def update_user(db: AsyncSession, ...):
    ...


async def delete_user(db: AsyncSession, ...):
    ...