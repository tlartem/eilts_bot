import uuid

from src.models.Base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Task(Base):
    section_id: Mapped[int] = mapped_column(ForeignKey("section.id"))

    number: Mapped[int]
    text: Mapped[str]
    answers: Mapped[list[str]]
    file_id: Mapped[uuid.UUID | None]

    section = relationship("Section", back_populates="tasks")
