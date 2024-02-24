from aiogram.filters.callback_data import CallbackData


class AdminCF(CallbackData, prefix="admin"):
    excel_parser: int = 0
    catalog_editor: int = 0
    excel_parser_download: int = 0
    excel_parser_upload: int = 0


admin_cd = AdminCF(excel_parser=1)
print(admin_cd.pack())



