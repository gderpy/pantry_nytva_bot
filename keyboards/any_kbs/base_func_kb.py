from pydantic import BaseModel


class BaseFunctionsKeyboard(BaseModel):
    button_0: tuple[str, str] = ("Отправить данные ✅", "send_sell_product_data")
    button_0_1: tuple[str, str] = ("Отправить данные ✅", "send_order_product_data")
    button_1: tuple[str, str] = ("Назад в меню 📱", "back_to_main_menu")

    def button_layout(self, sell=False, end=False):

        keyboard = [
            [self.button_0] if sell else [self.button_0_1],
            [self.button_1]
        ]

        if end:
            return keyboard
        return keyboard[1:]





