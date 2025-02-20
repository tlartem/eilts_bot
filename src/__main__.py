import asyncio
import sys
from aiogram import Dispatcher

from src.logs import get_logger
from src.bot_instance import bot
#from src.models import init_db
# from src.handlers import setup_routers

log = get_logger()

dp = Dispatcher()
# router = setup_routers()
# dp.include_router(router)


async def on_startup() -> None:
    """Инициализация приложения."""
    try:
        # db_manager.initialize_db()
        #await init_db()
        log.info("База данных инициализирована.")
    except Exception as e:
        log.error(f"Ошибка при инициализации: {e}")
        sys.exit(1)


async def main() -> None:
    """Основная функция запуска бота."""
    try:
        # Запускаем инициализацию на старте
        await on_startup()

        log.info("Запуск бота...")
        await dp.start_polling(bot, skip_updates=True)
    except Exception as e:
        log.error(f"Ошибка в работе бота: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
