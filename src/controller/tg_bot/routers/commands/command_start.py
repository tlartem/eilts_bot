from aiogram.filters import CommandStart
from aiogram import Router, types

router = Router()


@router.message(CommandStart)
async def command_start(message: types.Message) -> None:
    pass
