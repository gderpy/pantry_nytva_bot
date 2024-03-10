from pydantic import BaseModel
from callback_factory.catalog_callbacks import CatalogCF


class CatalogMenu(BaseModel):
    button_1: tuple[str, str] = ("Смартфоны", CatalogCF(category="phones").pack())
    button_2: tuple[str, str] = ("Лэтуаль", CatalogCF(category="cosmetic").pack())
    button_3: tuple[str, str] = ("Детские товары", CatalogCF(category="children_goods").pack())
    button_4: tuple[str, str] = ("Электроника", CatalogCF(category="electronic").pack())
    button_5: tuple[str, str] = ("Телевизоры", CatalogCF(category="tvs").pack())
    button_6: tuple[str, str] = ("Ноутбуки", CatalogCF(category="laptops").pack())
    button_7: tuple[str, str] = ("Электроинструменты", CatalogCF(category="power_tools").pack())
    button_8: tuple[str, str] = ("Назад в меню 📱", "back_to_main_menu")
    button_9: tuple[str, str] = ("Вернуться к категориям", "view_products_again")

    def button_layout(self, admin=True):

        keyboard = [
            [self.button_1, self.button_2],
            [self.button_3, self.button_4],
            [self.button_7],
            [self.button_8]
        ]

        return keyboard

    def electronic_section(self):
        return [
            [self.button_5, self.button_6],
            [self.button_9]
        ]

