from contextlib import asynccontextmanager

from fastapi import FastAPI

from logger import app_logger
from .startup_events import redis_startup


@asynccontextmanager
async def lifespan_handler(app: FastAPI) -> None:
    """
    Планировщик заданий для FastAPI:
    1. Выполнение до запуска сервера
    yield
    2. Выполнение после остановки сервера

    :param app: Объект приложения FastAPI
    :return:
    """
    app_logger.info('FastAPI lifespan startup')
    await redis_startup()

    yield
    app_logger.info('FastAPI lifespan shutdown')
