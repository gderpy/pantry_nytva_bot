import logging

from bot_requests.reqs import BotRequests


class OfferingProduct:

    __COUNT: int = 0

    def __init__(self):
        self.name: str = "...."
        self.price: str | int = "...."

        self.bot_reqs = BotRequests()

    def __get_req_from_req_obj(self):
        """Получить сообщение от бота из класса с запросами"""
        offer_reqs = self.bot_reqs.offering_reqs
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





