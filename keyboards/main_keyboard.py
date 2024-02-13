from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.any_kbs.menu import MainMenu
from keyboards.any_kbs.selling_kb import SellingProcessKeyboard
from keyboards.any_kbs.admin_kb import AdminMenu


class Keyboard:
    def __init__(self):
        self.main_menu: MainMenu = MainMenu()
        self.sell_kb: SellingProcessKeyboard = SellingProcessKeyboard()
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
sell_menu = keyboard.sell_kb.button_layout(end=False)
sell_menu_end = keyboard.sell_kb.button_layout(end=True)
admin_panel = keyboard.admin_panel.button_layout()

inline_common_main_menu = keyboard.create_kb(button_layout=common_main_menu)
inline_admin_main_menu = keyboard.create_kb(button_layout=admin_main_menu)
inline_sell_menu = keyboard.create_kb(button_layout=sell_menu)
inline_sell_menu_end = keyboard.create_kb(button_layout=sell_menu_end)
inline_admin_panel = keyboard.create_kb(button_layout=admin_panel)



