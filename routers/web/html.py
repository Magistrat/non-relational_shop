from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi import status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from depends import get_mongo_orders_service
from depends import get_mongo_shop_service
from services import MongoShopService

templates = Jinja2Templates(directory='templates')

html_router = APIRouter(
    tags=['HTML handlers services']
)


@html_router.get(
    path='/',
    summary='Главная страница магазина',
    status_code=status.HTTP_200_OK,
    response_class=HTMLResponse
)
async def get_main_page(
        request: Request,
        mongo_shop_service: MongoShopService = Depends(get_mongo_shop_service),
):
    """
    Главная страница магазина
    """
    shop_items = await mongo_shop_service.get_all_items_in_shop()

    return templates.TemplateResponse(
        'main_page.html',
        {
            'request': request,
            'shop_items': shop_items
        }
    )


@html_router.get(
    path='/basket',
    summary='Корзина с покупками интернет-магазина',
    status_code=status.HTTP_200_OK,
    response_class=HTMLResponse
)
async def get_basket(
        request: Request,
):
    """
    Корзина с покупками интернет-магазина
    """
    return templates.TemplateResponse(
        'basket.html',
        {
            'request': request,
        }
    )


@html_router.get(
    path='/orders',
    summary='Список всех заказов интернет-магазина',
    status_code=status.HTTP_200_OK,
    response_class=HTMLResponse
)
async def get_all_orders(
        request: Request,
        mongo_orders_service: MongoShopService = Depends(get_mongo_orders_service),
):
    """
    Список всех заказов интернет-магазина
    """
    return templates.TemplateResponse(
        'orders.html',
        {
            'request': request,
            'orders_items': await mongo_orders_service.get_orders()
        }
    )
