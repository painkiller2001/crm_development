import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from crm.core.database import Base, get_db
from main import app as application


TEST_BASE_URL = "sqlite+aiosqlite:///:memory:"
engine_test = create_async_engine(TEST_BASE_URL, echo=False)
TestingSessionLocal = async_sessionmaker(expire_on_commit=False, class_=AsyncSession, bind=engine_test)


async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session


application.dependency_overrides[get_db] = override_get_db


@pytest.fixture(autouse=True)
async def setup_test_db():
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine_test.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


BASE_URL = "http://test"


@pytest.fixture
async def async_client():
    transport = ASGITransport(app=application)
    async with AsyncClient(transport=transport, base_url=BASE_URL) as client:
        yield client


@pytest.fixture
async def test_user(async_client: AsyncClient):
    user_data = {
        "first_name": "Test",
        "last_name": "User",
        "role": "Manager",
        "department": "Finance",
        "email": "user@example.com",
        "password": "12345qqQ!",
    }
    response = await async_client.post("/users/create", json=user_data)
    user = response.json()
    user["password"] = "12345qqQ!"
    return user