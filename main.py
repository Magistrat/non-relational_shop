from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from uvicorn import run

from lifespan import lifespan_handler
from logger import app_logger
from logger import UNICORN_LOGGING_CONFIG
from routers.api import order_router
from routers.api import services_router
from routers.api import shop_router
from routers.web import html_router
from settings import APP
from settings import APP_VERSION
from settings import HOST
from settings import OPEN_API_VERSION
from settings import PORT
from settings import SWAGGER_TITLE


app = FastAPI(
    title=SWAGGER_TITLE,
    version=APP_VERSION,
    lifespan=lifespan_handler
)
app.mount("/static", StaticFiles(directory="static"), name="static")
app.openapi_version = OPEN_API_VERSION

app.include_router(order_router, prefix='/api')
app.include_router(shop_router, prefix='/api')
app.include_router(services_router, prefix='/api')
app.include_router(html_router)


def main() -> None:
    """
    Запуск сервера
    :return:
    """
    try:
        app_logger.info('Start FastAPI application')
        run(APP, host=HOST, port=PORT, reload=True, log_config=UNICORN_LOGGING_CONFIG)
    except KeyboardInterrupt:
        app_logger.warning('Stop FastAPI application')
    except Exception as e:
        pass
        app_logger.error(f'❌ FastAPI start filed: {e}')


if __name__ == '__main__':
    main()
