from sqlalchemy.ext.asyncio import AsyncSession

from handlers.sell_product import SellingProduct


class OrderingProduct(SellingProduct):
    async def insert_sell_product_data(self, session: AsyncSession):
        pass
