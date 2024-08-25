from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from app.config import Config


class MongoDBConnector:
    def __init__(self) -> None:
        self.client = MongoClient(Config.DB_URI, server_api=ServerApi("1"))
        self.db = self.client[Config.DB_NAME]

    def get_db(self):
        print(f"{Config.USERNAME}")
        print(f"{Config.PASSWORD}")
        print(f"{Config.DB_URI}")
        return self.db
