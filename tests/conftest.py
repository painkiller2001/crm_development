from main import app as application
import pytest

from httpx import AsyncClient, ASGITransport
from crm.core.database import Base, get_db

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine



# TEST Environment settings
TEST_BASE_URL = "sqlite+aiosqlite:///:memory:"
engine_test = create_async_engine(TEST_BASE_URL, echo=False)
TestingSessionLocal = async_sessionmaker(expire_on_commit=False, class_=AsyncSession, bind=engine_test)


async def override_get_db():
    async with TestingSessionLocal() as session:
        yield session


application.dependency_overrides[get_db] = override_get_db



# BASE_URL = "http://test"


# @pytest.fixture
# async def async_client():
#     transport = ASGITransport(app=application)
#     async with AsyncClient(transport=transport, base_url=BASE_URL) as client:
#         yield client


# @pytest.fixture
# async def async_customer():
#     ...


# @pytest.fixture
# async def async_deal():
#     ...