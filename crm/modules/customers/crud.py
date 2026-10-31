from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from .models import CustomerModel
from .schema import CustomerCreate, CustomerUpdate


async def create_customer():
    ...


async def get_customer():
    ...


async def get_customers():
    ...


async def update_customer():
    ...


async def delete_customer():
    ...