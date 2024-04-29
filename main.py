from fastapi import FastAPI
from uvicorn import run

from logger import app_logger
from routers.api import backend_router
from settings import APP
from settings import APP_VERSION
from settings import HOST
from settings import LOGGING_CONFIG
from settings import OPEN_API_VERSION
from settings import PORT
from settings import SWAGGER_TAGS_METADATA
from settings import SWAGGER_TITLE


app = FastAPI(
    title=SWAGGER_TITLE,
    openapi_tags=SWAGGER_TAGS_METADATA,
    version=APP_VERSION
)
app.openapi_version = OPEN_API_VERSION

app.include_router(backend_router, prefix='/api')


def main() -> None:
    """
    Запуск сервера
    :return:
    """
    try:
        app_logger.info('Start FastAPI application')
        run(APP, host=HOST, port=PORT, reload=True, log_config=LOGGING_CONFIG)
    except KeyboardInterrupt:
        app_logger.warning('Stop FastAPI application')
    except Exception as e:
        pass
        app_logger.error(f'❌ FastAPI start filed: {e}')


if __name__ == '__main__':
    main()
