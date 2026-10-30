from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crm.core.database import get_db

from crm.modules.users import crud
from .schema import UserUpdate, UserCreate

router = APIRouter(prefix='/users')


@router.post('/create')
async def create_user(new_user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = await crud.create_user(db=db, new_user_data=new_user_data)
    return new_user


@router.get('/')
async def get_users(db: AsyncSession = Depends(get_db)):
    users = await crud.get_users(db=db)
    return users


@router.get('/{id}')
async def get_user(id: int, db: AsyncSession = Depends(get_db)):
    user = await crud.get_user(db=db, user_id=id)

    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )


@router.put('/update/{id}')
async def update_user(id: int, new_user_data: UserUpdate, db: AsyncSession = Depends(get_db)):
    
    updated_user = await crud.update_user(db=db, user_id=id, new_user_data=new_user_data)

    if updated_user:
        return update_user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )


@router.delete('/delete/{id}')
async def delete_user(id: int, db: AsyncSession = Depends(get_db)):
    user = await crud.get_user(db=db, user_id=id)

    if user:
        await crud.delete_user(db=db, user_id=id)
        return None
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
