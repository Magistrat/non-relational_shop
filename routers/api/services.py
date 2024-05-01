import time

from fastapi import APIRouter
from fastapi_cache.decorator import cache


services_router = APIRouter(
    prefix='/services',
    tags=['Project services']
)


@services_router.get(path='/test/redis')
@cache(expire=20)
async def get_for_test_redis():
    time.sleep(2)
    return 1
