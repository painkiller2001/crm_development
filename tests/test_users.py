import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from crm.modules.users import crud


@pytest.mark.asyncio
async def test_create_user(async_client: AsyncClient):

    user_data = {
        "first_name": "Test",
        "last_name": "User",
        "role": "Manager",
        "department": "Sales",
        "email": "user@example.com",
        "password": "12345qqQ!"
    }

    response = await async_client.post("/users/create", json=user_data)
    
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == user_data["email"]
    assert data["first_name"] == user_data["first_name"]
    assert "password" not in data
    assert "hashed_password" not in data


@pytest.mark.asyncio
async def test_read_users(async_client: AsyncClient, auth_client, test_user: dict):
    
    user_data2 = {
        "first_name": "Test2",
        "last_name": "User2",
        "role": "Manager",
        "department": "Sales",
        "email": "user2@example.com",
        "password": "12345qqQ!"
    }

    create_response = await auth_client.post("/users/create", json=user_data2)
    assert create_response.status_code in (200, 201)

    response = await async_client.get("/users")

    assert response.status_code == 200
    data = response.json()
    emails = [user["email"] for user in data]
    assert test_user["email"] in emails
    assert user_data2["email"] in emails


@pytest.mark.asyncio
async def test_read_user(async_client: AsyncClient, auth_client, test_user: dict):
    user_id = test_user['id']

    response = await auth_client.get(f"/users/{user_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_user["email"]
    assert data["last_name"] == test_user["last_name"]



@pytest.mark.asyncio
async def test_update_user(auth_client: AsyncClient, test_user: dict):
    user_id = test_user["id"]

    update_data = {
        "first_name": "Upd Test",
        "last_name": "Upd User",
        "role": "Manager",
        "department": "Sales",
    }

    response = await auth_client.put(f"/users/{user_id}/update", json=update_data)
    assert response.status_code == 200

    get_response = await auth_client.get(f"/users/{user_id}")
    data = get_response.json()
    assert data["first_name"] == update_data["first_name"]
    assert data["last_name"] == update_data["last_name"]



@pytest.mark.asyncio
async def test_delete_user(auth_client, test_user: dict, db_session: AsyncSession):
    user_id = test_user['id']

    response = await auth_client.delete(f"/users/{user_id}/delete")

    assert response.status_code in (200, 204)

    deleted_user = await crud.get_user(db=db_session, user_id=user_id)
    assert deleted_user is None