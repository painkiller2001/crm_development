from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crm.core.database import get_db
from crm.modules.deals import crud

from .schema import DealCreate, DealUpdate

router = APIRouter(prefix='/deals', tags=["Deals"])


@router.post('/create')
async def create_deal(new_deal_data: DealCreate, db: AsyncSession = Depends(get_db)):
    new_deal = await crud.create_deal(new_deal_data=new_deal_data, db=db)
    return new_deal


@router.get('/{id}')
async def get_deal(deal_id: int, db: AsyncSession = Depends(get_db)):
    deal = await crud.get_deal(db=db, deal_id=deal_id)

    if deal:
        return deal
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Deal not found'
        )


@router.get('/')
async def get_deals(db: AsyncSession = Depends(get_db)):
    deals = await crud.get_deals(db=db)
    return deals


@router.put('/{id}/update')
async def update_deal(new_deal_data: DealUpdate, deal_id: int, db: AsyncSession = Depends(get_db)):
    deal = await crud.update_deal(new_deal_data=new_deal_data, deal_id=deal_id, db=db)

    if deal:
        return deal
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Deal not found'
        )


@router.delete('/{id}/delete')
async def delete_deal(deal_id: int, db: AsyncSession = Depends(get_db)):
    deal = await crud.get_deal(deal_id=deal_id, db=db)

    if deal:
        await crud.delete_user(db=db, deal_id=deal_id)
        return
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Deal not found'
        )