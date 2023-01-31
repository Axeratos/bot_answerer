from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

from core import Config # noqa

Base = declarative_base()
engine = create_async_engine(
    f"postgresql+asyncpg://"
    f"{Config.db.POSTGRES_USER}:{Config.db.POSTGRES_PASSWORD}@{Config.db.POSTGRES_HOST}/{Config.db.POSTGRES_DB}",
)
SessionLocal = async_sessionmaker(engine, expire_on_commit=True, class_=AsyncSession)
