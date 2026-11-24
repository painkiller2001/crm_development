import pytest


@pytest.mark.asyncio
@pytest.mark.parametrize(...)
async def test_entity_not_found(auth_client, method: str, url: str, object_data: dict | None):
    ...