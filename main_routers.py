from aiogram import Router

from handlers import start_handlers, admin_panel, base_functions

router = Router()
router.include_router(start_handlers.router)
router.include_router(admin_panel.router)
router.include_router(base_functions.router)











