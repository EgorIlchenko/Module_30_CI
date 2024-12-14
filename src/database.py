from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL: str = "sqlite+aiosqlite:///./recipes.db"

engine = create_async_engine(DATABASE_URL)

async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)  # type: ignore
Base = declarative_base()


async def get_session():
    async with async_session() as session:
        yield session
