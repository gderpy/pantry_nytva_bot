from handlers.sell_product.sell_text import SellingRequests

from pydantic import BaseModel


class BotRequests:
    def __init__(self):
        self.selling_reqs = SellingRequests()

    @staticmethod
    def get_reqs(reqs_obj: BaseModel):
        return list(reqs_obj.model_dump().keys())


bot_reqs = BotRequests()
sell_reqs = bot_reqs.selling_reqs

