import requests
from bs4 import BeautifulSoup
import pprint
import urllib.parse as urlparse
from urllib.parse import parse_qs
import datetime
import urllib.request
import json
import time

#proxy = 'ip:port'

# requests.get(url,headers=headers,proxies={'http':proxy,'https':proxy},timeout:4s)




headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Host': 'www.seloger.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    'Accept-Language': 'fr-fr',
    'Accept-Encoding': 'br, gzip, deflate',
    'Connection': 'keep-alive',
}



class proxiesBot:
    url = "https://free-proxy-list.net"

    def __init__(self):
        pass

    def getIps(self):
        res = requests.get(self.url,headers=headers)
        if res.ok:
            soup = BeautifulSoup(res.content,'html.parser')
            tab = soup.find('tbody')
            print(tab)







