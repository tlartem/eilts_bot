import os
import uuid

from aiogram import Router, types, F
from aiogram.types.input_file import FSInputFile

from src.adapter import postgres
from src.adapter.postgres import get_session
from src.config import settings
from src.keyboards.reply_kbs import module_kb
from src.models.File import File

router = Router(name=__name__)


@router.message(F.text == "Модуль")
async def choose_handler(message: types.Message) -> None:
    await message.answer(
        text="Выберите модуль, который хотите решить", reply_markup=module_kb
    )


@router.message(F.text == "Reading")
async def reading_handler(message: types.Message) -> None: ...


@router.message(content_types=["photo"])
async def load_photo(message: types.Message):
    photo = message.photo[-1]
    file_id = photo.file_id

    # Получаем информацию о файле
    file_info: types.File = await message.bot.get_file(file_id)
    file_server_path: str = file_info.file_path

    new_file = File(
        id=uuid.uuid4(),
        filename="repair",
        tg_file_id=file_id,
    )
    file: File = await postgres.file.add(get_session(), new_file)

    os.makedirs(settings.media_dir, exist_ok=True)
    # Понять что это может быть не картинка, а mp3
    file_destination = os.path.join(settings.media_dir, f"{file.id}.jpg")

    await message.bot.download_file(file_server_path, destination=file_destination)
    await message.reply("Фото получено и сохранено.")
