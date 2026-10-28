from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from .crud import get_user, get_users, delete_user
from crm.core.database import get_db


router = APIRouter(prefix='/users')


@router.post('/create')
async def create_user():
    ...


@router.get('/')
async def get_users(db: AsyncSession = Depends(get_db)):
    users = await get_users(db=db)
    return users


@router.get('/{id}')
async def get_user(id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db=db, user_id=id)

    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )


@router.put('/update/{id}')
async def update_user(id: int):
    ...


# @router.post('/delete/{id}')
# async def delete_user(id: int, db: AsyncSession = Depends(get_db)):
#     user = await get_user(db=db, user_id=id)

#     if user:
#         return None
#     else:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
#         )
