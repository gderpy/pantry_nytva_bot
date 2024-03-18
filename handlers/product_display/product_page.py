import openpyxl as ox
import asyncio

from pathlib import Path
from typing import Union
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from sql.models.categories_models import (PhonesTable, TvTable, LaptopsTable, CosmeticsTable,
                                          PowerToolsTable, ElectronicTable, ChildrenGoodsTable)
from sql.sql_engine import SQLEngine
from sql.models import Base, AllProductsTable

TableType = Union[PhonesTable, TvTable, LaptopsTable, CosmeticsTable, PowerToolsTable,
ElectronicTable, ChildrenGoodsTable]

table_matches = {
    PhonesTable: ["Смартфоны", PhonesTable],
    TvTable: ["Телевизоры", TvTable],
    LaptopsTable: ["Ноутбуки", LaptopsTable],
    CosmeticsTable: ["Лэтуаль", CosmeticsTable],
    PowerToolsTable: ["Электроинструменты", PowerToolsTable],
    ElectronicTable: ["Электроника", ElectronicTable],
    ChildrenGoodsTable: ["Детские товары", ChildrenGoodsTable]
}


class ProductPage:
    categories_dict = {
        "phones": ["Смартфоны", PhonesTable],
        "cosmetic": ["Лэтуаль", CosmeticsTable],
        "children_goods": ["Детские товары", ChildrenGoodsTable],
        "electronic": ["Электроника", ElectronicTable],
        "power_tools": ["Электроинструменты", PowerToolsTable],
        "tvs": ["Телевизоры", TvTable],
        "laptops": ["Ноутбуки", LaptopsTable]
    }

    def __init__(self):
        self.excel_template_path: Path = Path.cwd() / "excel_files/Обновленный Excel-файл.xlsx"
        self.excel_template_path_2: Path = Path.cwd().parents[1] / "excel_files/Обновленный Excel-файл.xlsx"
        self.sql_engine = SQLEngine()

    def get_name_and_model(self, category_name: str) -> tuple:
        name, model = self.categories_dict.get(category_name)
        return name, model

    def get_columns_names_from_excel(self):
        path = self.excel_template_path_2
        wb = ox.load_workbook(filename=path)

        # Достаем названия категорий из файла excel
        sheetnames = [sheetname for sheetname in wb.sheetnames
                      if sheetname not in ["Заявки", "На продажу"]]

        return sheetnames

    async def get_attrs_of_a_spec_category(self, table: TableType):
        sheetnames = self.get_columns_names_from_excel()

        category_name = table_matches[table]

        await self.sql_engine.display_a_product_of_a_specific_category(category=category_name)

        return category_name

    def get_column_names_of_category(self, category_name):
        name, model = self.get_name_and_model(category_name)

        excel_column_names = []

        wb = ox.load_workbook(self.excel_template_path)
        ws = wb[name]

        for column_number in range(3, ws.max_column + 1):
            excel_column_names.append(ws.cell(row=1, column=column_number).value)

        return excel_column_names, model

    async def get_product_info(self, category_name: str,
                               session: AsyncSession, product_id: int):

        excel_column_names, model = self.get_column_names_of_category(category_name=category_name)

        model: Base
        excel_column_names: list

        catalog_product = await session.get(AllProductsTable, product_id)
        product_name, product_price = catalog_product.name, catalog_product.price

        stmt = select(model).where(model.product_id == product_id)

        res = await session.execute(stmt)
        result = res.scalars().one()

        column_names = model.collect_column_names()

        product_data = []

        for column_name in column_names:
            if column_name == "product_id":
                continue
            product_data.append(result.__getattribute__(column_name))

        product_information = (
            f"<b><i>{product_name}</i></b>\n\n"
            f"<b><i>{'{:,}'.format(product_price).replace(",", " ")} руб</i></b>\n\n")

        for excel_cols_name, curr_data in zip(excel_column_names, product_data):

            font_excel_cols_name = f"<b><i>{excel_cols_name}</i></b>"
            font_curr_data = f"<i>{curr_data}</i>"

            if curr_data == "None":
                continue
            elif excel_cols_name == "Дополнительное описание":
                product_information += f"\n<b>{excel_cols_name}</b>\n{curr_data}"
            else:
                product_information += f"{font_excel_cols_name}: {font_curr_data}\n"

        return product_information[:-1]

        # 1: ('iPhone 12 64 ГБ зел.', 53999, PhonesTable(cpu: A14 Bionic,
        # ram: 4 ГБ, storage: 64 ГБ, display: AMOLED, battery: 2815 мА * ч,
        #    sim: 1+eSIM, camera: 12+12 Мп, description: Айфон за хорошую стоимость)
