from main import app as application
import pytest

from httpx import AsyncClient


BASE_URL = "http://test"


@pytest.fixture
async def async_client():
    async with AsyncClient(app=application, base_url=BASE_URL) as client:
        yield client