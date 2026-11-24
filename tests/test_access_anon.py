import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_read_users_anon(async_client: AsyncClient):
    response = await async_client.get("/users")
    assert response.status_code == 401 


@pytest.mark.asyncio
async def test_read_user_anon(async_client: AsyncClient, test_user: dict):
    user_id = test_user["id"]
    response = await async_client.get(f"/users/{user_id}")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_update_user_anon(async_client: AsyncClient, test_user: dict):
    user_id = test_user["id"]
    response = await async_client.put(f"/users/{user_id}/update")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_delete_user_anon(async_client: AsyncClient, test_user: dict):
    user_id = test_user['id']
    response = await async_client.delete(f"/users/{user_id}/delete")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_create_customer_anon(async_client: AsyncClient):
    response = await async_client.post("/customers/create")
    assert response.status_code == 401 


@pytest.mark.asyncio
async def test_read_customers_anon(async_client: AsyncClient, test_customer: dict):
    ...


@pytest.mark.asyncio
async def test_read_customer_anon(async_client: AsyncClient, test_customer: dict):
    customer_id = test_customer.id
    response = await async_client.get(f"/customers/{customer_id}")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_update_customer_anon(async_client: AsyncClient, test_customer: dict):
    customer_id = test_customer.id
    response = await async_client.put(f"/customers/{customer_id}/update")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_delete_customer_anon(async_client: AsyncClient, test_customer: dict):
    customer_id = test_customer.id
    response = await async_client.delete(f"/customers/{customer_id}/delete")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_create_deal_anon(async_client: AsyncClient):
    response = await async_client.get("/deals")
    assert response.status_code == 401 


@pytest.mark.asyncio
async def test_read_deals_anon(assync_client: AsyncClient, test_deal):
    ...
    

@pytest.mark.asyncio
async def test_read_deal_anon(async_client: AsyncClient, test_deal):
    deal_id = test_deal.id
    response = await async_client.get(f"/deals/{deal_id}")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_update_deal_anon(async_client: AsyncClient, test_deal):
    deal_id = test_deal.id
    response = await async_client.put(f"/deals/{deal_id}/update")
    assert response.status_code == 401


@pytest.mark.asyncio
async def test_delete_deal_anon(async_client: AsyncClient, test_deal):
    deal_id = test_deal.id
    response = await async_client.delete(f"/deals/{deal_id}/delete")
    assert response.status_code == 401