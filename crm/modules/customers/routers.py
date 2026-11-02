from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crm.core.database import get_db
from crm.modules.users import crud

from .schema import CustomerCreate, CustomerUpdate


router = APIRouter(prefix='/customers')


@router.post('/create/')
async def create_customer(new_customer_data: CustomerCreate, db: AsyncSession = Depends(get_db)):
    new_customer = await crud.create_user(db=db, new_customer_data=new_customer_data)
    return new_customer


@router.get('/')
async def get_customers():
    ...


@router.get('/{id}/customer/')
async def get_customer():
    ...


@router.put('')
async def update_customer():
    ...


@router.delete('')
async def delete_customer():
    ...
