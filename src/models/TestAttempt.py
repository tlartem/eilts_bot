from datetime import datetime

from src.models.Base import Base
from sqlalchemy import func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TestAttempt(Base):
    started_at: Mapped[datetime] = mapped_column(server_default=func.now())
    finished_at: Mapped[datetime | None]

    total_score: Mapped[float | None]

    user = relationship(back_populates="test_attempts")
    test = relationship(back_populates="test_attempts")

    task_answers = relationship(back_populates="attempt")
