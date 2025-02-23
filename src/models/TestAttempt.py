from datetime import datetime
from typing import List

from src.models.Base import Base
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .User import User
from .Test import Test
from .TaskAnswer import TaskAnswer


class TestAttempt(Base):
    started_at: Mapped[datetime] = mapped_column(server_default=func.now())
    finished_at: Mapped[datetime | None]

    total_score: Mapped[float | None]

    # Добавляем внешние ключи:
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    test_id: Mapped[int] = mapped_column(ForeignKey("tests.id"))

    # Определяем отношения с использованием внешних ключей:
    user: Mapped[User] = relationship("User", back_populates="test_attempts")
    test: Mapped[Test] = relationship("Test", back_populates="test_attempts")
    task_answers: Mapped[List[TaskAnswer]] = relationship(
        "TaskAnswer", back_populates="attempt"
    )
