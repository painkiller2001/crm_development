import pytest
from httpx import AsyncClient
# <<<<<<< feature/tests
# from crm.modules.deals import crud
# from sqlalchemy.ext.asyncio import AsyncSession
# =======
# >>>>>>> main


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

    response = await auth_client.post(f'/deals/create/', json=deal_data)

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == deal_data['name']
    assert data['responsible_id'] == deal_data['responsible_id']



@pytest.mark.asyncio
async def test_read_deal(async_client: AsyncClient, auth_client, test_deal):
    deal_id = test_deal.id

    response = await auth_client.get(f'/deals/{deal_id}/')

    assert response.status_code == 200
    data = response.json()
    assert data["name"] == test_deal.name
    assert data["email"] == test_deal.email


@pytest.mark.asyncio
async def test_update_deal(async_client: AsyncClient, auth_client, test_deal):
    deal_id = test_deal.id

    update_data = {
        name="Test deal",
        customer_id=test_customer.id,
        responsible_id=test_user["id"],
        price="100000",
        stage="Draft",
        description="Test desc for deal",
    }

    response = await auth_client.put(f'/deals/{deal_id}/update/', json=update_data)

    assert response.status_code == 200

    get_response = await auth_client.get(f"/deals/{deal_id}")
    data = get_response.json()
    assert data[] == update_data[]
    assert data[] == update_data[]


@pytest.mark.asyncio
async def test_delete_deal(db_session: AsyncSession, async_client: AsyncClient, auth_client, test_deal):
    deal_id = test_deal.id

    response = await auth_client.delete(f'/deals/{deal_id}/delete/')

    assert response.status_code in (200, 204)

    deleted_deal = await crud.get_deal(db=db_session, deal_id=deal_id)
    assert deleted_deal is None