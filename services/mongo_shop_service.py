from typing import List

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

    async def get_all_items_in_shop(self) -> List[ItemSchema]:
        """
        Получение всех товаров из MongoDB
        :return:
        """
        cursor = self._mongo_connect.records.find({})
        result = []

        for shop_item in await cursor.to_list(length=100):
            del shop_item['_id']
            # shop_item['_id'] = str(shop_item['_id'])
            result.append(shop_item)

        return result
