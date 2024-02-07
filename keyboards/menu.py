from pydantic import BaseModel


class MainMenu(BaseModel):
    button_1: tuple[str, str] = ("Посмотреть товары 🛍", "view_products")
    button_2: tuple[str, str] = ("Предложить свой товар ✏", "offer_a_product")
    button_3: tuple[str, str] = ("Про оплату 💳", "about_payment")
    button_4: tuple[str, str] = ("Помощь 📄", "help")
    admin_button_1: tuple[str, str] = ("Панель администратора 🖥", "admin_panel")

    def button_layout(self, admin=True):

        keyboard = [
            [self.button_1],
            [self.button_2],
            [self.button_3, self.button_4],
            [self.admin_button_1]
        ]

        if admin:
            return keyboard
        return keyboard[:-1]



