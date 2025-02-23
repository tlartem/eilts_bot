__all__ = ("command_routers",)

from aiogram import Router

from .command_start import router as start_router

router = Router(name=__name__)

router.include_router(
    start_router,
)
