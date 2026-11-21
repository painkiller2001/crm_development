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

    response = await auth_client.get(f'/customers/{customer_id}/')

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_customer.name
    assert data["email"] == test_customer.email
    


@pytest.mark.asyncio
async def test_update_customer(async_client: AsyncClient, auth_client, test_customer):
    customer_id = test_customer.id

    update_data = {
        'name': "Upd Test LLC",
        'phone': "Upd 123 563 (324)",
        'email': "upd_test_customer@test.com",
        'website': "upd_testcustomer.com",
        'address': "upd_Test St., Test State",
    }

    # response = await auth_client.put(f'/customers/{customer_id}/update/', json=update_data)

    assert response.status_code == 200

    get_response = await auth_client.get(f"/customers/{customer_id}")
    data = get_response.json()
    assert data['name'] == update_data['name']
    assert data["website"] == update_data["website"]


@pytest.mark.asyncio
async def test_delete_customer(db_session: AsyncSession, async_client: AsyncClient, auth_client, test_customer):
    customer_id = test_customer.id

    response = await auth_client.delete(f'/customers/{customer_id}/delete/')

    assert response.status_code in (200, 204)

    deleted_customer = await crud.get_customer(db=db_session, customer_id=customer_id)
    assert deleted_customer is None