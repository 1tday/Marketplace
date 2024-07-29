from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """Класс для работы с переменными окружения."""


    POSTGRES_DB_NAME: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str

    SECRET_KEY: str
    ALGORITHM: str

    REDIS_HOST: str
    REDIS_PORT: str

    SECRET: str
    PASSWORD: str

    @property
    def DATABASE_URL(self):
        return (f'postgresql+asyncpg://{self.POSTGRES_USER}:'
                f'{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:'
                f'{self.POSTGRES_PORT}/{self.POSTGRES_DB_NAME}')

    # для локальной разработки
    model_config = SettingsConfigDict(env_file='C:/Users/dkd29/OneDrive/Рабочий стол/TestProject/Marketplace/.env')

    # для запуска в docker
    # model_config = SettingsConfigDict(env_file='.env-docker')

settings = Settings()