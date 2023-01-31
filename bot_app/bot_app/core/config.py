import os

from dotenv import load_dotenv

load_dotenv()


class DbConfig:
    POSTGRES_USER = os.getenv("POSTGRES_USER")
    POSTGRES_HOST = os.getenv("POSTGRES_HOST")
    POSTGRES_DB = os.getenv("POSTGRES_DB")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_PORT = os.getenv("POSTGRES_PORT")


class BotConfig:
    BOT_TOKEN = os.getenv("TOKEN")


class Config:
    bot = BotConfig()
    db = DbConfig()
