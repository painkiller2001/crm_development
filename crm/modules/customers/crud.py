from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import CustomerModel
from .schema import CustomerCreate, CustomerUpdate


async def create_customer(db: AsyncSession, new_customer_data: CustomerCreate) -> CustomerModel | None:
    db_new_customer = CustomerModel(**new_customer_data.model_dump())
    db.add(db_new_customer)
    await db.commit()
    await db.refresh(db_new_customer)
    return db_new_customer


async def get_customer(db: AsyncSession, customer_id: int) -> CustomerModel | None:
    customer = await db.execute(select(CustomerModel).filter(CustomerModel.id == customer_id))
    return customer.scalars().first()


async def get_customers(db: AsyncSession) -> list[CustomerModel] | None:
    customer = await db.execute(select(CustomerModel))
    return customer.scalars().all()


async def update_customer(db: AsyncSession, customer_id: int, new_customer_data: CustomerUpdate) -> CustomerModel | None:
    customer = await db.execute(select(CustomerModel).filter(CustomerModel.id == customer_id))
    db_customer = customer.scalars.first()

    if not db_customer:
        return None

    updated_customer = new_customer_data.model_dump(exclude_unset=True)

    for field, data in update_customer.items():
        setattr(db_customer, field, data) 

    await db.commit()
    await db.refresh(db_customer)
    
    return db_customer


async def delete_customer(db: AsyncSession, customer_id: int) -> None:
    customer = await db.execute(select(CustomerModel).filter(CustomerModel.id == id))
    db.delete(customer.scalars().first())
    await db.commit()