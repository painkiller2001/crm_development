from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crm.core.database import get_db
from crm.core.security import get_current_user
from crm.modules.users import crud

from .schema import UserCreate, UserUpdate

router = APIRouter(prefix='/users', tags=["Users"])


@router.post('/create')
async def create_user(new_user_data: UserCreate, db: AsyncSession = Depends(get_db)):
    new_user = await crud.create_user(db=db, new_user_data=new_user_data)
    return new_user


@router.get('/')
async def get_users(db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    users = await crud.get_users(db=db)
    return users


@router.get('/{id}')
async def get_user(user_id: int, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    user = await crud.get_user(db=db, user_id=user_id)

    if user:
        return user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )


@router.put('/{id}/update')
async def update_user(user_id: int, new_user_data: UserUpdate, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    
    updated_user = await crud.update_user(db=db, user_id=user_id, new_user_data=new_user_data)

    if updated_user:
        return update_user
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )


@router.delete('/{id}/delete')
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db), current_user = Depends(get_current_user)):
    user = await crud.get_user(db=db, user_id=user_id)

    if user:
        await crud.delete_user(db=db, user_id=user_id)
        return
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
