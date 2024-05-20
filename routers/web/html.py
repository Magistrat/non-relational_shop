from fastapi import APIRouter
from fastapi import Request
from fastapi import status
from fastapi.templating import Jinja2Templates
from fastapi_cache.decorator import cache


templates = Jinja2Templates(directory='templates')

html_router = APIRouter(
    tags=['HTML handlers services']
)


@cache(expire=60)
@html_router.get(
    path='/',
    summary='Главная страница магазина',
    status_code=status.HTTP_200_OK,
)
async def get_main_page(request: Request):
    """
    Главная страница магазина
    """
    return templates.TemplateResponse(
        'index.html',
        {
            'request': request,
        }
    )
