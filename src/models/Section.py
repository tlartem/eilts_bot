from __future__ import annotations

import enum
from datetime import datetime
from typing import List, TYPE_CHECKING

from src.models.Base import Base
from sqlalchemy.orm import Mapped, relationship, mapped_column
from sqlalchemy import ForeignKey

from src.models.Task import Task

if TYPE_CHECKING:
    from src.models.Test import Test


class SectionType(enum.Enum):
    LISTENING = "LISTENING"
    READING = "READING"
    WRITING = "WRITING"
    SPEAKING = "SPEAKING"


class Section(Base):
    section_type: Mapped[SectionType]
    time_delta: Mapped[datetime]

    test_id: Mapped[int] = mapped_column(ForeignKey("tests.id"))

    test: Mapped[Test] = relationship("Test", back_populates="sections")
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="section")
