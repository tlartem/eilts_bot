from aiogram import Router, types, F
from aiogram.types.input_file import FSInputFile

from src.keyboards.reply_kbs import module_kb

router = Router(name=__name__)


@router.message(F.text == "Модуль")
async def choose_handler(message: types.Message) -> None:
    await message.answer(
        text="Выберите модуль, который хотите решить", reply_markup=module_kb
    )

@router.message(F.text == "Reading")
async def reading_handler(message: types.Message) -> None:
    ...