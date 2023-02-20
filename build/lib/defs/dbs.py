from pymongo import MongoClient
from pymongo.database import Database
from typing import Mapping, Any


def mongo_connector(host: str, port: int, db_name: str, collection_name: str):
    server_connection: MongoClient[Mapping[str, Any]] = MongoClient(host, port)
    db_nm: Database[Mapping[str, Any]] = server_connection[db_name]
    return db_nm[collection_name]
