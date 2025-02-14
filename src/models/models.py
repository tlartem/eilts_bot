from sqlalchemy import BigInteger, String, Integer, ForeignKey, Text, DateTime, JSON
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
    declared_attr,
)
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from sqlalchemy import Enum
import enum
from datetime import datetime

from src.config import get_sqlalchemy_url

# Создаем асинхронный движок SQLAlchemy
engine = create_async_engine(url=get_sqlalchemy_url())
async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


# Базовый класс для моделей
class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    # Авто имя таблиц по названию класса
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    pass


# Перечисление типов заданий
class TaskType(enum.Enum):
    LISTENING = "listening"
    READING = "reading"
    WRITING = "writing"
    SPEAKING = "speaking"


# Таблица пользователей
class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_id: Mapped[int] = mapped_column(BigInteger, unique=True, index=True)
    name: Mapped[str] = mapped_column(String(50))
    exam_type: Mapped[str] = mapped_column(
        String(15), default="Academic"
    )  # Academic или General
    registered_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    # Связь с результатами тестов
    results = relationship(
        "Result", back_populates="user", cascade="all, delete-orphan"
    )


# Таблица заданий Listening
class ListeningTask(Base):
    __tablename__ = "listening_tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    audio_file_id: Mapped[str] = mapped_column(
        String, nullable=False
    )  # ID файла в Telegram
    question_file_ids: Mapped[list[str]] = mapped_column(
        JSON, nullable=False
    )  # File IDs для вопросов задания
    answers: Mapped[dict] = mapped_column(
        JSON, nullable=False
    )  # Хранение вопросов в формате JSON


# Таблица заданий Reading
class ReadingTask(Base):
    __tablename__ = "reading_tasks"

    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True
    )  # Уникальный ID задания
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # Название задания
    description_file_ids: Mapped[list[str]] = mapped_column(
        JSON, nullable=False
    )  # File IDs для описания задания (тексты)
    question_file_ids: Mapped[list[str]] = mapped_column(
        JSON, nullable=False
    )  # File IDs для вопросов задания
    answers: Mapped[dict] = mapped_column(JSON, nullable=False)  # JSON с ответами


# Таблица заданий Writing
class WritingTask(Base):
    __tablename__ = "writing_tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    prompt: Mapped[str] = mapped_column(Text, nullable=False)  # Тема эссе
    task_type: Mapped[str] = mapped_column(
        String(10), nullable=False
    )  # Task 1 или Task 2


# Таблица заданий Speaking
class SpeakingTask(Base):
    __tablename__ = "speaking_tasks"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    question: Mapped[str] = mapped_column(Text, nullable=False)  # Вопрос для speaking
    part: Mapped[int] = mapped_column(
        Integer, nullable=False
    )  # Часть Speaking (1, 2, 3)


# Таблица результатов тестов
class Result(Base):
    __tablename__ = "results"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    task_id: Mapped[int] = mapped_column(
        Integer, nullable=False
    )  # ID задания (универсальный подход)
    task_type: Mapped[TaskType] = mapped_column(
        Enum(TaskType), nullable=False
    )  # "listening", "reading", "writing", "speaking"
    score: Mapped[str] = mapped_column(String(10), nullable=True)  # Баллы за тест
    submitted_text: Mapped[str] = mapped_column(
        Text, nullable=True
    )  # Для Writing и Speaking
    ai_feedback: Mapped[str] = mapped_column(Text, nullable=True)  # AI-оценка ответа
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="results")


# Функция для инициализации базы данных
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
