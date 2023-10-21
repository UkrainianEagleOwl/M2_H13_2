from pymongo import MongoClient
from pymongo.server_api import ServerApi

def get_mongo_db():
    uri = "my_mongodb_uri"
    client = MongoClient(uri, server_api=ServerApi('1'))
    
    db = client.M2_H08
    
    return db
