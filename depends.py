from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient
from motor.motor_asyncio import AsyncIOMotorDatabase

from services import MongoShopService
from settings import MONGO_PATH
from settings import MONGO_COLLECTION_ORDERS
from settings import MONGO_COLLECTION_SHOP


async def get_async_mongo_client_by_motor() -> AsyncIOMotorClient:
    """
    Возвращает асинхронный клиент к MongoDB через библиотеку motor
    :return: Асинхронный клиент к MongoDB
    """
    return AsyncIOMotorClient(MONGO_PATH)


async def get_async_mongo_connect_to_shop_by_motor(
        mongo_client: AsyncIOMotorClient = Depends(get_async_mongo_client_by_motor)
) -> AsyncIOMotorDatabase:
    """
    Возвращает асинхронное подключение к MongoDB в коллекцию SHOP через библиотеку motor
    :return:
    """
    return mongo_client[MONGO_COLLECTION_SHOP]


async def get_async_mongo_connect_to_orders_by_motor(
        mongo_client: AsyncIOMotorClient = Depends(get_async_mongo_client_by_motor)
) -> AsyncIOMotorDatabase:
    """
    Возвращает асинхронное подключение к MongoDB в коллекцию ORDERS через библиотеку motor
    :return:
    """
    return mongo_client[MONGO_COLLECTION_ORDERS]


async def get_mongo_shop_service(
        mongo_connect: AsyncIOMotorDatabase = Depends(get_async_mongo_connect_to_shop_by_motor)
) -> MongoShopService:
    """
    Фабричная функция для внедрения зависимости с MongoShopService.
    :param mongo_connect: Асинхронное подключение к MongoDB в коллекцию SHOP
    :return: Объект MongoShopService.
    """
    return MongoShopService(mongo_connect=mongo_connect)


async def get_mongo_orders_service(
        mongo_connect: AsyncIOMotorDatabase = Depends(get_async_mongo_connect_to_orders_by_motor)
) -> MongoShopService:
    """
    Фабричная функция для внедрения зависимости с MongoShopService.
    :param mongo_connect: Асинхронное подключение к MongoDB в коллекцию ORDERS
    :return: Объект MongoShopService.
    """
    return MongoShopService(mongo_connect=mongo_connect)
