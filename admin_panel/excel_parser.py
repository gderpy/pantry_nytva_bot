import logging

import pandas as pd
import openpyxl as ox

from pathlib import Path
from openpyxl import Workbook

from aiogram.types import File, CallbackQuery, BufferedInputFile
from aiogram import Bot
from sqlalchemy import select

from sql.sql_engine import SQLEngine
from sql.models import OrderTable, SellTable
from sql.models.base import Base


class ExcelParser:

    bot: Bot
    chat_id: int

    def __init__(self):
        self.excel_template_path: Path = Path.cwd() / "excel_files/Excel-файл шаблон.xlsx"
        self.session = SQLEngine().async_session

    def excel_file(self):
        return BufferedInputFile(open(self.excel_template_path, "rb").read(),
                                 filename="Ваш Excel-файл.xlsx")

    @staticmethod
    def __unload_orders_and_sells(sell_table_data: list,
                                  order_table_data: list,
                                  wb: Workbook):

        obj_data_list = [sell_table_data, order_table_data]

        for obj_data in obj_data_list:
            for ir in range(len(obj_data)):
                for ic in range(len(obj_data[ir])):

                    if obj_data == sell_table_data:
                        sheet_name = "На продажу"
                        startrow, startcol = 3, 1
                    else:
                        startrow, startcol = 3, 1
                        sheet_name = "Заявки"

                    wb[sheet_name].cell(startrow + ir, startcol + ic).value = obj_data[ir][ic]

    def read_excel_file(self):
        path = Path.cwd().parent / "excel_files" / "Excel-файл шаблон.xlsx"
        wb = ox.load_workbook(filename=path)

        sheetnames = ["Смартфоны", "Лэтуаль", "Детские товары", "Электроника", "Электроинструменты",
                      "Телевизоры", "Ноутбуки"]

        ws = wb["Смартфоны"]

        row_data = []

        for i in range(1, 11):
            row_data.append(ws.cell(row=2, column=i).value)

        return row_data

    async def __get_data_from_db_table(self, model: Base) -> list:
        async with self.session() as session:
            stmt = select(model)
            res = await session.execute(stmt)

            obj_data: list = []

            for data in res.scalars():
                obj_data.append(data.as_list())

            await session.commit()
            return obj_data

    async def download_excel_file(self):

        obj_data_orders = await self.__get_data_from_db_table(model=OrderTable)
        obj_data_sells = await self.__get_data_from_db_table(model=SellTable)

        logging.info(f"obj_data_orders: {obj_data_orders}")
        logging.info(f"obj_data_sells: {obj_data_sells}")

        wb = ox.load_workbook(filename=self.excel_template_path)

        self.__unload_orders_and_sells(order_table_data=obj_data_orders,
                                       sell_table_data=obj_data_sells,
                                       wb=wb)

        wb.save(filename=self.excel_template_path)

    async def upload_excel_file(self):
        pass




























