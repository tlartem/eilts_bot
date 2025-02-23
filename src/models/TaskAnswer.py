from src.models.Base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class TaskAnswer(Base):
    attempt_id: Mapped[int] = mapped_column(ForeignKey("testattempts.id"))
    task_id: Mapped[int] = mapped_column(ForeignKey("tasks.id"))
    user_response: Mapped[str]

    # Баллы за задание (вычисляются после завершения теста)
    score: Mapped[float | None]

    attempt = relationship("TestAttempt", back_populates="task_answers")
    task = relationship("Task")
