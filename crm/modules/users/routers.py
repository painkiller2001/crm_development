from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from . import crud
from core.database import get_db


router = APIRouter(prefix='/users')


@router.post('/create')
async def create_user():
    ...


@router.get('/')
async def get_users(db: AsyncSession = Depends(get_db)):
    users = await crud.get_users(db=db)
    return users


@router.get('/{id}')
async def get_user(id: int, db: AsyncSession = Depends(get_db)):
    if db.id:
        user = await crud.get_user(db=db, user_id=id)
        return user
    else:
        raise HTTPException


@router.put('/update/{id}')
async def update_user(id: int):
    ...


@router.post('/delete/{id}')
async def delete_user(id: int):
    ...
