import pytest
from httpx import AsyncClient
from crm.modules.deals import crud
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_create_deal(async_client: AsyncClient, auth_client, test_customer, test_user):
    ...   


@pytest.mark.asyncio
async def test_read_deal(async_client: AsyncClient, test_deal):
    ...


@pytest.mark.asyncio
async def test_update_deal(async_client: AsyncClient, auth_client, test_deal):
    ...


@pytest.mark.asyncio
async def test_delete_deal(db_session: AsyncSession, sasync_client: AsyncClient, auth_client, test_deal):
    ...