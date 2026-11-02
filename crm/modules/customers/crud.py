from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import CustomerModel
from .schema import CustomerCreate, CustomerUpdate


async def create_customer(db: AsyncSession, new_customer_data: CustomerCreate) -> CustomerModel | None:
    ...


async def get_customer(db: AsyncSession, customer_id: int) -> CustomerModel | None:
    customer = await db.execute(select(CustomerModel).filter(CustomerModel.id == customer_id))
    return customer.scalars().first()


async def get_customers(db: AsyncSession) -> list[CustomerModel] | None:
    ...


async def update_customer(db: AsyncSession, id: int, new_customer_data: CustomerUpdate) -> CustomerModel | None:
    ...


async def delete_customer(db: AsyncSession, id: int) -> None:
    ...