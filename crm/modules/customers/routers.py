from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from crm.core.database import get_db
from crm.core.security import get_current_user
from crm.modules.customers import crud

from .schema import CustomerCreate, CustomerUpdate

router = APIRouter(prefix='/customers', tags=["Customers"], dependencies=[Depends(get_current_user)])


@router.post('/create/')
async def create_customer(new_customer_data: CustomerCreate, db: AsyncSession = Depends(get_db)):
    new_customer = await crud.create_customer(db=db, new_customer_data=new_customer_data)
    return new_customer


@router.get('/')
async def get_customers(db: AsyncSession = Depends(get_db)):
    customers = await crud.get_customers(db=db)
    return customers


@router.get('/{id}/customer/')
async def get_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    customer = await crud.get_customer(db=db, customer_id=customer_id)

    if customer:
        return customer
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )


@router.put('/{id}/update/')
async def update_customer(new_customer_data: CustomerUpdate, customer_id: int, db: AsyncSession = Depends(get_db)):
    updated_customer = await crud.update_customer(db=db, new_customer_data=new_customer_data, customer_id=customer_id)

    if updated_customer:
        return updated_customer
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )


@router.delete('/{id}/delete/')
async def delete_customer(customer_id: int, db: AsyncSession = Depends(get_db)):
    customer = await crud.get_customer(customer_id=customer_id, db=db)

    if customer:
        await crud.delete_customer(customer_id=customer_id, db=db)
        return
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Customer not found"
        )
