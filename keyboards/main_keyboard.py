from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.any_kbs.menu import MainMenu
from keyboards.any_kbs.base_func_kb import BaseFunctionsKeyboard
from keyboards.any_kbs.admin_kb import AdminMenu
from keyboards.any_kbs.catalog import CatalogMenu


class Keyboard:
    def __init__(self):
        self.main_menu: MainMenu = MainMenu()
        self.sell_kb: BaseFunctionsKeyboard = BaseFunctionsKeyboard()
        self.admin_panel: AdminMenu = AdminMenu()
        self.catalog_menu: CatalogMenu = CatalogMenu()

    @staticmethod
    def create_kb(button_layout: list) -> InlineKeyboardMarkup:

        kb = []

        for b_row in button_layout:
            row = []
            for button in b_row:
                text, callback_data = button
                row.append(InlineKeyboardButton(text=text, callback_data=callback_data))
            kb.append(row)

        return InlineKeyboardMarkup(inline_keyboard=kb)


keyboard = Keyboard()

common_main_menu = keyboard.main_menu.button_layout(admin=False)
admin_main_menu = keyboard.main_menu.button_layout(admin=True)

base_sell_func_menu = keyboard.sell_kb.button_layout(end=False, sell=True)
base_sell_func_menu_end = keyboard.sell_kb.button_layout(end=True, sell=True)

base_order_func_menu = keyboard.sell_kb.button_layout(end=False, sell=False)
base_order_func_menu_end = keyboard.sell_kb.button_layout(end=True, sell=False)

admin_panel = keyboard.admin_panel.button_layout()
admin_excel_file = keyboard.admin_panel.hide_excel_file()
admin_cancel_upload_excel_file = keyboard.admin_panel.excel_parser_cancel_upload()
admin_start_to_upload_data_from_excel_file = keyboard.admin_panel.start_to_upload_data_from_excel_file_kb()

catalog_menu = keyboard.catalog_menu.button_layout()
catalog_menu_electronic_section = keyboard.catalog_menu.electronic_section()

#  ============================================================================= #

inline_common_main_menu = keyboard.create_kb(button_layout=common_main_menu)
inline_admin_main_menu = keyboard.create_kb(button_layout=admin_main_menu)

inline_base_sell_func_menu = keyboard.create_kb(button_layout=base_sell_func_menu)
inline_base_sell_func_menu_end = keyboard.create_kb(button_layout=base_sell_func_menu_end)

inline_base_order_func_menu = keyboard.create_kb(button_layout=base_order_func_menu)
inline_base_order_func_menu_end = keyboard.create_kb(button_layout=base_order_func_menu_end)

inline_admin_panel = keyboard.create_kb(button_layout=admin_panel)
inline_hide_excel_file = keyboard.create_kb(button_layout=admin_excel_file)
inline_admin_cancel_upload_excel_file = keyboard.create_kb(button_layout=admin_cancel_upload_excel_file)
inline_start_to_upload_data_from_excel_file = keyboard.create_kb(button_layout=admin_start_to_upload_data_from_excel_file)

inline_catalog_menu = keyboard.create_kb(button_layout=catalog_menu)
inline_catalog_menu_electronic_section = keyboard.create_kb(button_layout=catalog_menu_electronic_section)





