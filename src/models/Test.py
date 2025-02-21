from datetime import datetime

from src.models.Section import Section
from src.models.Base import Base
from sqlalchemy.orm import Mapped


class Test(Base):
    name: Mapped[str]
    time_delta: Mapped[datetime]

    sections: Mapped[Section]
