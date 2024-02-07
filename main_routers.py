from aiogram import Router

from handlers import start_handlers


router = Router()
router.include_router(start_handlers.router)






