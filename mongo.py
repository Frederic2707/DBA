from pymongo import MongoClient
import os

host = (os.getenv("DATABASE_HOST", "localhost"))

mongo_client = MongoClient('mongodb://root:root@'+host+':27017')
db = mongo_client.highestBTC
collection = db.hghesthash

def insert(hash, time, amountBTC, priceBTC):
    data = {"hash": hash, "time":time,"amountBTC":amountBTC,"priceBTC": priceBTC}
    collection.insert_one(data)


def insert_collection(value):
    collection.insert_one(value)


def check_double(hash):
    return collection.count({"hash": hash}) > 0
