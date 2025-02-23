from typing import List
import uuid

from src.models.Base import Base
from sqlalchemy import JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Task(Base):
    section_id: Mapped[int] = mapped_column(ForeignKey("sections.id"))


    # task_id: придумать

    number: Mapped[int]
    text: Mapped[str]
    answers: Mapped[List[str]] = mapped_column(JSON, nullable=False)
    file_id: Mapped[uuid.UUID | None]

    section = relationship("Section", back_populates="tasks")
