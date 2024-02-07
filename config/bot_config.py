import os

from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()


class BotConfig(BaseModel):
    API_TOKEN: str = os.getenv("API_TOKEN")
    ADMINS: list = [228931634]


bot_config = BotConfig()

API_TOKEN = bot_config.API_TOKEN
ADMINS = bot_config.ADMINS








