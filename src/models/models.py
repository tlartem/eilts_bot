# Создаем асинхронный движок SQLAlchemy
engine = create_async_engine(url=settings.db_url)
async_session = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


# Базовый класс для моделей


# Перечисление типов заданий


# Таблица пользователей


# Таблица заданий Listening
class ListeningTask(Base):
    audio_file_data: Mapped[LargeBinary] = mapped_column(
        LargeBinary, nullable=False
    )  # Сохраняем аудиофайл в базе данных
    question_file_data: Mapped[LargeBinary] = mapped_column(
        LargeBinary, nullable=False
    )  # Сохраняем файлы с вопросами
    # answers: Mapped[dict] = mapped_column(
    #    JSON, nullable=False
    # )  # Хранение вопросов в формате JSON


# Таблица заданий Reading
class ReadingTask(Base):
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # Название задания
    description_file_ids: Mapped[list[str]] = mapped_column(
        JSON, nullable=False
    )  # File IDs для описания задания (тексты)
    question_file_ids: Mapped[list[str]] = mapped_column(
        JSON, nullable=False
    )  # File IDs для вопросов задания
    # answers: Mapped[dict] = mapped_column(JSON, nullable=False)  # JSON с ответами


# Таблица результатов тестов
class Result(Base):
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    task_id: Mapped[int] = mapped_column(
        Integer, nullable=False
    )  # ID задания (универсальный подход)
    task_type: Mapped[TaskType] = mapped_column(
        Enum(TaskType), nullable=False
    )  # "listening", "reading", "writing", "speaking"
    score: Mapped[str | None] = mapped_column(String(10))  # Баллы за тест
    submitted_text: Mapped[str] = mapped_column(
        Text, nullable=True
    )  # Для Writing и Speaking
    ai_feedback: Mapped[str | None] = mapped_column(Text)  # AI-оценка ответа
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="results")


# Функция для инициализации базы данных
async def init_db() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
