from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from logger import app_logger
from settings import REDIS_CONNECTION_PATH


async def redis_startup():
    """
    Инициализация асинхронного подключения к REDIS для хранения кеша
    :return:
    """
    app_logger.info('Init connection to Redis for cache')
    redis = aioredis.from_url(
        REDIS_CONNECTION_PATH,
        encoding="utf8",
        decode_responses=True,
    )

    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
