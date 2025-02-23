__all__ = ("text_routers",)

from aiogram import Router

from .module_handler import router as module_router

router = Router(name=__name__)

router.include_router(
    module_router,
)
