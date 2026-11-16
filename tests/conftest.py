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


@pytest.fixture
async def db_session():
    async with TestingSessionLocal() as session:
        yield session


@pytest.fixture(autouse=True)
def override_dependency(db_session: AsyncSession):
    async def override_get_db():
        yield db_session

    application.dependency_overrides[get_db] = override_get_db
    yield
    application.dependency_overrides.clear()


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


@pytest.fixture
async def auth_client(async_client: AsyncClient, test_user: dict):
    login_data = {
        "username": test_user["email"],
        "password": test_user["password"],
    }
    response = await async_client.post("/login", data=login_data)
    token = response.json()["access_token"]
    async_client.headers.update({"Authorization": f"Bearer {token}"})
    yield async_client
    async_client.headers.pop("Authorization", None)


# @pytest.fixture
# async def test_customer(async_client: AsyncClient, auth_client: dict):
#     customer_data = {
#         "name": "Test LLC",
#         "phone": "123 563 (324)",
#         "email": "test_customer@test.com",
#         "website": "www.testllc.com",
#         "address": "Test St., Test State",
#     }
#     response = await async_client.post("/customers/create", json=customer_data)
#     customer = response.json()
#     return customer