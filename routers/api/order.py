from typing import List

from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from depends import get_mongo_shop_service
from depends import get_mongo_orders_service
from schemas import OrderFromShop
from schemas import OrderToMongo
from services import MongoShopService


order_router = APIRouter(
    prefix='/order',
    tags=['Backend order API']
)


@order_router.post(
    path='/',
    summary='Добавление интернет заказа',
    status_code=status.HTTP_200_OK,
)
async def add_order(
    request_body: OrderFromShop,
    mongo_shop_service: MongoShopService = Depends(get_mongo_shop_service),
    mongo_order_service: MongoShopService = Depends(get_mongo_orders_service),
) -> OrderToMongo:
    """
    Добавление интернет заказа
    """

    all_products = []
    for mongo_id in request_body.products:
        all_products.append(await mongo_shop_service.get_item_in_shop_by_id(mongo_id))

    result = OrderToMongo(
        username=request_body.username,
        phone=request_body.phone,
        address=request_body.address,
        products=all_products
    )
    await mongo_order_service.add_order_to_shop(order=result)
    return result


@order_router.get(
    path='/',
    summary='Получение интернет заказов',
    status_code=status.HTTP_200_OK,
)
async def get_order(
    mongo_order_service: MongoShopService = Depends(get_mongo_orders_service),
) -> List[OrderToMongo]:
    """
    Получение интернет заказов
    """
    return await mongo_order_service.get_orders()
