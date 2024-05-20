from fastapi import APIRouter
from fastapi import Request
from fastapi import status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


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
async def get_main_page(request: Request):
    """
    Главная страница магазина
    """
    return templates.TemplateResponse(
        'main_page.html',
        {
            'request': request,
        }
    )
