from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from depends import get_mongo_shop_service
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
) -> OrderToMongo:
    """
    Добавление интернет заказа
    """
    print()
    return None
