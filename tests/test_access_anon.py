import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_read_users_anon(async_client: AsyncClient):
    response = await async_client.get("/users")
    assert response.status_code == 401 


@pytest.mark.asyncio
async def test_read_user_anon():
    ...


@pytest.mark.asyncio
async def test_update_user_anon():
    ...


@pytest.mark.asyncio
async def test_delete_user_anon():
    ...


@pytest.mark.asyncio
async def test_create_customer_anon():
    ...


@pytest.mark.asyncio
async def test_read_customer_anon():
    ...


@pytest.mark.asyncio
async def test_update_customer_anon():
    ...


@pytest.mark.asyncio
async def test_delete_customer_anon():
    ...


@pytest.mark.asyncio
async def test_create_deal_anon():
    ...


@pytest.mark.asyncio
async def test_read_deal_anon():
    ...


@pytest.mark.asyncio
async def test_update_deal_anon():
    ...


@pytest.mark.asyncio
async def test_delete_deal_anon():
    ...