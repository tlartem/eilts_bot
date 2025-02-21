import enum
from datetime import datetime

from src.models.Base import Base
from sqlalchemy.orm import Mapped

from src.models.Task import Task


class SectionType(enum.Enum):
    LISTENING = "LISTENING"
    READING = "READING"
    WRITING = "WRITING"
    SPEAKING = "SPEAKING"


class Section(Base):
    section_type: Mapped[SectionType]
    time_delta: Mapped[datetime]

    tasks: Mapped[list[Task]]
