from pydantic import BaseModel
from callback_factory.catalog_callbacks import CatalogCF


class CatalogMenu(BaseModel):
    button_1: tuple[str, str] = ("Смартфоны", CatalogCF(phones=1).pack())
    button_2: tuple[str, str] = ("Лэтуаль", CatalogCF(cosmetic=1).pack())
    button_3: tuple[str, str] = ("Детские товары", CatalogCF(children_goods=1).pack())
    button_4: tuple[str, str] = ("Электроника", CatalogCF(electronic=1).pack())
    button_5: tuple[str, str] = ("Телевизоры", CatalogCF(electronic=1, tvs=1).pack())
    button_6: tuple[str, str] = ("Ноутбуки", CatalogCF(electronic=1, laptops=1).pack())
    button_7: tuple[str, str] = ("Электроинструменты", CatalogCF(power_tools=1).pack())
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

