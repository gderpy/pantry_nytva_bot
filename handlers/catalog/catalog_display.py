import logging

from sqlalchemy.orm import DeclarativeBase
from aiogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup

from sql.sql_engine import SQLEngine
from keyboards.catalog_kb import CategoryPage, Paginator, ChoosingCategory, ProductPage


class CatalogDisplay:
    def __init__(self):
        self.sql_engine: SQLEngine = SQLEngine()

    async def display_product_list(self, category: str):
        pass

    def __define_callback_factory_with_category(self, category: str):
        if category == "Смартфоны":
            return {"phones": 1}
        elif category == "Лэтуаль":
            return {"cosmetic": 1}
        elif category == "Детские товары":
            return {"children_goods": 1}
        elif category == "Электроника":
            return {"electronic": 1}
        elif category == "Электроинструменты":
            return {"power_tools": 1}
        elif category == "Телевизоры":
            return {"tvs": 1}
        elif category == "Ноутбуки":
            return {"laptops": 1}

    async def __build_list_products_kb(self,
                                 user_type: str,
                                 products: dict,
                                 products_number: int,
                                 category: str,
                                 current_page: int) -> InlineKeyboardMarkup:

        # products:
        # {1: 'POCO C51 64 ГБ син. - 4 999 руб',
        #  2: 'Oukitel C21 Pro 64 ГБ чрн. - 5 399 руб',
        #  3: 'Apple iPhone SE 2022 256 ГБ бел. - 79 999 руб',
        #  4: 'Xiaomi 12 Lite 128 ГБ чрн. - 29 999 руб',
        #  5: 'ASUS ROG Phone 7 256 ГБ чрн. - 94 999 руб',
        #  6: 'Samsung Galaxy A04 64 ГБ бел. - 11 999 руб'}

        def create_button(text: str, callback: str) -> InlineKeyboardButton:
            return InlineKeyboardButton(text=text, callback_data=callback)

        forward_button = InlineKeyboardButton(
                             text="⏩",
                             callback_data=CategoryPage(
                                 user_type=user_type,
                                 category=category,
                                 paginator=Paginator.next_page,
                                 current_page=current_page
                             ).pack())

        backward_button = InlineKeyboardButton(
                              text="⏪",
                              callback_data=CategoryPage(
                                  user_type=user_type,
                                  category=category,
                                  paginator=Paginator.previous_page,
                                  current_page=current_page
                              ).pack())

        if user_type == "user":
            cd = ChoosingCategory(user_type="user").pack()
        else:
            cd = ChoosingCategory(user_type="admin").pack()

        back_categories_button = InlineKeyboardButton(
                                    text="Назад к выбору категории",
                                    callback_data=cd)

        buttons_list: list[list[InlineKeyboardButton]] = []

        start_index = 1 if current_page == 1 else current_page * 8 - 7
        end_index = 9 if current_page == 1 else current_page * 8 + 1

        number_pages = products_number // 8 if products_number % 8 == 0 \
            else products_number // 8 + 1

        for i in range(start_index, end_index):

            if products.get(i) is None:
                if products_number > 8:
                    buttons_menu = buttons_list + [[backward_button], [back_categories_button]]
                else:
                    buttons_menu = buttons_list + [[back_categories_button]]
                return InlineKeyboardMarkup(inline_keyboard=buttons_menu)
            else:
                name = products[i]["catalog_name"]
                product_id = products[i]["id"]

                number_of_photos = await self.sql_engine.count_photos_in_product(product_id)

                buttons_list.append([InlineKeyboardButton(
                    text=name,
                    callback_data=ProductPage(
                        user_type=user_type,
                        category=category,
                        product_id=product_id,
                        current_page=current_page,
                        number_of_photos=number_of_photos,
                        first_press=True).pack()
                )])

        if current_page == 1 and products_number > 8:
            buttons_list += [[forward_button],
                             [back_categories_button]]

        elif current_page > products_number // 8:  # 2 >= 2
            buttons_list += [[backward_button],
                             [back_categories_button]]

        elif current_page <= number_pages:
            count_pages_button = InlineKeyboardButton(
                text=f"{current_page}/{number_pages}",
                callback_data="count_pages"
            )

            buttons_list += [[backward_button, count_pages_button, forward_button]]
            buttons_list += [[back_categories_button]]

        return InlineKeyboardMarkup(inline_keyboard=buttons_list)

    async def display_category_products(self,
                                        user_type: str,
                                        products: dict,
                                        category: str,
                                        current_page: int) -> InlineKeyboardMarkup:

        total_number: int = len(products)

        keyboard_catalog = await self.__build_list_products_kb(
            user_type=user_type,
            products=products,
            products_number=total_number,
            category=category,
            current_page=current_page)

        return keyboard_catalog

    async def check_products_in_category(self, model: DeclarativeBase, callback: CallbackQuery):
        if await self.sql_engine.count_products_in_category(model=model) == 0:
            return await callback.answer(text="Товары в данной категории отсутствуют",
                                         show_alert=True)
        return
