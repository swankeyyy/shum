from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn


class RunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8000


class ApiPrefix(BaseModel):
    prefix: str = "/api"


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        case_sensitive=False,   # чувствительность к регистру в переменных окружения
        env_nested_delimiter="__",
        env_prefix="APP__",
        env_file=".env"
    )
    run: RunConfig = RunConfig()
    db: DatabaseConfig
    api_prefix: ApiPrefix = ApiPrefix()


settings = Settings()
