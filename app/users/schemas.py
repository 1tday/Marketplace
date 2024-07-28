from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    """Модель отображения пользователя."""

    id: int
    username: str
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        from_attributes = True


class UserCreate(schemas.BaseUserCreate):
    """Модель создания пользователя."""

    username: str
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr
    password: str
    is_active: bool | None = True
    is_superuser: bool | None = False
    is_verified: bool | None = False


class UserUpdate(schemas.BaseUserUpdate):
    """Модель, позволяющая пользователю обновлять свои данные."""

    username: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    password: str | None = None
    email: EmailStr | None = None
    is_active: bool | None = None
    is_superuser: bool | None = None
    is_verified: bool | None = None