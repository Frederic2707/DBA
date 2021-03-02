import requests
from bs4 import BeautifulSoup

def scrape():
    url= "https://www.blockchain.com/btc/unconfirmed-transactions"
    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"}
    page = requests.get(url,headers = headers)

    soup = BeautifulSoup(page.content,"html.parser")

    big = -1
    price = 0.0

    varia = soup.select(".sc-20ch6p-0.beTSoK")[0].contents
    for i in range(1,len(varia)-1):
        lijn = (varia[i].contents[3].text)
        lijn=lijn.replace(",","")
        prijs = float (lijn[13:])
        if price < prijs:
            price = prijs
            big=i

    return (varia[big].contents[0].text[4:])
