import uuid

from src.models import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship


class File(Base):
    id: Mapped[uuid.UUID]
    filename: Mapped[str]
    tg_file_id: Mapped[str]
