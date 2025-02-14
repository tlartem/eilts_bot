import asyncio
import sys
from aiogram import Dispatcher

from src.logs import get_logger
from src.bot_instance import bot
from src.database import init_db
# from src.handlers import setup_routers

logger = get_logger()

dp = Dispatcher()
# router = setup_routers()
# dp.include_router(router)


async def on_startup():
    """Инициализация приложения."""
    try:
        # db_manager.initialize_db()
        await init_db()
        logger.info("База данных инициализирована.")
    except Exception as e:
        logger.error(f"Ошибка при инициализации: {e}")
        sys.exit(1)


async def main():
    """Основная функция запуска бота."""
    try:
        # Запускаем инициализацию на старте
        await on_startup()

        logger.info("Запуск бота...")
        await dp.start_polling(bot, skip_updates=True)
    except Exception as e:
        logger.error(f"Ошибка в работе бота: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
