from os import getenv
from dotenv import load_dotenv

load_dotenv('.env.list')


class Config:
    POSTGRES_DB = getenv('POSTGRES_DB')
    POSTGRES_USER = getenv('POSTGRES_USER')
    POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD')
    DB_HOST = getenv('DB_HOST')
