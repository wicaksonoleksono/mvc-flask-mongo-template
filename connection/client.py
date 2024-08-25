__author__ = "wicaksono"

from dotenv import load_dotenv


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# load from dotenv
load_dotenv()
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
# create uri ...
uri = "mongodb+srv://${DB_USERNAME}:${DB_PASSWORD}@todolist.lmhro.mongodb.net/${DB_NAME}?retryWrites=true&w=majority"

try:
    client.admin.command('ping')
    print(f"Pingged your deployment, you are sucessfully connected to {username} MonggoDB's!")
except Exception as e:
    print(e)