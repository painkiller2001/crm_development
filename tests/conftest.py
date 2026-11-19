import pytest
from httpx import ASGITransport, AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from crm.core.database import Base, get_db
from main import app as application
from crm.modules.customers import crud as customer_crud
from crm.modules.deals import crud as deal_crud
from crm.modules.customers.schema import CustomerCreate
from crm.modules.deals.schema import DealCreate


TEST_BASE_URL = "sqlite+aiosqlite:///:memory:"
engine_test = create_async_engine(TEST_BASE_URL, echo=False)
TestingSessionLocal = async_sessionmaker(expire_on_commit=False, class_=AsyncSession, bind=engine_test)


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
async def auth_client(test_user: dict):
    transport = ASGITransport(app=application)
    async with AsyncClient(transport=transport, base_url=BASE_URL) as client:
        login_data = {
            "username": test_user["email"],
            "password": test_user["password"],
        }
        response = await client.post("/login", data=login_data)
        token = response.json()["access_token"]
        client.headers.update({"Authorization": f"Bearer {token}"})
        yield client


@pytest.fixture
async def test_customer(db_session: AsyncSession):
    customer_data = CustomerCreate(
        name="Test LLC",
        phone="123 563 (324)",
        email="test_customer@test.com",
        website="testcustomer.com",
        address="Test St., Test State",
    )
    return await customer_crud.create_customer(db=db_session, new_customer_data=customer_data)


@pytest.fixture
async def test_deal(db_session: AsyncSession, test_customer, test_user: dict):
    deal_data = DealCreate(
        name="Test deal",
        customer_id=test_customer.id,
        responsible_id=test_user["id"],
        price="100000",
        stage="Draft",
        description="Test desc for deal",
    )
    return await deal_crud.create_deal(db=db_session, new_deal_data=deal_data)