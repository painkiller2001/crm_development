from main import app as application
import pytest

from httpx import AsyncClient, ASGITransport


BASE_URL = "http://test"


@pytest.fixture
async def async_client():
    transport = ASGITransport(app=application)
    async with AsyncClient(transport=transport, base_url=BASE_URL) as client:
        yield client


@pytest.fixture
async def async_customer():
    ...


@pytest.fixture
async def async_deal():
    ...