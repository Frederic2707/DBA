import threading
import time
import redishelper
import mongo
from scrape import scrape
active = True
"""

based on: https://www.tutorialspoint.com/python/python_multithreading.htm

"""
class redisThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while active: 
            time.sleep(60)
            mongo.insert_collection(redishelper.redisRetrieve("placeholder"))
            redishelper.keyDelete("placeholder")
class scrapeThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while active: 
            time.sleep(1)
            tijdelelijkeVar=(scrape())
            if mongo.check_double(tijdelelijkeVar["hash"]) == False:
                #redishelper.redisSave(tijdelelijkeVar, "placeholder")
                if redishelper.keyCheck("placeholder")==False :
                    redishelper.redisSave(tijdelelijkeVar,"placeholder")
                else:
                    last = redishelper.redisRetrieve("placeholder")
                    if tijdelelijkeVar["priceBTC"]>last["priceBTC"]:
                        redishelper.redisSave(tijdelelijkeVar,"placeholder")
                        print("valuechange")
                    print(tijdelelijkeVar)
    