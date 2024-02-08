from aiogram.utils.keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from keyboards.any_kbs.menu import MainMenu
from keyboards.any_kbs.offering_kb import OfferingProcessKeyboard


class Keyboard:
    def __init__(self):
        self.main_menu: MainMenu = MainMenu()
        self.offer_kb: OfferingProcessKeyboard = OfferingProcessKeyboard()

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
offer_menu = keyboard.offer_kb.button_layout(end=False)
offer_menu_end = keyboard.offer_kb.button_layout(end=True)

inline_common_main_menu = keyboard.create_kb(button_layout=common_main_menu)
inline_admin_main_menu = keyboard.create_kb(button_layout=admin_main_menu)
inline_offer_menu = keyboard.create_kb(button_layout=offer_menu)
inline_offer_menu_end = keyboard.create_kb(button_layout=offer_menu_end)



