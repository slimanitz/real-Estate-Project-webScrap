import requests
from bs4 import BeautifulSoup
import pprint
import json


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'br, gzip, deflate',
    'Host': 'www.seloger.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15',
    'Accept-Language': 'fr-fr',
    'Referer': 'https://www.seloger.com/immobilier/tout/immo-aix-en-provence-13/',
    'Connection': 'keep-alive',
}


class seLogerBot:
    url = ""
    def __init__(self,url):
        self.url = url

    def getOwner(self,soup):
        try:
            return soup.find('div', {'class': 'Contact__ContentContainer-sc-3d01ca-2 cKwmCO'}).getText().strip()
        except:
            return None

    def getPrice(self,soup):
        try:
            return soup.find('div',{'data-test':'sl.price-container'}).getText().strip()
        except:
            return None

    def getSize(self,soup):
        try:
            return soup.find('ul',{'data-test':'sl.tags'}).getText().strip()
        except:
            return None

    def getCity(self,soup):
        try:
            block = soup.find('div', {'class': 'ContentZone__Address-wghbmy-1 dlWlag'})
            spans = block.findAll('span')
            return spans[1].getText().strip()

        except:
            return None

    def getDepartement(self,soup):
        try:
            block =  soup.find('div',{'class':'ContentZone__Address-wghbmy-1 dlWlag'})
            spans = block.findAll('span')
            return spans[0].getText().strip()

        except:
            return None

    def getUrl(self,soup):
        try:
            urlsoup = soup.find('a',{'name':'classified-link'})
            url = urlsoup['href']
            return url
        except:
            return None



    def getPropertyData(self,cardSoup):
        owner = self.getOwner(cardSoup)
        price = self.getPrice(cardSoup)
        city = self.getCity(cardSoup)
        departement = self.getDepartement(cardSoup)
        size = self.getSize(cardSoup)
        url = self.getUrl(cardSoup)


        return{
            'owner':owner,
            'price':price,
            'city':city,
            'departement':departement,
            'size':size,
            'url':url
        }


    def getPropertiesData(self,url):
        cardsSoup = self.getAllCards(url)
        l = []
        for card in cardsSoup:
            pprint.pprint(self.getPropertyData(card))
            pprint.pprint("============================")
            l.append(card)
        return l



    def getAllCards(self,url):
        soup = self.getSoup(url)
        cards = soup.findAll('div', {'data-test': 'sl.card-container'})
        return cards





    def getSoup(self,url):
        response = requests.get(url,headers=headers)
        if response.ok:
            soup = BeautifulSoup(response.content,'html.parser')
            return soup


    def sendToDB(self):
        for propertyData in self.getPropertiesData():
            data = json.dumps(propertyData, indent=5)
            requests.post('localhost:3000',data)

    def getAllPagesPropertiesData(self):
        soup = self.getSoup(self.url)
        pagesNumber = self.getPagesNumber(soup)
        for i in range(pagesNumber):
            newUrl = self.url+'&LISTING-LISTpg='+str(i+1)
#            soup = self.getSoup(newUrl)
            self.getPropertiesData(newUrl)




    def getPagesNumber(self,soup):
        pagesList = soup.find('ul',{'data-test':'sl.simplepagination-container'})
        pagesNumber = pagesList.findAll('li')
        return len(pagesNumber)-1







