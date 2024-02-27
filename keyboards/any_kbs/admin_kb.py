from pydantic import BaseModel
from callback_factory.admin_callback import AdminCF


class AdminMenu(BaseModel):
    button_1: tuple[str, str] = ("Скачать Excel-файл 📥", AdminCF(excel_parser=1).pack())
    button_1_2: tuple[str, str] = ("Загрузить Excel-файл 📤", AdminCF(excel_parser_upload=1).pack())
    button_2: tuple[str, str] = ("Добавить фото 📸", AdminCF(catalog_editor=1).pack())
    button_3: tuple[str, str] = ("Назад в меню 📱", "back_to_main_menu")
    button_4: tuple[str, str] = ("Скрыть файл для скачивания 🗃", AdminCF(
                                                                    excel_parser=1,
                                                                    excel_parser_download=1
                                 ).pack())

    button_5: tuple[str, str] = ("Отменить действие ❌", AdminCF(excel_parser=1,
                                                                 excel_parser_cancel_upload=1).pack())

    button_6: tuple[str, str] = ("Начать выгрузку данных в каталог 📥", AdminCF(excel_parser=1,
                                                                                excel_parser_upload=1).pack())

    def button_layout(self, admin=True):

        keyboard = [
            [self.button_1],
            [self.button_1_2],
            [self.button_2],
            [self.button_3]
        ]

        return keyboard

    def hide_excel_file(self):
        return [
            [self.button_4]
        ]

    def excel_parser_cancel_upload(self):
        return [
            [self.button_5]
        ]

    def start_to_upload_data_from_excel_file_kb(self):
        return [
            [self.button_6],
            [self.button_5]
        ]




