from pydantic import BaseModel
from callback_factory.admin_callback import AdminCF


class AdminMenu(BaseModel):
    button_1: tuple[str, str] = ("Скачать Excel-файл 📓", AdminCF(excel_parser=1).pack())
    button_2: tuple[str, str] = ("Добавить фото 📸", AdminCF(catalog_editor=1).pack())
    button_3: tuple[str, str] = ("Назад в меню 📱", "back_to_main_menu")

    def button_layout(self, admin=True):

        keyboard = [
            [self.button_1],
            [self.button_2],
            [self.button_3]
        ]

        return keyboard

