import os
import uuid

import aiogram.types

from src.adapter.postgres import get_session
from src.config import settings
from adapter import postgres
from src.models.File import File


# @dp.message_handler(content_types=["photo"])
# async def load_photo(message: aiogram.types.Message):
#     photo = message.photo[-1]
#     file_id = photo.file_id
#
#     # Получаем информацию о файле
#     file_info: aiogram.types.File = await message.bot.get_file(file_id)
#     file_server_path: str = file_info.file_path
#
#     new_file = File(
#         id=uuid.uuid4(),
#         filename="repair",
#         tg_file_id=file_id,
#     )
#     file: File = await postgres.file.add(get_session(), new_file)
#
#     os.makedirs(settings.media_dir, exist_ok=True)
#     # Понять что это может быть не картинка, а mp3
#     file_destination = os.path.join(settings.media_dir, f"{file.id}.jpg")
#
#     await message.bot.download_file(file_server_path, destination=file_destination)
#     await message.reply("Фото получено и сохранено.")
