from aiogram import Router

from handlers import start_handlers, offering_product


router = Router()
router.include_router(start_handlers.router)
router.include_router(offering_product.router)








