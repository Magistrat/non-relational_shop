from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi import status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

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
