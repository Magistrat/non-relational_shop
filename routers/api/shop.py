from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from depends import get_mongo_shop_service
from schemas import ItemSchema
from services import MongoShopService


shop_router = APIRouter(
    prefix='/shop',
    tags=['Backend shop API']
)


@shop_router.post(
    path='/item',
    summary='Добавление товара в магазин',
    status_code=status.HTTP_200_OK,
)
async def add_item_to_shop(
    request_body: ItemSchema,
    mongo_shop_service: MongoShopService = Depends(get_mongo_shop_service),
):
    """
    Добавление товара в магазин
    """
    await mongo_shop_service.add_items_to_shop(shop_item=request_body)
    return None


@shop_router.get(
    path='/item/{mongo_id}',
    summary='Получение информации о товаре в магазине по ID',
    status_code=status.HTTP_200_OK,
)
async def get_item_in_shop_by_id(
    mongo_id: str,
    mongo_shop_service: MongoShopService = Depends(get_mongo_shop_service),
) -> ItemSchema:
    """
    Получение информации о товаре в магазине по ID
    """
    return await mongo_shop_service.get_item_in_shop_by_id(mongo_id=mongo_id)


@shop_router.get(
    path='/items',
    summary='Получение списка товаров в магазине',
    status_code=status.HTTP_200_OK,
    response_model=List[ItemSchema]
)
async def get_all_items_in_shop(
    mongo_shop_service: MongoShopService = Depends(get_mongo_shop_service),
):
    """
    Получение списка товаров в магазине
    """
    return await mongo_shop_service.get_all_items_in_shop()
