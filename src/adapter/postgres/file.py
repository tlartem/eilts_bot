from sqlalchemy.ext.asyncio import AsyncSession

from src.models.File import File


async def add(session: AsyncSession, file: File) -> File:
    session.add(file)
    await session.commit()
    await session.refresh(file)
    return file
