from typing import List

from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorDatabase
from fastapi import HTTPException

from schemas import ItemSchema
from schemas import OrderToMongo


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
        await self._mongo_connect.records.insert_one(shop_item.dict())

    async def get_all_items_in_shop(self) -> List[ItemSchema]:
        """
        Получение всех товаров из MongoDB
        :return: Список товаров в Магазине из MongoDB
        """
        cursor = self._mongo_connect.records.find({})
        result = []

        for shop_item in await cursor.to_list(length=100):
            shop_item['id'] = str(shop_item['_id'])
            del shop_item['_id']
            result.append(shop_item)

        return result

    async def get_item_in_shop_by_id(self, mongo_id: str) -> ItemSchema:
        """
        Получение товара из MongoDB по ID
        :param mongo_id: ID в MongoDB
        :return: Товар в Магазине
        """
        cursor = self._mongo_connect.records.find(
            {"_id": ObjectId(mongo_id)}
        )
        results = await cursor.to_list(length=10)
        if len(results) != 1:
            raise HTTPException(
                status_code=503,
                detail=f"Count of results from MongoDb don't equal to 1: {len(results)}"
            )

        return results[0]

    async def add_order_to_shop(self, order: OrderToMongo) -> None:
        """
        Добавляет заказа в MongoDB
        :param order: Заказа для добавления
        :return:
        """
        await self._mongo_connect.records.insert_one(order.dict())

    async def get_orders(self) -> List[OrderToMongo]:
        """
        Получение всех заказов интернет магазине
        :return: Список всех заказов магазина
        """
        cursor = self._mongo_connect.records.find({})
        result = []

        for order_item in await cursor.to_list(length=100):
            order_item['id'] = str(order_item['_id'])
            del order_item['_id']
            result.append(order_item)

        return result
