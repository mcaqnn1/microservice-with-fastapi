from contextlib import asynccontextmanager
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache import FastAPICache
from fastapi import FastAPI
from redis import asyncio as aioredis
from core.db.config import settings
import logging

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app:FastAPI):
    redis = aioredis.from_url(
        settings.REDIS_URL,
        encoding="utf-8",
        decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis=redis),prefix="cache")

    logger.info("Connected!")
    yield
    redis.aclose()
    logger.info("Disconnected!")
