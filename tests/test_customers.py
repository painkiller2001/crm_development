import pytest
from httpx import AsyncClient
from crm.modules.customers import crud
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_create_customer(async_client: AsyncClient, auth_client):
    ...


@pytest.mark.asyncio
async def test_read_customer(async_client: AsyncClient, auth_client, test_customer):
    ...


@pytest.mark.asyncio
async def test_update_customer(async_client: AsyncClient, auth_client, test_customer):
    ...


@pytest.mark.asyncio
async def test_delete_customer(async_client: AsyncClient, auth_client, test_customer):
    ...