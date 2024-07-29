import time

from fastapi import FastAPI
from sqlalchemy import text

from app.users.config import auth_backend
from app.users.manager import fastapi_users
from app.users.schemas import UserRead, UserCreate, UserUpdate

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from .config import settings

####################################
from .database.connection import engine
from .database.db import Base
from fastapi_cache.decorator import cache

app = FastAPI(title='marketplace')

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)

app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix='/auth',
    tags=['auth'],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix='/auth',
    tags=['auth'],
)

app.include_router(
    fastapi_users.get_users_router(
        UserRead, UserUpdate, requires_verification=True
    ),
    prefix='/users',
    tags=['users'],
)

@app.on_event('startup')
def startup():

    redis = aioredis.from_url(
        f'redis://{settings.REDIS_HOST}:{settings.REDIS_PORT}'
    )
    FastAPICache.init(RedisBackend(redis), prefix='fastapi-cache')


#################################################################################
@app.get("/users/")
async def create_user():
    # Логика создания пользователя
    return {123: 123}
@app.get("/users1/") # ПРОВЕРКА ПОДКЛЮЧЕНИЯ К БД
async def get_123():
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT VERSION()"))
        print(res.all())

@app.get("/long_operation")
@cache(expire=30)
def get_long():
    time.sleep(2)
    return "Долго, долго"