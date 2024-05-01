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
