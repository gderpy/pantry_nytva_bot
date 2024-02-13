from aiogram import Router

from handlers import start_handlers, sell_product, admin_panel, order_product


router = Router()
router.include_router(start_handlers.router)
router.include_router(admin_panel.router)
router.include_router(sell_product.router)
router.include_router(order_product.router)









