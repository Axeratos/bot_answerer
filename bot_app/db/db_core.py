from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base

Base = declarative_base()
engine = create_async_engine(
    "postgresql+asyncpg://app_owner:DwQ6MxFbJkojrSITCaiO6cJbIEpAveYIDiOv05Ij5BEy@localhost/app_database",
    echo=True
)
SessionLocal = async_sessionmaker(engine, expire_on_commit=True, class_=AsyncSession)
