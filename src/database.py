from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL: str = "sqlite+aiosqlite:///./recipes.db"

engine = create_async_engine(DATABASE_URL)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)  # type: ignore
Base = declarative_base()


async def get_session():
    async with async_session() as session:
        yield session
