from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from src.models import Base

from src.models import Section
from src.models import Task
from src.models import TaskAnswer
from src.models import Test
from src.models import TestAttempt
from src.models import User

from src.config import settings

engine = create_async_engine(url=settings.db_url)
async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
