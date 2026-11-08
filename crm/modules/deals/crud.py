from sqlalchemy import AsyncSession
from crm.modules.deals.models import DealModel

from crm.modules.deals.schema import DealCreate



async def create_deal(new_deal_data: DealCreate, db: AsyncSession) -> DealModel:
    new_deal = DealCreate(**new_deal_data.model_dump())
    db.add(new_deal)
    await db.commit()
    await db.refresh(new_deal)
    return new_deal


async def get_deal(deal_id: int, db: AsyncSession) -> DealModel | None:
    ...


async def get_deals(db: AsyncSession) -> list[DealModel]:
    ...


async def update_deal(deal_id: int, db: AsyncSession) -> DealModel | None:
    ...


async def delete_deal(deal_id: int, db: AsyncSession) -> None:
    ...