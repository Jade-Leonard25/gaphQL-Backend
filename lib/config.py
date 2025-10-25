import toml
from pydantic_settings import BaseSettings
from pydantic import BaseModel

class AppSettings(BaseModel):
    host: str
    port: int

class DatabaseSettings(BaseModel):
    url: str

class Settings(BaseSettings):
    app: AppSettings
    database: DatabaseSettings

    class Config:
        @classmethod
        def customise_sources(
            cls,
            init_settings,
            env_settings,
            file_secret_settings,
        ):
            return (
                init_settings,
                lambda settings: toml.load("config.toml"),
                env_settings,
                file_secret_settings,
            )

settings = Settings()
