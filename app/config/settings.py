from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    env: str = "dev"
    database_url: str
    allow_origins: list[str] = ["http://localhost:3000"]
    rate_limit_per_minute: int = 100

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instancia de configuración global para usar en toda la aplicación
settings = Settings()
