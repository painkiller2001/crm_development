import pytest
from httpx import AsyncClient


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