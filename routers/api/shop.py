from fastapi import APIRouter
from fastapi import status

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
):
    """
    Добавление товара в магазин
    """