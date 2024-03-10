import logging

from bot_text.text_data import BotText


class BaseFunctionsEngine:

    __COUNT: int = 0

    def __init__(self):
        self.name: str | None = None
        self.price: int | None = None
        self.contact: str | None = "...."

        self.bot_text = BotText()

    def __get_req_from_obj_text(self, obj_text: object):
        """Получить сообщение от бота из класса с запросами"""
        attr_name = self.bot_text.get_text(obj_text=obj_text)[self.__COUNT]
        return getattr(obj_text, attr_name)

    def basic_template(self, obj_text: object):
        req = self.__get_req_from_obj_text(obj_text=obj_text)
        self.__COUNT += 1
        return req

    def default_properties(self):
        """Вернуть локальные свойства к первоначальному виду"""
        for attr in vars(self).keys():
            if attr not in ["bot_text"]:
                setattr(self, attr, "....")
            elif attr == "bot_text":
                setattr(self, attr, BotText())

        self.__COUNT = 0

