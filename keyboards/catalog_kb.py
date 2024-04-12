from enum import Enum

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData


categories = {"phones", "cosmetic", "children_goods", "tvs", "laptops", "power_tools"}

categories_dict = {
    "phones": "Смартфоны",
    "cosmetic": "Лэтуаль",
    "children_goods": "Детские товары",
    "electronic": "Электроника",
    "power_tools": "Электроинструменты",
    "tvs": "Телевизоры",
    "laptops": "Ноутбуки"
}


class ChoosingCategory(CallbackData, prefix="category"):
    user_type: str


class Paginator(str, Enum):
    next_page = "next_page"
    previous_page = "previous_page"


class CategoryPage(CallbackData, prefix="category_page"):
    user_type: str
    category: str

    current_page: int = 1
    paginator: Paginator | bool = False

    return_after_photo: bool = False


def create_btn(text: str, callback_data: str):
    return InlineKeyboardButton(text=text, callback_data=callback_data)


def choosing_category_keyboard(user_type: str):
    def create_category_button(category_name: str,
                               callback_name: str,
                               user_type: str):

        return create_btn(text=category_name,
                          callback_data=CategoryPage(
                              user_type=user_type,
                              category=callback_name
                          ).pack())

    phones = create_category_button(category_name="Смартфоны",
                                    callback_name="phones",
                                    user_type=user_type)

    cosmetic = create_category_button(category_name="Лэтуаль",
                                      callback_name="cosmetic",
                                      user_type=user_type)

    children_goods = create_category_button(category_name="Детские товары",
                                            callback_name="children_goods",
                                            user_type=user_type)

    tvs = create_category_button(category_name="Телевизоры",
                                 callback_name="tvs",
                                 user_type=user_type)

    laptops = create_category_button(category_name="Ноутбуки",
                                     callback_name="laptops",
                                     user_type=user_type)

    power_tools = create_category_button(category_name="Электроинструменты",
                                         callback_name="power_tools",
                                         user_type=user_type)

    electronic = create_category_button(category_name="Электроника",
                                        callback_name="electronic",
                                        user_type=user_type)

    category_keyboard = [
        [phones, cosmetic],
        [children_goods, electronic],
        [power_tools]
    ]

    electronic_category_keyboard = [
        [tvs, laptops]
    ]

    return {"general_kb": category_keyboard,
            "electronic_category_kb": electronic_category_keyboard}


class ProductPage(CallbackData, prefix="product"):
    user_type: str
    category: str
    product_id: int
    current_page: int
    number_of_photos: int
    current_photo: int | bool = False
    photo_paginator: Paginator | bool = False
    page_paginator: Paginator | bool = False
    first_press: bool = False


class ProductCart(CallbackData, prefix="cart"):
    user_type: str


class PhotoAction(str, Enum):
    add_photo = "add"
    delete_photo = "remove"


class Photo(CallbackData, prefix="photo"):
    photo_action: PhotoAction | bool = False


def product_page_keyboard(user_type: str,
                          category: str,
                          product_id: int,
                          current_page: int,
                          number_of_photos: int,
                          current_photo: int,
                          page_paginator: Paginator | bool):

    def create_option_btn(text: str):

        return InlineKeyboardButton(
            text=text,
            callback_data=ProductPage(
                user_type=user_type,
                category=category,
                product_id=product_id,
                current_page=current_page,
                number_of_photos=number_of_photos,
                current_photo=current_photo
            ).pack()
        )

    btn_with_photo = InlineKeyboardButton(
        text="Еще фото ⏩",
        callback_data=ProductPage(
            user_type=user_type,
            category=category,
            product_id=product_id,
            current_page=current_page,
            number_of_photos=number_of_photos,
            current_photo=current_photo,
            photo_paginator=Paginator.next_page,
            page_paginator=page_paginator
        ).pack())

    btn_with_photo_2 = create_option_btn(text="⏪")
    btn_with_photo_2_1 = create_option_btn(text="⏩")
    btn_photo_pagination = InlineKeyboardButton(text="2/3", callback_data="photo_pagination")

    btn_adding_photo = InlineKeyboardButton(text="Добавить фото 📸", callback_data=Photo(
        photo_action=PhotoAction.add_photo
    ).pack())

    btn_delete_photo = InlineKeyboardButton(text="Удалить фото 🗑", callback_data=Photo(
        photo_action=PhotoAction.delete_photo
    ).pack())

    btn_show_added_photos = create_option_btn(text="Добавленные фото ⏩")

    btn_adding_item_to_cart = InlineKeyboardButton(text="Добавить товар в корзину 🛒",
                                                   callback_data=ProductCart(
                                                                user_type=user_type).pack())

    btn_back_to_catalog = InlineKeyboardButton(text="Вернуться в каталог 📲",
                                               callback_data=CategoryPage(
                                                   user_type=user_type,
                                                   category=category,
                                                   current_page=current_page,
                                                   paginator=page_paginator).pack())

    user_keyboard_without_photos_or_one_photo = [
        [btn_adding_item_to_cart],
        [btn_back_to_catalog]
    ]

    user_keyboard_with_photos = [
        [btn_with_photo],
        [btn_adding_item_to_cart],
        [btn_back_to_catalog]
    ]

    user_keyboard_with_photos_2 = [
        [btn_with_photo_2, btn_photo_pagination, btn_with_photo_2_1],
        [btn_adding_item_to_cart],
        [btn_back_to_catalog]
    ]

    user_keyboard_last_photo = [
        [btn_with_photo_2],
        [btn_adding_item_to_cart],
        [btn_back_to_catalog]
    ]

    admin_keyboard_without_photo = [
        [btn_adding_photo],
        [btn_back_to_catalog]
    ]

    admin_keyboard_with_photo = [
        [btn_show_added_photos],
        [btn_adding_photo],
        [btn_delete_photo],
        [btn_back_to_catalog]
    ]

    return {
        "user_keyboard_without_photos_or_one_photo": user_keyboard_without_photos_or_one_photo,
        "user_keyboard_with_photos": user_keyboard_with_photos,
        "user_keyboard_with_photos_2": user_keyboard_with_photos_2,
        "user_keyboard_last_photo": user_keyboard_last_photo,
        "admin_keyboard_without_photo": admin_keyboard_without_photo,
        "admin_keyboard_with_photo": admin_keyboard_with_photo
    }





