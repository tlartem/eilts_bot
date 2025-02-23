from __future__ import annotations
import enum
from typing import List, TYPE_CHECKING

from src.models.Base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import BigInteger


if TYPE_CHECKING:
    from src.models.TestAttempt import TestAttempt


class ExamType(enum.Enum):
    ACADEMIC = "ACADEMIC"
    GENERAL = "GENERAL"


class User(Base):
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    username: Mapped[str | None]
    exam_type: Mapped[ExamType] = mapped_column(default=ExamType.ACADEMIC)

    test_attempts: Mapped[List["TestAttempt"]] = relationship(
        "TestAttempt", back_populates="user"
    )
