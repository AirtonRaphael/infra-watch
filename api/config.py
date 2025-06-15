from dataclasses import dataclass
import os

from dotenv import load_dotenv


load_dotenv()


@dataclass
class Settings:
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_MINUTES: int
    DB_URL: str


def load_env() -> Settings:
    return Settings(
        SECRET_KEY=os.getenv("SECRET_KEY"),
        ALGORITHM=os.getenv("ALGORITHM"),
        ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "15")),
        REFRESH_TOKEN_EXPIRE_MINUTES=int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES", "60")),
        DB_URL=os.getenv("DB_URL"),
    )

settings = load_env()
