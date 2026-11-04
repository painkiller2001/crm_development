import os
from dotenv import load_dotenv

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base


load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql+asyncpg://user:password@localhost/dbname",
    )


engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(expire_on_commit=False, class_=AsyncSession, bind=engine)
Base = declarative_base()


async def get_db():
    db = AsyncSessionLocal()
    try:
        yield db
    finally:
        await db.close()