from pydantic_settings import BaseSettings,SettingsConfigDict
from functools import cached_property

class Settings(BaseSettings):
    DB_HOST:str
    DB_PORT:int
    DB_USER:str
    DB_PASSWORD:str
    DB_NAME:str
    DB_POOL_SIZE:int
    DB_MAX_OVERFLOW:int
    REDIS_HOST:str
    REDIS_PORT:int

    model_config = SettingsConfigDict(env_file=".env",extra="ignore")

    @cached_property
    def DATABASE_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    @cached_property
    def REDIS_URL(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"
    

settings = Settings()