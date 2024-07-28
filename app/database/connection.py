from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import settings


engine = create_async_engine(settings.DATABASE_URL)
async_session_maker = async_sessionmaker(
    bind=engine,  # Движок базы данных, который будет использоваться
    class_=AsyncSession,  # Класс сессии, который будет использоваться
    expire_on_commit=False  # Состояние объектов остаётся актуальным
)
