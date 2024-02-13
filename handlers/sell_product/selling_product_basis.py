import logging

from sqlalchemy.ext.asyncio import AsyncSession

from bot_requests.reqs import BotRequests
from sql.models import SellTable


class SellingProduct:

    __COUNT: int = 0

    def __init__(self):
        self.name: str = "...."
        self.price: str | int = "...."

        self.bot_reqs = BotRequests()

    def __get_req_from_req_obj(self):
        """Получить сообщение от бота из класса с запросами"""
        offer_reqs = self.bot_reqs.selling_reqs
        attr_name = self.bot_reqs.get_reqs(reqs_obj=offer_reqs)[self.__COUNT]
        return getattr(offer_reqs, attr_name)

    def basic_template(self):
        req = self.__get_req_from_req_obj()
        self.__COUNT += 1
        return req

    def default_properties(self):
        """Вернуть локальные свойства к первоначальному виду"""
        for attr in vars(self).keys():
            if attr not in ["bot_reqs"]:
                setattr(self, attr, "....")
            elif attr == "bot_reqs":
                setattr(self, attr, BotRequests())

        self.__COUNT = 0

    async def insert_sell_product_data(self, session: AsyncSession):
        product = SellTable(name=self.name, price=int(self.price))
        session.add(product)
        await session.commit()
         
         








