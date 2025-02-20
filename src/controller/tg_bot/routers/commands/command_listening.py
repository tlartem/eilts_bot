from aiogram import Router, types
from aiogram.filters import Command

from src.services import send_audio_listening, send_q_list_listening

router = Router()


@router.message(Command("send_listening"))
async def send_listening_test(message: types.Message) -> None:
    await send_audio_listening()
    await send_q_list_listening()
