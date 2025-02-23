# from loguru import Logger
# import sys
# from src.paths import LOG_FILE

# logger = Logger()

# # Настройка логирования
# logger.add(
#     LOG_FILE,
#     format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}",
#     level="INFO",
#     rotation="1 week",
#     retention="4 weeks",
#     compression="zip",
#     encoding="utf-8",
# )

# # Настройка вывода логов в консоль
# logger.add(
#     sys.stdout, format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}", level="INFO"
# )


# def get_logger() -> Logger:
#     return logger
