from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

DB_DIR = Path(__file__).resolve().parent

class BaseConfig(BaseSettings):
    postgres_db: str
    app_db_user: str
    app_db_password: str
    postgres_host: str = 'postgres'
    postgres_port: int = 5432
    app_db_schema: str = 'public'

    model_config = SettingsConfigDict(
            env_file=DB_DIR / '.env', env_file_encoding='utf-8'
    )
