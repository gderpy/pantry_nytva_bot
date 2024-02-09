import os

from pydantic import BaseModel
from dotenv import load_dotenv


load_dotenv()


class DBConfig(BaseModel):
    DRIVER: str = os.getenv("DRIVER")
    USERNAME: str = os.getenv("USER_NAME")
    PORT: str = os.getenv("PORT")
    HOST: str = os.getenv("HOST")
    PASSWORD: str = os.getenv("PASSWORD")
    DBNAME: str = os.getenv("DBNAME")

    postgres_url: str = f"{DRIVER}://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"


db_config = DBConfig()
postgres_url = db_config.postgres_url
print(postgres_url)

