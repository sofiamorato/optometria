"""
Configuración central de la aplicación.

Lee variables de entorno desde el archivo .env utilizando pydantic-settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Base de datos
    DATABASE_URL: str = "sqlite:///./optometria.db"

    # Seguridad / JWT
    SECRET_KEY: str = "cambiar-esta-clave-en-produccion"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480

    # CORS
    FRONTEND_ORIGIN: str = "http://localhost:3000"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
