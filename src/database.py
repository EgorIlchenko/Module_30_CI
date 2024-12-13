from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL: str = "sqlite+aiosqlite:///./recipes.db"

engine = create_async_engine(DATABASE_URL)

async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
# session_local = async_session()
Base = declarative_base()


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
