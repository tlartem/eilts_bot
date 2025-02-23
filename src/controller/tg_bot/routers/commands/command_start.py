from aiogram.filters import Command
from aiogram import Router, types

from src.keyboards.reply_kbs import start_kb
from src.services import create_user

router = Router(name=__name__)


@router.message(Command('start'))
async def command_start(message: types.Message) -> None:
    await create_user(tg_id=message.from_user.id, username=message.from_user.username)  # type: ignore[union-attr]
    await message.answer(
        text="Здравствуйте, это бот для подготовки к экзамену ielts!\nВы хотите решить тест целиком, или решить конкретный модуль?",
        reply_markup=start_kb,
    )
