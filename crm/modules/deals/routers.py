from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crm.core.database import get_db
from crm.modules.deals import crud

from .schema import DealCreate, DealUpdate


router = APIRouter(prefix='/deals')


@router.get('/{id}/')
async def get_deal():
    ...


@router.get('/')
async def get_deals():
    ...


@router.post('/create_deal/')
async def create_deal():
    ...


@router.put('/{id}/update')
async def update_deal():
    ...


@router.delete('/{id}/delete')
async def delete_deal():
    ...