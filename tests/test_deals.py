import pytest
from httpx import AsyncClient
from crm.modules.deals import crud
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.mark.asyncio
async def test_create_deal(async_client: AsyncClient, auth_client, test_user, test_customer):
    deal_data = {
        "name": "Test deal",
        "customer_id": test_customer.id,
        "responsible_id": test_user["id"],
        "price": "100000",
        "stage": "Draft",
        "description": "Test desc for deal",
    }

    response = await auth_client.post(f'/deals/create', json=deal_data)

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == deal_data['name']
    assert data['responsible_id'] == deal_data['responsible_id']


@pytest.mark.asyncio
async def test_read_deals(auth_client, test_deal, test_customer, test_user: dict):
    deal_data2 = {
        "name": "Test deal2",
        "customer_id": test_customer.id,
        "responsible_id": test_user["id"],
        "price": "1000002",
        "stage": "Draft",
        "description": "Test desc for deal2",
    }

    create_response = await auth_client.post(f'/deals/create', json=deal_data2)
    assert create_response.status_code in (200, 201)

    response = await auth_client.get("/deals")

    assert response.status_code == 200
    data = response.json()
    ids = [deal["id"] for deal in data]
    assert test_deal.id in ids
    assert create_response.json()["id"] in ids


@pytest.mark.asyncio
async def test_read_deal(async_client: AsyncClient, auth_client, test_deal):
    deal_id = test_deal.id

    response = await auth_client.get(f'/deals/{deal_id}')

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_deal.name
    assert data["customer_id"] == test_deal.customer_id
    assert data["responsible_id"] == test_deal.responsible_id
    assert data["price"] == test_deal.price
    assert data["description"] == test_deal.description


@pytest.mark.asyncio
async def test_update_deal(auth_client, test_deal):
    deal_id = test_deal.id

    update_data = {
        "name": "Updated test deal",
        "customer_id": test_deal.customer_id,
        "responsible_id": test_deal.responsible_id,
        "price": "250000",
        "stage": "In Progress",
        "description": "Updated desc for deal",
    }

    response = await auth_client.put(f"/deals/{deal_id}/update", json=update_data)

    assert response.status_code == 200

    get_response = await auth_client.get(f"/deals/{deal_id}")
    assert get_response.status_code == 200
    data = get_response.json()
    assert data["name"] == update_data["name"]
    assert str(data["price"]) == update_data["price"]
    assert data["stage"] == update_data["stage"]
    assert data["description"] == update_data["description"]


@pytest.mark.asyncio
async def test_delete_deal(db_session: AsyncSession, async_client: AsyncClient, auth_client, test_deal):
    deal_id = test_deal.id

    response = await auth_client.delete(f'/deals/{deal_id}/delete')

    assert response.status_code in (200, 204)

    deleted_deal = await crud.get_deal(db=db_session, deal_id=deal_id)
    assert deleted_deal is None