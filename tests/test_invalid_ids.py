import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(("method", "url", "payload"),
    [
        ("GET", "/users/99999", None),
        ("PUT", "/users/99999/update", {"first_name": "Ghost"}),
        ("DELETE", "/users/99999/delete", None),
        ],)
async def test_entity_not_found(auth_client, method: str, url: str, object_data: dict | None):
    response = await auth_client.request(method=method, url=url, json=object_data)
    assert response.status_code == 404