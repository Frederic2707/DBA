import threadingdata

thread1 = threadingdata.redisThread()
thread2 = threadingdata.scrapeThread()

thread1.start()
thread2.start()