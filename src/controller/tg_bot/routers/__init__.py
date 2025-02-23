__all__ = ("router",)

from aiogram import Router

from .commands import router as command_routers
from .text import router as text_routers

router = Router(name=__name__)

router.include_routers(command_routers, text_routers)
