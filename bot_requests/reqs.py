from handlers.offering_product.offer_reqs import OfferingRequests

from pydantic import BaseModel


class BotRequests:
    def __init__(self):
        self.offering_reqs = OfferingRequests()

    @staticmethod
    def get_reqs(reqs_obj: BaseModel):
        return list(reqs_obj.model_dump().keys())


bot_reqs = BotRequests()
offer_reqs = bot_reqs.offering_reqs

