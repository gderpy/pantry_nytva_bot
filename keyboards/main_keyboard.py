from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.any_kbs.menu import MainMenu
from keyboards.any_kbs.base_func_kb import BaseFunctionsKeyboard
from keyboards.any_kbs.admin_kb import AdminMenu


class Keyboard:
    def __init__(self):
        self.main_menu: MainMenu = MainMenu()
        self.sell_kb: BaseFunctionsKeyboard = BaseFunctionsKeyboard()
        self.admin_panel: AdminMenu = AdminMenu()

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

#  ============================================================================= #

inline_common_main_menu = keyboard.create_kb(button_layout=common_main_menu)
inline_admin_main_menu = keyboard.create_kb(button_layout=admin_main_menu)

inline_base_sell_func_menu = keyboard.create_kb(button_layout=base_sell_func_menu)
inline_base_sell_func_menu_end = keyboard.create_kb(button_layout=base_sell_func_menu_end)

inline_base_order_func_menu = keyboard.create_kb(button_layout=base_order_func_menu)
inline_base_order_func_menu_end = keyboard.create_kb(button_layout=base_order_func_menu_end)

inline_admin_panel = keyboard.create_kb(button_layout=admin_panel)



