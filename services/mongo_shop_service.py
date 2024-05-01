from motor.motor_asyncio import AsyncIOMotorDatabase

from schemas import ItemSchema


class MongoShopService:
    """
    Сервис взаимодействия с Mongo.
    """
    def __init__(self, mongo_connect: AsyncIOMotorDatabase):
        self._mongo_connect: AsyncIOMotorDatabase = mongo_connect

    async def add_items_to_shop(self, shop_item: ItemSchema) -> None:
        """
        Добавляет товар в MongoDB
        :param shop_item: Товар для добавления
        :return:
        """
        await self._mongo_connect.records.insert_one(dict(shop_item))
