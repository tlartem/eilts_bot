from __future__ import annotations

from datetime import datetime
from typing import List, TYPE_CHECKING

from src.models.Base import Base
from sqlalchemy.orm import Mapped, relationship

if TYPE_CHECKING:
    from src.models.TestAttempt import TestAttempt
    from src.models.Section import Section


class Test(Base):
    name: Mapped[str]
    time_delta: Mapped[datetime]

    sections: Mapped[List[Section]] = relationship("Section", back_populates="test")
    test_attempts: Mapped[List["TestAttempt"]] = relationship(
        "TestAttempt", back_populates="test"
    )
