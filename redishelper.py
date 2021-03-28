from redis import Redis
import json
import os

host = (os.getenv("REDIS_HOST", "localhost"))
redis = Redis(host=host, port=6379)
""" def redisSave():
    redis.set("naamhier", "datahier")
 """
def redisSave(data, naam):
    redis.set(naam, json.dumps(data))

def redisRetrieve(naam):
    return json.loads(redis.get(naam).decode('utf-8'))
def keyCheck(naam):
    return redis.exists(naam)> 0
def keyDelete(naam):
    if keyCheck(naam):
        redis.delete(naam)
