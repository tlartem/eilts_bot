import asyncio
import sys
from aiogram import Dispatcher

import logging

# from src.logs import get_logger
from src.bot_instance import bot
from src.adapter.postgres import init_db
from src.controller.tg_bot.routers import router

# log = get_logger()

dp = Dispatcher()
# router = setup_routers()
dp.include_router(router)


async def on_startup() -> None:
    """Инициализация приложения."""
    try:
        await init_db()
        # log.info("База данных инициализирована.")
    except Exception as e:
        print(e)
        # log.error(f"Ошибка при инициализации: {e}")
        sys.exit(1)


async def main() -> None:
    """Основная функция запуска бота."""
    try:
        # Запускаем инициализацию на старте
        await on_startup()
        # log.info("Запуск бота...")
        await dp.start_polling(bot, skip_updates=True)
    except Exception as e:
        print(e)
        # log.error(f"Ошибка в работе бота: {e}")
        sys.exit(1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
