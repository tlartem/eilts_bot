import enum

from src.models.Base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import BigInteger


class ExamType(enum.Enum):
    ACADEMIC = "ACADEMIC"
    GENERAL = "GENERAL"


class User(Base):
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    username: Mapped[str | None]
    exam_type: Mapped[ExamType] = mapped_column(default=ExamType.ACADEMIC)
