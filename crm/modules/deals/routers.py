from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crm.core.database import get_db

from .schema import DealCreate, DealUpdate

router = APIRouter(prefix='/deals')


@router.post('/create')
async def create_deal(new_deal_data: DealCreate, db: AsyncSession = Depends(get_db)):
    ...


@router.get('/{id}')
async def get_deal(id: int, db: AsyncSession = Depends(get_db)):
    deal = ...

    if deal:
        ...
    else:
        raise HTTPException(
            staus_code=status.HTTP_404_NOT_FOUND, detail='Deal not found'
        )


@router.get('/')
async def get_deals(db: AsyncSession = Depends(get_db)):
    ...


@router.put('/{id}/update')
async def update_deal(new_deal_data: DealUpdate, id: int, db: AsyncSession = Depends(get_db)):
    deal = ...

    if deal:
        ...
    else:
        raise HTTPException(
            staus_code=status.HTTP_404_NOT_FOUND, detail='Deal not found'
        )


@router.delete('/{id}/delete')
async def delete_deal(id: int, db: AsyncSession = Depends(get_db)):
    deal = ...

    if deal:
        ...
    else:
        raise HTTPException(
            staus_code=status.HTTP_404_NOT_FOUND, detail='Deal not found'
        )