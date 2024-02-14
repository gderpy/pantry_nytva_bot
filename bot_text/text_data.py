from handlers.base_functions.sell_product.sell_text import SellingText
from handlers.base_functions.order_product.order_text import OrderingText

from pydantic import BaseModel


class BotText:
    def __init__(self):
        self.selling_text = SellingText()
        self.ordering_text = OrderingText()

    @staticmethod
    def get_text(obj_text: BaseModel):
        return list(obj_text.model_dump().keys())



