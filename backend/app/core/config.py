from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # APPLICATION
    PROJECT_NAME: str = "Distributed Storage Platform"
    DEBUG: bool = True

    # SERVER
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # API
    API_V1_PREFIX: str = "/api/v1"

    # DATABASE
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    DATABASE_URL: str

    # JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"

    # REDIS
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379

    # MINIO
    MINIO_ENDPOINT: str = "minio:9000"
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()