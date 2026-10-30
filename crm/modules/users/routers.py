from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crm.core.database import get_db

from .crud import get_user, get_users, delete_user
from .schema import UserUpdate

router = APIRouter(prefix='/users')


@router.post('/create')
async def create_user(db: AsyncSession = Depends(get_db)):
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
async def update_user(id: int, new_user_data: UserUpdate, db: AsyncSession = Depends(get_db)):
    
    updated_user = await update_user(db=db, user_id=id, new_user_data=new_user_data)

    if user:
        ...
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )


@router.delete('/delete/{id}')
async def delete_user(id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user(db=db, user_id=id)

    if user:
        await delete_user(db=db, user_id=id)
        return None
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
