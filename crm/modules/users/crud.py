from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import UserModel
from .schema import UserCreate, UserUpdate

from crm.core.security import get_password_hash


async def create_user(db: AsyncSession, new_user_data: UserCreate) -> UserModel:

    user_data = new_user_data.model_dump()

    password = user_data.pop("password")
    hashed_password = get_password_hash(password)
    user_data["hashed_password"] = hashed_password

    db_new_user = UserModel(**user_data)
    db.add(db_new_user)
    await db.commit()
    await db.refresh(db_new_user)
    return db_new_user


async def get_user(db: AsyncSession, user_id: int) -> UserModel | None:
    user = await db.execute(select(UserModel).filter(UserModel.id == user_id))
    return user.scalars().first()


async def get_users(db: AsyncSession) -> list[UserModel]:
    users = await db.execute(select(UserModel))
    return users.scalars().all()


async def update_user(db: AsyncSession, user_id: int, new_user_data: UserUpdate) -> UserModel | None:
    user = await db.execute(select(UserModel).filter(UserModel.id == user_id))
    db_user = user.scalars().first()

    if not db_user:
        return None

    update_data = new_user_data.model_dump(exclude_unset=True)

    for field, data in update_data.items():
        setattr(db_user, field, data)
    
    await db.commit()
    await db.refresh(db_user)
    
    return db_user


async def delete_user(db: AsyncSession, user_id: int) -> None:
    user = await db.execute(select(UserModel).filter(UserModel.id == user_id))
    await db.delete(user.scalars().first())
    await db.commit()