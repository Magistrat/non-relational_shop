from fastapi import APIRouter
from fastapi import Depends
from fastapi import status

from depends import get_async_mongo_connect_to_shop_by_motor
from schemas import ItemSchema


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
    mongo_connect=Depends(get_async_mongo_connect_to_shop_by_motor)
):
    """
    Добавление товара в магазин
    """
    return None
