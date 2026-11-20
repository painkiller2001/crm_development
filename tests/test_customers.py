import pytest
from httpx import AsyncClient
from crm.modules.customers import crud
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_create_customer(async_client: AsyncClient, auth_client):
    customer_data = {
        'name': "Test LLC",
        'phone': "123 563 (324)",
        'email': "test_customer@test.com",
        'website': "testcustomer.com",
        'address': "Test St., Test State",
    }

    response = await auth_client.post(f'/customers/create/', json=customer_data)

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == customer_data["email"]
    assert data["name"] == customer_data["name"]


@pytest.mark.asyncio
async def test_read_customer(async_client: AsyncClient, auth_client, test_customer):
    customer_id = test_customer.id

    response = await auth_client.get(f'/customers/{customer_id}')

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_customer["name"]
    assert data["email"] == test_customer["email"]
    


@pytest.mark.asyncio
async def test_update_customer(async_client: AsyncClient, auth_client, test_customer):
    ...


@pytest.mark.asyncio
async def test_delete_customer(async_client: AsyncClient, auth_client, test_customer):
    ...

#