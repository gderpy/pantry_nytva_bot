from pydantic import BaseModel


class OfferingProcessKeyboard(BaseModel):
    button_0: tuple[str, str] = ("Отправить данные ✅", "send_product_data")
    button_1: tuple[str, str] = ("Назад в меню 📱", "back_to_main_menu")

    def button_layout(self, end=False):

        keyboard = [
            [self.button_0],
            [self.button_1]
        ]

        if end:
            return keyboard
        return keyboard[1:]





