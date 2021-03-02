from scrape import scrape
import time


hashlist=[]
while True:
    tijdelelijkeVar=(scrape())
    if tijdelelijkeVar not in hashlist:
        hashlist.append(tijdelelijkeVar)
        print(tijdelelijkeVar)
    time.sleep(60)
