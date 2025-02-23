from sqlalchemy import select
from sqlalchemy.exc import SQLAlchemyError

from src.models.User import User, ExamType
from src.adapter.postgres import get_session


async def create_user(tg_id: int, username: str | None) -> None:

    session = get_session()
    result = await session.execute(select(User).where(User.tg_id == tg_id))
    existing_user = result.scalars().first()
    if existing_user:
        return  # Пользователь уже существует, выходим из функции

    new_user = User(tg_id=tg_id, username=username, exam_type=ExamType.ACADEMIC)
    session.add(new_user)
    try:
        await session.commit()
    except SQLAlchemyError as e:
        await session.rollback()
        raise e
