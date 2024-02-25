from aiogram import Router

from handlers import start_handlers, admin_panel, base_functions, catalog
from handlers.admin_panel import download_excel_file

router = Router()
router.include_router(start_handlers.router)
router.include_router(admin_panel.router)
router.include_router(download_excel_file.router)
router.include_router(base_functions.router)
router.include_router(catalog.router)











